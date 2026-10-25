#!/usr/bin/env python3
"""
Rewrite Ch 03 (CPU Scheduling) with MAXIMUM BANGLA + English technical terms.
Pattern: Bangla বাক্য যেখানে technical terms English-এ থাকে।
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch3_marker_start = "// ---- Ch 03 - CPU Scheduling ----"
ch4_marker_start = "// ---- Ch 04 - Process Synchronization ----"

start_idx = text.find(ch3_marker_start)
assert start_idx != -1, "Ch 03 marker not found"
end_idx = text.find(ch4_marker_start, start_idx)
assert end_idx != -1, "Ch 04 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH3 = r'''// ---- Ch 03 - CPU Scheduling ----
  {
    id: "os-scheduling",
    subject: "os",
    title: "Ch 03 — CPU Scheduling",
    bangla: "সিপিইউ শিডিউলিং",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "CPU scheduling হলো multitasking-এর foundation। Operating system decide করে কোন process (বা thread) CPU পাবে এবং কতক্ষণ পাবে। এই chapter-এ goals, algorithms, ও trade-offs ব্যাখ্যা করা হয়েছে যেগুলো modern computers-কে responsive ও efficient করে তোলে।",
    sections: [
      { type: "h2", id: "criteria", title: "Scheduling Criteria" },
      {
        type: "p",
        text: "Scheduling algorithms compare করার জন্য আমরা কয়েকটি measurable criteria use করি। OS designer এই values optimize (maximise বা minimise) করার চেষ্টা করে।",
      },
      { type: "h3", title: "৫টি main criteria" },
      {
        type: "list",
        items: [
          "CPU utilisation — CPU কত শতাংশ সময় busy থাকে useful কাজ করে। Goal: maximise (CPU যত বেশি busy, তত ভালো)।",
          "Throughput — per unit time-এ কতগুলো process complete হয় (যেমন jobs per second)। Goal: maximise।",
          "Turnaround time — process arrival থেকে completion পর্যন্ত মোট সময় (waiting + execution + I/O)। Goal: minimise।",
          "Waiting time — একটি process ready queue-তে মোট কত সময় waiting করে। Goal: minimise।",
          "Response time — request submission (যেমন keystroke) থেকে first response (completion না) পর্যন্ত সময়। Goal: minimise (interactive systems-এর জন্য গুরুত্বপূর্ণ)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি coffee shop। CPU utilisation = barista কত ব্যস্ত (80% busy ভালো, 100% মানে customers wait করছে)। Throughput = প্রতি ঘণ্টায় কতগুলো coffee তৈরি হচ্ছে। Turnaround time = queue-তে ঢোকা থেকে শুরু করে coffee পান পর্যন্ত সময়। Waiting time = barista আপনার order শুরু করার আগে আপনি queue-তে কতক্ষণ ছিলেন। Response time = order দেওয়া থেকে শুরু করে barista-র 'I'll start right away' বলা পর্যন্ত সময়।",
      },

      { type: "h2", id: "preemption", title: "Preemptive vs Non-Preemptive Scheduling" },
      {
        type: "p",
        text: "Non-preemptive scheduling — একবার কোনো process CPU পেলে, সেটা ততক্ষণ hold করে যতক্ষণ না সেটা terminate হয় বা voluntarily yield করে (যেমন I/O-এর জন্য wait)। Scheduler জোর করে সেটিকে remove করতে পারে না।",
      },
      {
        type: "p",
        text: "Preemptive scheduling — scheduler একটি running process-কে interrupt করে CPU অন্য process-কে দিতে পারে। এই decision একটি timer (time quantum) বা higher-priority process arrive করার উপর ভিত্তি করে হতে পারে।",
      },
      { type: "h3", title: "Comparison" },
      {
        type: "list",
        items: [
          "Control — Non-preemptive: process decide করে কখন CPU release করবে; Preemptive: OS decide করে কখন CPU কেড়ে নেবে",
          "Overhead — Non-preemptive: low (কম context switch); Preemptive: higher (বেশি context switch)",
          "Fairness — Non-preemptive: poor (একটা long process অন্যদের starve করতে পারে); Preemptive: good (প্রতিটি process একটি slice পায়)",
          "Response time — Non-preemptive: interactive tasks-এর জন্য poor; Preemptive: excellent",
          "Example — Non-preemptive: batch systems (পুরোনো mainframes); Preemptive: সব modern OS (Linux, Windows, macOS)",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Non-preemptive হলো একটি meeting room: যে প্রথম team book করে সে ততক্ষণ থাকে যতক্ষণ না voluntarily leave করে। Preemptive হলো একটি classroom with a bell: প্রতি 50 মিনিট পর class change হয়ে যায়, teacher continue করতে চাইলেও।",
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: বেশির ভাগ modern scheduler preemptive — তারা fair CPU sharing enforce করার জন্য timer interrupt use করে।",
      },

      { type: "h2", id: "algorithms", title: "Scheduling Algorithms" },
      {
        type: "p",
        text: "এখন আমরা classic CPU scheduling algorithms দেখব। প্রতিটির strengths ও weaknesses আছে।",
      },

      { type: "h3", title: "First-Come, First-Served (FCFS)" },
      {
        type: "p",
        text: "Simplest algorithm — processes যে order-এ arrive করে সেই order-এ execute হয়, ঠিক queue (FIFO) এর মতো। Non-preemptive। Advantage: implement করা সহজ। Disadvantage: 'convoy effect' — একটি long process তার পিছনের সব short processes-কে block করে দেয়, যার ফলে average waiting time অনেক বেশি হয়ে যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি store-এ single checkout counter। Customers order অনুযায়ী serve হয়। যদি একজন customer এর full trolley থাকে, তাহলে পিছনের সবাই wait করতে হয়। এটাই convoy effect — একটা বড় job ছোট jobs-কে block করে।",
      },
      {
        type: "multi-code",
        filename: "fcfs",
        codeSamples: {
          cpp: `#include <iostream>
#include <vector>
using namespace std;

double fcfs(const vector<int>& burst) {
    int n = burst.size();
    int t = 0;
    double total_wait = 0;
    for (int i = 0; i < n; i++) {
        cout << "P" << i+1 << " wait=" << t << '\\n';
        total_wait += t;
        t += burst[i];
    }
    return total_wait / n;
}

int main() {
    cout << "Avg waiting time: " << fcfs({24, 3, 3}) << '\\n';
    // Output: P1 wait=0, P2 wait=24, P3 wait=27, avg=17
    return 0;
}`,
          go: `package main

import "fmt"

func fcfs(burst []int) float64 {
    t := 0
    totalWait := 0
    for i, b := range burst {
        fmt.Printf("P%d wait=%d\\n", i+1, t)
        totalWait += t
        t += b
    }
    return float64(totalWait) / float64(len(burst))
}

func main() {
    fmt.Println("Avg waiting time:", fcfs([]int{24, 3, 3}))
}`,
          python: `def fcfs(burst):
    t = 0
    total_wait = 0
    for i, b in enumerate(burst, 1):
        print(f"P{i} wait={t}")
        total_wait += t
        t += b
    return total_wait / len(burst)

print("Avg waiting time:", fcfs([24, 3, 3]))
# Output: P1 wait=0, P2 wait=24, P3 wait=27, avg=17.0`,
          java: `public class FCFS {
    static double fcfs(int[] burst) {
        int t = 0, totalWait = 0;
        for (int i = 0; i < burst.length; i++) {
            System.out.println("P" + (i+1) + " wait=" + t);
            totalWait += t;
            t += burst[i];
        }
        return (double) totalWait / burst.length;
    }
    public static void main(String[] args) {
        System.out.println("Avg waiting time: " + fcfs(new int[]{24, 3, 3}));
    }
}`,
        },
      },

      { type: "h3", title: "Shortest Job First (SJF)" },
      {
        type: "p",
        text: "যে process-এর smallest next CPU burst আছে সেটি আগে run করা হয়। এটি provably optimal যেটি average waiting time minimise করে (non-preemptive case-এ)। কিন্তু সমস্যা হলো — future burst time predict করা কঠিয়, সাধারণত exponential averaging use করা হয়।",
      },
      {
        type: "p",
        text: "Non-preemptive SJF — একবার কোনো process শুরু হলে সেটা completion পর্যন্ত run হয়। প্রতিটি scheduling decision-এ scheduler arrived processes-এর মধ্যে shortest job pick করে।",
      },
      {
        type: "p",
        text: "Preemptive SJF (Shortest Remaining Time First — SRTF) — যদি কোনো নতুন process এমন burst নিয়ে arrive করে যেটি current process-এর remaining time-এর চেয়ে ছোট, scheduler current process-কে preempt করে। এটি আরও ভালো average waiting time দেয়।",
      },
      {
        type: "p",
        text: "Disadvantage: starvation — যদি short jobs একটার পর একটা arrive করতে থাকে, long jobs কখনো run নাও হতে পারে। Real-life thinking — একটি hospital emergency room — triage সবচেয়ে critical (shortest) patients-কে আগে treat করে, কিন্তু একটি নতুন critical arrival কম critical patient-কে preempt করতে পারে।",
      },
      {
        type: "multi-code",
        filename: "sjf",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

double sjf(vector<pair<int,int>> procs) {  // (burst, id)
    sort(procs.begin(), procs.end());      // sort by burst
    int t = 0;
    double total = 0;
    for (auto& p : procs) {
        cout << "P" << p.second << " wait=" << t << '\\n';
        total += t;
        t += p.first;
    }
    return total / procs.size();
}

int main() {
    // (burst, id): P1=6, P2=8, P3=7, P4=3
    cout << "Avg: " << sjf({{6,1},{8,2},{7,3},{3,4}}) << '\\n';
    // Order: P4, P1, P3, P2 -> avg = (0+3+9+16)/4 = 7
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sort"
)

type P struct{ burst, id int }

func sjf(procs []P) float64 {
    sort.Slice(procs, func(i, j int) bool {
        return procs[i].burst < procs[j].burst
    })
    t := 0
    total := 0
    for _, p := range procs {
        fmt.Printf("P%d wait=%d\\n", p.id, t)
        total += t
        t += p.burst
    }
    return float64(total) / float64(len(procs))
}

func main() {
    avg := sjf([]P{{6,1},{8,2},{7,3},{3,4}})
    fmt.Println("Avg:", avg)
}`,
          python: `def sjf(procs):
    # procs: list of (burst, id)
    procs = sorted(procs)  # sort by burst
    t = 0
    total = 0
    for burst, pid in procs:
        print(f"P{pid} wait={t}")
        total += t
        t += burst
    return total / len(procs)

print("Avg:", sjf([(6, 1), (8, 2), (7, 3), (3, 4)]))
# Order: P4, P1, P3, P2 -> avg = 7.0`,
          java: `import java.util.*;

public class SJF {
    record P(int burst, int id) {}
    static double sjf(List<P> procs) {
        procs.sort(Comparator.comparingInt(p -> p.burst));
        int t = 0, total = 0;
        for (P p : procs) {
            System.out.println("P" + p.id + " wait=" + t);
            total += t;
            t += p.burst;
        }
        return (double) total / procs.size();
    }
    public static void main(String[] args) {
        System.out.println("Avg: " + sjf(Arrays.asList(
            new P(6, 1), new P(8, 2), new P(7, 3), new P(3, 4))));
    }
}`,
        },
      },

      { type: "h3", title: "Round Robin (RR)" },
      {
        type: "p",
        text: "Time-sharing systems-এর জন্য designed। প্রতিটি process একটি ছোট CPU time unit পায় যাকে time quantum (বা timeslice, সাধারণত 10–100 ms) বলে। Quantum expire হলে process preempt করে ready queue-এর পেছনে move হয়। Preemptive (timer দিয়ে)।",
      },
      {
        type: "p",
        text: "Advantage: good response time ও fairness। Disadvantage: performance quantum size-এর উপর heavily depend করে। Quantum অনেক বড় হলে FCFS-এ degenerate হয়ে যায়। Quantum অনেক ছোট হলে অনেক context switch হয়, overhead বেশি। Rule of thumb — quantum context-switch time-এর তুলনায় বড় হওয়া উচিত (যেমন 10–100 ms vs ~1–10 µs switch)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি classroom-এ প্রতিটি student-কে 5 মিনিট দেওয়া হল প্রশ্ন করার জন্য। ৫ মিনিট শেষ হলে পরের student-এ চলে যায়। সবাই সমান সুযোগ পায়।",
      },
      {
        type: "multi-code",
        filename: "round_robin",
        codeSamples: {
          cpp: `#include <iostream>
#include <queue>
#include <vector>

struct P { int id, burst; };

void round_robin(std::vector<P> procs, int quantum) {
    std::queue<P> q;
    for (auto& p : procs) q.push(p);
    int t = 0;
    while (!q.empty()) {
        P p = q.front(); q.pop();
        int run = std::min(quantum, p.burst);
        std::cout << "t=" << t << "  run P" << p.id
                  << " for " << run << '\\n';
        t += run;
        p.burst -= run;
        if (p.burst > 0) q.push(p);
        else std::cout << "        P" << p.id << " done at t=" << t << '\\n';
    }
}

int main() {
    round_robin({{1,8},{2,4},{3,6}}, 3);
    return 0;
}`,
          go: `package main

import "fmt"

type P struct{ id, burst int }

func roundRobin(procs []P, quantum int) {
    q := []P{}
    q = append(q, procs...)
    t := 0
    for len(q) > 0 {
        p := q[0]
        q = q[1:]
        run := quantum
        if p.burst < run { run = p.burst }
        fmt.Printf("t=%d  run P%d for %d\\n", t, p.id, run)
        t += run
        p.burst -= run
        if p.burst > 0 {
            q = append(q, p)
        } else {
            fmt.Printf("        P%d done at t=%d\\n", p.id, t)
        }
    }
}

func main() {
    roundRobin([]P{{1,8},{2,4},{3,6}}, 3)
}`,
          python: `from collections import deque

def round_robin(procs, quantum):
    q = deque(procs)
    t = 0
    while q:
        pid, burst = q.popleft()
        run = min(quantum, burst)
        print(f"t={t}  run P{pid} for {run}")
        t += run
        burst -= run
        if burst > 0:
            q.append((pid, burst))
        else:
            print(f"        P{pid} done at t={t}")

round_robin([(1, 8), (2, 4), (3, 6)], quantum=3)`,
          java: `import java.util.*;

public class RoundRobin {
    record P(int id, int burst) {}
    static void roundRobin(List<P> procs, int quantum) {
        Deque<P> q = new ArrayDeque<>(procs);
        int t = 0;
        while (!q.isEmpty()) {
            P p = q.poll();
            int run = Math.min(quantum, p.burst);
            System.out.printf("t=%d  run P%d for %d%n", t, p.id, run);
            t += run;
            int rem = p.burst - run;
            if (rem > 0) q.add(new P(p.id, rem));
            else System.out.printf("        P%d done at t=%d%n", p.id, t);
        }
    }
    public static void main(String[] args) {
        roundRobin(List.of(new P(1,8), new P(2,4), new P(3,6)), 3);
    }
}`,
        },
      },

      { type: "h3", title: "Priority Scheduling" },
      {
        type: "p",
        text: "প্রতিটি process-কে একটি priority (integer) assign করা হয়। CPU সেই process-কে দেওয়া হয় যার highest priority (ধরে নেওয়া হয় lower number = higher priority)। Preemptive বা non-preemptive হতে পারে।",
      },
      {
        type: "p",
        text: "Problem: starvation — low-priority processes কখনো run নাও হতে পারে। Solution: aging — সময়ের সাথে waiting processes-এর priority gradually increase করা হয়। যেমন P1 ৩ ক্ষেত্রে wait করলে তার priority 3 → 2 → 1 হয়ে যাবে, এবং সে সবসময় CPU পাবে।",
      },
      {
        type: "p",
        text: "Real-life thinking — airport boarding — first class (high priority) economy-এর আগে board করে। কিন্তু কিছুক্ষণ পরে economy-কেও call করা হয় (aging)।",
      },
      {
        type: "multi-code",
        filename: "priority_sched",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// lower number = higher priority
struct P { int id, burst, prio; };

void priority_sched(vector<P> procs) {
    sort(procs.begin(), procs.end(),
         [](const P& a, const P& b) { return a.prio < b.prio; });
    int t = 0;
    for (auto& p : procs) {
        cout << "P" << p.id << " prio=" << p.prio
             << " wait=" << t << '\\n';
        t += p.burst;
    }
}

int main() {
    // (id, burst, priority): lower = higher priority
    priority_sched({{1, 10, 3}, {2, 1, 1}, {3, 2, 2}});
    // Order: P2, P3, P1
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sort"
)

type P struct{ id, burst, prio int }

func prioritySched(procs []P) {
    sort.Slice(procs, func(i, j int) bool {
        return procs[i].prio < procs[j].prio
    })
    t := 0
    for _, p := range procs {
        fmt.Printf("P%d prio=%d wait=%d\\n", p.id, p.prio, t)
        t += p.burst
    }
}

func main() {
    prioritySched([]P{{1, 10, 3}, {2, 1, 1}, {3, 2, 2}})
}`,
          python: `def priority_sched(procs):
    # procs: list of (id, burst, priority), lower priority number = higher priority
    procs = sorted(procs, key=lambda x: x[2])
    t = 0
    for pid, burst, prio in procs:
        print(f"P{pid} prio={prio} wait={t}")
        t += burst

priority_sched([(1, 10, 3), (2, 1, 1), (3, 2, 2)])
# Order: P2 (prio=1), P3 (prio=2), P1 (prio=3)`,
          java: `import java.util.*;

public class PrioritySched {
    record P(int id, int burst, int prio) {}
    static void prioritySched(List<P> procs) {
        procs.sort(Comparator.comparingInt(p -> p.prio));
        int t = 0;
        for (P p : procs) {
            System.out.println("P" + p.id + " prio=" + p.prio + " wait=" + t);
            t += p.burst;
        }
    }
    public static void main(String[] args) {
        prioritySched(Arrays.asList(
            new P(1, 10, 3), new P(2, 1, 1), new P(3, 2, 2)));
    }
}`,
        },
      },

      { type: "h3", title: "Multilevel Queue Scheduling" },
      {
        type: "p",
        text: "Processes-কে তাদের type অনুযায়ী বিভিন্ন queues-এ categorize করা হয় (যেমন foreground interactive, background batch)। প্রতিটি queue-এর নিজস্ব scheduling algorithm থাকে। Permanent assignment — একটি process তার queue-এই থাকে। Queue-গুলোর মধ্যে scheduling সাধারণত fixed-priority preemptive — higher-priority queues আগে run হয়।",
      },
      {
        type: "p",
        text: "উদাহরণ: Queue 0 (system processes) — RR, quantum 50 ms। Queue 1 (interactive/foreground) — RR, quantum 20 ms। Queue 2 (batch/background) — FCFS। যদি Queue 0 empty না হয় সেটা run হবে; empty হলে Queue 1; নাহলে Queue 2।",
      },
      {
        type: "p",
        text: "Advantage: clear separation, obvious process classes-যুক্ত systems-এর জন্য suitable। Disadvantage: inflexible — কোনো process queue change করতে পারে না। এই সীমাবদ্ধতা দূর করতে MLFQ ব্যবহার হয়।",
      },

      { type: "h3", title: "Multilevel Feedback Queue (MLFQ)" },
      {
        type: "p",
        text: "সবচেয়ে general ও widely used scheduling algorithm (যেমন classic UNIX, modern BSD, ও Windows-এ)। এটি dynamically processes-কে queues-এর মধ্যে move করে তাদের behaviour-এর উপর ভিত্তি করে।",
      },
      { type: "h3", title: "MLFQ Rules" },
      {
        type: "list",
        items: [
          "১. একাধিক queues with different priorities। Higher-priority queues-এ ছোট time quanta থাকে।",
          "২. নতুন processes highest-priority queue-এ প্রবেশ করে।",
          "৩. যদি কোনো process তার সম্পূর্ণ quantum use করে, সে একটি lower-priority queue-তে drop হয়।",
          "৪. যদি কোনো process quantum expire হওয়ার আগে CPU yield করে (যেমন I/O-এর জন্য), সে একই queue-তে থাকে বা উপরে move হয়।",
          "৫. দীর্ঘ waiting time-এর পর কোনো process-কে higher queue-তে boost করা যেতে পারে (aging)।",
        ],
      },
      {
        type: "p",
        text: "Result: I/O-bound (interactive) processes-কে fast response পায়। CPU-bound processes ধীরে ধীরে lower queues-এ পড়ে, interactive processes-কে starve করে না। Real-life thinking — একটি restaurant with multiple lines — একটি quick coffee order express counter-এ যায় (high priority)। যদি কোনো order অনেক সময় নেয়, সেটা slower line-এ move হয়। অনেকক্ষণ waiting করা orders-কে expedite করা হয়।",
      },

      { type: "h2", id: "thread-sched", title: "Thread Scheduling" },
      {
        type: "p",
        text: "Modern operating systems processes না, threads schedule করে। Distinction threading model-এর উপর depend করে (Chapter 2 দেখুন)।",
      },
      {
        type: "list",
        items: [
          "User-level threads (ULT) — kernel সেই process-কে schedule করে যেটিতে অনেক user threads আছে। User thread library internally threads-কে single kernel thread-এ schedule করে। Kernel threads-সম্পর্কে অজ্ঞ — তাই একটি blocking thread পুরো process-কে block করে।",
          "Kernel-level threads (KLT) — kernel প্রতিটি thread আলাদাভাবে schedule করে। এটি cores-এ true parallelism এবং independent blocking allow করে।",
        ],
      },
      {
        type: "p",
        text: "Process-Contention Scope (PCS) — একই process-এর ভেতরে user threads-এর মধ্যে scheduling (user library দ্বারা managed)। System-Contention Scope (SCS) — সব processes-এর kernel threads-এর মধ্যে scheduling (OS দ্বারা managed)। Linux (NPTL)-এ pthread_create kernel threads create করে। Scheduler একই algorithms (যেমন CFS — Completely Fair Scheduler) threads-এ use করে, processes-এ না।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি company (process) with multiple employees (threads)। যদি company outsiders-এর কাছে black-box হয় (user-level), outsiders শুধু company দেখে, individuals কে না। যদি company প্রতিটি employee register করে (kernel-level), outsiders প্রত্যেককে আলাদাভাবে manage করতে পারে।",
      },

      { type: "h2", id: "realtime", title: "Real-Time Scheduling" },
      {
        type: "p",
        text: "Real-time systems-এ গ্যারান্টি দিতে হবে যে tasks তাদের deadlines meet করবে (যেমন airbag deployment, industrial robots)। দুটি category:",
      },
      {
        type: "list",
        items: [
          "Hard real-time — deadline miss হলে catastrophic failure হয়।",
          "Soft real-time — deadline miss হলে performance degrade করে কিন্তু fatal না।",
        ],
      },
      {
        type: "p",
        text: "Real-time scheduling প্রায়ই priority-based preemptive algorithms use করে, static বা dynamic priorities সহ।",
      },

      { type: "h3", title: "Rate-Monotonic Scheduling (RMS)" },
      {
        type: "p",
        text: "Assumptions: সব tasks periodic (fixed intervals-এ release হয়)। Deadline = period (job next release-এর আগে complete হতে হবে)। Tasks independent, preemptive। কোনো context-switch overhead নেই (theoretical model)। Rule: shorter period-যুক্ত tasks-কে higher priority দেওয়া হয়। এটি এমন systems-এর জন্য optimal static-priority algorithm।",
      },
      {
        type: "p",
        text: "Schedulability condition (simplified): n periodic tasks-এর একটি set-এর জন্য, RMS feasible যদি total utilisation ≤ n × (2^(1/n) − 1)। n=2 এর জন্য, 2 × (√2 − 1) ≈ 0.828। Limitation: different deadlines-যুক্ত tasks-এর জন্য optimal না (যদি deadline < period)। তবুও safety-critical systems-এ widely used।",
      },

      { type: "h3", title: "Earliest Deadline First (EDF)" },
      {
        type: "p",
        text: "Dynamic priority — যেকোনো সময়, যে task-এর earliest absolute deadline আছে সেটা next run হয়। Uniprocessors-এর জন্য optimal — যদি কোনো schedule deadlines meet করে, EDF-ও করবে (preemption সহ)। Utilisation 100%-এর কাছে যেতে পারে (RMS-এর 69%-এর বিপরীতে)। Disadvantage: deadlines sort করার overhead; overload-এ অনেক deadlines miss হতে পারে (unpredictable)।",
      },

      { type: "h3", title: "RMS vs EDF — Comparison" },
      {
        type: "list",
        items: [
          "Priority — RMS: static (fixed); EDF: dynamic",
          "Implementation — RMS: simple (fixed priorities); EDF: deadline sorting প্রয়োজন",
          "Utilisation bound (n→∞) — RMS: ≈ 69%; EDF: 100%",
          "Overload behaviour — RMS: predictable (low-priority tasks আগে starve); EDF: unpredictable (অনেক deadlines miss হতে পারে)",
          "Use case — RMS: hard real-time, safety-critical; EDF: soft real-time, multimedia",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — RMS হলো একজন mail carrier with fixed rounds: shorter routes-কে higher priority দেওয়া হয়। EDF হলো একজন journalist with article deadlines: যে article সবচেয়ে শীঘ্র due, সেটা next লেখা হয়, পরে arrive করলেও।",
      },
      {
        type: "multi-code",
        filename: "edf_schedule",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
#include <vector>

struct Task { int id, period, remaining; };

// simple EDF: pick task with smallest absolute deadline
// here we use period as deadline for one cycle
int main() {
    std::vector<Task> tasks = {
        {1, 4, 1},    // T1: period 4, 1 unit work
        {2, 6, 2},    // T2: period 6, 2 units work
        {3, 8, 3},    // T3: period 8, 3 units work
    };

    int totalTime = 24;  // LCM-ish demo horizon
    for (int t = 0; t < totalTime; t++) {
        // re-release tasks at their period boundaries
        for (auto& tk : tasks) {
            if (t % tk.period == 0) tk.remaining = tk.period == 4 ? 1
                : (tk.period == 6 ? 2 : 3);
        }
        std::vector<Task*> ready;
        for (auto& tk : tasks) if (tk.remaining > 0) ready.push_back(&tk);
        std::sort(ready.begin(), ready.end(),
            [](Task* a, Task* b) { return a->period < b->period; });
        if (!ready.empty()) {
            std::cout << "t=" << t << " run T" << ready[0]->id << '\\n';
            ready[0]->remaining--;
        } else {
            std::cout << "t=" << t << " idle\\n";
        }
    }
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sort"
)

type Task struct{ id, period, remaining int }

func main() {
    tasks := []Task{{1, 4, 1}, {2, 6, 2}, {3, 8, 3}}
    for t := 0; t < 24; t++ {
        for i := range tasks {
            if t%tasks[i].period == 0 {
                tasks[i].remaining = []int{1, 2, 3}[i]
            }
        }
        var ready []*Task
        for i := range tasks {
            if tasks[i].remaining > 0 { ready = append(ready, &tasks[i]) }
        }
        sort.Slice(ready, func(i, j int) bool {
            return ready[i].period < ready[j].period
        })
        if len(ready) > 0 {
            fmt.Printf("t=%d run T%d\\n", t, ready[0].id)
            ready[0].remaining--
        } else {
            fmt.Printf("t=%d idle\\n", t)
        }
    }
}`,
          python: `tasks = [
    {"id": 1, "period": 4, "remaining": 1, "wcet": 1},
    {"id": 2, "period": 6, "remaining": 2, "wcet": 2},
    {"id": 3, "period": 8, "remaining": 3, "wcet": 3},
]

for t in range(24):
    # re-release task at its period boundary
    for tk in tasks:
        if t % tk["period"] == 0:
            tk["remaining"] = tk["wcet"]
    ready = [tk for tk in tasks if tk["remaining"] > 0]
    ready.sort(key=lambda x: x["period"])
    if ready:
        print(f"t={t} run T{ready[0]['id']}")
        ready[0]["remaining"] -= 1
    else:
        print(f"t={t} idle")`,
          java: `import java.util.*;

public class EDF {
    public static void main(String[] args) {
        int[][] tasks = { {1, 4, 1}, {2, 6, 2}, {3, 8, 3} };
        int[] remaining = new int[tasks.length];
        for (int t = 0; t < 24; t++) {
            for (int i = 0; i < tasks.length; i++) {
                if (t % tasks[i][1] == 0) remaining[i] = tasks[i][2];
            }
            int pick = -1;
            for (int i = 0; i < tasks.length; i++) {
                if (remaining[i] > 0 &&
                    (pick == -1 || tasks[i][1] < tasks[pick][1])) {
                    pick = i;
                }
            }
            if (pick != -1) {
                System.out.printf("t=%d run T%d%n", t, tasks[pick][0]);
                remaining[pick]--;
            } else {
                System.out.printf("t=%d idle%n", t);
            }
        }
    }
}`,
        },
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Scheduling criteria — CPU utilisation, throughput, turnaround time, waiting time, response time।",
          "Preemptive vs non-preemptive — Preemptive = OS interrupt করতে পারে; Non-preemptive = process voluntarily yield করে।",
          "FCFS — simple কিন্তু convoy effect-এ ভোগে।",
          "SJF (SRTF) — average waiting time minimise করার জন্য optimal; burst time prediction প্রয়োজন।",
          "Round Robin — fair, excellent response; quantum size critical।",
          "Priority scheduling — aging দ্বারা starvation mitigate করা হয়।",
          "Multilevel queue — fixed categories; rigid।",
          "Multilevel feedback queue — queues-এর মধ্যে dynamic movement; modern OS-এ used।",
          "Thread scheduling — kernel-level threads individually scheduled; user-level threads শুধু process-এর মাধ্যমে।",
          "RMS — period-এর উপর ভিত্তি করে static priorities; utilisation bound ~69%।",
          "EDF — deadlines-এর উপর ভিত্তি করে dynamic priorities; optimal কিন্তু বেশি overhead।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: CPU scheduling বোঝা essential — যাতে বোঝা যায় OS কীভাবে responsiveness, fairness, ও throughput balance করে। পরের chapter memory management-এ যাব — সেটাও একইভাবে critical।",
      },
    ],
  },

'''

new_text = before + NEW_CH3 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 03 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
