#!/usr/bin/env python3
"""
Add Networking Ch 09 — Congestion Control & QoS (Maximum Bangla + English terms).
Rename: TCP Ch 09 → Ch 10, HTTP Ch 10 → Ch 11.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 09 → Ch 10, HTTP Ch 10 → Ch 11
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 09 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 10 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 10 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 11 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 09 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH9 = r'''  {
    id: "net-qos",
    subject: "net",
    title: "Ch 09 — Congestion Control & QoS",
    bangla: "কনজেশন কন্ট্রোল ও কোয়ালিটি অফ সার্ভিস",
    difficulty: "Medium",
    est: "1.5 hr",
    summary:
      "Congestion তখন হয় যখন network resources-এর চাহিদা available capacity-কে exceed করে। এই chapter-এ congestion control mechanisms, traffic shaping algorithms (leaky bucket, token bucket), ও key Quality of Service (QoS) parameters (delay, jitter, bandwidth) cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "causes", title: "Causes of Congestion" },
      {
        type: "p",
        text: "Congestion তখন হয় যখন network resources-এর চাহিদা available capacity-কে exceed করে। Common causes গুলো হলো:",
      },
      {
        type: "list",
        items: [
          "High traffic bursts — একাধিক sources থেকে হঠাৎ data-এর spikes।",
          "Insufficient link bandwidth — slow links bottleneck হয়ে যায়।",
          "Buffer overflow at routers — queues ভরে গেলে packets drop করা হয়।",
          "Slow receiver processing — receiver incoming data-র সাথে পাল্লা দিতে পারে না।",
          "Retransmissions — lost packets আরও traffic trigger করে, পরিস্থিতি আরও খারাপ করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি traffic jam। খুব বেশি গাড়ি একটি narrow road-এ ঢুকে পড়ে (high traffic bursts)। Road অনেক narrow (insufficient bandwidth)। Traffic signal-এ অনেক গাড়ি queue করে (buffer overflow)। কেউ slowly চলে (slow receiver)। কেউ পিছনে ফিরে আবার চেষ্টা করে (retransmissions)। সব মিলে একটা deadlock।",
      },

      { type: "h2", id: "traffic-shaping", title: "Traffic Shaping" },
      {
        type: "p",
        text: "Traffic shaping data transmission-এর rate ও burstiness control করে congestion avoid করতে। দুটি main algorithm আছে — Leaky Bucket ও Token Bucket।",
      },

      { type: "h3", title: "Leaky Bucket" },
      {
        type: "p",
        text: "Leaky Bucket algorithm input bursts নির্বিশেষে একটি constant output rate enforce করে। এটি নিচে একটি ছোট hole সহ bucket-এর মতো কাজ করে। Packets arbitrary rate-এ arrive করে, একটি bucket (queue)-তে রাখা হয়। Bucket একটি fixed rate-এ packets transmit (leak) করে। যদি bucket overflow হয়, packets discard করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bucket যার তলায় একটি ছোট গর্ত। আপনি যেভাবেই পানি ঢালুন (packets arrive), পানি গর্ত দিয়ে একটি constant rate-এ বের হবে। বেশি পানি ঢাললে bucket ভরে গিয়ে overflow হবে — বাড়তি পানি পড়ে যাবে (packets dropped)।",
      },
      {
        type: "multi-code",
        filename: "leaky_bucket",
        codeSamples: {
          cpp: `#include <iostream>
#include <queue>
using namespace std;

class LeakyBucket {
    queue<int> bucket;
    int capacity, leak_rate;
public:
    LeakyBucket(int cap, int rate) : capacity(cap), leak_rate(rate) {}

    // Try to add a packet. Returns true if accepted.
    bool add_packet(int id) {
        if ((int)bucket.size() >= capacity) return false;
        bucket.push(id);
        return true;
    }

    // Transmit 'leak_rate' packets.
    void leak() {
        for (int i = 0; i < leak_rate && !bucket.empty(); i++) {
            cout << "Transmitted packet " << bucket.front() << '\\n';
            bucket.pop();
        }
    }
};

int main() {
    LeakyBucket lb(5, 1);  // capacity=5, leak=1/sec
    // 10 packets arrive simultaneously
    for (int i = 1; i <= 10; i++) {
        if (!lb.add_packet(i))
            cout << "Dropped packet " << i << '\\n';
    }
    // Leak 1 per second for 5 seconds
    for (int t = 0; t < 5; t++) lb.leak();
}`,
          go: `package main

import "fmt"

type LeakyBucket struct {
    bucket    []int
    capacity  int
    leakRate  int
}

func NewLeakyBucket(cap, rate int) *LeakyBucket {
    return &LeakyBucket{capacity: cap, leakRate: rate}
}

func (lb *LeakyBucket) AddPacket(id int) bool {
    if len(lb.bucket) >= lb.capacity { return false }
    lb.bucket = append(lb.bucket, id)
    return true
}

func (lb *LeakyBucket) Leak() {
    for i := 0; i < lb.leakRate && len(lb.bucket) > 0; i++ {
        fmt.Printf("Transmitted packet %d\\n", lb.bucket[0])
        lb.bucket = lb.bucket[1:]
    }
}

func main() {
    lb := NewLeakyBucket(5, 1)
    for i := 1; i <= 10; i++ {
        if !lb.AddPacket(i) {
            fmt.Printf("Dropped packet %d\\n", i)
        }
    }
    for t := 0; t < 5; t++ { lb.Leak() }
}`,
          python: `from collections import deque

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.bucket = deque()
        self.capacity = capacity
        self.leak_rate = leak_rate

    def add_packet(self, pkt_id):
        if len(self.bucket) >= self.capacity:
            return False
        self.bucket.append(pkt_id)
        return True

    def leak(self):
        for _ in range(self.leak_rate):
            if not self.bucket:
                break
            print(f"Transmitted packet {self.bucket.popleft()}")

lb = LeakyBucket(5, 1)  # capacity=5, leak=1/sec
for i in range(1, 11):
    if not lb.add_packet(i):
        print(f"Dropped packet {i}")
for _ in range(5):
    lb.leak()`,
          java: `import java.util.*;

public class LeakyBucket {
    Queue<Integer> bucket = new LinkedList<>();
    int capacity, leakRate;

    LeakyBucket(int cap, int rate) { capacity = cap; leakRate = rate; }

    boolean addPacket(int id) {
        if (bucket.size() >= capacity) return false;
        bucket.add(id);
        return true;
    }

    void leak() {
        for (int i = 0; i < leakRate && !bucket.isEmpty(); i++) {
            System.out.println("Transmitted packet " + bucket.poll());
        }
    }

    public static void main(String[] args) {
        LeakyBucket lb = new LeakyBucket(5, 1);
        for (int i = 1; i <= 10; i++) {
            if (!lb.addPacket(i))
                System.out.println("Dropped packet " + i);
        }
        for (int t = 0; t < 5; t++) lb.leak();
    }
}`,
        },
      },

      { type: "h3", title: "Token Bucket" },
      {
        type: "p",
        text: "Token Bucket একটি নির্দিষ্ট limit পর্যন্ত bursts allow করে যখন average rate-ও shape করে। Tokens একটি constant rate-এ bucket-এ যোগ করা হয়। একটি packet শুধু তখনই transmit হতে পারে যখন যথেষ্ট tokens available। Bucket একটি নির্দিষ্ট সংখ্যক tokens (b) hold করে (burst size)। Tokens গুলো r tokens/sec rate-এ arrive করে। প্রতিটি packet t tokens consume করে। Bucket ভর্তি থাকলে নতুন tokens discard করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি amusement park-এর ride tokens। আপনি প্রতি মিনিটে একটি token পান (token generation rate)। আপনি সেগুলো জমা করতে পারেন সর্বোচ্চ ১০টি (bucket size)। যদি আপনি ১০টি token জমিয়ে রাখেন, আপনি একসাথে ১০টি ride করতে পারবেন (burst)। কিন্তু দীর্ঘ সময়ে আপনি প্রতি মিনিটে একটি ride পাবেন (average rate)।",
      },
      {
        type: "multi-code",
        filename: "token_bucket",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
using namespace std;

class TokenBucket {
    double tokens = 0;
    int capacity, rate;
public:
    TokenBucket(int cap, int r) : capacity(cap), rate(r) {}

    // Add tokens based on time elapsed (seconds).
    void refill(double elapsed) {
        tokens = min((double)capacity, tokens + elapsed * rate);
    }

    // Try to send a packet consuming 'cost' tokens.
    bool send(int cost) {
        if (tokens >= cost) {
            tokens -= cost;
            cout << "Sent packet (cost=" << cost
                 << ", tokens left=" << tokens << ")\\n";
            return true;
        }
        cout << "Dropped (tokens=" << tokens
             << ", needed=" << cost << ")\\n";
        return false;
    }
};

int main() {
    TokenBucket tb(10, 2);  // capacity=10, rate=2/sec
    tb.refill(5);           // 5 seconds → 10 tokens
    tb.send(3);             // ok, 7 left
    tb.send(5);             // ok, 2 left
    tb.send(5);             // drop, only 2
}`,
          go: `package main

import "fmt"

type TokenBucket struct {
    tokens   float64
    capacity int
    rate     int
}

func NewTokenBucket(cap, r int) *TokenBucket {
    return &TokenBucket{capacity: cap, rate: r}
}

func (tb *TokenBucket) Refill(elapsed float64) {
    tb.tokens = float64(tb.capacity)
    if t := tb.tokens + elapsed*float64(tb.rate); t < float64(tb.capacity) {
        tb.tokens = t
    }
}

func (tb *TokenBucket) Send(cost int) bool {
    if tb.tokens >= float64(cost) {
        tb.tokens -= float64(cost)
        fmt.Printf("Sent (tokens left=%.1f)\\n", tb.tokens)
        return true
    }
    fmt.Printf("Dropped (tokens=%.1f, needed=%d)\\n", tb.tokens, cost)
    return false
}

func main() {
    tb := NewTokenBucket(10, 2)
    tb.Refill(5)
    tb.Send(3)
    tb.Send(5)
    tb.Send(5)
}`,
          python: `class TokenBucket:
    def __init__(self, capacity, rate):
        self.tokens = 0
        self.capacity = capacity
        self.rate = rate

    def refill(self, elapsed):
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)

    def send(self, cost):
        if self.tokens >= cost:
            self.tokens -= cost
            print(f"Sent (tokens left={self.tokens:.1f})")
            return True
        print(f"Dropped (tokens={self.tokens:.1f}, needed={cost})")
        return False

tb = TokenBucket(10, 2)  # capacity=10, rate=2/sec
tb.refill(5)             # 5 sec → 10 tokens
tb.send(3)               # ok, 7 left
tb.send(5)               # ok, 2 left
tb.send(5)               # drop, only 2`,
          java: `public class TokenBucket {
    double tokens = 0;
    int capacity, rate;

    TokenBucket(int cap, int r) { capacity = cap; rate = r; }

    void refill(double elapsed) {
        tokens = Math.min(capacity, tokens + elapsed * rate);
    }

    boolean send(int cost) {
        if (tokens >= cost) {
            tokens -= cost;
            System.out.printf("Sent (tokens left=%.1f)%n", tokens);
            return true;
        }
        System.out.printf("Dropped (tokens=%.1f, needed=%d)%n", tokens, cost);
        return false;
    }

    public static void main(String[] args) {
        TokenBucket tb = new TokenBucket(10, 2);
        tb.refill(5);
        tb.send(3);
        tb.send(5);
        tb.send(5);
    }
}`,
        },
      },

      { type: "h3", title: "Leaky Bucket vs Token Bucket" },
      {
        type: "list",
        items: [
          "Output rate — Leaky Bucket: strictly constant; Token Bucket: varies, up to peak burst rate।",
          "Burst handling — Leaky Bucket: কোনো bursts allow করে না; Token Bucket: bursts allow করে (bucket size পর্যন্ত)।",
          "Long-term average rate — Leaky Bucket: fixed leak rate; Token Bucket: token generation rate।",
          "Packet discard — Leaky Bucket: bucket overflow হলে; Token Bucket: packet wait করে বা drop হয়।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Leaky Bucket হলো একটি faucet যা সবসময় একটি constant rate-এ পানি দেয়, আপনি যতই পানি ঢালুন। Token Bucket হলো একটি savings account — আপনি প্রতি মাসে একটি fixed amount পান, জমা করতে পারেন, এবং একসাথে বেশি খরচ করতে পারেন (burst) — কিন্তু দীর্ঘমেয়াদে average ঠিক থাকে।",
      },

      { type: "h2", id: "qos", title: "Quality of Service (QoS)" },
      {
        type: "p",
        text: "QoS বলতে বিভিন্ন traffic types-কে বিভিন্ন priority levels provide করার ability বোঝায়, যা predictable performance ensure করে।",
      },

      { type: "h3", title: "Delay (Latency)" },
      {
        type: "p",
        text: "Delay হলো সেই সময় যেটা একটি packet source থেকে destination-এ যেতে নেয়। Components গুলো হলো — Processing delay (bit errors ও header check করার সময়), Queuing delay (output buffer-এ wait করার সময়), Transmission delay (bits কে link-এ push করার সময়), Propagation delay (signal-এর medium-এ travel করার সময়)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি letter পাঠানো। Processing delay হলো letter লেখার সময়। Queuing delay হলো post office-এ queue-এ দাঁড়ানো। Transmission delay হলো postman-এর letter নেওয়ার সময়। Propagation delay হলো letter-এর রাস্তা দিয়ে যাওয়ার সময়। উদাহরণ — online gaming-এ round-trip delay (ping) 100 ms-এর বেশি হলে noticeable; 200 ms-এর বেশি হলে game unresponsive লাগে।",
      },

      { type: "h3", title: "Jitter" },
      {
        type: "p",
        text: "Jitter হলো packet arrival times-এর variation। High jitter real-time applications (VoIP, video conferencing)-এ সমস্যা তৈরি করে কারণ packets uneven intervals-এ play out হয়। উদাহরণ — একটি VoIP call-এ 50 ms jitter থাকলে jitter buffer প্রয়োজন (যা delay যোগ করে) playback smooth করতে; নাহলে audio choppy হয়ে যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি একটি restaurant-এ order করছেন। কখনো food ৫ মিনিটে আসে, কখনো ২০ মিনিটে। এই variation হলো jitter। যদি food সবসময় ১০ মিনিটে আসত (low jitter), আপনি প্রস্তুত থাকতেন। কিন্তু variation থাকলে আপনি হয়তো আগেই খেয়ে ফেলেছেন বা অনেকক্ষণ wait করছেন।",
      },

      { type: "h3", title: "Bandwidth" },
      {
        type: "p",
        text: "Bandwidth হলো একটি network path-এর maximum data rate (throughput)। সাধারণত bits per second (bps)-এ measured হয়। বিভিন্ন applications-এর বিভিন্ন bandwidth requirements আছে — Email/Web (< 1 Mbps, delay tolerant), Video streaming (3-25 Mbps, stable throughput প্রয়োজন), 4K Video call (15-30 Mbps, jitter sensitive), Large file download (100+ Mbps, শুধু speed গুরুত্বপূর্ণ)।",
      },
      {
        type: "p",
        text: "Real-life thinking — bandwidth হলো একটি highway-এর lanes সংখ্যা। একটি single-lane road-এ (low bandwidth) একসাথে অল্প গাড়ি যেতে পারে। একটি 8-lane highway-তে (high bandwidth) অনেক গাড়ি একসাথে যেতে পারে। QoS হলো কিছু lanes-কে emergency vehicles-এর জন্য reserve করা — তারা সবসময় চলতে পারে, traffic যাই হোক না কেন।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Congestion — resources-এর oversubscription থেকে হয়; shaping ও QoS এটি mitigate করতে help করে।",
          "Leaky bucket — constant output rate enforce করে; Token bucket — controlled bursts allow করে।",
          "QoS parameters (delay, jitter, bandwidth) — performance expectations define করে।",
          "Real-time apps — বিশেষত jitter ও delay-এ sensitive।",
          "এই mechanisms modern networks-এ implemented হয় (যেমন DiffServ, traffic policing, RED queue management) — fair ও predictable communication ensure করতে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Congestion control ও QoS বোঝা জরুরি কারণ এগুলো modern networks-এ reliable ও predictable communication ensure করে। পরের chapter-এ আমরা TCP-র 3-way handshake ও তারপর HTTP methods-এ যাব।",
      },
    ],
  },

'''

new_text = before + NEW_CH9 + after

# Verify
assert 'id: "net-qos"' in new_text, "net-qos missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 09 (Congestion Control & QoS) added. File size: {len(new_text)} bytes")
