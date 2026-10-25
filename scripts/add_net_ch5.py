#!/usr/bin/env python3
"""
Add Networking Ch 05 — Network Layer (Maximum Bangla + English terms).
Rename: TCP Ch 05 → Ch 06, HTTP Ch 06 → Ch 07.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 05 → Ch 06, HTTP Ch 06 → Ch 07
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 05 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 06 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 06 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 07 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 05 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH5 = r'''  {
    id: "net-network-layer",
    subject: "net",
    title: "Ch 05 — Network Layer",
    bangla: "নেটওয়ার্ক লেয়ার",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "Network layer (Layer 3) একাধিক networks জুড়ে end-to-end communication-এর জন্য responsible। এর main functions হলো — logical addressing (IP addresses assign করা), routing (source থেকে destination-এর best path determine করা), ও packet forwarding (packets কে incoming interface থেকে correct outgoing interface-এ move করা)।",
    sections: [
      { type: "h2", id: "functions", title: "Network Layer-র Functions" },
      {
        type: "p",
        text: "Network layer-র তিনটি main function আছে। Logical addressing — প্রতিটি host একটি IP address পায় (যেমন 192.168.1.10), যা source ও destination identify করতে use হয়। Routing — routers একে অপরের সাথে network topology সম্পর্কে information exchange করে এবং routing tables build করে। Forwarding — যখন একটি packet arrive করে, router তার table-এ destination IP খুঁজে বের করে এবং সেটিকে next hop-এ পাঠায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — postal system। Logical addressing হলো প্রতিটি বাড়ির address (IP address)। Routing হলো post office কীভাবে letter কোথায় পাঠাবে তার পথ ঠিক করা (routing table)। Forwarding হলো প্রতিটি sorting center-এ letter কে সঠিক বাক্সে ফেলা (incoming → outgoing interface)।",
      },

      { type: "h2", id: "ip-addressing", title: "IP Addressing" },
      { type: "h3", title: "IPv4 Address Classes" },
      {
        type: "p",
        text: "IPv4 addresses গুলো 32 bits long, সাধারণত চারটি decimal octets হিসেবে লেখা হয়। Originally addresses গুলোকে classes-এ ভাগ করা হয়েছিল। Class A (leading bits 0, first octet 1-126, mask 255.0.0.0, large networks)। Class B (leading bits 10, first octet 128-191, mask 255.255.0.0, medium networks)। Class C (leading bits 110, first octet 192-223, mask 255.255.255.0, small networks)। Class D (leading bits 1110, first octet 224-239, multicast)। Class E (leading bits 1111, first octet 240-255, experimental)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building। Class A হলো একটি বিশাল apartment complex যার অনেক floors ও কয়েকটি apartments। Class B হলো medium building। Class C হলো একটি ছোট building যার অল্প কয়েকটি apartments। Class D হলো intercom system (একজন একসাথে অনেককে call করে)। Class E হলো একটি building যা শুধু experiment-এর জন্য reserved।",
      },
      {
        type: "multi-code",
        filename: "ip_class_detect",
        codeSamples: {
          cpp: `#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// Detect IP address class from first octet.
char ip_class(const string& ip) {
    int first;
    char dot;
    istringstream iss(ip);
    iss >> first >> dot;
    if (first >= 1   && first <= 126) return 'A';
    if (first >= 128 && first <= 191) return 'B';
    if (first >= 192 && first <= 223) return 'C';
    if (first >= 224 && first <= 239) return 'D';
    return 'E';
}

int main() {
    cout << "10.0.0.1      -> Class " << ip_class("10.0.0.1")      << '\\n';   // A
    cout << "172.16.0.1    -> Class " << ip_class("172.16.0.1")    << '\\n';   // B
    cout << "192.168.1.1   -> Class " << ip_class("192.168.1.1")   << '\\n';   // C
    cout << "224.0.0.1     -> Class " << ip_class("224.0.0.1")     << '\\n';   // D
}`,
          go: `package main

import (
    "fmt"
    "strconv"
    "strings"
)

func ipClass(ip string) string {
    parts := strings.Split(ip, ".")
    first, _ := strconv.Atoi(parts[0])
    switch {
    case first >= 1   && first <= 126: return "A"
    case first >= 128 && first <= 191: return "B"
    case first >= 192 && first <= 223: return "C"
    case first >= 224 && first <= 239: return "D"
    default: return "E"
    }
}

func main() {
    fmt.Println("10.0.0.1    -> Class", ipClass("10.0.0.1"))    // A
    fmt.Println("172.16.0.1  -> Class", ipClass("172.16.0.1"))  // B
    fmt.Println("192.168.1.1 -> Class", ipClass("192.168.1.1")) // C
}`,
          python: `def ip_class(ip):
    """Detect IP address class from first octet."""
    first = int(ip.split(".")[0])
    if 1   <= first <= 126: return "A"
    if 128 <= first <= 191: return "B"
    if 192 <= first <= 223: return "C"
    if 224 <= first <= 239: return "D"
    return "E"

for ip in ["10.0.0.1", "172.16.0.1", "192.168.1.1", "224.0.0.1"]:
    print(f"{ip:15s} -> Class {ip_class(ip)}")`,
          java: `public class IPClass {
    static char ipClass(String ip) {
        int first = Integer.parseInt(ip.split("\\\\.")[0]);
        if (first >= 1   && first <= 126) return 'A';
        if (first >= 128 && first <= 191) return 'B';
        if (first >= 192 && first <= 223) return 'C';
        if (first >= 224 && first <= 239) return 'D';
        return 'E';
    }
    public static void main(String[] args) {
        System.out.println("10.0.0.1    -> Class " + ipClass("10.0.0.1"));
        System.out.println("172.16.0.1  -> Class " + ipClass("172.16.0.1"));
        System.out.println("192.168.1.1 -> Class " + ipClass("192.168.1.1"));
    }
}`,
        },
      },

      { type: "h3", title: "Subnetting" },
      {
        type: "p",
        text: "Subnetting একটি বড় network কে ছোট, manageable subnets-এ ভাগ করে। এটি host bits কে network portion-এর জন্য borrow করে। উদাহরণ — 192.168.1.0/24 (Class C, 256 addresses)। ৪টি subnets প্রয়োজন যাতে প্রতিটিতে অন্তত ৫০টি hosts থাকে। ২টি bits borrow করো → new subnet mask = /26 (255.255.255.192)। Subnets সংখ্যা = 2² = 4। Hosts per subnet = 2⁶ - 2 = 62।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি বড় office floor কে ছোট cabins-এ ভাগ করা। পুরো floor একটি /24 network। প্রতিটি cabin একটি subnet। Cabin এর walls হলো subnet bits। প্রতিটি cabin-এ কয়েকজন বসতে পারে (hosts per subnet)।",
      },
      {
        type: "multi-code",
        filename: "subnet_calculator",
        codeSamples: {
          cpp: `#include <cmath>
#include <iostream>
using namespace std;

// Calculate number of subnets and hosts per subnet.
void subnet_info(int original_prefix, int borrowed_bits) {
    int new_prefix = original_prefix + borrowed_bits;
    int num_subnets = 1 << borrowed_bits;            // 2^borrowed
    int host_bits = 32 - new_prefix;
    int hosts_per_subnet = (1 << host_bits) - 2;      // 2^host - 2
    cout << "New prefix: /" << new_prefix << '\\n';
    cout << "Subnets: " << num_subnets << '\\n';
    cout << "Hosts per subnet: " << hosts_per_subnet << '\\n';
}

int main() {
    // 192.168.1.0/24, borrow 2 bits → /26
    subnet_info(24, 2);
    // Output: /26, 4 subnets, 62 hosts each
}`,
          go: `package main

import "fmt"

func subnetInfo(originalPrefix, borrowedBits int) {
    newPrefix := originalPrefix + borrowedBits
    numSubnets := 1 << borrowedBits
    hostBits := 32 - newPrefix
    hostsPerSubnet := (1 << hostBits) - 2
    fmt.Printf("New prefix: /%d\\n", newPrefix)
    fmt.Printf("Subnets: %d\\n", numSubnets)
    fmt.Printf("Hosts per subnet: %d\\n", hostsPerSubnet)
}

func main() {
    subnetInfo(24, 2)  // /26, 4 subnets, 62 hosts each
}`,
          python: `def subnet_info(original_prefix, borrowed_bits):
    new_prefix = original_prefix + borrowed_bits
    num_subnets = 2 ** borrowed_bits
    host_bits = 32 - new_prefix
    hosts_per_subnet = 2 ** host_bits - 2
    print(f"New prefix: /{new_prefix}")
    print(f"Subnets: {num_subnets}")
    print(f"Hosts per subnet: {hosts_per_subnet}")

subnet_info(24, 2)  # /26, 4 subnets, 62 hosts each`,
          java: `public class SubnetCalc {
    static void subnetInfo(int originalPrefix, int borrowedBits) {
        int newPrefix = originalPrefix + borrowedBits;
        int numSubnets = 1 << borrowedBits;
        int hostBits = 32 - newPrefix;
        int hostsPerSubnet = (1 << hostBits) - 2;
        System.out.println("New prefix: /" + newPrefix);
        System.out.println("Subnets: " + numSubnets);
        System.out.println("Hosts per subnet: " + hostsPerSubnet);
    }
    public static void main(String[] args) {
        subnetInfo(24, 2);  // /26, 4 subnets, 62 hosts each
    }
}`,
        },
      },

      { type: "h3", title: "CIDR (Classless Inter-Domain Routing)" },
      {
        type: "p",
        text: "CIDR class boundaries remove করে। একটি IP address কে prefix length সহ লেখা হয় (যেমন /20)। এটা supernetting allow করে — একাধিক networks কে একটি route-এ aggregate করা। উদাহরণ — 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24 কে 192.168.0.0/22-তে combine করা (কারণ first 22 bits common)। এটি routing table entries reduce করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building-এ ৪টি floors। প্রতিটি floor-এ একটি doorbell list। CIDR হলো সব floors-এর doorbells কে একটি single entry তে merge করা — 'Building A' বললেই চারটো floor বোঝায়।",
      },

      { type: "h3", title: "IPv6 Basics" },
      {
        type: "p",
        text: "IPv6 128-bit addresses use করে (৮টি groups of ৪ hex digits হিসেবে লেখা হয়)। Main features — কোনো broadcast নেই (multicast ও anycast use করে), auto-configuration (SLAAC), simplified header (কোনো checksum নেই, routers-এ কোনো fragmentation নেই)। IPv6 address types — Unicast (single interface), Multicast (one-to-many), Anycast (one-to-nearest)।",
      },

      { type: "h2", id: "routing-algorithms", title: "Routing Algorithms" },
      { type: "h3", title: "Distance Vector (Bellman-Ford)" },
      {
        type: "p",
        text: "প্রতিটি router তার সম্পূর্ণ routing table neighbors-এর সাথে periodically share করে। Hop count-এর মতো metrics use করা হয়। Problem — slow convergence, count-to-infinity। উদাহরণ — তিনটি routers A-B-C। B-C link fail করে। A ভাবে সে B-এর মাধ্যমে C-তে পৌঁছাতে পারবে (cost 3), B ভাবে A-এর মাধ্যমে (cost 4) — loop যতক্ষণ না infinity (16) set করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি গ্রামে মানুষ একে অপরকে গল্প করে যে সে কোথায় যেতে পারে। প্রতিটি মানুষ তার neighbor-দের বলে কোথায় যাওয়া যায়। কিন্তু যদি একটি road বন্ধ হয়ে যায়, তারা অনেকক্ষণ না জেনে ভুল তথ্য দিতে থাকে (count-to-infinity)।",
      },

      { type: "h3", title: "Link State (Dijkstra)" },
      {
        type: "p",
        text: "প্রতিটি router সম্পূর্ণ topology learn করে এবং Dijkstra algorithm দিয়ে shortest paths compute করে। প্রতিটি router Link State Advertisements (LSAs) সব অন্য routers-এ flood করে। Advantage — fast convergence, কোনো loops নেই।",
      },
      {
        type: "p",
        text: "Real-life thinking — প্রতিজনের কাছে একটি সম্পূর্ণ city map আছে। প্রত্যেকে নিজে Dijkstra চালিয়ে best route বের করে। যদি কোনো road বন্ধ হয়ে যায়, সবাই তখনই জানে এবং নতুন route বের করে — কোনো গল্প বা confusion নেই।",
      },
      {
        type: "multi-code",
        filename: "dijkstra_routing",
        codeSamples: {
          cpp: `#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// Dijkstra's shortest path algorithm.
// graph[u] = list of (neighbor, weight).
vector<int> dijkstra(int V, vector<vector<pair<int,int>>>& graph, int src) {
    vector<int> dist(V, INT_MAX);
    vector<bool> visited(V, false);
    dist[src] = 0;
    for (int i = 0; i < V; i++) {
        int u = -1, minD = INT_MAX;
        for (int j = 0; j < V; j++)
            if (!visited[j] && dist[j] < minD) { minD = dist[j]; u = j; }
        if (u == -1) break;
        visited[u] = true;
        for (auto& [v, w] : graph[u])
            if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
    }
    return dist;
}

int main() {
    // 4 nodes: A=0, B=1, C=2, D=3
    vector<vector<pair<int,int>>> g(4);
    g[0] = {{1,2},{2,5}};   // A-B:2, A-C:5
    g[1] = {{0,2},{2,3},{3,1}};  // B-A:2, B-C:3, B-D:1
    g[2] = {{0,5},{1,3},{3,2}};  // C-A:5, C-B:3, C-D:2
    g[3] = {{1,1},{2,2}};   // D-B:1, D-C:2
    auto dist = dijkstra(4, g, 0);  // from A
    for (int i = 0; i < 4; i++)
        cout << "A -> " << (char)('A'+i) << " = " << dist[i] << '\\n';
    // A->A=0, A->B=2, A->C=5, A->D=3
}`,
          go: `package main

import "fmt"

func dijkstra(V int, graph [][][]int, src int) []int {
    dist := make([]int, V)
    visited := make([]bool, V)
    for i := range dist { dist[i] = 1 << 30 }
    dist[src] = 0
    for i := 0; i < V; i++ {
        u, minD := -1, 1<<30
        for j := 0; j < V; j++ {
            if !visited[j] && dist[j] < minD {
                minD = dist[j]; u = j
            }
        }
        if u == -1 { break }
        visited[u] = true
        for _, edge := range graph[u] {
            v, w := edge[0], edge[1]
            if dist[u]+w < dist[v] { dist[v] = dist[u] + w }
        }
    }
    return dist
}

func main() {
    // graph[u] = list of [neighbor, weight]
    graph := [][][]int{
        {{1, 2}, {2, 5}},
        {{0, 2}, {2, 3}, {3, 1}},
        {{0, 5}, {1, 3}, {3, 2}},
        {{1, 1}, {2, 2}},
    }
    dist := dijkstra(4, graph, 0)
    names := []string{"A", "B", "C", "D"}
    for i, d := range dist {
        fmt.Printf("A -> %s = %d\\n", names[i], d)
    }
}`,
          python: `def dijkstra(V, graph, src):
    """graph[u] = list of (neighbor, weight)."""
    dist = [float('inf')] * V
    visited = [False] * V
    dist[src] = 0
    for _ in range(V):
        u, min_d = -1, float('inf')
        for j in range(V):
            if not visited[j] and dist[j] < min_d:
                min_d, u = dist[j], j
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

# 4 nodes: A=0, B=1, C=2, D=3
graph = [
    [(1, 2), (2, 5)],           # A-B:2, A-C:5
    [(0, 2), (2, 3), (3, 1)],   # B-A:2, B-C:3, B-D:1
    [(0, 5), (1, 3), (3, 2)],   # C-A:5, C-B:3, C-D:2
    [(1, 1), (2, 2)],           # D-B:1, D-C:2
]
dist = dijkstra(4, graph, 0)
names = ["A", "B", "C", "D"]
for i, d in enumerate(dist):
    print(f"A -> {names[i]} = {d}")`,
          java: `import java.util.*;

public class Dijkstra {
    static int[] dijkstra(int V, List<List<int[]>> graph, int src) {
        int[] dist = new int[V];
        boolean[] visited = new boolean[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        for (int i = 0; i < V; i++) {
            int u = -1, minD = Integer.MAX_VALUE;
            for (int j = 0; j < V; j++) {
                if (!visited[j] && dist[j] < minD) { minD = dist[j]; u = j; }
            }
            if (u == -1) break;
            visited[u] = true;
            for (int[] edge : graph.get(u)) {
                int v = edge[0], w = edge[1];
                if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
            }
        }
        return dist;
    }
    public static void main(String[] args) {
        List<List<int[]>> graph = new ArrayList<>();
        graph.add(Arrays.asList(new int[]{1,2}, new int[]{2,5}));
        graph.add(Arrays.asList(new int[]{0,2}, new int[]{2,3}, new int[]{3,1}));
        graph.add(Arrays.asList(new int[]{0,5}, new int[]{1,3}, new int[]{3,2}));
        graph.add(Arrays.asList(new int[]{1,1}, new int[]{2,2}));
        int[] dist = dijkstra(4, graph, 0);
        String[] names = {"A", "B", "C", "D"};
        for (int i = 0; i < 4; i++)
            System.out.println("A -> " + names[i] + " = " + dist[i]);
    }
}`,
        },
      },

      { type: "h3", title: "Flooding" },
      {
        type: "p",
        text: "একটি router incoming packet কে সব interface-এ forward করে যেটার উপর এসেছে সেটা ছাড়া। Military, OSPF initial LSA propagation, বা robustness-এর জন্য use হয়। Control mechanisms — hop count limit, sequence numbers।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন postman যে একটি letter পায় এবং সেটিকে প্রতিটি house-এ এক এক করে দেয়। খুব reliable কিন্তু অনেক কাগজ নষ্ট হয়। যেহেতু একটা letter অনেকবার copy হয়, একটা sequence number দিয়ে আগে পাওয়া copies discard করা যায়।",
      },

      { type: "h2", id: "routing-protocols", title: "Routing Protocols" },
      { type: "h3", title: "RIP (Routing Information Protocol)" },
      {
        type: "p",
        text: "Distance-vector protocol, hop count কে metric হিসেবে use করে (max 15 hops)। প্রতি 30 second-এ updates করে। উদাহরণ — RIP route entry: 192.168.5.0/24 via 10.0.0.2, metric 2।",
      },
      { type: "h3", title: "OSPF (Open Shortest Path First)" },
      {
        type: "p",
        text: "Link-state protocol, cost (bandwidth-এর উপর based) use করে। Hierarchical design — areas গুলো একটি backbone (Area 0)-এর সাথে connected। Faster convergence, VLSM/CIDR support করে।",
      },
      { type: "h3", title: "BGP (Border Gateway Protocol)" },
      {
        type: "p",
        text: "Path-vector protocol যেটা Autonomous Systems (AS)-এর মধ্যে use হয়। Routes-এ AS_PATH attribute include করা থাকে loops prevent করতে। উদাহরণ — AS 100, 200.1.0.0/16-কে path [100] সহ advertise করে। AS 200 সেটি receive করে, নিজের AS prepend করে: [200, 100]।",
      },
      {
        type: "p",
        text: "Real-life thinking — RIP হলো neighbors একে অপরকে gossip করে (আমি X-এ যেতে পারি, 2 hops)। OSPF হলো সবার কাছে একটি full map আছে এবং প্রত্যেকে নিজে route বের করে। BGP হলো বিভিন্ন দেশের post offices একে অপরের সাথে আলোচনা করে যে কোন package কোন দেশে যাবে।",
      },

      { type: "h2", id: "additional-topics", title: "Additional Topics" },
      { type: "h3", title: "Fragmentation" },
      {
        type: "p",
        text: "যখন একটি packet একটি link-এর MTU (Maximum Transmission Unit)-এর চেয়ে বড়, router সেটিকে fragments-এ ভাগ করে। IPv4 fragments গুলো destination-এ reassemble করা হয়; IPv6 in-path fragmentation allow করে না। উদাহরণ — MTU = 1500 bytes, original packet = 4000 bytes। তিনটি fragments — Fragment 1 (offset 0, length 1500), Fragment 2 (offset 1480, length 1500), Fragment 3 (offset 2960, length 1020)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি বড় parcel কে ছোট ছোট বাক্সে ভাগ করা যাতে প্রতিটি বাক্স একটি narrow door দি�়ে যেতে পারে। Destination-এ সব বাক্স একসাথে যোগ করে আসল parcel পাওয়া যায়।",
      },
      { type: "h3", title: "NAT (Network Address Translation)" },
      {
        type: "p",
        text: "NAT একাধিক private IP addresses (যেমন 192.168.1.x) কে একটি single public IP share করতে allow করে। Common types — Source NAT (SNAT) outbound traffic-এর জন্য, Port Address Translation (PAT)। উদাহরণ — 192.168.1.10:12345 → 203.0.113.5:50001।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building যার একটি single public phone আছে। প্রতিটি apartment থেকে call করলে receptionist সেটিকে public number থেকে বের করে এবং একটি extension number assign করে। Incoming call-এ receptionist extension number দেখে সঠিক apartment-এ পাঠায়।",
      },
      { type: "h3", title: "ICMP (Internet Control Message Protocol)" },
      {
        type: "p",
        text: "ICMP error reporting ও diagnostics-এর জন্য use হয়। এটি IP-এর ভেতরে encapsulate করা থাকে। Common message types — Echo request/reply (ping), Destination unreachable (port/network unreachable), Time exceeded (traceroute-এ used), Redirect (host-কে better gateway সম্পর্কে inform)। উদাহরণ — ping 8.8.8.8 একটি ICMP Echo Request পাঠায়; Google-এর server Echo Reply দিয়ে উত্তর দেয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি delivery service-এ যদি কোনো package deliver না হয়, তাহলে একটি 'return to sender' sticker লাগানো হয় সমস্যার কারণ লেখা (ICMP Destination Unreachable)। Traceroute হলো প্রতিটি মাইলফলকে দাঁড়িয়ে জিজ্ঞেস করা 'এখানে কতক্ষণ লেগেছে?'",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Subnetting — host bits কে network-এর জন্য borrow করো (যেমন 192.168.1.0/26 → 4 subnets of 62 hosts)।",
          "CIDR — prefixes aggregate করো (যেমন 192.168.0.0/22 চারটি /24-এর জন্য)।",
          "Distance Vector — Bellman-Ford, periodic updates (RIP)।",
          "Link State — Dijkstra, full topology (OSPF)।",
          "Flooding — incoming ব্যতীত সব ports-এ পাঠাও (LSA distribution)।",
          "NAT — private ও public IPs এর মধ্যে map করো (home router একটি public IP share করে)।",
          "ICMP — error reporting ও diagnostics (ping, traceroute)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Network Layer বোঝা জরুরি কারণ এটি পুরো Internet-এর routing-এর ভিত্তি। পরের chapter-এ আমরা Transport Layer-এ যাব — যেখানে TCP ও UDP end-to-end communication handle করে।",
      },
    ],
  },

'''

new_text = before + NEW_CH5 + after

# Verify
assert 'id: "net-network-layer"' in new_text, "net-network-layer missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'id: "net-data-link"' in new_text, "net-data-link missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 05 (Network Layer) added. File size: {len(new_text)} bytes")
