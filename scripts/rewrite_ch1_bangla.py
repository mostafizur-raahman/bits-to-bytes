#!/usr/bin/env python3
"""
Rewrite Ch 01 (Introduction) with MAXIMUM BANGLA + English technical terms.

Old pattern (incorrect):
  "English sentence. English sentence. English sentence. ছোট Bangla gloss."
  → User saw mostly English

New pattern (correct):
  "Bangla বাক্য যেখানে technical terms English-এ থাকে।"
  Examples:
  - "Operating system (OS) হলো এমন একটি fundamental software যেটি computer-এ সবসময় চলে।"
  - "OS hardware resources manage করে এবং application programs-এর জন্য foundation তৈরি করে।"

Rules:
- Maximum Bangla (Hindi/Bangla script)
- All technical terms stay English (OS, kernel, process, hardware, CPU, RAM, etc.)
- Real-life analogies in Bangla + English technical terms
- Code samples unchanged
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
      "Operating system (OS) হলো সবচেয়ে fundamental software যেটি একটি computer-এ চলে। এটি hardware resources manage করে এবং application programs-এর জন্য foundation তৈরি করে। এই chapter-এ modern operating systems-এর core concepts, architecture, ও services নিয়ে আলোচনা করা হয়েছে।",
    sections: [
      { type: "h2", id: "what", title: "What is an Operating System?" },
      {
        type: "p",
        text: "Operating system (OS) হলো এমন একটি software layer যেটি user (বা application programs) আর computer hardware-এর মাঝে বসে। এর main job হলো hardware-এর messy details abstract করা এবং programs-এর execution-এর জন্য একটি clean, convenient, efficient environment দেওয়া। ছাড়া OS হলে প্রতিটি program-কে নিজে নিজে disk driver, network card, keyboard সব handle করতে হতো।",
      },
      {
        type: "p",
        text: "Operating system (OS) হলো এমন একটি software যেটি computer-এ সবচেয়ে fundamental ভাবে চলে। এটি hardware resources manage করে এবং application programs-এর জন্য foundation তৈরি করে। এই chapter-এ core concepts, architecture, ও services নিয়ে আলোচনা করা হয়েছে, real-life examples সহ যাতে আইডিয়াগুলো concrete হয়।",
      },

      { type: "h3", title: "Real-life human-thinking example" },
      {
        type: "p",
        text: "OS কে ভাবতে পারেন একজন hotel manager হিসেবে। Guests (applications) room, food, cleaning ইত্যাদি চায়। Manager (OS) decide করে কে কোন room পাবে, kitchen কখন চলবে, এবং নিশ্চিত করে যে guests একে অপরকে disturb করবে না। Actual physical rooms, elevators, kitchen (hardware) সব staff manage করে — guests-এর plumbing বা electrical wiring সম্পর্কে কিছু জানার দরকার নেই। একইভাবে browser খুললে আপনি ভাবেন না keypress কীভাবে CPU পর্যন্ত পৌঁছায় — OS সেটা manage করে।",
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
        text: "একটি OS তিনটি major role পালন করে — resource manager, virtual machine, ও interface। প্রতিটি role একে অপরের পরিপূরক — একটি ছাড়া বাকি দুটি কাজ করতে পারে না।",
      },

      { type: "h3", title: "1. Resource Manager" },
      {
        type: "p",
        text: "Hardware resources (CPU, memory, disk, network) limited। OS সেগুলো competing programs-এর মধ্যে fair ও efficient ভাবে allocate করে। যেমন যখন ১০টা program একসাথে CPU চায়, OS decide করে কে আগে চলবে, কে অপেক্ষা করবে। এই scheduling decision ছাড়া সব একসাথে চালানো গেলে system crash করবে।",
      },
      {
        type: "p",
        text: "Real-life thinking — ভাবুন একটা busy restaurant kitchen। একটা stove (CPU), একটা refrigerator (memory), আর অনেক orders (programs)। Head chef (OS) decide করে কোন order আগে stove পাবে, যাতে কোনো single order সবাইকে block না করে। সব একসাথে cook করতে চাইলে kitchen-এ chaos হবে।",
      },

      { type: "h3", title: "2. Virtual Machine" },
      {
        type: "p",
        text: "OS hardware-এর একটি abstraction তৈরি করে যেটি program করা সহজ। যেমন, আপনি raw disk sectors এর বদলে files ও folders দেখেন; pixel buffers ও interrupts এর বদলে cursor সহ window দেখেন। এর ফলে একজন programmer-কে hardware-এর প্রতিটি detail (hardware register, interrupt vector) না জেনেও program লেখা যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — food-delivery app-এ order করলে আপনাকে জানতে হয় না kitchen কীভাবে cook করে বা কোন rider deliver করবে। App হলো abstraction; kitchen + rider হলো hardware। OS program-কে ঠিক একইভাবে abstraction দেয়।",
      },

      { type: "h3", title: "3. Interface (between user and hardware)" },
      {
        type: "p",
        text: "OS একটি user interface দেয় — command-line (CLI) বা graphical (GUI) — যার মাধ্যমে আপনি programs run করতে পারেন, files manage করতে পারেন, settings configure করতে পারেন। আজকের desktop user-রা শুধু mouse দিয়ে click করে কাজ চালায়, কিন্তু সেই click-এর পেছনে আসলে অনেকগুলো system call হচ্ছে।",
      },
      {
        type: "p",
        text: "Real-life thinking — light switch tap করলে আপনি ভাবেন না electrical wiring, voltage, বা bulb filament সম্পর্কে। Switch হলো interface; wiring hidden। OS-এর GUI/CLI হলো switch, kernel হলো wiring।",
      },

      { type: "h2", id: "architecture", title: "Computer System Architecture" },
      {
        type: "p",
        text: "একটি computer system চারটি main hardware component নিয়ে গঠিত। এগুলো system bus-এর মাধ্যমে communicate করে। এই চারটি component ছাড়া কোনো computer complete না — এমনকি আপনার smartphone-ও এই একই চার component দিয়ে তৈরি।",
      },

      { type: "h3", title: "1. CPU (Central Processing Unit)" },
      {
        type: "list",
        items: [
          "Instructions execute করে (arithmetic, logic, control)",
          "কয়েকটি cores থাকে (প্রতিটি core একটি আলাদা program/thread run করতে পারে)",
          "ছোট, fast cache memory (L1, L2, L3) থাকে",
        ],
      },

      { type: "h3", title: "2. Memory (RAM — Random Access Memory)" },
      {
        type: "list",
        items: [
          "CPU যে data ও instructions actively use করে সেগুলো store করে",
          "Volatile — power off হলে content হারিয়ে যায়",
          "Bytes-এ ভাগ করা, প্রতিটির unique address থাকে",
        ],
      },

      { type: "h3", title: "3. I/O Devices" },
      {
        type: "list",
        items: [
          "Input: keyboard, mouse, microphone, scanner",
          "Output: monitor, printer, speakers",
          "Storage: hard disk, SSD, USB drive (এগুলোও I/O হিসেবে treat হয়)",
          "Network: Ethernet, Wi-Fi (specialised I/O)",
        ],
      },

      { type: "h3", title: "4. System Bus" },
      {
        type: "p",
        text: "System bus হলো communication highway যেটি CPU, memory, ও I/O controllers-কে connect করে। এতে address bus, data bus, ও control bus থাকে। এটি হলো hardware components-এর মধ্যে যোগাযোগের পথ।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটা restaurant kitchen (CPU) refrigerator (memory) থেকে ingredients নিয়ে dishes prepare করে। Waiters (I/O) customers থেকে orders আনে আর finished food নিয়ে যায়। Kitchen pass (bus) হলো যেখানে orders ও dishes hand করা হয়। Bus না থাকলে components একে অপরের সাথে communicate করতে পারবে না।",
      },

      { type: "h2", id: "structures", title: "OS Structure: Monolithic, Layered, Microkernel, Hybrid" },
      {
        type: "p",
        text: "Operating systems বিভিন্ন architectural style-এ build করা হয়, প্রতিটির performance, security, ও maintainability-এর মধ্যে trade-off আছে। কোনোটা fast কিন্তু fragile, কোনোটা stable কিন্তু slow — modern OS গুলো hybrid approach নেয়।",
      },

      { type: "h3", title: "Monolithic Kernel" },
      {
        type: "p",
        text: "সব OS services একটি single kernel address space (kernel mode)-এ চলে। এটি fast কারণ communication-এ খুব কম overhead আছে, কিন্তু যেকোনো part-এ bug থাকলে পুরো system crash করতে পারে। একটি bug পুরো system কে crash করতে পারে। Examples: Linux, older UNIX, MS-DOS।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটা ছোট shop যেখানে owner সব করে: cook, clean, money handle। Efficient কিন্তু exhausting; একটা mistake সব নষ্ট করে দেয়। Linux monolithic kernel ও একইভাবে fast, কিন্তু bug হলে পুরো system একসাথে crash করে।",
      },

      { type: "h3", title: "Layered Kernel" },
      {
        type: "p",
        text: "OS কে layers-এ ভাগ করা হয়, প্রতিটি layer তার নিচের layer-এর উপর built। Lower layers upper layers-কে services দেয়। এটি modularity বাড়ায় কিন্তু layer-crossing overhead-এর কারণে slow হতে পারে। এক layer থেকে আরেক layer-এ যেতে সময় লাগে। Example: THE system (Dijkstra, 1968) — first layered OS design।",
      },

      { type: "h3", title: "Microkernel" },
      {
        type: "p",
        text: "শুধু essential services (IPC, memory management, basic scheduling) kernel mode-এ চলে। Drivers, file systems, ও networking user-mode processes হিসেবে চলে। এটি বেশি secure ও stable, কিন্তু context switches-এর কারণে slower। এক component crash হলে পুরো system crash করে না। Examples: QNX, L4, MINIX।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি large organisation যেখানে প্রতিটি department (security, catering, IT) independent। Catering fail করলেও company এখনও চলে। Microkernel-এ driver crash হলে শুধু সেই service মারা যায়, kernel বেঁচে থাকে।",
      },

      { type: "h3", title: "Hybrid Kernel" },
      {
        type: "p",
        text: "একটি compromise — বেশির ভাগ services kernel-এ speed-এর জন্য থাকে, কিন্তু কিছু user space-এ চলে। Monolithic kernels-এর performance ও microkernels-এর modularity একসাথে combine করে। Windows NT ও macOS XNU এই approach নেয়।",
      },

      { type: "h2", id: "user-kernel", title: "User Mode vs Kernel Mode" },
      {
        type: "p",
        text: "CPUs-এ কমপক্ষে দুটি privilege level থাকে যাতে OS কে buggy বা malicious programs থেকে protect করা যায়। এই privilege separation না থাকলে যেকোনো user program পুরো system নষ্ট করতে পারত।",
      },

      { type: "h3", title: "Kernel Mode (Supervisor Mode, Ring 0)" },
      {
        type: "list",
        items: [
          "Privileged instructions execute করতে পারে (যেমন halt CPU, change memory mapping, access I/O devices directly)",
          "Entire physical memory access করতে পারে",
          "OS kernel এখানে চলে",
        ],
      },

      { type: "h3", title: "User Mode (Ring 3 on x86)" },
      {
        type: "list",
        items: [
          "Privileged instructions execute করতে পারে না",
          "Memory access process-এর নিজস্ব address space-এ restricted",
          "Applications এখানে চলে",
        ],
      },

      {
        type: "p",
        text: "CPU কীভাবে জানে কোন mode-এ আছে? CPU status register-এ একটি mode bit থাকে যেটি kernel (0) বা user (1) indicate করে। User mode থেকে kernel mode-এ switch হওয়ার তিনটি trigger: (1) System call (যেমন read a file) — program একটি special instruction (syscall, int 0x80) execute করে। (2) Interrupt (যেমন timer, keyboard press)। (3) Exception (যেমন division by zero, page fault)। Switch হলে CPU current state save করে এবং একটি predefined kernel handler-এ jump করে। Handle করার পর আবার user mode-এ ফিরে যায়।",
      },

      {
        type: "p",
        text: "Real-life thinking — user mode হলো shopping mall-এ হাঁটার permission (public areas)। আপনি cash vault বা electrical room-এ ঢুকতে পারবেন না। Kernel mode হলো security staff যারা যেকোনো জায়গায় যেতে পারে, যেকোনো door খুলতে পারে, ventilation shut করতে পারে। System call হলো যখন আপনি security guard-কে বলেন একটি locked door খুলতে — আপনি নিজে খুলতে পারেন না, কিন্তু guard পারে।",
      },

      { type: "h2", id: "syscall", title: "System Calls and API" },
      {
        type: "p",
        text: "System call হলো user program থেকে OS-এ একটি privileged service-এর জন্য request (যেমন open a file, create a process, allocate memory)। System calls হলো একমাত্র উপায় যেখানে একটি user program kernel functionality access করতে পারে। Common Linux/UNIX system calls — Process control: fork(), exec(), wait(), exit()। File management: open(), read(), write(), close()। Information maintenance: getpid(), time()। Communication: socket(), send(), recv()।",
      },
      {
        type: "p",
        text: "API (Application Programming Interface) হলো একটি library (যেমন C standard library) থেকে দেওয়া functions-এর সেট যেগুলো প্রায়ই system calls wrap করে। একটি API এক বা একাধিক system call call করতে পারে, বা কোনো system call ছাড়াই কাজ করতে পারে। যেমন printf() ভেতরে write() syscall করে, কিন্তু formatting নিজেই handle করে। সুবিধা হলো একই API different OS-এ কাজ করে, কারণ প্রতিটি OS-এ আসল syscall আলাদা।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি (application) একটি bank থেকে টাকা withdraw করতে চান। আপনি একটি withdrawal slip পূরণ করেন (API call)। Teller (system call handler) আপনার balance check করে (kernel), vault-এ যায় (hardware), এবং আপনাকে cash দেয়। আপনি নিজে কখনো vault-এ ঢুকতে পারবেন না। অর্থাৎ user program কখনো directly hardware access করে না — সব সময় syscall-এর মাধ্যমে।",
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
        text: "Operating systems একটি set of core services দেয় যেগুলো user ও programmer-দের জীবন সহজ করে। প্রতিটি service-এর নির্দিষ্ট কাজ আছে, এবং সবগুলো একসাথে মিলে একটি smooth user experience তৈরি করে।",
      },
      {
        type: "list",
        items: [
          "Program execution — একটি program কে memory-তে load করে run করা (যেমন .exe double-click বা ./a.out run)",
          "I/O operations — files, devices read/write করা (printf, scanf, disk access)",
          "File system manipulation — files/directories create, delete, rename করা (mkdir, rm, file explorer)",
          "Communication — processes-এর মধ্যে data exchange (pipes, sockets, shared memory)",
          "Error detection — hardware errors, memory faults, division by zero handle করা (segmentation fault handler)",
          "Resource allocation — CPU time, memory, devices assign করা (scheduler, memory manager)",
          "Accounting — user অনুযায়ী resource usage track রাখা (top, ps, system logs)",
          "Protection — unauthorised access prevent করা (file permissions, memory protection)",
        ],
      },
      {
        type: "p",
        text: "Utilities হলো user-level programs যেগুলো OS-এর সাথে আসে (যেমন ls, cp, grep, Task Manager)। এগুলো কাজ করতে system calls use করে। Real-life thinking — একটি hotel services দেয়: luggage storage (resource allocation), wake-up calls (communication), laundry (I/O)। Utilities হলো concierge desk-এর মতো — তারা hotel-এর internal systems-এর উপর depend করে। অর্থাৎ utility program গুলো নিজে নিজে OS service করে না, বরং syscall-এর মাধ্যমে OS-কে কাজ করতে বলে।",
      },

      { type: "h2", id: "booting", title: "Booting Process" },
      {
        type: "p",
        text: "Booting (সংক্ষেপে 'bootstrap') হলো সেই sequence of operations যেটি operating system কে memory-তে load করে এবং computer on করলে শুরু করে। এটি একটি deterministic sequence — প্রতিবার computer on করলে একই ধাপ অনুসরণ করা হয়।",
      },
      { type: "h3", title: "Step-by-step boot flow" },
      {
        type: "list",
        items: [
          "1. Power-on — CPU real mode-এ শুরু হয় (limited memory access) এবং একটি fixed memory address-এ jump করে যেখানে BIOS firmware থাকে",
          "2. BIOS or UEFI — Basic Input/Output System (পুরোনো) বা Unified Extensible Firmware Interface (modern) hardware initialize করে: clocks, memory controller, disk detection",
          "3. POST (Power-On Self Test) — critical hardware (CPU, RAM, disk controllers) check করে। Fatal error হলে beep codes বা message দেখায়",
          "4. Bootloader loading — BIOS/UEFI first sector (MBR বা EFI System Partition) read করে এবং bootloader (GRUB, Windows Boot Manager) load করে",
          "5. Kernel loading — bootloader OS kernel (Linux-এ vmlinuz) memory-তে read করে, সম্ভবত একটি initrd সহ যেটিতে initial drivers থাকে",
          "6. Kernel initialisation — protected/long mode-এ switch করে, memory management set up করে, interrupt handlers, device drivers, root file system mount করে",
          "7. Init process — kernel প্রথম user-mode process শুরু করে (traditionally /sbin/init, এখন Linux-এ systemd, macOS-এ launchd)",
          "8. Login — system একটি login prompt দেখায় (text বা graphical); login সফল হলে shell বা desktop environment পান",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — সকালে একটি restaurant খোলা। প্রথমে main power on করেন (power-on)। তারপর manager check করেন kitchen equipment কাজ করছে কিনা (POST)। Chef আসেন এবং menu prepare করা শুরু করেন (kernel init)। প্রথম waiter clock in করে (init process)। সবশেষে door খোলে এবং customers আসে (login)। আজকের fast-boot computer-এ পুরো sequence টা 5-15 সেকেন্ডে শেষ হয়।",
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
          "OS definition — software যেটি hardware manage করে, virtual machine দেয়, interface দেয়",
          "Roles — resource manager, virtual machine, interface",
          "Computer architecture — CPU, RAM, I/O devices bus-এর সাথে connected",
          "OS structures — Monolithic (fast, fragile), Microkernel (stable, slower), Hybrid (balanced)",
          "User vs kernel mode — privilege separation; system calls mode switch করে",
          "System call — kernel service-এর জন্য request; API সেটি abstract করে",
          "OS services — program execution, I/O, file system, communication, accounting, protection",
          "Booting — Power-on → BIOS/UEFI → bootloader → kernel → init → login",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: এই fundamentals গুলো ভালোভাবে বোঝার পরেই পরের chapter (Process Management, Scheduling, Memory Management) পড়তে হবে। প্রতিটি advanced topic এই basics-এর উপর দাঁড়িয়ে আছে।",
      },
    ],
  },

'''

new_text = before + NEW_CH1 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 01 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
