#!/usr/bin/env python3
"""
Reformat Ch 01 (Introduction) with the correct content format:
- English sentence (user-provided, kept intact)
- + ONE brief Bangla sentence (with English technical terms allowed) — not pure Bangla
- + Real-life human-thinking example
- + Code samples in C++, Go, Python, Java

Pattern (from user):
"English sentence. প্রতিটি service-এর নির্দিষ্ট কাজ আছে, এবং সবগুলো একসাথে মিলে একটি smooth user experience তৈরি করে।"
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch1_marker_start = "// ---- Ch 01 - Introduction ----"
ch2_marker_start = "// ---- Ch 02 - Process Management ----"

start_idx = text.find(ch1_marker_start)
assert start_idx != -1, "Ch 01 marker not found"
end_idx = text.find(ch2_marker_start, start_idx)
assert end_idx != -1, "Ch 02 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH1 = r'''// ---- Ch 01 - Introduction ----
  {
    id: "os-introduction",
    subject: "os",
    title: "Ch 01 — Introduction",
    bangla: "পরিচিতি (Introduction)",
    difficulty: "Easy",
    est: "1 hr",
    summary:
      "An operating system is the most fundamental software that runs on a computer. It manages hardware resources and provides a foundation for application programs. This chapter covers the core concepts, architecture, and services of modern operating systems.",
    sections: [
      { type: "h2", id: "what", title: "What is an Operating System?" },
      {
        type: "p",
        text: "An operating system (OS) is the most fundamental software that runs on a computer. It manages hardware resources and provides a foundation for application programs. OS হলো hardware আর application-এর মাঝে একটি abstraction layer, যেটি hardware-এর complexity লুকিয়ে একটি clean interface দেয়।",
      },
      {
        type: "p",
        text: "An operating system is a software layer that sits between the user (or application programs) and the computer hardware. Its main job is to abstract the messy details of hardware and provide a clean, convenient, and efficient environment for programs to execute. ছাড়া OS হলে প্রতিটি program-কে নিজে নিজে disk driver, network card, keyboard সব handle করতে হতো।",
      },

      { type: "h3", title: "Real-life human-thinking example" },
      {
        type: "p",
        text: "Think of the OS as a hotel manager. The guests (applications) ask for rooms, food, cleaning, etc. The manager (OS) decides who gets which room, when the kitchen operates, and ensures that guests don't disturb each other. The actual physical rooms, elevators, and kitchen (hardware) are managed by the staff — without guests needing to know the plumbing or electrical wiring. একইভাবে browser খুললে আপনি ভাবেন না কীভাবে keypress CPU পর্যন্ত পৌঁছায় — OS সেটা manage করে।",
      },

      { type: "h3", title: "Examples of operating systems you encounter daily" },
      {
        type: "list",
        items: [
          "Windows (desktops, laptops)",
          "Linux (servers, Android phones, embedded devices)",
          "macOS (Apple desktops/laptops)",
          "iOS (iPhones, iPads)",
          "Android (phones, tablets, smart TVs)",
        ],
      },

      { type: "h2", id: "roles", title: "Roles of an Operating System" },
      {
        type: "p",
        text: "An OS plays three major roles — resource manager, virtual machine, and interface. প্রতিটি role একে অপরের পরিপূরক, একটি ছাড়া বাকি দুটি কাজ করতে পারে না।",
      },

      { type: "h3", title: "1. Resource Manager" },
      {
        type: "p",
        text: "Hardware resources (CPU, memory, disk, network) are limited. The OS allocates them fairly and efficiently among competing programs. যেমন যখন ১০টা program একসাথে CPU চায়, OS decide করে কে আগে চলবে, কে অপেক্ষা করবে।",
      },
      {
        type: "p",
        text: "Real-life thinking — imagine a busy restaurant kitchen. One stove (CPU), one refrigerator (memory), many orders (programs). The head chef (OS) decides which order gets the stove next, so no single order blocks everyone. সব একসাথে চাইলে kitchen-এ chaos হবে।",
      },

      { type: "h3", title: "2. Virtual Machine" },
      {
        type: "p",
        text: "The OS creates an abstraction of the hardware that is simpler to program. For instance, you see files and folders instead of raw disk sectors; you see a window with a cursor instead of pixel buffers and interrupts. এর ফলে programmer-কে hardware-এর প্রতিটি detail না জেনেও program লেখা যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — when you order food on a delivery app, you don't need to know how the kitchen cooks it or which rider delivers. The app is the abstraction; the kitchen + rider is the hardware. OS program-কে ঠিক একইভাবে abstraction দেয়।",
      },

      { type: "h3", title: "3. Interface (between user and hardware)" },
      {
        type: "p",
        text: "The OS provides a user interface – command-line (CLI) or graphical (GUI) – through which you can run programs, manage files, and configure settings. আজকের desktop user-রা শুধু mouse দিয়ে click করে কাজ চালায়, কিন্তু সেই click-এর পেছনে অনেকগুলো system call হচ্ছে।",
      },
      {
        type: "p",
        text: "Real-life thinking — when you tap a light switch, you don't think about electrical wiring, voltage, or the bulb filament. The switch is the interface; the wiring is hidden. OS GUI/CLI হলো switch, kernel হলো wiring।",
      },

      { type: "h2", id: "architecture", title: "Computer System Architecture" },
      {
        type: "p",
        text: "A computer system consists of four main hardware components. They communicate over a system bus. এই চারটি component ছাড়া কোনো computer complete না, এমনকি আপনার smartphone-ও।",
      },

      { type: "h3", title: "1. CPU (Central Processing Unit)" },
      {
        type: "list",
        items: [
          "Executes instructions (arithmetic, logic, control)",
          "Contains several cores (each can run a separate program/thread)",
          "Has a small, fast cache memory (L1, L2, L3)",
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
          "Input: keyboard, mouse, microphone, scanner",
          "Output: monitor, printer, speakers",
          "Storage: hard disk, SSD, USB drive (also treated as I/O)",
          "Network: Ethernet, Wi-Fi (specialised I/O)",
        ],
      },

      { type: "h3", title: "4. System Bus" },
      {
        type: "p",
        text: "The communication highway that connects CPU, memory, and I/O controllers. Includes address bus, data bus, and control bus. এটি হলো hardware component গুলোর মধ্যে যোগাযোগের পথ।",
      },
      {
        type: "p",
        text: "Real-life thinking — a restaurant kitchen (CPU) prepares dishes using ingredients from a refrigerator (memory). Waiters (I/O) bring orders from customers and take finished food out. The kitchen pass (bus) is where orders and dishes are handed. Bus না থাকলে components একে অপরের সাথে কথা বলতে পারবে না।",
      },

      { type: "h2", id: "structures", title: "OS Structure: Monolithic, Layered, Microkernel, Hybrid" },
      {
        type: "p",
        text: "Operating systems are built in different architectural styles, each with trade-offs between performance, security, and maintainability. কোনোটা fast কিন্তু fragile, কোনোটা stable কিন্তু slow — modern OS গুলো hybrid approach নেয়।",
      },

      { type: "h3", title: "Monolithic Kernel" },
      {
        type: "p",
        text: "All OS services run in a single kernel address space (kernel mode). This is fast because there is little overhead for communication, but a bug in any part can crash the whole system. একটি bug পুরো system কে crash করতে পারে। Examples: Linux, older UNIX, MS-DOS.",
      },
      {
        type: "p",
        text: "Real-life thinking — a small shop where the owner does everything: cooks, cleans, handles money. Efficient but exhausting; one mistake spoils everything. Linux monolithic kernel ও একইভাবে fast, কিন্তু bug হলে পুরো system একসাথে crash।",
      },

      { type: "h3", title: "Layered Kernel" },
      {
        type: "p",
        text: "The OS is divided into layers, each built on top of the layer below. Lower layers provide services to upper layers. This improves modularity but can be slow due to layer-crossing overhead. এক layer থেকে আরেক layer-এ যেতে সময় লাগে। Example: THE system (Dijkstra, 1968).",
      },

      { type: "h3", title: "Microkernel" },
      {
        type: "p",
        text: "Only essential services (IPC, memory management, basic scheduling) run in kernel mode. Drivers, file systems, and networking run as user-mode processes. This is more secure and stable, but slower due to context switches. এক component crash হলে পুরো system crash করে না। Examples: QNX, L4, MINIX.",
      },
      {
        type: "p",
        text: "Real-life thinking — a large organisation where each department (security, catering, IT) is independent. If catering fails, the company still runs. Microkernel-এ driver crash হলে শুধু সেই service মারা যায়, kernel বেঁচে থাকে।",
      },

      { type: "h3", title: "Hybrid Kernel" },
      {
        type: "p",
        text: "A compromise – most services live in kernel for speed, but some run in user space. Combines the performance of monolithic kernels with some modularity of microkernels. Windows NT ও macOS XNU এই approach নেয়।",
      },

      { type: "h2", id: "user-kernel", title: "User Mode vs Kernel Mode" },
      {
        type: "p",
        text: "CPUs have at least two privilege levels to protect the OS from buggy or malicious programs. এই privilege separation না থাকলে যেকোনো user program পুরো system নষ্ট করতে পারত।",
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
        text: "How does the CPU know which mode it's in? A mode bit in the CPU status register indicates kernel (0) or user (1). Switching from user mode to kernel mode happens via three triggers: (1) System call (e.g., read a file) — the program executes a special instruction (syscall, int 0x80). (2) Interrupt (e.g., timer, keyboard press). (3) Exception (e.g., division by zero, page fault). When a switch happens, the CPU saves the current state and jumps to a predefined kernel handler. After handling, it returns to user mode.",
      },

      {
        type: "p",
        text: "Real-life thinking — user mode is being allowed to walk in a shopping mall (public areas). You can't enter the cash vault or the electrical room. Kernel mode is the security staff who can go anywhere, open any door, shut down the ventilation. System call হলো যখন আপনি security guard-কে বলেন একটি locked door খুলতে — আপনি নিজে খুলতে পারেন না, কিন্তু guard পারে।",
      },

      { type: "h2", id: "syscall", title: "System Calls and API" },
      {
        type: "p",
        text: "A system call is a request from a user program to the OS for a privileged service (e.g., open a file, create a process, allocate memory). System calls are the only way a user program can access kernel functionality. Common Linux/UNIX system calls — Process control: fork(), exec(), wait(), exit(). File management: open(), read(), write(), close(). Information maintenance: getpid(), time(). Communication: socket(), send(), recv().",
      },
      {
        type: "p",
        text: "API (Application Programming Interface) is a set of functions provided by a library (like the C standard library) that often wraps system calls. An API may call one or more system calls, or do work without any system call. যেমন printf() ভেতরে write() syscall করে, কিন্তু formatting নিজেই handle করে। সুবিধা হলো একই API different OS-এ কাজ করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — you (application) want to withdraw money from a bank. You fill a withdrawal slip (API call). The teller (system call handler) checks your balance (kernel), goes to the vault (hardware), and gives you cash. You never enter the vault yourself. অর্থাৎ user program কখনো directly hardware access করে না — সব সময় syscall এর মাধ্যমে।",
      },

      { type: "h3", title: "Practical demo — getpid syscall" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় একটি simple program দেখানো হলো যেটি নিজের PID (process ID) ও parent PID দেখায় — প্রতিটি ভাষা ভেতরে ভেতরে getpid / getppid syscall করে।",
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
        text: "Tip: Linux-এ strace ./your_program দিয়ে দেখুন কোন syscalls হচ্ছে। প্রায় সব high-level operation (file পড়া, network call, even printf) এক বা একাধিক syscall-এ পরিণত হয়।",
      },

      { type: "h2", id: "services", title: "OS Services and Utilities" },
      {
        type: "p",
        text: "Operating systems provide a set of core services that make life easier for users and programmers. প্রতিটি service-এর নির্দিষ্ট কাজ আছে, এবং সবগুলো একসাথে মিলে একটি smooth user experience তৈরি করে।",
      },
      {
        type: "list",
        items: [
          "Program execution — load a program into memory and run it (double-click an .exe or run ./a.out)",
          "I/O operations — read/write files, devices (printf, scanf, disk access)",
          "File system manipulation — create, delete, rename files/directories (mkdir, rm, file explorer)",
          "Communication — data exchange between processes (pipes, sockets, shared memory)",
          "Error detection — handle hardware errors, memory faults, division by zero (segmentation fault handler)",
          "Resource allocation — assign CPU time, memory, devices (scheduler, memory manager)",
          "Accounting — keep track of resource usage per user (top, ps, system logs)",
          "Protection — prevent unauthorised access (file permissions, memory protection)",
        ],
      },
      {
        type: "p",
        text: "Utilities are user-level programs that come with the OS (e.g., ls, cp, grep, Task Manager). They use system calls to perform their work. Real-life thinking — a hotel provides services: luggage storage (resource allocation), wake-up calls (communication), laundry (I/O). Utilities are like the concierge desk — they rely on the hotel's internal systems. অর্থাৎ utility program গুলো নিজে নিজে OS service করে না, বরং syscall এর মাধ্যমে OS-কে কাজ করতে বলে।",
      },

      { type: "h2", id: "booting", title: "Booting Process" },
      {
        type: "p",
        text: "Booting (short for 'bootstrap') is the sequence of operations that loads the operating system into memory and starts it when you turn on the computer. এটি একটি deterministic sequence — প্রতিবার কম্পিউটার চালু করলে একই ধাপ অনুসরণ করা হয়।",
      },
      { type: "h3", title: "Step-by-step boot flow" },
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
        type: "p",
        text: "Real-life thinking — opening a restaurant in the morning. First you turn on the main power (power-on). Then the manager checks the kitchen equipment works (POST). The chef arrives and starts preparing the menu (kernel init). The first waiter clocks in (init process). Finally, the door opens and customers come in (login). আজকের fast-boot কম্পিউটারে পুরো sequence টা 5-15 সেকেন্ডে শেষ হয়।",
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: SSD ও UEFI-র কারণে আজকের boot আগের চেয়ে অনেক দ্রুত। তবে এখনও এই ৮টি ধাপ একইভাবে হয়।",
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

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 01 reformatted with brief Bangla gloss pattern. File size: {len(new_text)} bytes")
