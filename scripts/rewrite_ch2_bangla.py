#!/usr/bin/env python3
"""
Rewrite Ch 02 (Process Management) with MAXIMUM BANGLA + English technical terms.
Same pattern as Ch 01 rewrite.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch2_marker_start = "// ---- Ch 02 - Process Management ----"
ch3_marker_start = "// ---- Ch 03 - CPU Scheduling ----"

start_idx = text.find(ch2_marker_start)
assert start_idx != -1, "Ch 02 marker not found"
end_idx = text.find(ch3_marker_start, start_idx)
assert end_idx != -1, "Ch 03 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH2 = r'''// ---- Ch 02 - Process Management ----
  {
    id: "os-processes",
    subject: "os",
    title: "Ch 02 — Process Management",
    bangla: "প্রসেস ম্যানেজমেন্ট",
    difficulty: "Medium",
    est: "1.5 hr",
    summary:
      "Process হলো যেকোনো operating system-এর core concept। এই chapter-এ ব্যাখ্যা করা হয়েছে process কী, OS কীভাবে সেটি manage করে, এবং modern systems কীভাবে threads use করে performance ও responsiveness improve করে।",
    sections: [
      { type: "h2", id: "concept", title: "Process Concept: Program vs Process" },
      {
        type: "p",
        text: "Program হলো একটি passive entity — disk-এ একটি file যেখানে instructions ও data থাকে (যেমন a.out, chrome.exe)। Process হলো একটি active entity — execution-এ থাকা একটি program, যার নিজস্ব memory, registers, ও state থাকে। অর্থাৎ program হলো static file, process হলো সেই program-এর live execution।",
      },
      { type: "h3", title: "Key distinction" },
      {
        type: "list",
        items: [
          "Program: static, disk-এ store থাকে, কোনো resources allocate করা না।",
          "Process: dynamic, memory-তে load থাকে, OS own করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি recipe (program) শুধু কাগজে লেখা text। যখন আপনি recipe follow করেন — pan heat করেন, onion chop করেন, stir করেন — সেটা হলো process। একই recipe অনেক chef একসাথে cook করতে পারে, প্রত্যেকটা আলাদা process।",
      },

      { type: "h2", id: "states", title: "Process States" },
      {
        type: "p",
        text: "একটি process execute হওয়ার সময় state change করে। OS এই states track করে যাতে CPU ও memory efficiently manage করা যায়। প্রতিটি process তার lifetime-এ পাঁচটি state-এর মধ্য দিয়ে যায়।",
      },
      { type: "h3", title: "The 5 Process States" },
      {
        type: "list",
        items: [
          "New — process create হচ্ছে (যেমন fork() call হয়েছে কিন্তু ready না)",
          "Ready — process memory-তে আছে, CPU-এর জন্য অপেক্ষা করছে",
          "Running — instructions এই মুহূর্তে CPU-তে execute হচ্ছে",
          "Waiting — process block হয়ে আছে, কোনো event-এর জন্য অপেক্ষা করছে (I/O completion, signal)",
          "Terminated — process execution শেষ করেছে (যেমন exit() call হয়েছে)",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant-এ customer। New: door-এ ঢুকেছে, এখনও seat পায়নি। Ready: table-এর জন্য queue-এ অপেক্ষা করছে। Running: table-এ বসে খাচ্ছে। Waiting: waiter-এর জন্য bill-এর অপেক্ষা করছে। Terminated: restaurant ছেড়ে চলে গেছে। ঠিক একইভাবে process গুলো queue থেকে CPU পায়, কাজ করে, শেষ হয়।",
      },

      { type: "h2", id: "pcb", title: "Process Control Block (PCB)" },
      {
        type: "p",
        text: "প্রতিটি process-এর জন্য OS একটি data structure maintain করে যাকে Process Control Block (task control block ও বলা হয়) বলে। এতে process manage করার জন্য সব information থাকে। প্রতিটি process-এর জন্য kernel-এ একটি PCB entry থাকে।",
      },
      { type: "h3", title: "PCB-র contents" },
      {
        type: "list",
        items: [
          "Process ID (PID) — unique numerical identifier",
          "Program counter — execute হবে এমন next instruction-এর address",
          "CPU registers — সব general-purpose registers, stack pointer, ইত্যাদি",
          "Memory limits — base ও limit registers, page tables",
          "Open file list — file descriptors ও তাদের permissions",
          "I/O status — এই process-এর জন্য assigned devices",
          "Process state — new, ready, running, waiting, terminated",
          "Priority — scheduling priority (যদি থাকে)",
          "Accounting info — কত CPU time use হয়েছে, process owner, ইত্যাদি",
        ],
      },
      {
        type: "p",
        text: "যখন OS একটি process pause করে (যেমন আরেকটা run করার জন্য), সে process-এর CPU state তার PCB-তে save করে। Resume করার সময় PCB থেকে restore করে। এটাই context switch-এর ভিত্তি — পরের section-এ দেখব।",
      },

      { type: "h2", id: "queues", title: "Process Scheduling Queues" },
      {
        type: "p",
        text: "OS বিভিন্ন queues maintain করে যাতে processes-কে তাদের lifecycle জুড়ে manage করা যায়। প্রতিটি process কোনো না কোনো queue-তে অবস্থান করে — কখনো ready, কখনো device queue।",
      },
      { type: "h3", title: "Queue-র ধরন" },
      {
        type: "list",
        items: [
          "Job queue — system-এর সব processes (disk-এ বা memory-তে)",
          "Ready queue — Ready state-এ থাকা processes, CPU-এর জন্য অপেক্ষা করছে। PCBs-এর linked list হিসেবে store করা থাকে।",
          "Device queue — নির্দিষ্ট I/O device-এর জন্য অপেক্ষা করা processes (যেমন disk, printer)। প্রতিটি device-এর নিজস্ব queue থাকে।",
        ],
      },
      {
        type: "p",
        text: "Flow: New process → Ready queue → CPU (Running) → যদি I/O লাগে → Device queue → আবার Ready queue → Terminated। Real-life thinking — restaurant-এ customers। Job queue = সব customers যারা reserve করেছে। Ready queue = waiting area-তে থাকা customers। Device queue = নির্দিষ্ট waiter-এর জন্য অপেক্ষা করা customers। একটি process এই cycle বারবার পার করে।",
      },

      { type: "h2", id: "context-switch", title: "Context Switching" },
      {
        type: "p",
        text: "Context switching হলো currently running process-এর state (PCB) save করা এবং অন্য একটি process-এর saved state load করা। এটি CPU-কে efficiently processes-এর মধ্যে switch করতে দেয়, concurrency-র illusion তৈরি করে। CPU আসলে এক সময়ে একটাই process চালায়, কিন্তু fast context switch-এর কারণে মনে হয় সব একসাথে চলছে।",
      },
      { type: "h3", title: "Context switch-এর ধাপ" },
      {
        type: "list",
        items: [
          "1. Current process-এর CPU registers ও program counter তার PCB-তে save করা",
          "2. PCB state update করা (যেমন Running → Ready)",
          "3. PCB-কে appropriate queue-তে move করা (ready বা device queue)",
          "4. Ready queue থেকে আরেকটি process select করা (scheduler দিয়ে)",
          "5. তার PCB থেকে CPU registers load করা, program counter সহ",
          "6. নতুন process execute শুরু করা",
        ],
      },
      {
        type: "p",
        text: "Overhead: context switching হলো pure overhead — CPU switching-এর সময় কোনো useful কাজ করে না। Cost hardware support (কতগুলো register save করতে হবে) ও memory management (TLB flush)-এর উপর depend করে। সাধারণত 1-10 µs প্রতি switch।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন professor assignments grade করছেন। যখন একজন student প্রশ্ন জিজ্ঞাসে, professor তার current paper-এ জায়গা চিহ্নিত করে (PCB), student-এর দিকে ঘোরেন (new process), উত্তর দেন, তারপর আগের paper-এ ফিরে যান (state restore)। প্রতিবার switch করতে গেলে সময় নষ্ট হয়।",
      },

      { type: "h2", id: "creation", title: "Process Creation and Termination" },
      { type: "h3", title: "Creation — fork() ও exec()" },
      {
        type: "p",
        text: "একটি process আরেকটি process fork() system call (Unix/Linux) বা CreateProcess() (Windows) দিয়ে create করতে পারে। Create করা process হলো parent, নতুনটা হলো child। Unix-এ fork() parent-এর একটা exact copy তৈরি করে, child পায় নতুন PID।",
      },
      {
        type: "p",
        text: "fork() (Unix/Linux): parent process-এর exact copy create করে (text, data, heap, stack)। Child পায় নতুন PID ও নিজস্ব memory space। fork() return করে: child process-এ 0; parent-এ child-এর PID; error হলে -1। এই return value difference দিয়ে parent ও child আলাদা code path নেয়।",
      },
      {
        type: "p",
        text: "exec() family current process-এর memory কে একটি নতুন program দিয়ে replace করে। সাধারণত fork()-এর পরে use হয় অন্য একটি program run করার জন্য। অর্থাৎ fork() করে child তৈরি করলাম, exec() দিয়ে সেই child-কে অন্য program-এ পরিণত করলাম।",
      },
      { type: "h3", title: "fork() vs exec()" },
      {
        type: "list",
        items: [
          "fork() calling process-কে clone করে।",
          "exec() নতুন program load করে, পুরোনোটাকে discard করে।",
        ],
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

      { type: "h3", title: "Termination — exit() ও zombie/orphan" },
      {
        type: "p",
        text: "একটি process exit() system call দিয়ে terminate হয়। কারণ: normal completion (main থেকে return বা exit), error বা fatal condition, অন্য process দিয়ে kill (যেমন Unix-এ kill)। যখন কোনো process terminate হয়, OS তার সব resources release করে এবং parent-কে signal পাঠায়।",
      },
      {
        type: "list",
        items: [
          "Zombie process — এমন child যেটি terminate হয়েছে কিন্তু parent এখনও wait() call করেনি। PCB রাখা হয় (exit status store করার জন্য)।",
          "Orphan process — এমন child যার parent child-এর আগে terminate হয়ে গেছে। Unix-এ এমন children-কে init process (PID 1) adopt করে, যে তাদের wait() করে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: Zombie process গুলো memory নেয় না কিন্তু PCB entry দখল করে রাখে। অনেক zombie হলে process table পূর্ণ হয়ে যেতে পারে, নতুন process create করা যাবে না। তাই parent-এর wait() call করা জরুরি।",
      },

      { type: "h2", id: "hierarchy", title: "Process Hierarchies" },
      {
        type: "p",
        text: "Operating systems সাধারণত processes-কে tree-তে organize করে। Root হলো প্রথম process (যেমন Linux-এ init বা systemd, macOS-এ launchd)। প্রতিটি parent তার child গুলোকে manage করে, আবার child গুলো নিজের child তৈরি করতে পারে।",
      },
      {
        type: "code",
        lang: "text",
        text: `init (PID 1)
├─ systemd-logind
├─ sshd
│   └─ bash (user login)
│       └─ gcc (compiler)
└─ chrome
    ├─ chrome (tab process)
    └─ chrome (GPU process)`,
      },
      {
        type: "p",
        text: "Real-life thinking — একটি company CEO (init) যিনি managers (parents) hire করেন, যারা employees (children) hire করেন। কোনো manager leave করলে, employees কে CEO-তে reassign করা যেতে পারে (orphan adoption)। একইভাবে OS-এ parent মারা গেলে child-কে init-এ reassign করা হয়।",
      },

      { type: "h2", id: "process-vs-thread", title: "Process vs Thread" },
      {
        type: "p",
        text: "Thread হলো একটি process-এর ভেতরের lightweight unit of execution। একটি process-এ কমপক্ষে একটি thread (main thread) থাকে। একই process-এর একাধিক thread সেই process-এর memory ও resources share করে। অর্থাৎ thread হলো process-এর ভেতরের ছোট execution unit, যেগুলো memory share করে।",
      },
      { type: "h3", title: "Process vs Thread — Comparison" },
      {
        type: "list",
        items: [
          "Memory space — Process: প্রতিটির আলাদা address space; Thread: একই process-এর ভেতরে shared address space",
          "Resource overhead — Process: high (PCB, page tables, file descriptors); Thread: low (শুধু stack, registers, program counter)",
          "Creation time — Process: slow (memory copy, data structures set up); Thread: fast (বেশির ভাগ resources share)",
          "Context switch — Process: expensive (TLB flush, memory remapping); Thread: cheap (একই address space, কোনো TLB flush নেই)",
          "Communication — Process: IPC (pipes, sockets, shared memory); Thread: shared variables দিয়ে direct",
          "Isolation — Process: strong (এক process অন্যটিকে corrupt করতে পারে না); Thread: weak (এক thread পুরো process crash করতে পারে)",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Process = একটি সম্পূর্ণ বাড়ি: আলাদা kitchen, bathroom, bedroom — অন্য বাড়ি থেকে isolated। Thread = সেই বাড়িতে থাকা একজন মানুষ: সবাই kitchen, bathroom share করে। তারা সরাসরি কথা বলতে পারে, কিন্তু একজন kitchen পুড়িয়ে দিলে বাড়ির সবাই affected হয়। একই কারণে browser tabs process হিসেবে চলে — একটা crash হলে আর সব tab বেঁচে থাকে।",
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

      { type: "h2", id: "ult-klt", title: "User-Level Threads vs Kernel-Level Threads" },
      {
        type: "p",
        text: "Threads দুটি level-এ implement করা যেতে পারে — user-level (ULT) ও kernel-level (KLT)। ULT kernel-কে জানায় না, KLT kernel সরাসরি manage করে।",
      },
      { type: "h3", title: "User-Level Threads (ULT)" },
      {
        type: "p",
        text: "Entirely user-space library দিয়ে manage করা হয় (যেমন কিছু implementation-এ POSIX Pthreads)। Kernel তাদের existence সম্পর্কে অজ্ঞ — সে শুধু একটি single process দেখে। এদের advantage হলো very fast creation ও switching, কারণ kernel mode switch লাগে না।",
      },
      {
        type: "list",
        items: [
          "Advantages: Very fast creation ও switching (কোনো kernel mode switch নেই)। Portable।",
          "Disadvantages: এক thread I/O-তে block হলে পুরো process block হয়ে যায় (kernel সেই process-এর আরেকটি thread schedule করতে পারে না)। Multiple CPU cores utilize করতে পারে না।",
        ],
      },
      { type: "h3", title: "Kernel-Level Threads (KLT)" },
      {
        type: "p",
        text: "OS kernel সরাসরি manage করে। Kernel প্রতিটি thread আলাদাভাবে জানে। Modern Linux (NPTL) ও Windows threads হলো KLT। এদের advantage হলো cores-এ true concurrency, কিন্তু thread creation ও switching-এ syscall লাগে।",
      },
      {
        type: "list",
        items: [
          "Advantages: Cores-এ true concurrency; এক thread block হলে অন্যদের block করে না।",
          "Disadvantages: Create ও switch করতে slow (system call প্রয়োজন)। প্রতি thread-এ বেশি overhead।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — ULT হলো একটি personal to-do list যেটা আপনি নিজে manage করেন (manager এর কোনো involvement নেই)। একটি task stuck হলে আপনার পুরো list stuck। KLT হলো একটি team যেটা manager দিয়ে manage হয় — প্রতিটি task track করা হয়, একটি stuck হলে অন্যগুলো আটকে যায় না। আজকের OS সাধারণত KLT ব্যবহার করে কারণ multicore CPU তখন সম্পূর্ণ utilize হয়।",
      },

      { type: "h2", id: "models", title: "Multithreading Models" },
      {
        type: "p",
        text: "User-level threads ও kernel-level threads-এর মধ্যে relationship তিনটি classic model দ্বারা defined হয়। এগুলো বলে দেয় কতগুলো ULT কতগুলো KLT-এর সাথে mapped হবে।",
      },
      { type: "h3", title: "1. Many-to-One Model" },
      {
        type: "p",
        text: "অনেক user threads একটি single kernel thread-এ mapped। Kernel প্রতি process-এ শুধু একটি thread দেখে। Pros: খুব lightweight। Cons: কোনো parallelism নেই (একসময়ে শুধু এক thread run হয়); blocking I/O সব আটকে দেয়। Example: ancient Unix thread libraries (obsolete)। আজকে আর ব্যবহার হয় না।",
      },
      { type: "h3", title: "2. One-to-One Model" },
      {
        type: "p",
        text: "প্রতিটি user thread আলাদা একটি kernel thread-এ mapped। Pros: true parallelism (প্রতিটি user thread আলাদা core-এ run হতে পারে); blocking I/O অন্যদের affect করে না। Cons: প্রতি thread-এ kernel overhead তৈরি করে; kernel thread limit-এ bounded। Examples: Linux (NPTL), Windows, macOS। আজকের standard model।",
      },
      { type: "h3", title: "3. Many-to-Many Model" },
      {
        type: "p",
        text: "অনেক user threads ছোট বা সমান সংখ্যক kernel threads-এ multiplexed। Kernel threads-এর সংখ্যা পর্যন্ত parallelism allow করে। Pros: performance ও overhead balance করে; user threads freely create করা যায়। Cons: implement করা complex (scheduler activations প্রয়োজন)। Example: original Solaris, পুরোনো hybrid implementations (এখন one-to-one দ্বারা বেশির ভাগ replace হয়ে গেছে কারণ kernel threads সস্তা)।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Program vs process — Program passive disk-এ; process active memory-তে নিজস্ব state সহ।",
          "Process states — new → ready → running → waiting → terminated।",
          "PCB — kernel data structure যেটি সব per-process information store করে।",
          "Scheduling queues — job, ready, device queues process flow manage করার জন্য।",
          "Context switching — PCB save ও restore করে processes-এর মধ্যে CPU switch করা।",
          "Process creation — fork() clone করে, exec() memory image replace করে।",
          "Process termination — exit() resources release করে; parent status-এর জন্য wait() করে।",
          "Process hierarchy — tree structure যেটি init/systemd-এ root হয়।",
          "Process vs thread — threads একই process-এ memory share করে; threads lightweight।",
          "User vs kernel threads — ULT: user-managed, fast, parallelism নেই; KLT: kernel-managed, slower, full concurrency।",
          "Multithreading models — Many-to-one (obsolete), One-to-one (modern), Many-to-many (compromise)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Process ও thread বোঝার পরে CPU scheduling (পরের chapter) পড়া সহজ হবে। কারণ scheduler সত্যিকারের process ও thread গুলোর মধ্যেই decide করে কে CPU পাবে।",
      },
    ],
  },

'''

new_text = before + NEW_CH2 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 02 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
