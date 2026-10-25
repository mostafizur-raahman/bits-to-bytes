#!/usr/bin/env python3
"""
Reformat Ch 02 - Process Management with the new content format:
- English content (user-provided, kept intact)
- + ONE brief Bangla sentence (with English technical terms allowed)
- + Real-life human-thinking example
- + Multi-language code samples (C++/Go/Python/Java)
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
      "A process is the core concept of any operating system. This chapter explains what a process is, how the OS manages it, and how modern systems use threads to improve performance and responsiveness.",
    sections: [
      { type: "h2", id: "concept", title: "Process Concept: Program vs Process" },
      {
        type: "p",
        text: "A program is a passive entity — a file on disk containing instructions and data (e.g., a.out, chrome.exe). A process is an active entity — a program in execution, with its own memory, registers, and state. অর্থাৎ program হলো static file, process হলো সেই program-এর live execution।",
      },
      { type: "h3", title: "Key distinction" },
      {
        type: "list",
        items: [
          "Program: static, stored on disk, no resources allocated.",
          "Process: dynamic, loaded into memory, owned by the OS.",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — a recipe (program) is just text on paper. When you follow the recipe — heat the pan, chop onions, stir — that's a process. একই recipe অনেক chef একসাথে cook করতে পারে, প্রত্যেকটা আলাদা process।",
      },

      { type: "h2", id: "states", title: "Process States" },
      {
        type: "p",
        text: "As a process executes, it changes state. The OS tracks these states to manage CPU and memory efficiently. প্রতিটি process তার lifetime-এ এই পাঁচটি state-এর মধ্য দিয়ে যায়।",
      },
      { type: "h3", title: "The 5 Process States" },
      {
        type: "list",
        items: [
          "New — process is being created (e.g., fork() called but not yet ready)",
          "Ready — process is in memory, waiting to be assigned to the CPU",
          "Running — instructions are actually being executed on the CPU",
          "Waiting — process is blocked, waiting for some event (I/O completion, signal)",
          "Terminated — process has finished execution (e.g., exit() called)",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — a customer in a restaurant. New: enters the door, not yet seated. Ready: waiting in queue for a table. Running: sitting at table, eating. Waiting: waiting for the waiter to bring the bill. Terminated: leaves the restaurant. ঠিক একইভাবে process গুলো queue থেকে CPU পায়, কাজ করে, শেষ হয়।",
      },

      { type: "h2", id: "pcb", title: "Process Control Block (PCB)" },
      {
        type: "p",
        text: "For each process, the OS maintains a data structure called the Process Control Block (also called task control block). It contains all the information needed to manage the process. প্রতিটি process-এর জন্য kernel-ে একটি PCB entry থাকে।",
      },
      { type: "h3", title: "Contents of PCB" },
      {
        type: "list",
        items: [
          "Process ID (PID) — unique numerical identifier",
          "Program counter — address of the next instruction to execute",
          "CPU registers — all general-purpose registers, stack pointer, etc.",
          "Memory limits — base and limit registers, page tables",
          "Open file list — file descriptors and their permissions",
          "I/O status — devices assigned to this process",
          "Process state — new, ready, running, waiting, terminated",
          "Priority — scheduling priority (if any)",
          "Accounting info — CPU time used, process owner, etc.",
        ],
      },
      {
        type: "p",
        text: "When the OS pauses a process (e.g., to run another), it saves the process's CPU state into its PCB. When it resumes, it restores from the PCB. এটা হলো context switch-এর ভিত্তি — পরের section-এ দেখব।",
      },

      { type: "h2", id: "queues", title: "Process Scheduling Queues" },
      {
        type: "p",
        text: "The OS maintains several queues to manage processes throughout their lifecycle. প্রতিটি process কোনো না কোনো queue-তে অবস্থান করে — কখনো ready, কখনো device queue।",
      },
      { type: "h3", title: "Types of Queues" },
      {
        type: "list",
        items: [
          "Job queue — all processes in the system (on disk or in memory)",
          "Ready queue — processes in the Ready state, waiting for CPU. Stored as a linked list of PCBs.",
          "Device queue — processes waiting for a specific I/O device (e.g., disk, printer). Each device has its own queue.",
        ],
      },
      {
        type: "p",
        text: "Flow: New process → Ready queue → CPU (Running) → if I/O → Device queue → back to Ready queue → Terminated. Real-life thinking — customers at a restaurant. Job queue = all customers who reserved. Ready queue = customers in the waiting area. Device queue = customers waiting for a specific waiter. একটি process এই cycle বারবার পার করে।",
      },

      { type: "h2", id: "context-switch", title: "Context Switching" },
      {
        type: "p",
        text: "Context switching is the act of saving the state (PCB) of the currently running process and loading the saved state of another process. It allows the CPU to switch between processes efficiently, giving the illusion of concurrency. CPU আসলে এক সময়ে একটাই process চালায়, কিন্তু fast context switch-এর কারণে মনে হয় সব একসাথে চলছে।",
      },
      { type: "h3", title: "Steps of a Context Switch" },
      {
        type: "list",
        items: [
          "1. Save CPU registers and program counter of the current process into its PCB.",
          "2. Update the PCB state (e.g., from Running → Ready).",
          "3. Move the PCB to the appropriate queue (ready or device queue).",
          "4. Select another process from the ready queue (via scheduler).",
          "5. Load its PCB into CPU registers, including program counter.",
          "6. Start executing the new process.",
        ],
      },
      {
        type: "p",
        text: "Overhead: context switching is pure overhead — the CPU does no useful work while switching. The cost depends on hardware support (how many registers to save) and memory management (TLB flush). সাধারণত 1-10 µs প্রতি switch।",
      },
      {
        type: "p",
        text: "Real-life thinking — a professor grading assignments. When a student asks a question, the professor saves their place in the current paper (PCB), turns to the student (new process), answers, then returns to the previous paper (restores state). প্রতিবার switch করতে গেলে সময় নষ্ট হয়।",
      },

      { type: "h2", id: "creation", title: "Process Creation and Termination" },
      { type: "h3", title: "Creation — fork() and exec()" },
      {
        type: "p",
        text: "A process can create another process using the fork() system call (Unix/Linux) or CreateProcess() (Windows). The creating process is the parent, the new one is the child. Unix-এ fork() parent-এর একটা exact copy তৈরি করে, child পায় নতুন PID।",
      },
      {
        type: "p",
        text: "fork() (Unix/Linux): Creates an exact copy of the parent process (text, data, heap, stack). Child gets a new PID and its own memory space. fork() returns: 0 to the child process; child's PID to the parent; -1 on error. এই return value difference দিয়ে parent ও child আলাদা code path নেয়।",
      },
      {
        type: "p",
        text: "exec() family replaces the current process's memory with a new program. Typically used after fork() to run a different program. অর্থাৎ fork() করে child তৈরি করলাম, exec() দিয়ে সেই child-কে অন্য program-এ পরিণত করলাম।",
      },
      { type: "h3", title: "fork() vs exec()" },
      {
        type: "list",
        items: [
          "fork() clones the calling process.",
          "exec() loads a new program, discarding the old one.",
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

      { type: "h3", title: "Termination — exit() and zombie/orphan" },
      {
        type: "p",
        text: "A process terminates via exit() system call. Reasons: normal completion (return from main or exit), error or fatal condition, killed by another process (e.g., kill on Unix). যখন কোনো process terminate হয়, OS তার সব resources release করে এবং parent-কে signal পাঠায়।",
      },
      {
        type: "list",
        items: [
          "Zombie process — a child that has terminated but whose parent has not yet called wait(). The PCB is kept (to store exit status).",
          "Orphan process — a child whose parent terminates before the child. On Unix, such children are adopted by the init process (PID 1), which calls wait() on them.",
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
        text: "Operating systems typically organise processes into trees. The root is the first process (e.g., init or systemd on Linux, launchd on macOS). প্রতিটি parent তার child গুলোকে manage করে, আবার child গুলো নিজের child তৈরি করতে পারে।",
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
        text: "Real-life thinking — a company CEO (init) who hires managers (parents), who hire employees (children). If a manager leaves, employees may be reassigned to the CEO (orphan adoption). একইভাবে OS-এ parent মারা গেলে child-কে init-এ reassign করা হয়।",
      },

      { type: "h2", id: "process-vs-thread", title: "Process vs Thread" },
      {
        type: "p",
        text: "A thread is a lightweight unit of execution within a process. A process has at least one thread (the main thread). Multiple threads within the same process share the process's memory and resources. অর্থাৎ thread হলো process-এর ভেতরের ছোট execution unit, যেগুলো memory share করে।",
      },
      { type: "h3", title: "Process vs Thread — Comparison" },
      {
        type: "list",
        items: [
          "Memory space — Process: separate address space per process; Thread: shared address space within a process",
          "Resource overhead — Process: high (PCB, page tables, file descriptors); Thread: low (only stack, registers, program counter)",
          "Creation time — Process: slow (copy memory, set up data structures); Thread: fast (share most resources)",
          "Context switch — Process: expensive (TLB flush, memory remapping); Thread: cheap (same address space, no TLB flush)",
          "Communication — Process: IPC (pipes, sockets, shared memory); Thread: direct via shared variables",
          "Isolation — Process: strong (one process cannot corrupt another); Thread: weak (one thread can crash the whole process)",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Process = an entire house: separate kitchen, bathroom, bedroom — isolated from other houses. Thread = a person living in that house: all people share the kitchen, bathroom, etc. They can talk directly, but one person burning the kitchen affects everyone in the house. একই কারণে browser tabs process হিসেবে চলে — একটা crash হলে আর সব tab বেঁচে থাকে।",
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
        text: "Threads can be implemented at two different levels — user-level (ULT) ও kernel-level (KLT)। ULT kernel-কে জানায় না, KLT kernel সরাসরি manage করে।",
      },
      { type: "h3", title: "User-Level Threads (ULT)" },
      {
        type: "p",
        text: "Managed entirely by a user-space library (e.g., POSIX Pthreads on some implementations). The kernel is unaware of their existence — it sees only a single process. এদের advantage হলো very fast creation ও switching, কারণ kernel mode switch লাগে না।",
      },
      {
        type: "list",
        items: [
          "Advantages: Very fast creation and switching (no kernel mode switch). Portable.",
          "Disadvantages: If one thread blocks on I/O, the entire process blocks (the kernel cannot schedule another thread from the same process). Cannot utilise multiple CPU cores.",
        ],
      },
      { type: "h3", title: "Kernel-Level Threads (KLT)" },
      {
        type: "p",
        text: "Managed directly by the OS kernel. The kernel knows each thread individually. Modern Linux (NPTL) ও Windows threads হলো KLT। এদের advantage হলো true concurrency across cores, কিন্তু thread creation ও switching এ syscall লাগে।",
      },
      {
        type: "list",
        items: [
          "Advantages: True concurrency across cores; one thread blocking does not block others.",
          "Disadvantages: Slower to create and switch (requires system calls). More overhead per thread.",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — ULT is like a personal to-do list that you manage yourself (no manager involvement). If one task is stuck, your whole list is stuck. KLT is like a team managed by a manager — each task is tracked, one stuck task doesn't stop others. আজকের OS সাধারণত KLT ব্যবহার করে কারণ multicore CPU তখন সম্পূর্ণ utilize হয়।",
      },

      { type: "h2", id: "models", title: "Multithreading Models" },
      {
        type: "p",
        text: "The relationship between user-level threads and kernel-level threads is defined by three classic models. এগুলো বলে দেয় কতগুলো ULT কতগুলো KLT-এর সাথে mapped হবে।",
      },
      { type: "h3", title: "1. Many-to-One Model" },
      {
        type: "p",
        text: "Many user threads mapped to a single kernel thread. The kernel sees only one thread per process. Pros: very lightweight. Cons: no parallelism (only one thread runs at a time); blocking I/O stops all. Example: ancient Unix thread libraries (obsolete). আজকে আর ব্যবহার হয় না।",
      },
      { type: "h3", title: "2. One-to-One Model" },
      {
        type: "p",
        text: "Each user thread maps to a distinct kernel thread. Pros: true parallelism (each user thread can run on a different core); blocking I/O does not affect others. Cons: creates kernel overhead per thread; limited by kernel thread limits. Examples: Linux (NPTL), Windows, macOS. আজকের standard model।",
      },
      { type: "h3", title: "3. Many-to-Many Model" },
      {
        type: "p",
        text: "Many user threads multiplexed onto a smaller or equal number of kernel threads. Allows parallelism up to the number of kernel threads. Pros: balances performance and overhead; user threads can be created freely. Cons: complex to implement (scheduler activations needed). Example: original Solaris, older hybrid implementations (now largely replaced by one-to-one due to cheap kernel threads).",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Program vs process — Program is passive on disk; process is active in memory with its own state.",
          "Process states — new → ready → running → waiting → terminated.",
          "PCB — kernel data structure storing all per-process information.",
          "Scheduling queues — job, ready, device queues to manage process flow.",
          "Context switching — saving and restoring PCB to switch CPU between processes.",
          "Process creation — fork() clones, exec() replaces memory image.",
          "Process termination — exit() releases resources; parent wait() for status.",
          "Process hierarchy — tree structure rooted at init/systemd.",
          "Process vs thread — threads share memory within a process; threads are lighter.",
          "User vs kernel threads — ULT: user-managed, fast, no parallelism; KLT: kernel-managed, slower, full concurrency.",
          "Multithreading models — Many-to-one (obsolete), One-to-one (modern), Many-to-many (compromise).",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Process ও thread বোঝার পরে CPU scheduling (পরের চ্যাপ্টার) পড়া সহজ হবে। কারণ scheduler সত্যিকারের process ও thread গুলোর মধ্যেই decide করে কে CPU পাবে।",
      },
    ],
  },

'''

new_text = before + NEW_CH2 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 02 reformatted. File size: {len(new_text)} bytes")
