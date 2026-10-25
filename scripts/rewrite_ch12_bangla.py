#!/usr/bin/env python3
"""
Rewrite Ch 12 (Distributed OS) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch12_marker_start = "// ---- Ch 12 - Distributed OS ----"
ch13_marker_start = "// ---- Ch 13 - Advanced Topics ----"

start_idx = text.find(ch12_marker_start)
assert start_idx != -1, "Ch 12 marker not found"
end_idx = text.find(ch13_marker_start, start_idx)
assert end_idx != -1, "Ch 13 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH12 = r'''// ---- Ch 12 - Distributed OS ----
  {
    id: "os-distributed",
    subject: "os",
    title: "Ch 12 — Distributed OS",
    bangla: "ডিস্ট্রিবিউটেড অপারেটিং সিস্টেম",
    difficulty: "Hard",
    est: "2.5 hr",
    summary:
      "Distributed operating system independent computers (nodes)-এর একটি collection manage করে যেগুলো users-দের কাছে একটি single coherent system হিসেবে appear করে। এই chapter-এ core concepts introduce করা হয়েছে — system models, communication, synchronization, mutual exclusion, distributed file systems, ও consensus algorithms।",
    sections: [
      { type: "h2", id: "models", title: "Distributed System Models" },
      {
        type: "p",
        text: "Distributed systems কীভাবে nodes interact করে ও resources share করে তার উপর ভিত্তি করে classify করা যেতে পারে। দুটি main model আছে।",
      },
      { type: "h3", title: "Client-Server Model" },
      {
        type: "p",
        text: "এক বা একাধিক servers services provide করে (যেমন file storage, database) clients যারা request করে। Servers passive (request-এর জন্য wait করে); clients active (request initiate করে)। Examples — Web browsing (browser client, web server), email (mail client, mail server)। Communication — network-এর উপর request-reply (প্রায়ই TCP/IP)।",
      },
      { type: "h3", title: "Peer-to-Peer (P2P) Model" },
      {
        type: "p",
        text: "সব nodes (peers) সমান — প্রত্যেকটি client ও server উভয় হিসেবে act করতে পারে। কোনো central coordinator নেই। Resources সরাসরি peers-এর মধ্যে share করা হয়। Examples — BitTorrent (file sharing), Bitcoin (blockchain), Skype (early version)। Challenges — discovery, security, fault tolerance, incentive mechanisms।",
      },
      {
        type: "p",
        text: "Real-life thinking — Client-server হলো একটি library যেখানে একজন central librarian (server) আছে — patrons (clients) librarian-কে books চায়। Peer-to-peer হলো একটি study group যেখানে প্রতিটি member books আনে এবং directly share করে — কোনো leader নেই।",
      },

      { type: "h2", id: "rpc", title: "Remote Procedure Call (RPC) ও Message Passing" },
      {
        type: "p",
        text: "Distributed components network-এর উপর messages send করে communicate করে। দুটি dominant model আছে।",
      },
      { type: "h3", title: "Message Passing" },
      {
        type: "p",
        text: "Processes explicitly messages send ও receive করে send(destination, message) ও receive(source, message) use করে। Synchronous (blocking) — sender receiver message accept করা পর্যন্ত wait করে। Simpler কিন্তু slower। Asynchronous (non-blocking) — sender immediately continue করে; messages buffer হয়। বেশি efficient কিন্তু care প্রয়োজন।",
      },
      { type: "h3", title: "Remote Procedure Call (RPC)" },
      {
        type: "p",
        text: "Communication-কে একটি local procedure call-এর মতো দেখায়। Client একটি function call করে; RPC system arguments marshal করে, server-এ একটি request পাঠায়, results unmarshal করে, এবং সেগুলো return করে।",
      },
      { type: "h3", title: "RPC-র ধাপ" },
      {
        type: "list",
        items: [
          "১. Client foo(args) call করে (client stub)।",
          "২. Stub args-কে একটি message-এ marshal করে।",
          "৩. Transport server-এ message পাঠায়।",
          "৪. Server stub args unmarshal করে, local foo call করে।",
          "৫. Results marshal হয়ে ফিরে পাঠানো হয়।",
          "৬. Client stub result unmarshal করে এবং client-এ return করে।",
        ],
      },
      { type: "h3", title: "RPC-র Challenges" },
      {
        type: "list",
        items: [
          "Binding — client কীভাবে server-এর address জানবে? (Registry, naming service)",
          "Failure modes — server crash, network partition, lost messages।",
          "Idempotency — retry করা লাগতে পারে duplicate effects ছাড়া।",
        ],
      },
      {
        "type": "p",
        text: "Real-life thinking — একজন interpreter সহ একটি phone call। আপনি English-এ কথা বলেন (local call); interpreter Japanese-এ translate করে (message), অন্য ব্যক্তি answer করে; interpreter ফিরিয়ে translate করে। আপনাকে language বা phone network details জানতে হবে না।",
      } as any,
      {
        type: "multi-code",
        filename: "rpc_demo",
        codeSamples: {
          cpp: `#include <iostream>
#include <string>
#include <thread>
#include <vector>
// Simplified in-memory RPC demo (no real network).
// In real RPC you'd use gRPC, Apache Thrift, or similar.

// "Server" function: registered under name "add"
int add(int a, int b) { return a + b; }

// "Client stub" simulates marshalling + remote call
int rpc_call(const std::string& func, int a, int b) {
    if (func == "add") return add(a, b);
    throw std::runtime_error("unknown function");
}

int main() {
    std::cout << "rpc_call('add', 3, 4) = "
              << rpc_call("add", 3, 4) << '\\n';  // 7
}`,
          go: `package main

import "fmt"

// "Server" function
func add(a, b int) int { return a + b }

// "Client stub" simulates marshalling + remote call
func rpcCall(funcName string, a, b int) int {
    if funcName == "add" {
        return add(a, b)
    }
    panic("unknown function")
}

func main() {
    fmt.Println("rpcCall('add', 3, 4) =", rpcCall("add", 3, 4))  // 7
}`,
          python: `# Simplified in-memory RPC demo (no real network).
# In real RPC you'd use gRPC, Apache Thrift, or xmlrpc.

# "Server" function
def add(a, b):
    return a + b

# "Client stub" simulates marshalling + remote call
def rpc_call(func_name, a, b):
    if func_name == "add":
        return add(a, b)
    raise ValueError("unknown function")

print("rpc_call('add', 3, 4) =", rpc_call("add", 3, 4))  # 7`,
          java: `// Simplified in-memory RPC demo.
import java.util.*;
import java.util.function.*;

public class RpcDemo {
    static Map<String, BiFunction<Integer, Integer, Integer>> registry = new HashMap<>();

    static {
        registry.put("add", (a, b) -> a + b);
    }

    // "Client stub"
    static int rpcCall(String func, int a, int b) {
        BiFunction<Integer, Integer, Integer> f = registry.get(func);
        if (f == null) throw new RuntimeException("unknown function");
        return f.apply(a, b);
    }

    public static void main(String[] args) {
        System.out.println("rpcCall('add', 3, 4) = " + rpcCall("add", 3, 4));
    }
}`,
        },
      },

      { type: "h2", id: "transparency", title: "Network Transparency ও Naming" },
      {
        type: "p",
        text: "Network transparency মানে users ও applications বুঝতে পারবে না যে একটি resource local না remote। এটি achieve করতে, distributed systems-এ একটি unified naming scheme প্রয়োজন।",
      },
      { type: "h3", title: "Naming Requirements" },
      {
        type: "list",
        items: [
          "Location transparency — একটি resource-এর name তার physical location reveal করবে না (যেমন file://server/share/doc.txt — সম্পূর্ণ transparent না; ভালো: UUID)।",
          "Location independence — resource move হতে পারে তার name change না করে।",
        ],
      },
      { type: "h3", title: "Approaches" },
      {
        type: "list",
        items: [
          "Host+path — যেমন NFS: server:/path। Low transparency (name-এ server include আছে)।",
          "Global namespace — যেমন AFS (Andrew File System): /afs/cs.cmu.edu/file। Medium (cell name include আছে)।",
          "Unique identifiers — UUIDs, content-addressed storage (IPFS)। High (location opaque)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Host+path হলো 'Room 204-এ John' (transparent না — John move করলে name change)। Global namespace হলো 'John, employee ID 4711' (transparent — HR জানে John কোথায় sit করে)। UUID হলো John-এর biometric template — আপনি তার fingerprint scan করেন তাকে যেকোনো জায়গায় find করতে।",
      },

      { type: "h2", id: "clocks", title: "Distributed Synchronization: Lamport ও Vector Clocks" },
      {
        type: "p",
        text: "Distributed systems-এ, বিভিন্ন nodes-এ physical clocks drift হতে পারে। Events order করতে আমরা logical clocks use করি।",
      },
      { type: "h3", title: "Lamport Clock (Lamport Timestamp)" },
      {
        type: "p",
        text: "প্রতিটি process একটি counter maintain করে। Rules — একটি process-এর ভেতরে event হলে counter increment করো। Message send করার সময়, current counter include করো। Message receive করার সময়, local counter = max(local, received) + 1 set করো।",
      },
      { type: "h3", title: "Happens-before relation (→)" },
      {
        type: "list",
        items: [
          "যদি a ও b একই process-এ events হয় এবং a-র আগে b ঘটে, তাহলে a → b।",
          "যদি a একটি message send করে এবং b সেটি receive করে, তাহলে a → b।",
          "যদি a → b এবং b → c, তাহলে a → c।",
        ],
      },
      {
        type: "p",
        text: "Lamport clocks satisfy করে: যদি a → b হয় তাহলে L(a) < L(b)। তবে L(a) < L(b) হলে a → b imply করে না (concurrent events-এ arbitrary order থাকতে পারে)।",
      },
      { type: "h3", title: "Vector Clock" },
      {
        type: "p",
        text: "প্রতিটি process N দৈর্ঘ্যের একটি vector রাখে (processes-এর সংখ্যা)। Rules — Internal event-এ নিজের entry increment করো। Send-এ নিজের entry increment করো, সম্পূর্ণ vector send করো। Receive-এ প্রতিটি entry max(local, received)-এ update করো, তারপর নিজের entry increment করো। Properties — V(a) < V(b) component-wise iff a → b। Concurrent events-এর incomparable vectors থাকে।",
      },
      {
        type: "p",
        text: "Real-life thinking — Lamport clock হলো একটি bakery-তে একটি counter। Tickets events-এর order বলে কিন্তু ৫ ও ৫ সহ দুটি tickets unrelated হতে পারে। Vector clock হলো একটি log যেখানে প্রত্যেকের নিজস্ব counter আছে। Logs compare করলে ঠিক কে কখন কী জানত তা reveal করে।",
      },
      {
        type: "multi-code",
        filename: "lamport_clock",
        codeSamples: {
          cpp: `#include <atomic>
#include <iostream>
#include <mutex>

class LamportClock {
    std::atomic<int> t{0};
    std::mutex m;
public:
    int local() {
        std::lock_guard<std::mutex> lk(m);
        return ++t;
    }
    int send() {
        std::lock_guard<std::mutex> lk(m);
        return ++t;
    }
    int receive(int msgTs) {
        std::lock_guard<std::mutex> lk(m);
        int cur = t.load();
        if (msgTs > cur) t = msgTs;
        return ++t;
    }
};

int main() {
    LamportClock a, b;
    a.local();                  // a=1
    int m = a.send();           // a=2, message carries 2
    b.local();                  // b=1
    b.receive(m);               // b=max(1,2)+1=3
    std::cout << "a=" << a.local() << " b=" << b.local() << '\\n';
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

type LamportClock struct {
    mu sync.Mutex
    t  int
}

func (c *LamportClock) Local() int {
    c.mu.Lock(); defer c.mu.Unlock()
    c.t++
    return c.t
}
func (c *LamportClock) Send() int {
    c.mu.Lock(); defer c.mu.Unlock()
    c.t++
    return c.t
}
func (c *LamportClock) Receive(msgTs int) int {
    c.mu.Lock(); defer c.mu.Unlock()
    if msgTs > c.t { c.t = msgTs }
    c.t++
    return c.t
}

func main() {
    var a, b LamportClock
    a.Local()
    m := a.Send()
    b.Local()
    b.Receive(m)
    fmt.Printf("a=%d b=%d\\n", a.Local(), b.Local())
}`,
          python: `import threading

class LamportClock:
    def __init__(self):
        self.t = 0
        self.lock = threading.Lock()

    def local(self):
        with self.lock:
            self.t += 1
            return self.t

    def send(self):
        with self.lock:
            self.t += 1
            return self.t

    def receive(self, msg_ts):
        with self.lock:
            self.t = max(self.t, msg_ts) + 1
            return self.t

a, b = LamportClock(), LamportClock()
a.local()
m = a.send()
b.local()
b.receive(m)
print(f"a={a.local()} b={b.local()}")`,
          java: `import java.util.concurrent.atomic.AtomicInteger;

class LamportClock {
    private final AtomicInteger t = new AtomicInteger(0);
    public int local() { return t.incrementAndGet(); }
    public int send()  { return t.incrementAndGet(); }
    public synchronized int receive(int msgTs) {
        int cur = t.get();
        if (msgTs > cur) t.set(msgTs);
        return t.incrementAndGet();
    }
}

public class LamportDemo {
    public static void main(String[] args) {
        LamportClock a = new LamportClock();
        LamportClock b = new LamportClock();
        a.local();
        int m = a.send();
        b.local();
        b.receive(m);
        System.out.println("a=" + a.local() + " b=" + b.local());
    }
}`,
        },
      },

      { type: "h2", id: "mutual-exclusion", title: "Distributed Mutual Exclusion" },
      {
        type: "p",
        text: "বিভিন্ন machines-এর processes-কে একটি shared resource access করতে হতে পারে (যেমন একটি printer, একটি file)। তিনটি classic algorithm আছে।",
      },
      { type: "h3", title: "১. Centralized Algorithm" },
      {
        type: "p",
        text: "একজন coordinator (server) permission grant করে। একটি process request পাঠায়; যদি অন্য কেউ resource hold করে না থাকে, coordinator grant করে; নাহলে, process queue হয়। Pros — simple, fair, minimal messages (৩টি per critical section: request, grant, release)। Cons — single point of failure; coordinator bottleneck।",
      },
      { type: "h3", title: "২. Distributed Algorithm (Ricart-Agrawala)" },
      {
        type: "p",
        text: "সব processes সমান। যখন একটি process critical section-এ ঢুকতে চায়, সে একটি request (Lamport timestamp সহ) সব অন্য processes-এ পাঠায়। সে তখনই ঢোকে যখন সব অন্যরা 'OK' reply করে। একটি process immediately reply করে যদি সে resource না চায়, অথবা তার নিজের request-এর later timestamp থাকে (higher number = lower priority)। নাহলে, সে request queue করে। Messages — 2×(N-1) per entry (request + reply)। High overhead।",
      },
      { type: "h3", title: "৩. Token-Based Algorithm (Token Ring)" },
      {
        type: "p",
        text: "একটি single token processes-এর মধ্যে একটি logical ring-এ circulate করে। একটি process তখনই critical section-এ ঢুকতে পারে যখন সে token hold করে। Pros — কোনো starvation নেই; low demand-এ low overhead (token pass হয়ে যায়)। Cons — lost token recovery প্রয়োজন; latency ring size-এর অনুপাতে।",
      },
      { type: "h3", title: "Mutual Exclusion Algorithms Comparison" },
      {
        type: "list",
        items: [
          "Centralized — 3 messages per CS (req, grant, rel), low fault tolerance (coordinator fail), coordinator yes।",
          "Ricart-Agrawala — 2(N-1) messages per CS, high fault tolerance (যেকোনো process recover করতে পারে), coordinator না।",
          "Token ring — 0 to N messages per CS (token pass), medium (token loss), coordinator না (logical ring)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি office-এ single-key restroom। Centralized — একজন secretary (coordinator) request-এ key hand করে। Distributed — প্রত্যেক employee-এর সব অন্যদের list আছে; আপনি সবাইকে call করেন। যদি অন্য কেউ already restroom-এ থাকে, তারা 'I'm busy' বলে যদি না আপনার timestamp (urgency) higher হয়। Token-based — employees একটি circle-এ sit করে এবং একটি physical key pass করে। যে key hold করে সে শুধু সেই restroom use করতে পারে।",
      },

      { type: "h2", id: "dfs", title: "Distributed File Systems (NFS, AFS)" },
      {
        type: "p",
        text: "Distributed file systems remote servers-এর files-কে local-এর মতো access করতে allow করে।",
      },
      { type: "h3", title: "NFS (Network File System)" },
      {
        type: "list",
        items: [
          "Sun Microsystems (1984) দ্বারা developed। Unix/Linux-এ widely used।",
          "Protocol — stateless; প্রতিটি request independent (server client state remember করে না)।",
          "Mounting — client একটি remote directory-কে একটি local mount point-এ mount করে (যেমন mount server:/export /mnt)।",
          "Transparency — partial; path server name বা mount convention include করে।",
          "Cache consistency — weak (clients কয়েক সেকেন্ড cache করে; close-to-open consistency)।",
        ],
      },
      { type: "h3", title: "AFS (Andrew File System)" },
      {
        type: "list",
        items: [
          "Carnegie Mellon University (1980s) দ্বারা developed।",
          "Protocol — stateful; server track করে কোন client-এর কোন file আছে।",
          "Whole-file caching — যখন একটি client file open করে, সম্পূর্ণ file local disk (বা memory)-তে fetch হয়। Close হলে, modified হলে, সম্পূর্ণ file ফিরে পাঠানো হয়।",
          "Scalability — cell hierarchy use করে; excellent wide-area performance।",
          "Consistency — callback mechanism; server client-কে notify করার promise করে যখন একটি file change হয়।",
        ],
      },
      { type: "h3", title: "NFS vs AFS Comparison" },
      {
        type: "list",
        items: [
          "State — NFS: stateless; AFS: stateful (callbacks)।",
          "Caching — NFS: block-level, short timeout; AFS: whole-file, long-term।",
          "Scalability — NFS: LAN-এর জন্য ভালো; AFS: WAN-এর জন্য excellent।",
          "Consistency — NFS: close-to-open; AFS: callback + version।",
          "Complexity — NFS: simpler; AFS: বেশি complex।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — NFS হলো একটি library যেখানে আপনি pages একে একে read করতে পারেন, কিন্তু librarian যেকোনো moment-এ book re-shelve করতে পারে (stateless)। AFS হলো আপনি সম্পূর্ণ book check out করেন, বাড়ি নিয়ে যান, এবং library promise করে আপনাকে call করবে যদি অন্য কেউ সেটি দরকার করে (callback)।",
      },

      { type: "h2", id: "consensus", title: "Consensus: Paxos ও Raft (Conceptual)" },
      {
        type: "p",
        text: "Consensus algorithms distributed processes-এর একটি set-কে একটি single value-তে agree করতে allow করে যদি কিছু processes fail (crash বা unreliable) হয়ে যায়। Distributed databases-এ use হয় (যেমন etcd, ZooKeeper, Spanner)।",
      },
      { type: "h3", title: "Paxos" },
      {
        type: "p",
        text: "Leslie Lamport (1990s) দ্বারা developed। Difficult to understand হওয়ার জন্য famous কিন্তু robust। Roles — Proposer (একটি value suggest করে), Acceptor (proposals-এ vote করে), Learner (chosen value learn করে)।",
      },
      { type: "h3", title: "Basic Paxos Phases" },
      {
        type: "list",
        items: [
          "১. Prepare — Proposer acceptors-এর majority-তে prepare(proposal_number) পাঠায়।",
          "২. Promise — Acceptor promise করে যে সে কখনো lower-numbered proposals accept করবে না; last accepted value return করে (যদি থাকে)।",
          "৩. Accept — Proposer accept(proposal_number, value) পাঠায় — value তার নিজের বা returned-টি হতে পারে।",
          "৪. Accepted — Acceptors accept করে যদি তারা higher numbers promise না করে থাকে; majority reached → consensus।",
        ],
      },
      {
        type: "p",
        text: "Paxos-কে a sequence of decisions (log replication)-এর জন্য Multi-Paxos-এ extend করা যায়।",
      },
      { type: "h3", title: "Raft" },
      {
        type: "p",
        text: "Paxos-এর চেয়ে বেশি understandable হওয়ার জন্য designed (Diego Ongaro, 2014)। Leader-based approach use করে।",
      },
      { type: "h3", title: "Raft-র Key Components" },
      {
        type: "list",
        items: [
          "Leader election — একটি server leader; অন্যরা followers। যদি followers leader থেকে কিছু না শুনে (timeout), তারা election শুরু করে।",
          "Log replication — Leader client commands accept করে, তার log-এ append করে, followers-এ replicate করে। যখন majority accept করে, command commit হয়।",
          "Safety — শুধু most up-to-date log যুক্ত leader elect হতে পারে (overwritten entries prevent করে)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Paxos হলো chair ছাড়া একটি committee। প্রত্যেক member একটি motion propose করতে পারে; তারা rounds-এ vote করে, এবং কিছু members absent হতে পারে (fail)। শেষ পর্যন্ত, তারা একটি single outcome-এ agree করে — কিন্তু process complex। Raft হলো একটি team যার একজন elected captain (leader) আছে। Captain সবাইকে বলে কী করতে হবে। Captain disappear হলে, team নতুন captain elect করে। Follow করা অনেক সহজ।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: CAP theorem অনুযায়ী, একটি distributed system একসাথে Consistency, Availability, ও Partition tolerance-এর মধ্যে যেকোনো দুটি পাবে। Network partition এড়ানো যায় না (P mandatory), তাই আসলে CP বা AP-র মধ্যে বেছে নিতে হয়।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Client-server — Centralised server অনেক clients serve করে (web, email)।",
          "Peer-to-peer — সব nodes সমান; কোনো central coordinator নেই (BitTorrent)।",
          "RPC — Remote call local function call-এর মতো দেখায়; network details hide করে।",
          "Message passing — Explicit send/receive; বেশি flexible কিন্তু programmer-visible।",
          "Network transparency — Resource names location hide করে; global namespaces বা UUIDs।",
          "Lamport clock — Logical clock events order করে; যদি a → b তাহলে L(a) < L(b)।",
          "Vector clock — Causal relationships capture করে; concurrent events detect করতে পারে।",
          "Distributed mutual exclusion — Centralised, distributed (Ricart-Agrawala), token-based algorithms।",
          "NFS — Stateless, block-caching, simple, LAN-এর জন্য।",
          "AFS — Stateful, whole-file caching, callbacks, WAN-এর জন্য।",
          "Paxos — Classic consensus; robust কিন্তু complex।",
          "Raft — Leader-based consensus; understandability-র জন্য designed।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Distributed operating systems OS abstraction-কে একাধিক machines জুড়ে extend করে। এই chapter একটি overview provide করেছে, কিন্তু modern large-scale systems build করতে networking, fault tolerance, ও distributed algorithms-এর deeper study essential।",
      },
    ],
  },

'''

# Fix the typo in `as any` block
NEW_CH12 = NEW_CH12.replace(
    '''      {
        "type": "p",
        text: "Real-life thinking — একজন interpreter সহ একটি phone call। আপনি English-এ কথা বলেন (local call); interpreter Japanese-এ translate করে (message), অন্য ব্যক্তি answer করে; interpreter ফিরিয়ে translate করে। আপনাকে language বা phone network details জানতে হবে না।",
      } as any,''',
    '''      {
        type: "p",
        text: "Real-life thinking — একজন interpreter সহ একটি phone call। আপনি English-এ কথা বলেন (local call); interpreter Japanese-এ translate করে (message), অন্য ব্যক্তি answer করে; interpreter ফিরিয়ে translate করে। আপনাকে language বা phone network details জানতে হবে না।",
      },'''
)

new_text = before + NEW_CH12 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 12 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
