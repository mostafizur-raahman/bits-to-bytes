#!/usr/bin/env python3
"""
Rewrite Ch 05 (Deadlocks) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch5_marker_start = "// ---- Ch 05 - Deadlocks ----"
ch6_marker_start = "// ---- Ch 06 - Memory Management ----"

start_idx = text.find(ch5_marker_start)
assert start_idx != -1, "Ch 05 marker not found"
end_idx = text.find(ch6_marker_start, start_idx)
assert end_idx != -1, "Ch 06 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH5 = r'''// ---- Ch 05 - Deadlocks ----
  {
    id: "os-deadlocks",
    subject: "os",
    title: "Ch 05 — Deadlocks",
    bangla: "ডেডলক",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "Multiprogramming environment-এ processes resources-এর জন্য compete করে। কখনো এমন হয় যে কিছু processes চিরকাল stuck হয়ে যায়, প্রত্যেকটি একটি resource-এর জন্য অপেক্ষা করে যেটি এই set-এর অন্য কোনো process hold করে আছে। এই situation হলো deadlock। এই chapter-এ deadlocks কীভাবে হয়, কীভাবে represent করতে হয়, এবং prevent/avoid/detect/ignore করার classic strategies আলোচনা করা হয়েছে।",
    sections: [
      { type: "h2", id: "characterization", title: "Deadlock Characterization" },
      {
        type: "p",
        text: "Deadlock তখন হয় যখন দুটি বা ততোধিক processes প্রত্যেকেই অসীম সময় ধরে একটি event-এর জন্য wait করে (সাধারণত resource release) যেটি শুধু অন্য একটি waiting process ঘটাতে পারে। Deadlock হতে হলে চারটি necessary condition একসাথে hold করতে হবে।",
      },
      { type: "h3", title: "The Four Conditions" },
      {
        type: "list",
        items: [
          "Mutual exclusion — কমপক্ষে একটি resource non-shareable mode-এ hold হতে হবে। এক সময়ে শুধু একটি process সেই resource use করতে পারবে।",
          "Hold and wait — একটি process যে কমপক্ষে একটি resource hold করে আছে, সে অন্যান্য processes-এর hold করা অতিরিক্ত resources acquire করার জন্য wait করছে।",
          "No preemption — Resources কোনো process থেকে জোর করে taken away করা যাবে না। শুধু holding process সেগুলো voluntarily release করতে পারে।",
          "Circular wait — এমন একটি set {P₀, P₁, …, Pₙ} আছে যেখানে P₀ একটি resource-এর জন্য wait করে যেটি P₁ hold করে, P₁ এর জন্য wait করে যেটি P₂ hold করে, …, Pₙ P₀-এর hold করা resource-এর জন্য wait করে।",
        ],
      },
      {
        type: "p",
        text: "চারটিই একসাথে hold হতে হবে। যেকোনো একটি break করলে deadlock impossible — এটাই পরের prevention strategies যা করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — দুটি car একটি four-way stop intersection-এ meet করে। Mutual exclusion — এক সময়ে শুধু একটি car intersection occupy করতে পারে। Hold and wait — প্রতিটি car তার position hold করে এবং অপরটি move করার জন্য wait করে। No preemption — কোনো traffic officer নেই যে car-কে aside push করবে। Circular wait — Car A wait করে Car B clear করার জন্য; Car B wait করে Car A clear করার জন্য। দুটিই block হয়।",
      },

      { type: "h3", title: "Classic two-lock deadlock (code এ)" },
      {
        type: "p",
        text: "নিচে দুটি thread দেখানো হলো যারা প্রত্যেকে একটি mutex grab করে তারপর অপরটির জন্য reach করে। যদি Thread 1 mutexA acquire করে এবং Thread 2 mutexB acquire করে তাদের দ্বিতীয় lock()-এর আগে, দুটোই চিরকাল block হয়। লক্ষ্য করুন এই program হাজার হাজার বার সঠিকভাবে run হতে পারে — deadlock শুধু তখন হয় যখন interleaving ঠিক ভুল হয়, যা এই bugs কে reproduce করা এত কঠিন করে তোলে।",
      },
      {
        type: "multi-code",
        filename: "deadlock_demo",
        codeSamples: {
          cpp: `#include <iostream>
#include <mutex>
#include <thread>

std::mutex mutexA, mutexB;

// Careful! Run this many times — it may deadlock.
void thread1() {
    std::lock_guard<std::mutex> lkA(mutexA);
    // small delay to force interleaving
    for (volatile int i = 0; i < 100000; i++);
    std::lock_guard<std::mutex> lkB(mutexB);
    std::cout << "T1 in critical section\\n";
}

void thread2() {
    std::lock_guard<std::mutex> lkB(mutexB);
    for (volatile int i = 0; i < 100000; i++);
    std::lock_guard<std::mutex> lkA(mutexA);
    std::cout << "T2 in critical section\\n";
}

int main() {
    std::thread t1(thread1), t2(thread2);
    t1.join(); t2.join();
    return 0;
}
// Fix: use std::lock(mutexA, mutexB) — locks both atomically, avoiding deadlock`,
          go: `package main

import (
    "fmt"
    "sync"
    "time"
)

var mutexA, mutexB sync.Mutex

func main() {
    var wg sync.WaitGroup
    wg.Add(2)

    go func() {
        defer wg.Done()
        mutexA.Lock()
        time.Sleep(10 * time.Millisecond)  // force interleaving
        mutexB.Lock()
        fmt.Println("T1 in critical section")
        mutexB.Unlock(); mutexA.Unlock()
    }()

    go func() {
        defer wg.Done()
        mutexB.Lock()
        time.Sleep(10 * time.Millisecond)
        mutexA.Lock()
        fmt.Println("T2 in critical section")
        mutexA.Unlock(); mutexB.Unlock()
    }()

    wg.Wait()
    // This program may deadlock. Fix: always lock in same order.
}`,
          python: `import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()

def thread1():
    with mutexA:
        time.sleep(0.01)  # force interleaving
        with mutexB:
            print("T1 in critical section")

def thread2():
    with mutexB:
        time.sleep(0.01)
        with mutexA:
            print("T2 in critical section")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start(); t2.start()
t1.join(); t2.join()
# May deadlock. Fix: acquire locks in same order in both threads.`,
          java: `public class DeadlockDemo {
    static final Object mutexA = new Object();
    static final Object mutexB = new Object();

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            synchronized (mutexA) {
                try { Thread.sleep(10); } catch (InterruptedException e) {}
                synchronized (mutexB) {
                    System.out.println("T1 in critical section");
                }
            }
        });

        Thread t2 = new Thread(() -> {
            synchronized (mutexB) {
                try { Thread.sleep(10); } catch (InterruptedException e) {}
                synchronized (mutexA) {
                    System.out.println("T2 in critical section");
                }
            }
        });

        t1.start(); t2.start();
        t1.join(); t2.join();
        // May deadlock. Fix: always acquire in same order.
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: উপরের program গুলো deadlock হতে পারে। Fix হলো সব threads-এ একই order-এ locks acquire করা (lock ordering) — এটা circular wait break করে।",
      },

      { type: "h2", id: "rag", title: "Resource Allocation Graph (RAG)" },
      {
        type: "p",
        text: "Resource Allocation Graph (RAG) হলো একটি directed graph যেটি visually resource allocation-এর state represent করে। এটি detect করতে help করে যে deadlock আছে কিনা।",
      },
      { type: "h3", title: "RAG-র components" },
      {
        type: "list",
        items: [
          "Vertices — দুটি প্রকার: Process vertices (circles): P₁, P₂, …, Pₙ। Resource vertices (squares): R₁, R₂, …, Rₘ (প্রতিটির এক বা একাধিক identical instances থাকতে পারে)।",
          "Request edge (Pᵢ → Rⱼ) — Process Pᵢ একটি instance of Rⱼ request করেছে এবং wait করছে।",
          "Assignment edge (Rⱼ → Pᵢ) — Rⱼ-এর একটি instance Pᵢ-কে allocate করা হয়েছে।",
        ],
      },
      {
        type: "p",
        text: "Arrow-এর direction হলো পুরো trick — resource-এর দিকে মানে 'আমি এটা চাইছি', resource থেকে দূরে মানে 'এটা আমার কাছে আছে'।",
      },
      { type: "h3", title: "Reading a RAG — rules" },
      {
        type: "list",
        items: [
          "No cycle → No deadlock, guaranteed।",
          "Cycle, সব resources-এর single instance → Deadlock, guaranteed।",
          "Cycle, কিছু resource-এর multiple instances → Possible deadlock — আরও check প্রয়োজন (detection algorithm run করতে হবে)।",
        ],
      },
      {
        type: "p",
        text: "সংক্ষেপে — cycle হলো deadlock-এর necessary condition, কিন্তু শুধু তখনই sufficient যখন cycle-এর প্রতিটি resource-এর exactly একটি instance আছে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি whiteboard যেখানে দেখানো হয় কে কোন resource hold করে (যেমন printer, scanner) এবং কে কী-এর জন্য wait করছে। Person থেকে resource-এ arrow মানে 'আমি এটা চাই'; resource থেকে person-এ arrow মানে 'এই person-এর কাছে এটা আছে'। আপনি arrow-এর circle দেখলে people deadlock-এ থাকতে পারে।",
      },

      { type: "h2", id: "methods", title: "Methods for Handling Deadlocks" },
      {
        type: "p",
        text: "Operating systems deadlocks handle করার জন্য চারটি approaches-এর একটি use করে — idealistic থেকে pragmatic।",
      },
      {
        type: "list",
        items: [
          "Prevention — নিশ্চিত করা যে চারটি condition-এর অন্তত একটি কখনো hold না করে। Overhead high, rarely used।",
          "Avoidance — extra information use করে carefully resources allocate করা। Overhead medium, fixed resources-এর জন্য feasible।",
          "Detection & Recovery — deadlock হতে দেওয়া, তারপর break করা। Overhead medium, databases-এ common।",
          "Ignorance (Ostrich Algorithm) — ধরে নেওয়া deadlocks হবে না। Overhead none, most general-purpose OSes (Windows, Linux)।",
        ],
      },

      { type: "h2", id: "prevention", title: "1. Deadlock Prevention" },
      {
        type: "p",
        text: "Prevention নিশ্চিত করে যে চারটি necessary condition-এর অন্তত একটি impossible হয়। OS resource allocation এমনভাবে design করে যাতে conditions break হয়।",
      },
      { type: "h3", title: "Breaking Mutual Exclusion" },
      {
        type: "p",
        text: "সাধারণত possible না। কিছু resources inherently non-shareable (যেমন printer)। কিন্তু read-only files-এর জন্য shared access allow করা যায়।",
      },
      { type: "h3", title: "Breaking Hold and Wait" },
      {
        type: "p",
        text: "Process-কে require করা যে সে যা কিছু resources কখনো দরকার তা একসাথে request করবে, অথবা আরও resources request করার আগে সব held resources release করবে। Drawback — low resource utilisation; starvation possible।",
      },
      { type: "h3", title: "Breaking No Preemption" },
      {
        type: "p",
        text: "যদি কোনো process কিছু resources hold করে অন্য একটি unavailable resource request করে, OS জোর করে currently held resources take করে (preempt করে) এবং process-কে restart করে। Drawback — state-যুক্ত resources-এর ক্ষেত্রে implement করা কঠিন (যেমন partially written file)।",
      },
      { type: "h3", title: "Breaking Circular Wait — Lock Ordering" },
      {
        type: "p",
        text: "সব resource types-এ একটি total ordering impose করা। প্রতিটি process-কে increasing order-এ resources request করতে হবে (যেমন tape drive (1), তারপর printer (2), তারপর disk (3))। একটি process higher-numbered resource request করলে সে সব lower-numbered ones already hold করে থাকতে হবে। Practical — কিছু systems-এ used। Linux kernel-এ lock order rules এই প্যাটার্ন follow করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant যেটা circular wait eliminate করে tables-এ numbers assign করে: আপনাকে table 1-এ খেয়ে table 2-এ যেতে হবে, এবং কখনো table 3 থেকে table 2-তে ফিরে যাওয়া যাবে না।",
      },
      {
        type: "multi-code",
        filename: "lock_ordering",
        codeSamples: {
          cpp: `#include <iostream>
#include <mutex>
#include <thread>

std::mutex mutexA, mutexB;

// CORRECT: always lock in the same order — prevents circular wait.
// Convention: lock A first, then B, in BOTH threads.
void thread1() {
    std::lock(mutexA, mutexB);   // atomic lock of both
    std::lock_guard<std::mutex> lkA(mutexA, std::adopt_lock);
    std::lock_guard<std::mutex> lkB(mutexB, std::adopt_lock);
    std::cout << "T1 in critical section\\n";
}

void thread2() {
    std::lock(mutexA, mutexB);   // same order!
    std::lock_guard<std::mutex> lkA(mutexA, std::adopt_lock);
    std::lock_guard<std::mutex> lkB(mutexB, std::adopt_lock);
    std::cout << "T2 in critical section\\n";
}

int main() {
    std::thread t1(thread1), t2(thread2);
    t1.join(); t2.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

var mutexA, mutexB sync.Mutex

func main() {
    var wg sync.WaitGroup
    wg.Add(2)

    // CORRECT: same order in both goroutines — mutexA first, then mutexB
    run := func(name string) {
        defer wg.Done()
        mutexA.Lock()
        mutexB.Lock()
        fmt.Println(name, "in critical section")
        mutexB.Unlock()
        mutexA.Unlock()
    }

    go run("T1")
    go run("T2")
    wg.Wait()
}`,
          python: `import threading

mutexA = threading.Lock()
mutexB = threading.Lock()

# CORRECT: same order in both threads
def thread1():
    with mutexA:
        with mutexB:
            print("T1 in critical section")

def thread2():
    with mutexA:        # same order!
        with mutexB:
            print("T2 in critical section")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start(); t2.start()
t1.join(); t2.join()`,
          java: `public class LockOrdering {
    static final Object mutexA = new Object();
    static final Object mutexB = new Object();

    public static void main(String[] args) throws InterruptedException {
        // CORRECT: same order in both threads — mutexA first, then mutexB
        Runnable r1 = () -> {
            synchronized (mutexA) {
                synchronized (mutexB) {
                    System.out.println("T1 in critical section");
                }
            }
        };
        Runnable r2 = () -> {
            synchronized (mutexA) {  // same order!
                synchronized (mutexB) {
                    System.out.println("T2 in critical section");
                }
            }
        };

        Thread t1 = new Thread(r1), t2 = new Thread(r2);
        t1.start(); t2.start();
        t1.join(); t2.join();
    }
}`,
        },
      },

      { type: "h2", id: "avoidance", title: "2. Deadlock Avoidance — Banker's Algorithm" },
      {
        type: "p",
        text: "Banker's Algorithm (Dijkstra, 1965) deadlock avoid করে resource allocation grant করার আগে simulate করে। OS প্রতিটি process-কে তার maximum resource needs আগে declare করতে বলে।",
      },
      { type: "h3", title: "Safe State কী?" },
      {
        type: "p",
        text: "একটি state safe যদি এমন একটি process sequence থাকে যেখানে প্রতিটি process, তার maximum remaining need দেওয়া হলে, currently available resources ও আগের finished processes-এর held resources দিয়ে finish হতে পারে। যদি কোনো request grant করা একটি unsafe state-এ lead করে, OS সেই request delay করে (process wait করে)।",
      },
      { type: "h3", title: "Data structures (n processes, m resource types)" },
      {
        type: "list",
        items: [
          "Available[m] — প্রতিটি resource-এর available instances।",
          "Max[n][m] — প্রতিটি process-এর maximum demand।",
          "Allocation[n][m] — প্রতিটি process-এ বর্তমানে allocate করা।",
          "Need[n][m] = Max[i][j] - Allocation[i][j] — remaining need।",
        ],
      },
      { type: "h3", title: "Safety Algorithm" },
      {
        type: "list",
        items: [
          "১. Work = Available, Finish[n] = false।",
          "২. এমন একটি i খুঁজে বের করো যেখানে Finish[i]==false এবং Need[i] <= Work।",
          "৩. Work = Work + Allocation[i], Finish[i]=true। Step 2-এ যাও।",
          "৪. যদি সব Finish[i]==true হয়ে যায়, state safe।",
        ],
      },
      { type: "h3", title: "Resource-Request Algorithm (process Pᵢ Request[i] চাইলে)" },
      {
        type: "list",
        items: [
          "১. যদি Request[i] > Need[i], error (maximum exceed হয়েছে)।",
          "২. যদি Request[i] > Available, wait করতে হবে।",
          "৩. Pretend to allocate: Available -= Request[i], Allocation[i] += Request[i], Need[i] -= Request[i]।",
          "৪. Safety Algorithm run করো। যদি safe হয়, real-এ allocate করো; নাহলে roll back করো এবং Pᵢ wait করে।",
        ],
      },
      {
        type: "p",
        text: "Safe, unsafe, ও deadlocked states — এগুলো এক নয়। প্রতিটি deadlocked state unsafe, কিন্তু unsafe state এখনো deadlock না; এটা এমন একটি state যেখান থেকে system deadlock-এ drift হতে পারে। Banker's algorithm conservative — এটা safe region থেকে বের হতে রাজি না।",
      },

      { type: "h3", title: "Worked Example 1 — Single Resource Type" },
      {
        type: "p",
        text: "একটি system-এ একটি resource type-এর 12 instances আছে। P0 (Allocation=5, Max=10, Need=5), P1 (2, 4, 2), P2 (2, 9, 7)। Allocated = 5+2+2 = 9, Available = 12-9 = 3। Safety algorithm চালানো যাক:",
      },
      {
        type: "list",
        items: [
          "Step 1: P1 (Need=2 <= Work=3) → Work = 3+2 = 5",
          "Step 2: P0 (Need=5 <= Work=5) → Work = 5+5 = 10",
          "Step 3: P2 (Need=7 <= Work=10) → Work = 10+2 = 12",
          "সব processes finish হয়ে গেছে → state safe, sequence ⟨P1, P0, P2⟩",
        ],
      },
      {
        type: "p",
        text: "Order এখানে গুরুত্বপূর্ণ। P0 (Need 5 > 3) বা P2 (Need 7 > 3) দিয়ে শুরু করা impossible — শুধু P1 first run করতে পারে, এবং এটা P1 resources return করায় সবাই unblock হয়।",
      },
      {
        type: "p",
        text: "এখন ধরুন P2 আরেকটি instance request করে। Tentatively grant করলে: Allocation[P2]=3, Need[P2]=6, Available=2। Step 1: P1 (Need=2 <= Work=2) → Work=4। Step 2: P0 (Need=5 > 4) ✘, P2 (Need=6 > 4) ✘। কোনো safety sequence নেই, তাই state unsafe। Banker's algorithm P2-এর request deny করে এবং তাকে wait করায় — যদিও resource physically available ছিল।",
      },

      { type: "h3", title: "Worked Example 2 — Multiple Resource Types" },
      {
        type: "p",
        text: "৫টি processes, ৩টি resource types যার totals A=10, B=5, C=7। Standard textbook case। Total allocated = (7, 2, 5), তাই Available = (3, 3, 2)। Safety sequence: ⟨P1, P3, P4, P2, P0⟩। একটি comparison যেমন (1,2,2) ≤ (3,3,2) প্রতিটি resource type-এর জন্য hold হতে হবে — একটি component ওتجا করলে সেই round-এ process disqualify।",
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Exam tip: safety sequences unique না। ⟨P1, P3, P4, P0, P2⟩ ও এখানে কাজ করবে। যেকোনো valid sequence state safe প্রমাণ করে। যদি প্রশ্ন জিজ্ঞাসা করে 'এই state safe কি?', একটি sequence খুঁজে পাওয়াই enough।",
      },

      { type: "h3", title: "Banker's Algorithm — Code implementation" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় Banker's safety algorithm implementation দেখানো হলো। এটি একটি state safe কিনা check করে।",
      },
      {
        type: "multi-code",
        filename: "bankers_safe",
        codeSamples: {
          cpp: `#include <iostream>
#include <vector>
using namespace std;

bool isSafe(vector<int> avail, vector<vector<int>> maxN,
            vector<vector<int>> alloc) {
    int n = maxN.size(), m = avail.size();
    vector<vector<int>> need(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            need[i][j] = maxN[i][j] - alloc[i][j];

    vector<bool> finish(n, false);
    vector<int> work = avail;
    int done = 0;
    while (done < n) {
        bool progressed = false;
        for (int i = 0; i < n; i++) {
            if (finish[i]) continue;
            bool ok = true;
            for (int j = 0; j < m; j++)
                if (need[i][j] > work[j]) { ok = false; break; }
            if (ok) {
                for (int j = 0; j < m; j++) work[j] += alloc[i][j];
                finish[i] = true; done++; progressed = true;
            }
        }
        if (!progressed) break;
    }
    return done == n;
}

int main() {
    vector<int> avail = {3, 3, 2};
    vector<vector<int>> maxN = {{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}};
    vector<vector<int>> alloc = {{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}};
    cout << (isSafe(avail, maxN, alloc) ? "SAFE" : "UNSAFE") << '\\n';
}`,
          go: `package main

import "fmt"

func isSafe(avail []int, maxN, alloc [][]int) bool {
    n := len(maxN); m := len(avail)
    need := make([][]int, n)
    for i := 0; i < n; i++ {
        need[i] = make([]int, m)
        for j := 0; j < m; j++ {
            need[i][j] = maxN[i][j] - alloc[i][j]
        }
    }
    finish := make([]bool, n)
    work := append([]int(nil), avail...)
    done := 0
    for done < n {
        progressed := false
        for i := 0; i < n; i++ {
            if finish[i] { continue }
            ok := true
            for j := 0; j < m; j++ {
                if need[i][j] > work[j] { ok = false; break }
            }
            if ok {
                for j := 0; j < m; j++ { work[j] += alloc[i][j] }
                finish[i] = true; done++; progressed = true
            }
        }
        if !progressed { break }
    }
    return done == n
}

func main() {
    safe := isSafe(
        []int{3, 3, 2},
        [][]int{{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}},
        [][]int{{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}},
    )
    if safe { fmt.Println("SAFE") } else { fmt.Println("UNSAFE") }
}`,
          python: `def is_safe(avail, max_n, alloc):
    n, m = len(max_n), len(avail)
    need = [[max_n[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    work = avail[:]
    done = 0
    while done < n:
        progressed = False
        for i in range(n):
            if finish[i]: continue
            if all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m): work[j] += alloc[i][j]
                finish[i] = True
                done += 1
                progressed = True
        if not progressed: break
    return done == n

avail  = [3, 3, 2]
max_n  = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
alloc  = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
print("SAFE" if is_safe(avail, max_n, alloc) else "UNSAFE")`,
          java: `import java.util.*;

public class Bankers {
    static boolean isSafe(int[] avail, int[][] maxN, int[][] alloc) {
        int n = maxN.length, m = avail.length;
        int[][] need = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                need[i][j] = maxN[i][j] - alloc[i][j];
        boolean[] finish = new boolean[n];
        int[] work = avail.clone();
        int done = 0;
        while (done < n) {
            boolean progressed = false;
            for (int i = 0; i < n; i++) {
                if (finish[i]) continue;
                boolean ok = true;
                for (int j = 0; j < m; j++)
                    if (need[i][j] > work[j]) { ok = false; break; }
                if (ok) {
                    for (int j = 0; j < m; j++) work[j] += alloc[i][j];
                    finish[i] = true; done++; progressed = true;
                }
            }
            if (!progressed) break;
        }
        return done == n;
    }

    public static void main(String[] args) {
        int[] avail = {3, 3, 2};
        int[][] maxN = {{7,5,3},{3,2,2},{9,0,2},{2,2,2},{4,3,3}};
        int[][] alloc = {{0,1,0},{2,0,0},{3,0,2},{2,1,1},{0,0,2}};
        System.out.println(isSafe(avail, maxN, alloc) ? "SAFE" : "UNSAFE");
    }
}`,
        },
      },
      { type: "h3", title: "Banker's Algorithm-র Limitations" },
      {
        type: "list",
        items: [
          "Fixed number of processes/resources প্রয়োজন।",
          "Processes-কে maximum needs declare করতে হবে — প্রায়ই impossible।",
          "প্রতিটি request-এ O(m × n²) overhead।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bank (OS) যেটা কখনো টাকা lend করে না যদি সে সব future customer withdrawal requests satisfy করতে না পারে। Banker জানে প্রতিটি customer-এর credit limit।",
      },

      { type: "h2", id: "detection", title: "3. Deadlock Detection ও Recovery" },
      {
        type: "p",
        text: "Deadlock হতে দাও, detect করো, তারপর break করো। সেইসব systems-এ used যেখানে deadlock rare বা processes long-running।",
      },
      { type: "h3", title: "Detection with Single Instance per Resource" },
      {
        type: "p",
        text: "Wait-for Graph use করো — RAG-র একটি reduced version যেখানে resource nodes remove করা হয়; একটি edge Pᵢ → Pⱼ মানে Pᵢ একটি resource-এর জন্য wait করে যেটি Pⱼ hold করে। Periodic graph cycle detection (যেমন depth-first search) deadlock identify করে। n processes-এর জন্য cycle detection O(n²)।",
      },
      { type: "h3", title: "Detection with Multiple Instances" },
      {
        type: "p",
        text: "Banker's algorithm-এর মতো কিন্তু Max ছাড়া একটি algorithm use করো — শুধু সেই processes গুলো খুঁজে বের করো যারা current available resources দিয়ে finish হতে পারে। যদি কেউই finish না করতে পারে, deadlock আছে।",
      },
      { type: "h3", title: "Detection কতবার run করবে?" },
      {
        type: "p",
        text: "এটা একটি real trade-off। প্রতিটি resource request-এ run করলে deadlock যেই moment-এ form হয় সেই moment-এ catch করে এবং exactly কোন process cause করেছে identify করে, কিন্তু overhead severe। ঘণ্টায় একবার run করলে cheap, কিন্তু অনেক cycles থাকতে পারে এবং কাকে blame করবে তা বলা impossible। একটি common compromise — শুধু তখন detection trigger করা যখন CPU utilisation একটি threshold এর নিচে নেমে যায় (যেমন 40%), কারণ blocked processes সহ একটি system idle হয়ে যায়।",
      },
      { type: "h3", title: "Recovery Options" },
      {
        type: "list",
        items: [
          "Process termination — সব deadlocked processes abort করো (বা একে একে)। Expensive; work হারানো যায়।",
          "Resource preemption — একটি process থেকে resources নাও এবং অন্যকে দাও। Process-কে safe checkpoint-এ rollback করতে হবে, possible starvation।",
        ],
      },
      {
        type: "p",
        text: "Practice-এ অনেক system সহজভাবে system restart করে বা processes manually kill করে। Real-life thinking — একজন system administrator যিনি খেয়াল করেন সব servers stuck — একটি process kill করেন (sledgehammer) বা একটি service restart করেন।",
      },

      { type: "h2", id: "ostrich", title: "4. Deadlock Ignorance — Ostrich Algorithm" },
      {
        type: "p",
        text: "Ostrich Algorithm ধরে নেয় যে deadlocks এত rare যে prevention, avoidance, বা detection-এর overhead খরচের মোক্ষমা নেই। OS deadlocks handle করার জন্য কিছু করে না।",
      },
      {
        type: "list",
        items: [
          "Most general-purpose OSes (Windows, Linux, macOS) এ বেশির ভাগ resource types-এর জন্য used।",
          "কেন? Deadlocks সাধারণত programmer bugs এর কারণে হয়, OS design-এর না। OS locking primitives দেয়; programmer-এর দায়িত্ব circular wait avoid করা।",
          "Deadlock হলে system freeze বা crash করে — user reboot করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — মাথা বালিতে গুঁজে দেওয়া। Ostrich problem ignore করে। অনেক application-এর জন্য acceptable (যেমন আপনার web browser deadlock হলে — আপনি সহজেই restart করেন)।",
      },

      { type: "h2", id: "vs-starvation", title: "Deadlock vs Starvation" },
      {
        type: "p",
        text: "দুটোই একটি process-কে অনেকক্ষণ wait করতে দেয়, তাই সহজে confuse হয়। পার্থক্য হলো wait টা কখনো নিজে থেকে শেষ হতে পারে কিনা।",
      },
      {
        type: "p",
        text: "Deadlock-এ involved processes permanently blocked। System-এ কিছুই change করতে পারে না — তাদের দরকারী resources একে অপরের hold করা, তাই যত সময় wait করলেও কাজ হবে না। Starvation (indefinite postponement ও বলা হয়)-এ process technically still eligible to run। Resources free হয়, কিন্তু scheduler সেগুলো অন্য কাউকে দিয়ে দেয়। একটি starving process যেকোনো moment-এ serve হতে পারে; শুধু কখনো হয় না।",
      },
      { type: "h3", title: "Deadlock vs Starvation — Comparison" },
      {
        type: "list",
        items: [
          "Cause — Deadlock: circular wait, চারটি conditions; Starvation: scheduling বা priority policy যেটা অন্যদের favor করে।",
          "Processes affected — Deadlock: একটি set of processes, একে অপরকে block করে; Starvation: সাধারণত একটি single low-priority process।",
          "Resources — Deadlock: blocked processes-এর নিজেদের দ্বারা held, কখনো release হয় না; Starvation: regularly release হয়, কিন্তু সবসময় অন্য কাউকে allocate হয়।",
          "নিজে থেকে resolve হতে পারে? — Deadlock: কখনো না, বাইরের intervention প্রয়োজন; Starvation: হ্যাঁ, যদি load কমে বা priority shift হয়, process শেষ পর্যন্ত run হতে পারে।",
          "CPU utilisation — Deadlock: involved processes blocked; লক্ষণীয়ভাবে drop; Starvation: system busy — useful কাজ করছে, শুধু victim-এর জন্য না।",
          "Typical remedy — Deadlock: prevention, avoidance (Banker's), detection ও recovery; Starvation: aging — process যত বেশি wait করে তার priority তত বাড়ানো।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Deadlock হলো একটি traffic gridlock যেখানে চারটি car একে অপরকে একটি circle-এ block করে — কেউ আর move করে না যতক্ষণ না একজন traffic officer physically intervene করে। Starvation হলো একজন driver যে busy motorway-এ merge করার চেষ্টা করছে rush hour-এ — road ঠিকঠাক move করছে এবং gaps ও আসছে, কিন্তু দ্রুতগামী car-গুলো সেগুলো নিয়ে যাচ্ছে। Driver যেকোনো moment-এ merge করতে পারে, এবং traffic কমলে একসময় করবে।",
      },
      { type: "h3", title: "Livelock — তৃতীয় case" },
      {
        type: "p",
        text: "দুটি processes একে অপরের প্রতি respond করতে থাকে এবং state change করতে থাকে, কিন্তু forward progress করে না। Deadlock-এর মতো তারা blocked না — তারা actively CPU burn করছে। Classic analogy — দুজন মানুষ একটি corridor-এ meet করে এবং দুজনই একই direction-এ step aside করে, বারবার। Deadlock হলো traffic jam; livelock হলো polite standoff।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Deadlock conditions — mutual exclusion, hold and wait, no preemption, circular wait (চারটিই দরকার)।",
          "Resource allocation graph — processes, resources, requests, ও allocations represent করার জন্য visual tool।",
          "RAG-তে cycles — No cycle → no deadlock। Cycle + single instances → deadlock। Cycle + multiple instances → maybe।",
          "Deadlock prevention — চারটি condition-এর একটি break করো (যেমন resource ordering, একসাথে সব request করো)।",
          "Deadlock avoidance — Banker's algorithm — system safe state-এ রাখো; max needs প্রয়োজন।",
          "Safe vs unsafe state — Safe → একটি completion order আছে। Unsafe → গ্যারান্টি নেই, কিন্তু এখনো deadlock না।",
          "Deadlock detection — periodic check (wait-for graph বা detection algorithm); তারপর termination বা preemption দিয়ে recover করো।",
          "Deadlock ignorance — কিছু করো না — Windows, Linux এ বেশির ভাগ resources-এর জন্য used; user reboot করে।",
          "Deadlock vs starvation — Deadlock কখনো intervention ছাড়া resolve হয় না; starvation resolve হতে পারে, এবং aging দিয়ে cure হয়।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Deadlocks বোঝা concurrency control-এর loop close করে। পরের chapter physical side-এ যায় — memory management।",
      },
    ],
  },

'''

new_text = before + NEW_CH5 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 05 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
