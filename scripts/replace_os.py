#!/usr/bin/env python3
"""Replace the OS section of content.ts with all 13 OS chapter topics."""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
content = CONTENT_FILE.read_text()

os_section_start = content.find("/* ============== OS ============== */")
assert os_section_start != -1, "OS section marker not found"

topics_end_marker = "\n];\n\nexport const PROJECTS"
topics_end = content.find(topics_end_marker, os_section_start)
assert topics_end != -1, "TOPICS array end not found"

before = content[:os_section_start]

new_os_section = '''/* ============== OS ============== */

  // ---- Ch 01 - Introduction ----
  {
    id: "os-introduction",
    subject: "os",
    title: "Ch 01 — Introduction",
    bangla: "পরিচিতি (Introduction)",
    difficulty: "Easy",
    est: "30 min",
    summary:
      "What an OS is, its history, types (batch / time-sharing / real-time / distributed), and the kernel vs user-space split. System calls are the doorway between them.",
    sections: [
      { type: "h2", id: "what", title: "What is an Operating System?" },
      {
        type: "p",
        text: "Operating System (OS, অপারেটিং সিস্টেম) হলো এমন একটি system software যা hardware ও application-এর মাঝে একটি abstraction layer হিসেবে কাজ করে। এটি CPU, memory, disk, network-এর মতো resource গুলো manage করে এবং applications-কে একটি clean, portable interface (system calls) দেয়। ছাড়া OS হলে প্রতিটি program-কে নিজে নিজে disk driver, network card, keyboard সব handle করতে হতো।",
      },
      {
        type: "p",
        text: "OS-এর প্রধান কাজ চারটি: (1) Resource management — কে কখন CPU পাবে, কে কতটা memory পাবে তা schedule করা। (2) Process isolation — এক process অন্যটির memory বা file নষ্ট করতে না পারে। (3) Abstraction — hardware-এর জটিলতা লুকিয়ে high-level API (file, socket, process) দেওয়া। (4) Concurrency — একাধিক program একসাথে চালানোর illusion তৈরি করা।",
      },
      { type: "h3", title: "Types of Operating Systems" },
      {
        type: "list",
        items: [
          "Batch OS — ১৯৫০s, punch card যুগ, no interaction (early IBM mainframes)",
          "Time-sharing OS — একাধিক user terminal, প্রত্যেকে মনে করে সে একা (Unix, VMS)",
          "Personal OS — একজন user, GUI-centric (Windows, macOS, Linux desktop)",
          "Real-time OS (RTOS) — strict deadline, microsecond-level (VxWorks, FreeRTOS, QNX)",
          "Distributed OS — অনেক machine এক হিসেবে দেখা (Plan 9, Amoeba)",
          "Embedded OS — small footprint, IoT devices (Embedded Linux, Zephyr)",
          "Mobile OS — power-aware, touch-centric (Android, iOS)",
        ],
      },
      { type: "h2", id: "kernel", title: "Kernel vs User Space" },
      {
        type: "p",
        text: "Modern CPU-তে দুটি privilege level থাকে — kernel mode ও user mode। Kernel mode-এ সব instruction (হার্ডওয়্যার register, raw memory) চলতে পারে। User mode-এ নির্দিষ্ট instruction নিষিদ্ধ, যেমন সরাসরি I/O port access। User program kernel-এ যেতে হলে system call (syscall) করে — এটি একটি special instruction (x86-এ `syscall` / `int 0x80`) যা CPU-কে kernel mode-এ switch করে এবং একটি registered handler-এ লাফ দেয়।",
      },
      {
        type: "p",
        text: "এই বিভাজনের কারণ: security ও stability। যদি কোনো user program crash করে, শুধু সেই process মারা যায়, পুরো system নয়। কিন্তু kernel-mode code crash করলে পুরো machine hang করে (kernel panic, blue screen)। তাই kernel-এ যত কম code থাকে তত ভালো — microkernel approach (Mach, L4) এই ভাবের endpoint।",
      },
      { type: "h3", title: "Get your own PID — a basic syscall" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় নিজের process ID (PID) ও parent PID দেখানো হলো। প্রতিটি ভাষা এই information-এর জন্য kernel-এ getpid / getppid syscall করে।",
      },
      {
        type: "multi-code",
        filename: "getpid",
        codeSamples: {
          cpp: `#include <iostream>
#include <unistd.h>   // POSIX header for getpid / getppid

int main() {
    std::cout << "PID:  " << getpid()  << '\\n';
    std::cout << "PPID: " << getppid() << '\\n';
    return 0;
}
// Compile: g++ getpid.cpp -o getpid
// Run:     ./getpid`,
          go: `package main

import (
    "fmt"
    "os"
)

func main() {
    // Go exposes pid via os.Getpid() — internally calls getpid syscall
    fmt.Println("PID: ", os.Getpid())
    fmt.Println("PPID:", os.Getppid())
}
// Run: go run getpid.go`,
          python: `import os

# os.getpid() — calls libc getpid(), which calls kernel syscall
print("PID: ", os.getpid())
print("PPID:", os.getppid())
# Run: python getpid.py`,
          java: `public class GetPid {
    public static void main(String[] args) {
        // ProcessHandle (Java 9+) exposes the OS pid
        long pid  = ProcessHandle.current().pid();
        long ppid = ProcessHandle.current().parent()
                        .map(ProcessHandle::pid).orElse(-1);
        System.out.println("PID:  " + pid);
        System.out.println("PPID: " + ppid);
    }
}
// Run: javac GetPid.java && java GetPid`,
        },
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Linux-এ `strace ./your_program` দিয়ে দেখুন কোন syscalls হচ্ছে। প্রায় সব high-level operation (file পড়া, network call, even printf) এক বা একাধিক syscall-এ পরিণত হয়। এটি OS বোঝার সবচেয়ে concrete উপায়।",
      },
    ],
  },

  // ---- Ch 02 - Process Management ----
  {
    id: "os-processes",
    subject: "os",
    title: "Ch 02 — Process Management",
    bangla: "প্রসেস ম্যানেজমেন্ট",
    difficulty: "Medium",
    est: "1 hr",
    summary:
      "Process = running program with own memory. PCB, states, context switch, fork/exec/wait. Threads share memory inside a process.",
    sections: [
      { type: "h2", id: "what", title: "What is a Process?" },
      {
        type: "p",
        text: "Process (প্রসেস) হলো একটি executing program — code, data, heap, stack, open files, register state — সব মিলে একটি self-contained execution context। যখন আপনি একটি program run করেন, OS সেটিকে একটি PID দিয়ে process table-এ entry তৈরি করে। প্রতিটি process-এর নিজস্ব virtual memory space থাকে — অর্থাৎ এক process অন্য process-এর memory সরাসরি access করতে পারে না (OS-enforced protection)।",
      },
      {
        type: "p",
        text: "OS প্রতিটি process-এর জন্য একটি Process Control Block (PCB) রাখে। PCB-তে থাকে: PID, process state, program counter, CPU registers, memory limits, open file descriptors, scheduling priority। যখন OS এক process থেকে অন্যটিতে switch করে (context switch), সে PCB-তে পুরোনো process-এর state সংরক্ষণ করে এবং নতুনটির state restore করে। এই operation বেশ দামি — ~1-10 µs প্রতি switch।",
      },
      { type: "h3", title: "Process States (5-state model)" },
      {
        type: "list",
        items: [
          "New — just created, OS allocating PCB",
          "Ready — waiting for a CPU core",
          "Running — currently executing on a CPU",
          "Waiting / Blocked — waiting for I/O or an event (sleep, disk read, lock)",
          "Terminated — finished, PCB waiting to be reaped by parent (zombie)",
        ],
      },
      { type: "h2", id: "fork-exec", title: "fork / exec / wait" },
      {
        type: "p",
        text: "Unix-এ নতুন process তৈরির প্রধান প্যাটার্ন হলো fork-exec-wait। fork() বর্তমান process-এর একটি প্রায়-exact copy তৈরি করে (copy-on-write)। child process exec() call করে নিজের memory image পুরোপুরি replace করে একটি নতুন program দিয়ে। parent wait() করে child শেষ হওয়া পর্যন্ত।",
      },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় একই প্যাটার্ন দেখানো হলো — একটি child process spawn করে যে `/bin/echo hello` execute করবে, parent তার শেষ হওয়া পর্যন্ত অপেক্ষা করবে।",
      },
      {
        type: "multi-code",
        filename: "fork_exec",
        codeSamples: {
          cpp: `#include <iostream>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();          // create a child
    if (pid == 0) {
        // child — replace image with /bin/echo
        execl("/bin/echo", "echo", "hello", nullptr);
        perror("exec failed");
        _exit(1);
    } else if (pid > 0) {
        // parent — wait for child to finish
        int status;
        waitpid(pid, &status, 0);
        std::cout << "child exited with " << WEXITSTATUS(status) << '\\n';
    } else {
        perror("fork failed");
    }
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os/exec"
)

func main() {
    // Go does not expose fork() directly for safety;
    // exec.Command spawns a child via fork+exec internally.
    cmd := exec.Command("/bin/echo", "hello")
    out, err := cmd.Output()         // blocks until child exits
    if err != nil {
        fmt.Println("exec failed:", err)
        return
    }
    fmt.Printf("child output: %s", out)
}`,
          python: `import subprocess

# subprocess.run() = fork + exec + wait in one call
result = subprocess.run(
    ["/bin/echo", "hello"],
    capture_output=True,
    text=True,
)
print("child output:", result.stdout, end="")
print("exit code:", result.returncode)`,
          java: `public class ForkExec {
    public static void main(String[] args) throws Exception {
        // ProcessBuilder starts a child process (fork+exec equivalent)
        ProcessBuilder pb = new ProcessBuilder("/bin/echo", "hello");
        Process p = pb.start();
        int code = p.waitFor();   // wait for child to exit
        System.out.println("exit code: " + code);
    }
}`,
        },
      },
      { type: "h3", title: "Threads" },
      {
        type: "p",
        text: "Thread হলো process-এর ভেতরের একটি unit of CPU execution। একই process-এর সব thread সেই process-এর memory share করে (code, heap, file descriptors), কিন্তু প্রতিটি thread-এর নিজস্ব stack ও program counter থাকে। Thread switch করা process switch থেকে সস্তা, কারণ memory translation tables change করতে হয় না।",
      },
      {
        type: "multi-code",
        filename: "threads",
        codeSamples: {
          cpp: `#include <iostream>
#include <thread>
#include <vector>

void worker(int id) {
    std::cout << "thread " << id << " running\\n";
}

int main() {
    std::vector<std::thread> ts;
    for (int i = 0; i < 4; i++) ts.emplace_back(worker, i);
    for (auto& t : ts) t.join();
    return 0;
}
// Compile: g++ -std=c++17 -pthread threads.cpp -o threads`,
          go: `package main

import (
    "fmt"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    for i := 0; i < 4; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            fmt.Println("thread", id, "running")
        }(i)
    }
    wg.Wait()
}`,
          python: `import threading

def worker(i):
    print(f"thread {i} running")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
for t in threads: t.start()
for t in threads: t.join()
# Note: GIL blocks true parallel CPU work in CPython.
`,
          java: `public class Threads {
    public static void main(String[] args) throws InterruptedException {
        Runnable worker = () -> System.out.println(
            "thread " + Thread.currentThread().threadId() + " running"
        );
        Thread[] ts = new Thread[4];
        for (int i = 0; i < 4; i++) { ts[i] = new Thread(worker); ts[i].start(); }
        for (Thread t : ts) t.join();
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: যখন অনেক thread একই memory তে write করে, race condition হয়। পরের চ্যাপ্টারে (Process Synchronization) এটা আলোচনা করা হয়েছে।",
      },
    ],
  },

  // ---- Ch 03 - CPU Scheduling ----
  {
    id: "os-scheduling",
    subject: "os",
    title: "Ch 03 — CPU Scheduling",
    bangla: "সিপিইউ শিডিউলিং",
    difficulty: "Medium",
    est: "1 hr",
    summary:
      "Deciding which ready process runs next. FCFS, SJF, Round Robin, Priority, MLFQ — each with trade-offs in throughput, fairness, response time.",
    sections: [
      { type: "h2", id: "what", title: "What is Scheduling?" },
      {
        type: "p",
        text: "CPU scheduling হলো OS-এর সিদ্ধান্ত নেওয়া যে ready state-এ থাকা অনেকগুলো process-এর মধ্যে কোন process-টিকে এখন CPU দেওয়া হবে। লক্ষ্য হলো throughput maximize করা, response time কমানো, fairness নিশ্চিত করা এবং starvation এড়ানো। বিভিন্ন algorithm বিভিন্ন trade-off করে — কোনোটি throughput-এ ভালো, কোনোটি fairness-এ।",
      },
      { type: "h3", title: "Common Algorithms" },
      {
        type: "list",
        items: [
          "FCFS (First-Come First-Served) — simplest, but convoy effect (slow jobs block everything)",
          "SJF (Shortest Job First) — optimal average wait time, but unfair to long jobs (starvation)",
          "Round Robin — time quantum per process, fair but context-switch overhead",
          "Priority — high priority first, can starve low priority (aging helps)",
          "MLFQ (Multi-Level Feedback Queue) — adaptive, used in modern OS",
        ],
      },
      { type: "h2", id: "round-robin", title: "Round Robin Simulation" },
      {
        type: "p",
        text: "নিচে Round Robin scheduler এর সরল simulation দেখানো হলো চারটি ভাষায়। প্রতিটি process-কে fixed time quantum (3 ms) পর্যন্ত চলার সুযোগ দেওয়া হয়, তারপর পরের process-এ যাওয়া হয়।",
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
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Quantum ছোট হলে response time ভালো কিন্তু context-switch overhead বেশি। Quantum বড় হলে Round Robin আসলে FCFS-এ পরিণত হয়। সাধারণ চয়েস 10–100 ms। Linux CFS (Completely Fair Scheduler) এর চেয়ে অনেক বেশি sophisticated।",
      },
    ],
  },

  // ---- Ch 04 - Process Synchronization ----
  {
    id: "os-sync",
    subject: "os",
    title: "Ch 04 — Process Synchronization",
    bangla: "প্রসেস সিঙ্ক্রোনাইজেশন",
    difficulty: "Hard",
    est: "1.5 hr",
    summary:
      "Race conditions, critical sections, mutex, semaphore, monitor. Classic problems: producer-consumer, dining philosophers, readers-writers.",
    sections: [
      { type: "h2", id: "what", title: "Race Condition & Critical Section" },
      {
        type: "p",
        text: "যখন অনেক thread বা process একই shared data-তে concurrently read-modify-write করে, তখন ফলাফল নির্ভর করে কোন thread কোন order-এ চলবে তার উপর। একে race condition বলে। সমাধান হলো সেই code segment-কে protect করা যাতে এক সময়ে শুধু একটি thread সেখানে থাকে — একে critical section বলে।",
      },
      {
        type: "p",
        text: "Critical section solve করার চারটি requirement: (1) Mutual exclusion — এক thread critical section-এ থাকলে অন্য কেউ ঢুকতে পারবে না। (2) Progress — যদি কেউ critical section-এ না থাকে, কে ঢুকবে সেটা অ-এ-ঢুকতে-চাওয়া thread গুলো ঠিক করবে। (3) Bounded waiting — একটি thread-এর অপেক্ষার একটি upper bound থাকতে হবে, otherwise starvation। (4) Performance — খরচ যেন যুক্তিযুক্ত।",
      },
      { type: "h2", id: "mutex", title: "Mutex — Mutual Exclusion Lock" },
      {
        type: "p",
        text: "Mutex (mutual exclusion) হলো সবচেয়ে সাধারণ synchronization primitive। এটি একটি flag যা 0 বা 1। এক thread lock করলে (atomic test-and-set), অন্য thread যখন lock করতে চায় তখন block হয়ে যায় যতক্ষণ না প্রথম thread unlock করে। atomic operation-এর জন্য hardware support দরকার (e.g., x86 `lock cmpxchg`)।",
      },
      {
        type: "multi-code",
        filename: "mutex_counter",
        codeSamples: {
          cpp: `#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

int counter = 0;
std::mutex m;

void bump(int n) {
    for (int i = 0; i < n; i++) {
        std::lock_guard<std::mutex> lk(m);   // RAII lock
        counter++;
    }
}

int main() {
    std::vector<std::thread> ts;
    for (int i = 0; i < 8; i++) ts.emplace_back(bump, 10000);
    for (auto& t : ts) t.join();
    std::cout << "counter=" << counter << '\\n';   // 80000
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

func main() {
    var counter int
    var mu sync.Mutex
    var wg sync.WaitGroup

    for i := 0; i < 8; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for j := 0; j < 10000; j++ {
                mu.Lock()
                counter++
                mu.Unlock()
            }
        }()
    }
    wg.Wait()
    fmt.Println("counter=", counter)   // 80000
}`,
          python: `import threading

counter = 0
lock = threading.Lock()

def bump(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

ts = [threading.Thread(target=bump, args=(10000,)) for _ in range(8)]
for t in ts: t.start()
for t in ts: t.join()
print("counter=", counter)   # 80000`,
          java: `public class MutexCounter {
    static int counter = 0;
    public static void main(String[] args) throws InterruptedException {
        Object lock = new Object();
        Thread[] ts = new Thread[8];
        for (int i = 0; i < 8; i++) {
            ts[i] = new Thread(() -> {
                for (int j = 0; j < 10000; j++) {
                    synchronized (lock) { counter++; }
                }
            });
            ts[i].start();
        }
        for (Thread t : ts) t.join();
        System.out.println("counter=" + counter);   // 80000
    }
}`,
        },
      },
      { type: "h3", title: "Semaphore — Counting Lock" },
      {
        type: "p",
        text: "Semaphore হলো একটি integer যা atomic increment (V / signal) ও decrement (P / wait) করা যায়। যদি value 0 হয়ে যায়, পরের P() block হয়। Mutex হলো binary semaphore (value 0 বা 1)। Counting semaphore (e.g., initial value 3) N-টি thread একসাথে যেতে দেয়। Producer-consumer problem-এ bounded buffer তৈরি করতে counting semaphore ব্যবহার হয়।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: ভুলে গেলে deadlock হতে পারে — যেমন দুটি thread দুটি lock একে অপরের চেয়ে আগে lock করতে চায়। চায়ের অধ্যায় (Deadlocks)-এ এটি আলোচনা করা হয়েছে।",
      },
    ],
  },

  // ---- Ch 05 - Deadlocks ----
  {
    id: "os-deadlocks",
    subject: "os",
    title: "Ch 05 — Deadlocks",
    bangla: "ডেডলক",
    difficulty: "Hard",
    est: "1.5 hr",
    summary:
      "4 necessary conditions, prevention, avoidance (Banker's algorithm), detection, recovery. Deadlock vs starvation.",
    sections: [
      { type: "h2", id: "what", title: "What is a Deadlock?" },
      {
        type: "p",
        text: "Deadlock হলো এমন অবস্থা যেখানে দুটি বা ততোধিক process/thread একে অপরের জন্য চিরকাল অপেক্ষা করে থাকে, এবং কেউই এগিয়ে যেতে পারে না। ক্লাসিক উদাহরণ: P1 এর resource A আছে, B চায়। P2 এর B আছে, A চায়। কেউ ছাড়বে না — দুজনই অসীম অপেক্ষায়।",
      },
      { type: "h3", title: "Coffman's 4 Necessary Conditions" },
      {
        type: "p",
        text: "Deadlock হতে হলে একসাথে এই চারটি condition পূরণ হতে হবে। যেকোনো একটি ভাঙলে deadlock হবে না:",
      },
      {
        type: "list",
        items: [
          "Mutual exclusion — কোনো রিসোর্স একসময় শুধু এক process-এ দেওয়া যায়",
          "Hold and wait — এক process এক রিসোর্স ধরে রেখে আরেকটি চাইতে পারে",
          "No preemption — OS জোর করে রিসোর্স কেড়ে নিতে পারে না",
          "Circular wait — একটি cycle তৈরি হয় (P1→P2→P3→P1)",
        ],
      },
      { type: "h2", id: "strategies", title: "Strategies to Handle Deadlocks" },
      {
        type: "list",
        items: [
          "Prevention — চারটি condition-এর একটি ভাঙা (e.g., total order দিয়ে lock করলে circular wait ভাঙে)",
          "Avoidance — runtime-এ রাখা, কিন্তু প্রতিটি request safe কিনা check করা (Banker's algorithm)",
          "Detection + recovery — deadlock হতে দেওয়া, তারপর একটি victim process কে kill করা",
          "Ignore — বেশির ভাগ OS (Linux, Windows) এটাই করে, কারণ deadlock rare এবং detection দামি",
        ],
      },
      { type: "h2", id: "bankers", title: "Banker's Algorithm (Avoidance)" },
      {
        type: "p",
        text: "Dijkstra-র Banker's algorithm একটি deadlock avoidance scheme। প্রতিটি process তার maximum resource need আগে declare করে। যখন কোনো process request করে, OS check করে এই request grant করলে কি এমন একটি safe state থাকবে যেখানে সব process sequence-এ শেষ করা যায়। যদি হ্যাঁ — request grant করে। না হলে wait করায়।",
      },
      {
        type: "multi-code",
        filename: "bankers_safe",
        codeSamples: {
          cpp: `#include <iostream>
#include <vector>
using namespace std;

// is state safe?  Work[] = available;  finish[i] = true if P[i] done
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
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: অধিকাংশ production OS (Linux, Windows) deadlock avoidance করে না — কারণ প্রতিটি process-এর max need আগে জানা কঠিন, এবং Banker's algorithm O(n²m) check করে। তার বদলে prevention এবং timeout-based recovery বেশি ব্যবহৃত হয়।",
      },
    ],
  },

  // ---- Ch 06 - Memory Management ----
  {
    id: "os-memory",
    subject: "os",
    title: "Ch 06 — Memory Management",
    bangla: "মেমোরি ম্যানেজমেন্ট",
    difficulty: "Medium",
    est: "1 hr",
    summary:
      "Contiguous allocation, paging, segmentation, fragmentation. Process memory layout: text, data, BSS, heap, stack.",
    sections: [
      { type: "h2", id: "what", title: "Why Memory Management?" },
      {
        type: "p",
        text: "Main memory (RAM) হলো একটি scarce resource — সব process, kernel, file cache একসাথে share করে। OS-এর কাজ হলো প্রতিটি process-কে একটি protected address space দেওয়া, অপ্রয়োজনীয় allocation এড়ানো, এবং fragmentation কমানো। যদি কোনো process তার সীমা ছাড়িয়ে যায়, OS সেটিকে SIGSEGV (segmentation fault) পাঠিয়ে kill করে।",
      },
      { type: "h3", title: "Process Memory Layout" },
      {
        type: "code",
        lang: "text",
        text: `+--------------------+  high address
| Stack       v      |  local vars, function frames
+--------------------+
| (gap)              |
+--------------------+
| Heap        ^      |  malloc / new — grows up
+--------------------+
| BSS                |  uninitialized globals
+--------------------+
| Data               |  initialized globals
+--------------------+
| Text (Code)        |  the compiled instructions
+--------------------+  low address`,
      },
      { type: "h2", id: "paging", title: "Paging" },
      {
        type: "p",
        text: "Paging-এ virtual memory কে fixed-size pages (সাধারণত 4 KB) এ ভাগ করা হয়, এবং physical memory কে একই size-এর frames এ। Page table হলো per-process mapping: কোন virtual page-টি কোন physical frame-এ আছে। সুবিধা: external fragmentation থাকে না, যেকোনো free frame যেকোনো page-এ বসতে পারে। অসুবিধা: internal fragmentation (শেষ page অর্ধেক খালি থাকতে পারে)।",
      },
      {
        type: "p",
        text: "Address translation করে MMU (Memory Management Unit)। Virtual address কে two ভাগে ভাগ করা হয়: page number (উপরের bit গুলো) ও offset (নিচের bit গুলো)। Page number দিয়ে page table-এ খুঁজে frame number বের করা হয়, তারপর offset যোগ করে physical address তৈরি করা হয়।",
      },
      { type: "h3", title: "Simulate a Page Table Lookup" },
      {
        type: "multi-code",
        filename: "page_table",
        codeSamples: {
          cpp: `#include <iostream>
#include <unordered_map>
#include <vector>

struct MMU {
    std::unordered_map<int, int> pageTable;   // page -> frame
    int pageSize;

    int translate(int vaddr) {
        int page = vaddr / pageSize;
        int off  = vaddr % pageSize;
        auto it = pageTable.find(page);
        if (it == pageTable.end()) {
            std::cerr << "PAGE FAULT: page " << page << '\\n';
            return -1;
        }
        return it->second * pageSize + off;
    }
};

int main() {
    MMU mmu{ { {0, 5}, {1, 9}, {2, 3} }, 4096 };
    std::cout << "0x0 -> " << mmu.translate(0) << '\\n';        // 20480
    std::cout << "0x1001 -> " << mmu.translate(4097) << '\\n';   // 37401
}`,
          go: `package main

import "fmt"

type MMU struct {
    pageTable map[int]int
    pageSize  int
}

func (m *MMU) translate(vaddr int) int {
    page := vaddr / m.pageSize
    off := vaddr % m.pageSize
    frame, ok := m.pageTable[page]
    if !ok {
        fmt.Println("PAGE FAULT: page", page)
        return -1
    }
    return frame*m.pageSize + off
}

func main() {
    m := &MMU{
        pageTable: map[int]int{0: 5, 1: 9, 2: 3},
        pageSize:  4096,
    }
    fmt.Println("0x0 ->", m.translate(0))
    fmt.Println("0x1001 ->", m.translate(4097))
}`,
          python: `class MMU:
    def __init__(self, page_table, page_size=4096):
        self.page_table = page_table
        self.page_size = page_size

    def translate(self, vaddr):
        page = vaddr // self.page_size
        off  = vaddr % self.page_size
        if page not in self.page_table:
            print(f"PAGE FAULT: page {page}")
            return -1
        return self.page_table[page] * self.page_size + off

mmu = MMU({0: 5, 1: 9, 2: 3})
print("0x0 ->", mmu.translate(0))
print("0x1001 ->", mmu.translate(4097))`,
          java: `import java.util.*;

public class MMU {
    Map<Integer, Integer> pageTable;
    int pageSize;
    MMU(Map<Integer,Integer> pt, int ps) { pageTable = pt; pageSize = ps; }

    int translate(int vaddr) {
        int page = vaddr / pageSize;
        int off  = vaddr % pageSize;
        Integer frame = pageTable.get(page);
        if (frame == null) {
            System.out.println("PAGE FAULT: page " + page);
            return -1;
        }
        return frame * pageSize + off;
    }

    public static void main(String[] args) {
        var pt = Map.of(0, 5, 1, 9, 2, 3);
        MMU mmu = new MMU(pt, 4096);
        System.out.println("0x0 -> " + mmu.translate(0));
        System.out.println("0x1001 -> " + mmu.translate(4097));
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: Page table নিজেই অনেক memory নিতে পারে। 32-bit system-এ 4 KB page হলে 4 GB প্রতি process-এ 4 MB page table লাগে। সমাধান: multi-level page table + TLB (Translation Lookaside Buffer) cache।",
      },
    ],
  },

  // ---- Ch 07 - Virtual Memory ----
  {
    id: "os-virtual-memory",
    subject: "os",
    title: "Ch 07 — Virtual Memory",
    bangla: "ভার্চুয়াল মেমোরি",
    difficulty: "Hard",
    est: "1.5 hr",
    summary:
      "Demand paging, page faults, TLB, copy-on-write. Page replacement: FIFO, LRU, Optimal, Clock. Thrashing.",
    sections: [
      { type: "h2", id: "what", title: "What is Virtual Memory?" },
      {
        type: "p",
        text: "Virtual memory হলো এমন একটি technique যেখানে প্রতিটি process-কে মনে হয় সে একটি contiguous, বিশাল memory space একা পাচ্ছে, যদিও বাস্তবে physical RAM ছোট এবং অনেক process-এর সাথে share করা হচ্ছে। OS ও MMU একসাথে virtual-to-physical address translation করে page table ও TLB (Translation Lookaside Buffer) ব্যবহার করে।",
      },
      {
        type: "p",
        text: "যদি page-টি এই মুহূর্তে RAM-ে না থাকে (disk-এ swapped out), page fault হয় — OS trap করে, disk থেকে page কে RAM-ে আনে, page table update করে, এবং faulting instruction আবার চালায়। এই process-কে demand paging বলে। এর ফলে program তার logical মতো বড় হতে পারে যদি physical RAM ছোট হয়।",
      },
      { type: "h2", id: "replacement", title: "Page Replacement Algorithms" },
      {
        type: "p",
        text: "যখন RAM পূর্ণ এবং নতুন page আনতে হবে, OS কোন existing page-কে swap out করবে সেই সিদ্ধান্ত নেয়। ভালো algorithm future-ে যে pages ব্যবহার হবে সেগুলো ধরে রাখে। কিন্তু future জানা যায় না — তাই heuristic দিয়ে approximate করা হয়।",
      },
      {
        type: "list",
        items: [
          "FIFO — যে page সবার আগে এসেছিল সে বের যায় (সহজ, কিন্তু Belady's anomaly আছে)",
          "Optimal — ভবিষ্যতে সবচেয়ে দেরিতে দরকার হবে সেটা বের করা (theoretical bound, বাস্তবায়নযোগ্য নয়)",
          "LRU — সবচেয়ে বেশি সময় ধরে ব্যবহৃত হয়নি সেটা বের করা (ভালো, কিন্তু দামি)",
          "Clock (Second Chance) — LRU-র approximation, একটি circular list + reference bit",
        ],
      },
      { type: "h3", title: "LRU Page Replacement Simulation" },
      {
        type: "multi-code",
        filename: "lru_replace",
        codeSamples: {
          cpp: `#include <iostream>
#include <list>
#include <unordered_map>
#include <vector>
using namespace std;

int lru(const vector<int>& refs, int frames) {
    list<int> cache;                         // front = LRU
    unordered_map<int, list<int>::iterator> pos;
    int faults = 0;
    for (int p : refs) {
        if (pos.count(p)) {
            cache.erase(pos[p]);             // move to MRU
        } else {
            faults++;
            if ((int)cache.size() == frames) {
                pos.erase(cache.front());
                cache.pop_front();
            }
        }
        cache.push_back(p);
        pos[p] = prev(cache.end());
    }
    return faults;
}

int main() {
    cout << lru({7,0,1,2,0,3,0,4,2,3,0,3,2}, 3) << '\\n';   // 7
}`,
          go: `package main

import "container/list"

func lru(refs []int, frames int) int {
    cache := list.New()
    pos := map[int]*list.Element{}
    faults := 0
    for _, p := range refs {
        if e, ok := pos[p]; ok {
            cache.Remove(e)
        } else {
            faults++
            if cache.Len() == frames {
                old := cache.Front()
                delete(pos, old.Value.(int))
                cache.Remove(old)
            }
        }
        pos[p] = cache.PushBack(p)
    }
    return faults
}

func main() {
    println(lru([]int{7,0,1,2,0,3,0,4,2,3,0,3,2}, 3))   // 7
}`,
          python: `from collections import OrderedDict

def lru(refs, frames):
    cache = OrderedDict()   # tail = MRU
    faults = 0
    for p in refs:
        if p in cache:
            cache.move_to_end(p)
        else:
            faults += 1
            if len(cache) == frames:
                cache.popitem(last=False)
            cache[p] = True
    return faults

print(lru([7,0,1,2,0,3,0,4,2,3,0,3,2], 3))   # 7`,
          java: `import java.util.*;

public class LRU {
    static int lru(int[] refs, int frames) {
        // tail = MRU
        LinkedHashMap<Integer, Boolean> cache = new LinkedHashMap<>(16, 0.75f, true);
        int faults = 0;
        for (int p : refs) {
            if (!cache.containsKey(p)) {
                faults++;
                if (cache.size() == frames) {
                    Iterator<Integer> it = cache.keySet().iterator();
                    it.next(); it.remove();
                }
            }
            cache.put(p, true);
        }
        return faults;
    }

    public static void main(String[] args) {
        System.out.println(lru(new int[]{7,0,1,2,0,3,0,4,2,3,0,3,2}, 3));
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: যদি working set RAM-র চেয়ে বড় হয়ে যায়, page fault rate অস্বাভাবিক বেড়ে যায় — একে thrashing বলে। CPU প্রায় সব সময় swapping-এ নষ্ট করে, actual work প্রায় বন্ধ। সমাধান: working set model, অথবা কিছু process-কে swap out করা।",
      },
    ],
  },

  // ---- Ch 08 - File System ----
  {
    id: "os-filesystem",
    subject: "os",
    title: "Ch 08 — File System",
    bangla: "ফাইল সিস্টেম",
    difficulty: "Medium",
    est: "1 hr",
    summary:
      "Files, directories, inodes, FAT vs NTFS vs ext4, mount points, journaling. Open/read/write/close lifecycle.",
    sections: [
      { type: "h2", id: "what", title: "What is a File System?" },
      {
        type: "p",
        text: "File system (ফাইল সিস্টেম) হলো OS-ের সেই অংশ যা disk-ে data কীভাবে organize ও store করা হবে তা manage করে। এটি raw block device-কে একটি hierarchical structure হিসেবে দেখায় — files (নাম দেওয়া data collection) ও directories (file ও অন্য directory রাখে)। ব্যবহারকারী শুধু 'cat hello.txt' চালায়, কিন্তু OS-কে আসলে খুঁজে বের করতে হয় disk-এর কোন block-এ hello.txt-এর data আছে।",
      },
      { type: "h3", title: "Common File Systems" },
      {
        type: "list",
        items: [
          "ext4 — Linux default, journaling, extents, supports large files",
          "XFS — SGI origin, high parallelism, used in RHEL/CentOS",
          "NTFS — Windows default, journaling, ACLs, compression",
          "FAT32 / exFAT — simple, cross-platform, USB drives",
          "APFS — Apple, copy-on-write, snapshots, encryption",
          "ZFS — CoW, checksums, pools, advanced RAID",
        ],
      },
      { type: "h2", id: "inode", title: "Inode — Index Node" },
      {
        type: "p",
        text: "Unix file system-এ প্রতিটি file-এর একটি inode থাকে — একটি data structure যেখানে file-এর metadata (size, owner, permissions, timestamps) ও disk block pointer থাকে। মজার বিষয়: inode-এ file-ের নাম থাকে না — নাম থাকে directory entry-তে (যেটি নিজে একটি file-name → inode-number mapping table)। একই inode একাধিক নামে থাকতে পারে (hard link)।",
      },
      { type: "h3", title: "Open / Read / Write / Close" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় file read/write দেখানো হলো। প্রতিটি ভাষা ভেতরে ভেতরে open/read/write/close syscall করে।",
      },
      {
        type: "multi-code",
        filename: "file_io",
        codeSamples: {
          cpp: `#include <fstream>
#include <iostream>
#include <string>

int main() {
    // write
    {
        std::ofstream out("hello.txt");
        out << "hello, filesystem\\n";
    }
    // read
    std::ifstream in("hello.txt");
    std::string line;
    while (std::getline(in, line)) std::cout << line << '\\n';
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os"
)

func main() {
    // write (0644 = rw-r--r--)
    err := os.WriteFile("hello.txt", []byte("hello, filesystem\\n"), 0644)
    if err != nil { panic(err) }

    // read
    data, err := os.ReadFile("hello.txt")
    if err != nil { panic(err) }
    fmt.Print(string(data))
}`,
          python: `# write
with open("hello.txt", "w") as f:
    f.write("hello, filesystem\\n")

# read
with open("hello.txt", "r") as f:
    print(f.read(), end="")`,
          java: `import java.nio.file.*;

public class FileIO {
    public static void main(String[] args) throws Exception {
        Path p = Paths.get("hello.txt");
        Files.writeString(p, "hello, filesystem\\n");
        String content = Files.readString(p);
        System.out.print(content);
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: প্রতিটি open file-ের জন্য kernel-ে একটি file descriptor (FD) entry থাকে। যদি close না করেন, FD leak হয়। Linux-ে ulimit -n দিয়ে per-process FD limit দেখুন (default 1024)।",
      },
    ],
  },

  // ---- Ch 09 - I/O System ----
  {
    id: "os-io",
    subject: "os",
    title: "Ch 09 — I/O System",
    bangla: "আই/ও সিস্টেম",
    difficulty: "Medium",
    est: "50 min",
    summary:
      "I/O hardware (polling, interrupts, DMA), I/O software layers, device drivers, spooling. Asynchronous I/O.",
    sections: [
      { type: "h2", id: "what", title: "How Does I/O Work?" },
      {
        type: "p",
        text: "I/O (Input/Output) বলতে disk, network, keyboard, GPU, printer — সব hardware device-ের সাথে data exchange বোঝায়। এই device গুলো CPU থেকে অনেক ধীর — disk seek ~10 ms, network round-trip ~50 ms, যেখানে CPU cycle ~1 ns। তাই OS-কে এমন ভাবে design করতে হয় যাতে CPU device-ের জন্য অপেক্ষা না করে।",
      },
      { type: "h3", title: "Three I/O Mechanisms" },
      {
        type: "list",
        items: [
          "Polling — CPU বারবার device-ের status register চেক করে (CPU নষ্ট হয়)",
          "Interrupt-driven — device কাজ শেষে interrupt পাঠায়, CPU অন্য কাজ করে",
          "DMA (Direct Memory Access) — DMA controller নিজে থেকে device<->memory transfer করে, CPU শুধু শুরু ও শেষে জড়িত",
        ],
      },
      { type: "h2", id: "async", title: "Asynchronous I/O" },
      {
        type: "p",
        text: "Modern application-ে synchronous I/O (read call block হয়) এড়িয়ে asynchronous I/O ব্যবহার করা হয়। Thread I/O wait না করে, OS-কে request করে এবং অন্য কাজ করতে থাকে। যখন I/O শেষ, kernel callback বা future complete করে।",
      },
      {
        type: "multi-code",
        filename: "async_io",
        codeSamples: {
          cpp: `#include <iostream>
#include <fstream>
#include <future>
#include <vector>

int main() {
    std::vector<std::future<std::string>> futures;
    for (int i = 0; i < 3; i++) {
        futures.push_back(std::async(std::launch::async, [i] {
            std::ifstream in("file_" + std::to_string(i) + ".txt");
            return std::string((std::istreambuf_iterator<char>(in)),
                               std::istreambuf_iterator<char>());
        }));
    }
    for (auto& f : futures) std::cout << f.get() << '\\n';
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os"
    "sync"
)

func main() {
    var wg sync.WaitGroup
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            data, _ := os.ReadFile(fmt.Sprintf("file_%d.txt", i))
            fmt.Println(string(data))
        }(i)
    }
    wg.Wait()
}`,
          python: `import asyncio
import aiofiles  # pip install aiofiles

async def read_file(i):
    async with aiofiles.open(f"file_{i}.txt") as f:
        return await f.read()

async def main():
    contents = await asyncio.gather(*(read_file(i) for i in range(3)))
    for c in contents:
        print(c)

asyncio.run(main())`,
          java: `import java.nio.file.*;
import java.util.concurrent.*;

public class AsyncIO {
    public static void main(String[] args) throws Exception {
        ExecutorService pool = Executors.newFixedThreadPool(3);
        var futures = new CompletableFuture[3];
        for (int i = 0; i < 3; i++) {
            final int idx = i;
            futures[i] = CompletableFuture.supplyAsync(() -> {
                try { return Files.readString(Path.of("file_" + idx + ".txt")); }
                catch (Exception e) { return ""; }
            }, pool);
        }
        for (var f : futures) System.out.println(f.get());
        pool.shutdown();
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Node.js, Go, Java NIO — সব modern runtime একই kernel mechanism (Linux-ে epoll, macOS-এ kqueue, Windows-ে IOCP) ব্যবহার করে। Single thread অনেক I/O handle করতে পারে, যেহেতু প্রতিটি operation non-blocking।",
      },
    ],
  },

  // ---- Ch 10 - Protection & Security ----
  {
    id: "os-security",
    subject: "os",
    title: "Ch 10 — Protection & Security",
    bangla: "সুরক্ষা ও নিরাপত্তা",
    difficulty: "Medium",
    est: "50 min",
    summary:
      "Access matrix, ACL, capabilities, authentication, principle of least privilege. Buffer overflow & ASLR.",
    sections: [
      { type: "h2", id: "what", title: "Protection vs Security" },
      {
        type: "p",
        text: "Protection (সুরক্ষা) হলো OS-ের internal mechanism যা নিশ্চিত করে যে কোনো process তার permission-ের বাইরে resource access করতে পারবে না। Security (নিরাপত্তা) হলো বৃহত্তর ধারণা — external attacker থেকে system রক্ষা করা, যার অংশ হলো protection। Security = protection + authentication + cryptography + audit + physical security।",
      },
      { type: "h3", title: "Principle of Least Privilege" },
      {
        type: "p",
        text: "প্রতিটি process, user, বা program-কে শুধু ততটুকু privilege দেওয়া উচিত যতটুকু তার কাজের প্রয়োজন — আর এক মিনিট বেশি না। একে Principle of Least Privilege (PoLP) বলে। যেমন web server-কে root permission দেওয়া উচিত নয়; সে শুধু একটি unprivileged user হিসেবে চলবে, যাতে attacker exploit করলেও সীমিত ক্ষতি হয়।",
      },
      { type: "h2", id: "acl", title: "Access Control List (ACL)" },
      {
        type: "p",
        text: "ACL হলো প্রতিটি resource-ের সাথে যুক্ত একটি list যা বলে কোন user কোন operation করতে পারে। যেমন file ACL বলতে পারে: 'alice: read+write, bob: read-only, others: none'। এটি column-wise view — resource কেন্দ্রিক। বিপরীত ধারণা capability — যেখানে user-এর কাছে একটি unforgeable token থাকে যা resource access দেয় (row-wise view)।",
      },
      {
        type: "multi-code",
        filename: "acl_check",
        codeSamples: {
          cpp: `#include <iostream>
#include <string>
#include <unordered_map>

enum class Perm { NONE = 0, READ = 1, WRITE = 2, EXEC = 4 };

inline Perm operator|(Perm a, Perm b) {
    return static_cast<Perm>(static_cast<int>(a) | static_cast<int>(b));
}
inline bool has(Perm set, Perm p) {
    return (static_cast<int>(set) & static_cast<int>(p)) != 0;
}

int main() {
    // file -> user -> permission
    std::unordered_map<std::string,
        std::unordered_map<std::string, Perm>> acl = {
        {"secret.txt", { {"alice", Perm::READ | Perm::WRITE},
                          {"bob",   Perm::READ} }}
    };

    auto& fileAcl = acl["secret.txt"];
    Perm aliceP = fileAcl["alice"];

    std::cout << "alice read: "  << has(aliceP, Perm::READ)  << '\\n';
    std::cout << "alice write: " << has(aliceP, Perm::WRITE) << '\\n';
    std::cout << "alice exec: "  << has(aliceP, Perm::EXEC)  << '\\n';
    return 0;
}`,
          go: `package main

import "fmt"

type Perm int

const (
    Read Perm = 1 << iota
    Write
    Exec
)

func (p Perm) Has(bit Perm) bool { return p&bit != 0 }

func main() {
    acl := map[string]map[string]Perm{
        "secret.txt": {
            "alice": Read | Write,
            "bob":   Read,
        },
    }
    alice := acl["secret.txt"]["alice"]
    fmt.Println("alice read:",  alice.Has(Read))
    fmt.Println("alice write:", alice.Has(Write))
    fmt.Println("alice exec:",  alice.Has(Exec))
}`,
          python: `from enum import Flag, auto

class Perm(Flag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    EXEC = auto()

acl = {
    "secret.txt": {
        "alice": Perm.READ | Perm.WRITE,
        "bob":   Perm.READ,
    },
}

alice = acl["secret.txt"]["alice"]
print("alice read:",  bool(alice & Perm.READ))
print("alice write:", bool(alice & Perm.WRITE))
print("alice exec:",  bool(alice & Perm.EXEC))`,
          java: `import java.util.*;

public class ACL {
    enum Perm { NONE, READ, WRITE, EXEC }
    static class PermSet {
        final Set<Perm> perms;
        PermSet(Perm... ps) { perms = EnumSet.noneOf(Perm.class);
            for (Perm p : ps) if (p != Perm.NONE) perms.add(p); }
        boolean has(Perm p) { return perms.contains(p); }
    }

    public static void main(String[] args) {
        Map<String, Map<String, PermSet>> acl = Map.of(
            "secret.txt", Map.of(
                "alice", new PermSet(Perm.READ, Perm.WRITE),
                "bob",   new PermSet(Perm.READ)
            )
        );
        PermSet alice = acl.get("secret.txt").get("alice");
        System.out.println("alice read: "  + alice.has(Perm.READ));
        System.out.println("alice write: " + alice.has(Perm.WRITE));
        System.out.println("alice exec: "  + alice.has(Perm.EXEC));
    }
}`,
        },
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: সবচেয়ে বড় security risk হলো buffer overflow — C/C++ program-ে user input সরাসরি fixed-size buffer-ে copy করলে adjacent memory overwrite হয়ে যায়। Modern OS-ে ASLR (Address Space Layout Randomization), DEP/NX, stack canaries দিয়ে এটা mitigate করা হয়। Rust, Go, Java memory-safe ভাষায় এই সমস্যা প্রায় নেই।",
      },
    ],
  },

  // ---- Ch 11 - Virtualization & Cloud ----
  {
    id: "os-virt",
    subject: "os",
    title: "Ch 11 — Virtualization & Cloud",
    bangla: "ভার্চুয়ালাইজেশন ও ক্লাউড",
    difficulty: "Medium",
    est: "45 min",
    summary:
      "Hypervisor types, containerization (Docker, K8s), cloud service models (IaaS, PaaS, SaaS). VM vs container.",
    sections: [
      { type: "h2", id: "what", title: "What is Virtualization?" },
      {
        type: "p",
        text: "Virtualization হলো একটি physical hardware-কে একাধিক isolated execution environment-ে ভাগ করা। প্রতিটি environment-ে নিজস্ব OS (guest) চলতে পারে, এবং তারা একে অপরকে দেখে না। এর ফলে একটি physical server-ে অনেক OS workload চালানো যায়, utilization বাড়ে ও cost কমে। এই কাজের জন্য একটি thin software layer দরকার — hypervisor।",
      },
      { type: "h3", title: "Hypervisor Types" },
      {
        type: "list",
        items: [
          "Type 1 (bare-metal) — সরাসরি hardware-ে চলে, কোনো host OS নেই (VMware ESXi, Xen, KVM, Hyper-V)",
          "Type 2 (hosted) — একটি host OS-ের উপর program হিসেবে চলে (VirtualBox, VMware Workstation, QEMU)",
          "Paravirtualization — guest OS-কে modified করা হয় hypervisor call করার জন্য (Xen)",
          "Hardware-assisted — Intel VT-x / AMD-V এর সাহায্যে কাছাকাছি native performance (KVM)",
        ],
      },
      { type: "h2", id: "containers", title: "Containers vs VMs" },
      {
        type: "p",
        text: "VM (Virtual Machine) প্রতিটির নিজস্ব kernel থাকে, gigabyte-এ মাপা যায়, বুট হতে মিনিট লাগে। Container (যেমন Docker) শুধু user-space isolate করে — kernel host-এর সাথে share করে। কয়েক megabyte, সেকেন্ডে বুট। এর পেছনে দুটি kernel feature — namespaces (isolation) ও cgroups (resource limit)।",
      },
      {
        type: "list",
        items: [
          "PID namespace — container-ে নিজস্ব PID 1 থাকে",
          "Network namespace — নিজস্ব loopback, routes, firewall",
          "Mount namespace — নিজস্ব filesystem tree",
          "User namespace — container-এর root host-ে unprivileged",
          "Cgroups — CPU, memory, IO limit",
        ],
      },
      { type: "h3", title: "Spawn an Isolated Subprocess" },
      {
        type: "multi-code",
        filename: "isolated_subprocess",
        codeSamples: {
          cpp: `#include <sched.h>
#include <unistd.h>
#include <sys/wait.h>
#include <iostream>

// Run a child with a NEW PID namespace + UID/GID mapping.
// Requires CAP_SYS_ADMIN (run with sudo or setcap).
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // become a sub-reaper in a new PID + mount namespace
        unshare(CLONE_NEWPID | CLONE_NEWNS);
        // re-exec yourself, you'll now be PID 1 in the new namespace
        execl("/bin/echo", "echo", "isolated", nullptr);
    } else {
        int status; waitpid(pid, &status, 0);
        std::cout << "child done, status=" << status << '\\n';
    }
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os/exec"
    "syscall"
)

func main() {
    cmd := exec.Command("/bin/echo", "isolated")
    // Ask kernel to give this child its own PID + mount namespace
    cmd.SysProcAttr = &syscall.SysProcAttr{
        Cloneflags: syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
    }
    out, err := cmd.Output()
    if err != nil { fmt.Println("err:", err); return }
    fmt.Println(string(out))
}`,
          python: `import subprocess

# Linux only — child gets its own PID namespace.
# Requires root or CAP_SYS_ADMIN.
proc = subprocess.Popen(
    ["/bin/echo", "isolated"],
    stdout=subprocess.PIPE,
    start_new_session=True,  # new session, but not a full namespace
)
out, _ = proc.communicate()
print(out.decode(), end="")`,
          java: `// Java standard library doesn't expose namespace flags.
// Real containers are launched via the Docker / containerd API.
import java.nio.file.*;

public class IsolatedSubprocess {
    public static void main(String[] args) throws Exception {
        ProcessBuilder pb = new ProcessBuilder("docker", "run", "--rm",
            "alpine:3", "echo", "isolated");
        pb.inheritIO();
        Process p = pb.start();
        System.out.println("exit=" + p.waitFor());
    }
}`,
        },
      },
      { type: "h2", id: "cloud", title: "Cloud Service Models" },
      {
        type: "list",
        items: [
          "IaaS (Infrastructure as a Service) — VM rent করো, OS-tuning তোমার (AWS EC2, GCP Compute)",
          "PaaS (Platform as a Service) — runtime ready, শুধু code deploy (Heroku, App Engine, Vercel)",
          "SaaS (Software as a Service) — সম্পূর্ণ app (Gmail, Notion, Figma)",
          "FaaS (Functions as a Service) — per-request billing, no server mgmt (AWS Lambda, Cloud Functions)",
        ],
      },
    ],
  },

  // ---- Ch 12 - Distributed OS ----
  {
    id: "os-distributed",
    subject: "os",
    title: "Ch 12 — Distributed OS",
    bangla: "ডিস্ট্রিবিউটেড অপারেটিং সিস্টেম",
    difficulty: "Hard",
    est: "1.5 hr",
    summary:
      "Distributed systems, RPC, message passing, clock sync (Lamport, vector clocks), consensus (Paxos, Raft).",
    sections: [
      { type: "h2", id: "what", title: "What is a Distributed System?" },
      {
        type: "p",
        text: "Distributed system (ডিস্ট্রিবিউটেড সিস্টেম) হলো এমন একটি system যেখানে অনেকগুলো independent computer একটি network-ে যুক্ত থাকে এবং ব্যবহারকারীর কাছে একটি single coherent system হিসেবে দেখা যায়। বাস্তবে কোনো 'single OS' নেই — প্রতিটি node তার নিজস্ব OS ও state রাখে — কিন্তু high-level protocol (RPC, message passing, consensus) দিয়ে তারা coordinate করে।",
      },
      {
        type: "p",
        text: "Distributed system-এ একটি মৌলিক সমস্যা — clocks sync করা। প্রতিটি machine-ের নিজস্ব clock, এবং physical clock গুলো ধীরে ধীরে drift করে (NTP-তেও কয়েক ms-এর difference থাকে)। তাই event-ের ordering নির্ধারণ করা কঠিন। Lamport clock ও vector clock এই সমস্যা solve করার logical clock approach।",
      },
      { type: "h2", id: "lamport", title: "Lamport Logical Clocks" },
      {
        type: "p",
        text: "Leslie Lamport-এর idea: physical clock-ের চেয়ে event-ের causal order বেশি গুরুত্বপূর্ণ। প্রতিটি process একটি monotonic integer রাখে। প্রতিটি local event-ের আগে সে increment করে। যখন এক message পাঠায়, সে তার clock value message-ে attach করে। যখন receiver message পায়, সে নিজের clock ও message-এর timestamp-ের maximum নিয়ে +1 করে।",
      },
      {
        type: "multi-code",
        filename: "lamport_clock",
        codeSamples: {
          cpp: `#include <iostream>
#include <atomic>
#include <mutex>

class LamportClock {
    std::atomic<int> t{0};
    std::mutex m;
public:
    int local() {
        return ++t;        // before any event
    }
    int send() {
        return ++t;        // piggyback on outgoing msg
    }
    int receive(int msgTs) {
        std::lock_guard<std::mutex> lk(m);
        t = std::max(t.load(), msgTs) + 1;
        return t;
    }
};

int main() {
    LamportClock a, b;
    a.local();                  // a=1
    int m = a.send();           // a=2, msg carries 2
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
      { type: "h3", title: "Consensus: Paxos & Raft" },
      {
        type: "p",
        text: "Distributed system-ে একটি fundamental problem হলো consensus — অনেক node কীভাবে একটি value-তে agree করবে, যদি কিছু node crash করে বা network partition হয়? Paxos (Lamport, 1998) ও Raft (Ongaro, 2014) দুটি practical consensus algorithm, যা modern distributed system-এ ব্যবহৃত হয় (etcd, Consul, ZooKeeper, Spanner)।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: CAP theorem অনুযায়ী, distributed system একসাথে Consistency, Availability, Partition tolerance — এর মধ্যে যেকোনো দুটি পাবে। Network partition এড়ানো যায় না (P mandatory), তাই আসলে CP বা AP-র মধ্যে বেছে নিতে হয়।",
      },
    ],
  },

  // ---- Ch 13 - Advanced Topics ----
  {
    id: "os-advanced",
    subject: "os",
    title: "Ch 13 — Advanced Topics",
    bangla: "অ্যাডভান্সড টপিকস",
    difficulty: "Medium",
    est: "50 min",
    summary:
      "Real-time OS, embedded OS, mobile OS, multicore scheduling, GPU computing, energy-aware scheduling.",
    sections: [
      { type: "h2", id: "what", title: "Beyond General-Purpose OS" },
      {
        type: "p",
        text: "আজকের OS শুধু desktop / server-ে সীমাবদ্ধ নয়। Real-time OS (RTOS) strict deadline মানে (যেমন airbag controller কয়েক ms-এ বের হবে)। Embedded OS ছোট footprint ও কম power নেয় (IoT ডিভাইস)। Mobile OS power-aware, touch-centric। এই সব ক্ষেত্রে general-purpose OS (Linux, Windows) এর চেয়ে specialized design প্রয়োজন।",
      },
      { type: "h3", title: "Categories of Specialized OS" },
      {
        type: "list",
        items: [
          "RTOS (Real-Time) — VxWorks, FreeRTOS, Zephyr, QNX — hard/soft deadline",
          "Embedded OS — Embedded Linux, NuttX, TinyOS — small footprint, low power",
          "Mobile OS — Android, iOS — touch UI, app sandboxing, battery",
          "Multicore / NUMA-aware OS — Linux with CFS + scheduler domains",
          "GPU / heterogeneous OS — CUDA runtime, ROCm",
        ],
      },
      { type: "h2", id: "rtos", title: "Real-Time Scheduling" },
      {
        type: "p",
        text: "RTOS-ে deadline miss = system failure। তাই scheduling algorithm শুধু fairness নয়, deadline guarantee করে। দুটি classic algorithm: Rate Monotonic (RM) — ছোট period বেশি priority, এবং Earliest Deadline First (EDF) — যার deadline সবচেয়ে কাছে তাকে priority দেওয়া। EDF তাত্ত্বিকভাবে optimal — যদি কোনো schedule feasible হয়, EDF তা পাবে।",
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
        // earliest deadline = smallest period
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
    tasks := []Task{
        {1, 4, 1}, {2, 6, 2}, {3, 8, 3},
    }
    for t := 0; t < 24; t++ {
        // re-release
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
    record Task(int id, int period, int[] wcet) {}

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
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Multicore scheduling এখন OS-ের সবচেয়ে active research area — Linux-ে EEVDF (Earliest Eligible Virtual Deadline First) সম্প্রতি CFS-কে replace করেছে (kernel 6.6+)। আর GPU computing, NPU, eBPF — এসব modern trend-ে OS concept গুলো নতুন করে apply হচ্ছে।",
      },
    ],
  },
];
'''

after = content[topics_end + len(topics_end_marker):]
new_content = before + new_os_section + after

# Sanity check
os_count = new_content.count('id: "os-')
assert os_count == 13, f"Expected 13 OS topics, got {os_count}"
assert ": Project[] = [" in new_content, "PROJECTS export missing"
assert "export const CHEATSHEETS" in new_content, "CHEATSHEETS export missing"

CONTENT_FILE.write_text(new_content)
print(f"OK — replaced OS section with 13 chapters. File size: {len(new_content)} bytes")
