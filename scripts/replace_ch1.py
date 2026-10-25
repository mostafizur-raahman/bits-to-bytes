#!/usr/bin/env python3
"""
Replace Ch 01 - Introduction topic with detailed content provided by the user.
Includes multi-lang code samples (C++, Go, Python, Java) for system calls demo.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Find the Ch 01 topic block to replace.
# It starts at `// ---- Ch 01 - Introduction ----` and ends just before
# `// ---- Ch 02 - Process Management ----`.
ch1_marker_start = "// ---- Ch 01 - Introduction ----"
ch2_marker_start = "// ---- Ch 02 - Process Management ----"

start_idx = text.find(ch1_marker_start)
assert start_idx != -1, "Ch 01 marker not found"

end_idx = text.find(ch2_marker_start, start_idx)
assert end_idx != -1, "Ch 02 marker not found"

# The block to replace is text[start_idx:end_idx]
# We want to keep the new Ch 01 + the comment line for Ch 02 (just the comment, not Ch 02 itself)
# Actually, end_idx is the start of the Ch 02 comment line, which includes the leading spaces.
# Let's check what's at end_idx
# Lines 668, 669 are:
#   668:      ],
#   669:    },
#   670: (empty?)
#   671:  // ---- Ch 02 - Process Management ----
# So end_idx points to the start of `// ---- Ch 02` (with no leading spaces).
# That means text[start_idx:end_idx] ends with `},\n` (the close of Ch 01 topic).
# We just need to replace text[start_idx:end_idx] with our new Ch 01 content
# (which should end with `},\n`).

before = text[:start_idx]
after = text[end_idx:]

# Important: ALL escape sequences in JS template literals.
# In a JS template literal (backticks), `\\n` is the literal two-char string "\n".
# In Python source, `\\n` in a regular string is also `\n` (one backslash, one n).
# So if we write `\\n` in Python source, it becomes `\\n` (two chars) in the output
# file, which is what we want.
#
# In a Python triple-quoted regular string, backslash escapes are processed.
# So `\\n` -> two chars `\n` (backslash + n). Good.
# And `\\\\n` -> two chars `\\n` (two backslashes + n)? No, that's `\\` + `n`.
# Let me use raw strings to be safe.

NEW_CH1 = r'''// ---- Ch 01 - Introduction ----
  {
    id: "os-introduction",
    subject: "os",
    title: "Ch 01 — Introduction",
    bangla: "পরিচিতি (Introduction)",
    difficulty: "Easy",
    est: "1 hr",
    summary:
      "OS is the most fundamental software on a computer. This chapter covers what an OS is, its three roles (resource manager / virtual machine / interface), computer architecture, OS structures (monolithic / layered / microkernel / hybrid), user vs kernel mode, system calls, OS services, and the booting process.",
    sections: [
      { type: "h2", id: "what", title: "What is an Operating System?" },
      {
        type: "p",
        text: "An operating system (OS, অপারেটিং সিস্টেম) is a software layer that sits between the user (or application programs) and the computer hardware. Its main job is to abstract the messy details of hardware and provide a clean, convenient, and efficient environment for programs to execute. ছাড়া OS হলে প্রতিটি program-কে নিজে নিজে disk driver, network card, keyboard সব handle করতে হতো।",
      },
      {
        type: "p",
        text: "Real-life analogy — think of the OS as a hotel manager. The guests (applications) ask for rooms, food, cleaning, etc. The manager (OS) decides who gets which room, when the kitchen operates, and ensures that guests don't disturb each other. The actual physical rooms, elevators, and kitchen (hardware) are managed by the staff without guests needing to know the plumbing or electrical wiring.",
      },
      { type: "h3", title: "Examples of Operating Systems You Use Daily" },
      {
        type: "list",
        items: [
          "Windows — desktops, laptops",
          "Linux — servers, Android phones, embedded devices",
          "macOS — Apple desktops and laptops",
          "iOS — iPhones, iPads",
          "Android — phones, tablets, smart TVs",
        ],
      },

      { type: "h2", id: "roles", title: "Roles of an Operating System" },
      {
        type: "p",
        text: "An OS plays three major roles. প্রতিটি role একে অপরের পরিপূরক — একটি ছাড়া বাকি দুটি কাজ করতে পারে না।",
      },
      { type: "h3", title: "1. Resource Manager" },
      {
        type: "p",
        text: "Hardware resources (CPU, memory, disk, network) are limited. The OS allocates them fairly and efficiently among competing programs. যেমন যখন ১০টা program একসাথে চায় CPU, OS decide করে কে আগে চলবে, কে অপেক্ষা করবে। এই scheduling decision ছাড়া সব একসাথে চালানো গেলে system crash করবে।",
      },
      { type: "h3", title: "2. Virtual Machine" },
      {
        type: "p",
        text: "The OS creates an abstraction of the hardware that is simpler to program. For instance, you see files and folders instead of raw disk sectors; you see a window with a cursor instead of pixel buffers and interrupts. এর ফলে একজন programmer কে hardware-এর প্রতিটি detail (হার্ডওয়্যার register, interrupt vector) না জেনেও program লেখা যায়।",
      },
      { type: "h3", title: "3. Interface (between user and hardware)" },
      {
        type: "p",
        text: "The OS provides a user interface — command-line (CLI) or graphical (GUI) — through which you can run programs, manage files, and configure settings. আজকের desktop user-রা শুধু mouse দিয়ে click করে কাজ চালায়, কিন্তু সেই click-এর পেছনে আসলে অনেকগুলো system call হচ্ছে।",
      },

      { type: "h2", id: "architecture", title: "Computer System Architecture" },
      {
        type: "p",
        text: "A computer system consists of four main hardware components. They communicate over a system bus. এই চারটি component ছাড়া কোনো computer complete না — এমনকি আপনার smartphone-ও এই একই চার component দিয়ে তৈরি।",
      },
      { type: "h3", title: "1. CPU (Central Processing Unit)" },
      {
        type: "list",
        items: [
          "Executes instructions — arithmetic, logic, control",
          "Contains several cores (each can run a separate program/thread)",
          "Has a small, fast cache memory (L1, L2, L3) to reduce RAM access",
        ],
      },
      { type: "h3", title: "2. Memory (RAM — Random Access Memory)" },
      {
        type: "list",
        items: [
          "Stores data and instructions that the CPU actively uses",
          "Volatile — loses content on power off",
          "Divided into bytes, each with a unique address",
        ],
      },
      { type: "h3", title: "3. I/O Devices" },
      {
        type: "list",
        items: [
          "Input — keyboard, mouse, microphone, scanner",
          "Output — monitor, printer, speakers",
          "Storage — hard disk, SSD, USB drive (also treated as I/O)",
          "Network — Ethernet, Wi-Fi (specialised I/O)",
        ],
      },
      { type: "h3", title: "4. System Bus" },
      {
        type: "p",
        text: "The communication highway that connects CPU, memory, and I/O controllers. Includes address bus, data bus, and control bus. Real-life analogy: A restaurant kitchen (CPU) prepares dishes using ingredients from a refrigerator (memory). Waiters (I/O) bring orders from customers and take finished food out. The kitchen pass (bus) is where orders and dishes are handed.",
      },

      { type: "h2", id: "structures", title: "OS Structure: Monolithic / Layered / Microkernel / Hybrid" },
      {
        type: "p",
        text: "Operating systems are built in different architectural styles, each with trade-offs between performance, security, and maintainability. কোনোটা fast কিন্তু fragile, কোনোটা stable কিন্তু slow। Modern OS গুলো hybrid approach নেয় — দুটির মধ্যে balance।",
      },
      { type: "h3", title: "Monolithic Kernel" },
      {
        type: "p",
        text: "All OS services run in a single kernel address space (kernel mode). This is fast because there is little overhead for communication, but a bug in any part can crash the whole system. Examples: Linux, older UNIX, MS-DOS. Real-life: A small shop where the owner does everything — cooks, cleans, handles money. Efficient but exhausting; one mistake spoils everything.",
      },
      { type: "h3", title: "Layered Kernel" },
      {
        type: "p",
        text: "The OS is divided into layers, each built on top of the layer below. Lower layers provide services to upper layers. This improves modularity but can be slow due to layer-crossing overhead. Example: THE system (Dijkstra, 1968) — first layered OS design.",
      },
      { type: "h3", title: "Microkernel" },
      {
        type: "p",
        text: "Only essential services (IPC, memory management, basic scheduling) run in kernel mode. Drivers, file systems, and networking run as user-mode processes. This is more secure and stable, but slower due to context switches. Examples: QNX, L4, MINIX (the inspiration for Linux's early design). Real-life: A large organisation where each department (security, catering, IT) is independent. If catering fails, the company still runs.",
      },
      { type: "h3", title: "Hybrid Kernel" },
      {
        type: "p",
        text: "A compromise — most services live in kernel for speed, but some run in user space. Combines the performance of monolithic kernels with some modularity of microkernels. Examples: Windows NT (and later Windows versions), macOS XNU.",
      },

      { type: "h2", id: "user-kernel", title: "User Mode vs Kernel Mode" },
      {
        type: "p",
        text: "CPUs have at least two privilege levels to protect the OS from buggy or malicious programs. এই বিভাজন না থাকলে যেকোনো user program পুরো system নষ্ট করতে পারত।",
      },
      { type: "h3", title: "Kernel Mode (Supervisor Mode, Ring 0)" },
      {
        type: "list",
        items: [
          "Can execute privileged instructions (e.g., halt CPU, change memory mapping, access I/O devices directly)",
          "Has access to the entire physical memory",
          "The OS kernel runs here",
        ],
      },
      { type: "h3", title: "User Mode (Ring 3 on x86)" },
      {
        type: "list",
        items: [
          "Cannot execute privileged instructions",
          "Access to memory is restricted to the process's own address space",
          "Applications run here",
        ],
      },
      {
        type: "p",
        text: "How does the CPU know which mode it's in? A mode bit in the CPU status register indicates kernel (0) or user (1). Switching from user mode to kernel mode happens via: (1) System call (e.g., read a file) — the program executes a special instruction (syscall, int 0x80). (2) Interrupt (e.g., timer, keyboard press). (3) Exception (e.g., division by zero, page fault). When a switch happens, the CPU saves the current state and jumps to a predefined kernel handler. After handling, it returns to user mode.",
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Real-life analogy — User mode: allowed to walk in the shopping mall (public areas). You can't enter the cash vault or the electrical room. Kernel mode: security staff can go anywhere, open any door, and shut down the ventilation. System call: you ask a security guard to open a locked door for you.",
      },

      { type: "h2", id: "syscall", title: "System Calls & API — Practical Demo" },
      {
        type: "p",
        text: "A system call is a request from a user program to the OS for a privileged service (open a file, create a process, allocate memory). System calls are the only way a user program can access kernel functionality. নিচে চারটি ভাষায় একটি simple program দেখানো হলো যেটি নিজের PID (process ID) ও parent PID দেখায় — প্রতিটি ভাষা ভেতরে ভেতরে getpid / getppid syscall করে।",
      },
      {
        type: "multi-code",
        filename: "getpid_syscall",
        codeSamples: {
          cpp: `#include <iostream>
#include <unistd.h>   // POSIX: getpid / getppid

int main() {
    // getpid() is a libc wrapper that invokes the kernel syscall
    std::cout << "PID:  " << getpid()  << '\\n';
    std::cout << "PPID: " << getppid() << '\\n';
    return 0;
}
// Compile: g++ getpid.cpp -o getpid
// Run:     ./getpid
// Trace:   strace ./getpid   (see actual syscalls)`,
          go: `package main

import (
    "fmt"
    "os"
)

func main() {
    // Go's os.Getpid() calls libc getpid(), which traps into the kernel
    fmt.Println("PID: ", os.Getpid())
    fmt.Println("PPID:", os.Getppid())
}
// Run: go run getpid.go
// Trace: strace -f go run getpid.go`,
          python: `import os

# os.getpid() — calls libc getpid(), which makes a syscall
print("PID: ", os.getpid())
print("PPID:", os.getppid())
# Run:    python getpid.py
# Trace:  strace python getpid.py 2>&1 | grep getpid`,
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
// Compile: javac GetPid.java
// Run:     java GetPid`,
        },
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Linux-এ strace ./your_program দিয়ে দেখুন কোন syscalls হচ্ছে। প্রায় সব high-level operation (file পড়া, network call, even printf) এক বা একাধিক syscall-এ পরিণত হয়। এটি OS বোঝার সবচেয়ে concrete উপায়।",
      },

      { type: "h2", id: "services", title: "OS Services & Utilities" },
      {
        type: "p",
        text: "Operating systems provide a set of core services that make life easier for users and programmers. প্রতিটি service-এর নির্দিষ্ট কাজ আছে, এবং সবগুলো একসাথে মিলে একটি smooth user experience তৈরি করে।",
      },
      {
        type: "list",
        items: [
          "Program execution — load a program into memory and run it (e.g., double-click an .exe or run ./a.out)",
          "I/O operations — read/write files, devices (printf, scanf, disk access)",
          "File system manipulation — create, delete, rename files/directories (mkdir, rm, file explorer)",
          "Communication — data exchange between processes (pipes, sockets, shared memory)",
          "Error detection — handle hardware errors, memory faults, division by zero (segfault handler)",
          "Resource allocation — assign CPU time, memory, devices (scheduler, memory manager)",
          "Accounting — keep track of resource usage per user (top, ps, system logs)",
          "Protection — prevent unauthorised access (file permissions, memory protection)",
        ],
      },
      {
        type: "p",
        text: "Utilities are user-level programs that come with the OS (e.g., ls, cp, grep, Task Manager). They use system calls to perform their work. Real-life: A hotel provides services — luggage storage (resource allocation), wake-up calls (communication), laundry (I/O). Utilities are like the concierge desk — they rely on the hotel's internal systems.",
      },

      { type: "h2", id: "booting", title: "Booting Process" },
      {
        type: "p",
        text: "Booting (short for 'bootstrap') is the sequence of operations that loads the operating system into memory and starts it when you turn on the computer. এটি একটি deterministic sequence — প্রতিবার কম্পিউটার চালু করলে একই ধাপ অনুসরণ করা হয়।",
      },
      { type: "h3", title: "Step-by-Step Boot Flow" },
      {
        type: "list",
        items: [
          "1. Power-on — CPU starts in real mode (limited memory access) and jumps to a fixed memory address where the BIOS firmware resides",
          "2. BIOS or UEFI — Basic Input/Output System (older) or Unified Extensible Firmware Interface (modern) initialises hardware: clocks, memory controller, disk detection",
          "3. POST (Power-On Self Test) — checks critical hardware (CPU, RAM, disk controllers). Fatal error → beep codes or message",
          "4. Bootloader loading — BIOS/UEFI reads the first sector (MBR or EFI System Partition) and loads bootloader (GRUB, Windows Boot Manager)",
          "5. Kernel loading — bootloader reads the OS kernel (vmlinuz on Linux) into memory, possibly with an initrd containing initial drivers",
          "6. Kernel initialisation — switches to protected/long mode, sets up memory management, interrupt handlers, device drivers, mounts root file system",
          "7. Init process — kernel starts the first user-mode process (traditionally /sbin/init, now systemd on Linux or launchd on macOS)",
          "8. Login — system presents a login prompt (text or graphical); after login, you get a shell or desktop environment",
        ],
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: আজকের fast-boot কম্পিউটারে এই পুরো sequence 5-15 সেকেন্ডে শেষ হয়। SSD ও UEFI-র কারণে আগের চেয়ে অনেক দ্রুত। তবে এখনও এই ৮টি ধাপ একইভাবে হয়।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "OS definition — software that manages hardware, provides virtual machine, gives interface",
          "Roles — resource manager, virtual machine, interface",
          "Computer architecture — CPU, RAM, I/O devices connected via bus",
          "OS structures — Monolithic (fast, fragile), Microkernel (stable, slower), Hybrid (balanced)",
          "User vs kernel mode — privilege separation; system calls switch modes",
          "System call — request for kernel service; API abstracts it",
          "OS services — program execution, I/O, file system, communication, accounting, protection",
          "Booting — Power-on → BIOS/UEFI → bootloader → kernel → init → login",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: এই fundamentals গুলো ভালোভাবে বোঝার পরেই পরের চ্যাপ্টার (Process Management, Scheduling, Memory Management) পড়তে হবে। প্রতিটি advanced topic এই basics-এর উপর দাঁড়িয়ে আছে।",
      },
    ],
  },

'''

new_text = before + NEW_CH1 + after

# Sanity check
assert new_text.count('id: "os-') == 13, f"Expected 13 OS topics, got {new_text.count('id: \"os-')}"
assert 'export const PROJECTS' in new_text, "PROJECTS export missing"
assert 'export const CHEATSHEETS' in new_text, "CHEATSHEETS export missing"

CONTENT_FILE.write_text(new_text)
print(f"OK — replaced Ch 01 with detailed content. File size: {len(new_text)} bytes")
