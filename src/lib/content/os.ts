import type { Topic } from "./types";

export const OS_TOPICS: Topic[] = [
// ---- Ch 01 - Introduction ----
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

// ---- Ch 02 - Process Management ----
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

// ---- Ch 03 - CPU Scheduling ----
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

// ---- Ch 04 - Process Synchronization ----
  {
    id: "os-sync",
    subject: "os",
    title: "Ch 04 — Process Synchronization",
    bangla: "প্রসেস সিঙ্ক্রোনাইজেশন",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "যখন অনেক processes বা threads একই shared data-তে concurrently access করে, ফলাফল unpredictable বা incorrect হতে পারে। Process synchronization নিশ্চিত করে যে cooperative processes controlled ভাবে execute হয়, race conditions prevent হয় এবং data integrity preserve হয়। এই chapter-এ classic problems, solutions, ও system-level tools আলোচনা করা হয়েছে।",
    sections: [
      { type: "h2", id: "critical-section", title: "Critical Section Problem" },
      {
        type: "p",
        text: "Critical section হলো code-এর এমন একটি segment যেটি shared variables বা resources access করে (যেমন একটি file, একটি global counter) যেগুলো একাধিক process বা thread একসাথে execute করতে পারবে না।",
      },
      {
        type: "p",
        text: "Critical section problem হলো এমন একটি protocol design করা যেটি নিশ্চিত করে যে যখন একটি process তার critical section-এর ভেতরে থাকে, তখন কোনো অন্য process একই shared resources access করে এমন তার নিজের critical section-এ প্রবেশ করতে পারবে না।",
      },
      { type: "h3", title: "Typical process-এর structure" },
      {
        type: "code",
        lang: "c",
        text: `do {
    // Entry section — critical section-এ ঢোকার permission request
    // Critical section — shared variables access
    // Exit section — permission release
    // Remainder section — non-critical কাজ
} while (true);`,
      },
      {
        type: "p",
        text: "Real-life thinking — একটি ATM machine (critical section)। এক সময়ে শুধু একজন ব্যক্তি use করতে পারে। Waiting করা people (processes) কে coordinate করতে হবে — যদি দুজন একসাথে use করতে চায়, system double-dispense cash করতে পারে বা balances corrupt করতে পারে।",
      },

      { type: "h2", id: "requirements", title: "Solution Requirements" },
      {
        type: "p",
        text: "Critical section problem-এর valid solution তিনটি condition satisfy করতে হবে:",
      },
      {
        type: "list",
        items: [
          "Mutual exclusion — যদি process Pᵢ তার critical section execute করে, কোনো অন্য process তার critical section-এ থাকতে পারবে না।",
          "Progress — যদি কোনো process critical section-এ না থাকে এবং কিছু processes enter করতে চায়, শুধু সেই processes গুলো যারা তাদের remainder section-এ নেই তারা participate করবে কে enter করবে সেটা decide করতে। Selection অসীমকাল পর্যন্ত postpone করা যাবে না।",
          "Bounded waiting — একটি process critical section-এ enter করার request করার পর, কতগুলো অন্য processes এই request grant হওয়ার আগে enter করতে পারবে তার একটি bound (limit) আছে। কোনো starvation থাকবে না।",
        ],
      },

      { type: "h2", id: "peterson", title: "Software Solution: Peterson's Algorithm" },
      {
        type: "p",
        text: "Peterson's algorithm (1981) হলো দুটি processes (P0 ও P1) এর জন্য একটি classic software-only solution যেটি তিনটি requirements সব satisfy করে। এটি hardware atomic operations ছাড়াই কাজ করে।",
      },
      { type: "h3", title: "Data structures" },
      {
        type: "list",
        items: [
          "int turn; — কার turn সেটা indicate করে।",
          "bool flag[2]; — প্রতিটি flag[i] indicate করে যে process i enter করতে ready।",
        ],
      },
      {
        type: "multi-code",
        filename: "peterson_algo",
        codeSamples: {
          cpp: `#include <iostream>
#include <thread>
#include <atomic>

std::atomic<int> turn{0};
std::atomic<bool> flag[2] = {false, false};
int counter = 0;  // shared resource

void worker(int i) {
    int j = 1 - i;
    for (int k = 0; k < 10000; k++) {
        flag[i] = true;          // I want to enter
        turn = j;                // courtesy: let other go first
        while (flag[j] && turn == j);  // busy wait
        // --- critical section ---
        counter++;
        // --- exit section ---
        flag[i] = false;
    }
}

int main() {
    std::thread t0(worker, 0), t1(worker, 1);
    t0.join(); t1.join();
    std::cout << "counter=" << counter << '\\n';  // 20000
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
    "sync/atomic"
)

var turn int32 = 0
var flag = [2]bool{false, false}
var counter int32 = 0

func worker(i int, wg *sync.WaitGroup) {
    defer wg.Done()
    j := 1 - i
    for k := 0; k < 10000; k++ {
        flag[i] = true
        atomic.StoreInt32(&turn, int32(j))
        for flag[j] && atomic.LoadInt32(&turn) == int32(j) {
            // busy wait
        }
        counter++
        flag[i] = false
    }
}

func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    go worker(0, &wg)
    go worker(1, &wg)
    wg.Wait()
    fmt.Println("counter=", counter)  // 20000
}`,
          python: `import threading

turn = 0
flag = [False, False]
counter = 0
lock = threading.Lock()  # to safely update flag/turn (Peterson's classic assumes atomics)

def worker(i):
    global turn, flag, counter
    j = 1 - i
    for _ in range(10000):
        with lock:
            flag[i] = True
            turn = j
        while flag[j] and turn == j:
            pass  # busy wait
        # --- critical section ---
        counter += 1
        # --- exit ---
        with lock:
            flag[i] = False

ts = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("counter=", counter)  # 20000 (GIL makes it sequential anyway)`,
          java: `import java.util.concurrent.atomic.*;

public class Peterson {
    static AtomicInteger turn = new AtomicInteger(0);
    static AtomicBoolean[] flag = {
        new AtomicBoolean(false), new AtomicBoolean(false)
    };
    static int counter = 0;

    static void worker(int i) {
        int j = 1 - i;
        for (int k = 0; k < 10000; k++) {
            flag[i].set(true);
            turn.set(j);
            while (flag[j].get() && turn.get() == j) {
                // busy wait
                Thread.yield();
            }
            counter++;  // critical section
            flag[i].set(false);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t0 = new Thread(() -> worker(0));
        Thread t1 = new Thread(() -> worker(1));
        t0.start(); t1.start();
        t0.join(); t1.join();
        System.out.println("counter=" + counter);  // 20000
    }
}`,
        },
      },
      {
        type: "p",
        text: "Real-life thinking — দুজন মানুষ একটি single phone booth share করছে। প্রত্যেকে হাত তোলে (flag[i]=true) এবং politely বলে 'You go first' (turn = j)। যদি দুজনই হাত তোলে, যার turn সে (last spoken 'you first' অনুযায়ী) step back করে এবং অপরকে যেতে দেয়।",
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: Peterson's algorithm elegant কিন্তু modern CPU architectures-এ out-of-order execution এর কারণে কাজ করে না যতক্ষণ না memory barriers use করা হয়। এটি শুধু pedagogical classic হিসেবে থাকে।",
      },

      { type: "h2", id: "hardware", title: "Hardware Support: Test-and-Set ও Compare-and-Swap" },
      {
        type: "p",
        text: "Modern processors atomic hardware instructions provide করে যেগুলো একটি uninterruptible step-এ memory read, modify, ও write করে। এই instructions efficient synchronization primitives build করতে use হয়।",
      },

      { type: "h3", title: "Test-and-Set (TAS)" },
      {
        type: "p",
        text: "Atomically একটি memory location read করে এবং সেটিতে true (বা 1) write করে। এটি একটি single uninterruptible operation, তাই দুটি threads একসাথে TAS call করলে একটি পাবে old value false, অপরটি পাবে true।",
      },
      {
        type: "code",
        lang: "c",
        text: `bool test_and_set(bool *target) {
    bool old = *target;
    *target = true;
    return old;
}`,
      },
      {
        type: "p",
        text: "Mutual exclusion using TAS (shared variable lock = false initially): while (test_and_set(&lock)); // busy wait এর মাধ্যমে process lock acquire করার চেষ্টা করে। যেহেতু TAS atomic, একসাথে দুটি process lock acquire করতে পারবে না।",
      },

      { type: "h3", title: "Compare-and-Swap (CAS)" },
      {
        type: "p",
        text: "Atomically একটি variable-কে একটি given value-র সাথে compare করে; যদি equal হয়, সেটি একটি new value-র সাথে swap হয়। CAS modern lock-free programming-এ অত্যন্ত গুরুত্বপূর্ণ — এটি Java Atomic classes, Rust Arc/Mutex ইত্যাদির ভিত্তি।",
      },
      {
        type: "code",
        lang: "c",
        text: `int compare_and_swap(int *value, int expected, int new_value) {
    int old = *value;
    if (old == expected)
        *value = new_value;
    return old;
}`,
      },
      {
        type: "p",
        text: "Using CAS for mutual exclusion: while (compare_and_swap(&lock, 0, 1) != 0); // wait until lock 0 হয়। Real-life thinking — একটি restroom key। TAS হলো key available থাকলে grab করা এবং একই motion-এ সেটি 'taken' mark করা। CAS হলো বলা 'If key hook-এ আছে, নাও এবং একটা busy sign রেখে দাও; নাহলে কিছু করো না'।",
      },

      { type: "h2", id: "mutex-spinlock", title: "Mutex Locks ও Spinlocks" },
      {
        type: "p",
        text: "Mutex (MUTual EXclusion) হলো একটি simple locking mechanism যেটি acquire() ও release() operations support করে। দুটি প্রকার আছে — blocking mutex ও spinlock।",
      },
      {
        type: "list",
        items: [
          "Mutex lock (blocking) — thread lock acquire করতে না পারলে sleep হয়ে যায় (context switch)। Long critical sections-এর জন্য ভালো।",
          "Spinlock — thread lock acquire করতে না পারলে busy-wait (spin) করে একটি loop-এ, CPU consume করে। Short critical sections-এর জন্য ভালো (কোনো context-switch overhead নেই)।",
        ],
      },
      { type: "h3", title: "Mutex vs Spinlock — Comparison" },
      {
        type: "list",
        items: [
          "Waiting behaviour — Mutex: thread sleep হয়; Spinlock: thread spins (busy-wait)",
          "CPU usage during wait — Mutex: প্রায় zero; Spinlock: high (cycles waste)",
          "Context switch overhead — Mutex: yes (scheduler ও back); Spinlock: none",
          "Best when — Mutex: critical section long বা I/O involved; Spinlock: critical section very short",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Mutex হলো meeting room-এর জন্য wait করা — আপনি আপনার office-এ যান (sleep) এবং free হলে notify পান। Spinlock হলো red light-এর জন্য wait করা — আপনি engine চালু রাখেন, steering wheel tap করতে থাকেন।",
      },

      { type: "h2", id: "mutex-demo", title: "Mutex Demo — Concurrent Counter" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় একটি concurrent counter দেখানো হলো যেখানে অনেক threads একসাথে একটি shared counter increment করে। Mutex ছাড়া race condition হবে এবং final value ভুল হবে। Mutex দিয়ে প্রতিটি increment atomic হয়।",
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

      { type: "h2", id: "semaphores", title: "Semaphores" },
      {
        type: "p",
        text: "Semaphore হলো একটি integer variable যেটি initialization ছাড়া শুধু দুটি atomic operations দিয়ে access করা যায়: wait() (P, down, decrement ও নামেও পরিচিত) এবং signal() (V, up, increment)।",
      },
      { type: "h3", title: "Binary Semaphore" },
      {
        type: "p",
        text: "শুধু 0 ও 1 value নেয় — mutex lock-এর মতো behave করে। wait(S) যদি S > 0 হয় তাহলে decrement করে এবং proceed করে; নাহলে block/wait করে। signal(S) সবসময় S increment করে।",
      },
      { type: "h3", title: "Counting Semaphore" },
      {
        type: "p",
        text: "যেকোনো non-negative integer value নিতে পারে — available resources-এর সংখ্যা represent করে। wait(S) decrement করে; যদি S < 0 হয়ে যায় process block হয়। signal(S) increment করে; যদি blocked processes থাকে একজনকে wake করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি parking garage with 50 spaces। একটি counter available spots দেখায়। wait() = car enters (counter--)। signal() = car leaves (counter++)। যদি counter 0 হয়ে যায়, cars-কে queue (block) করতে হয় বাইরে। উদাহরণ: তিনটি printers। Initialize semaphore printers = 3। প্রতিটি process printing-এর আগে wait(&printers), পরে signal(&printers) করে। চতুর্থ process block হবে যতক্ষণ না একটি printer free হয়।",
      },

      { type: "h2", id: "classical", title: "Classical Synchronization Problems" },
      {
        type: "p",
        text: "এই classic problems গুলো synchronization-এর challenges এবং semaphores, mutexes, monitors-এর use illustrate করে।",
      },

      { type: "h3", title: "1. Bounded Buffer (Producer-Consumer)" },
      {
        type: "p",
        text: "Problem — একটি fixed-size buffer। Producers তাতে data write করে; consumers data বের করে নেয়। Producer কে full buffer-এ write করতে পারবে না; consumer empty buffer থেকে read করতে পারবে না। দুটি producers (বা consumers) একসাথে buffer access করতে পারবে না।",
      },
      {
        type: "p",
        text: "Solution তিনটি semaphore use করে: mutex = 1 (buffer access protect করে), empty = n (empty slots সংখ্যা), full = 0 (filled slots সংখ্যা)। Producer প্রথমে wait(&empty) করে (empty slot আছে কিনা দেখে), তারপর wait(&mutex) করে, item add করে, signal(&mutex) ও signal(&full) করে। Consumer একইভাবে full থেকে empty-তে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি pizza delivery counter (buffer)। Baker (producer) pizzas make করে shelf-এ রাখে। Cashier (consumer) customers-এর জন্য নেয়। Baker shelf full হলে থামে (empty=0)। Cashier shelf empty হলে wait করে (full=0)। একসাথে একজনই shelf touch করে (mutex)।",
      },
      {
        type: "multi-code",
        filename: "producer_consumer",
        codeSamples: {
          cpp: `#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

std::queue<int> buffer;
const int N = 5;
std::mutex m;
std::condition_variable notFull, notEmpty;

void producer(int id) {
    for (int i = 0; i < 10; i++) {
        std::unique_lock<std::mutex> lk(m);
        notFull.wait(lk, []{ return buffer.size() < N; });
        buffer.push(i);
        std::cout << "P" << id << " produced " << i << '\\n';
        notEmpty.notify_one();
    }
}

void consumer(int id) {
    for (int i = 0; i < 10; i++) {
        std::unique_lock<std::mutex> lk(m);
        notEmpty.wait(lk, []{ return !buffer.empty(); });
        int v = buffer.front(); buffer.pop();
        std::cout << "C" << id << " consumed " << v << '\\n';
        notFull.notify_one();
    }
}

int main() {
    std::thread p(producer, 1), c(consumer, 1);
    p.join(); c.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

const N = 5

func main() {
    buffer := make(chan int, N)
    var wg sync.WaitGroup
    wg.Add(2)

    go func() {
        defer wg.Done()
        for i := 0; i < 10; i++ {
            buffer <- i
            fmt.Println("P1 produced", i)
        }
    }()

    go func() {
        defer wg.Done()
        for i := 0; i < 10; i++ {
            v := <-buffer
            fmt.Println("C1 consumed", v)
        }
    }()

    wg.Wait()
}`,
          python: `import threading
import queue

N = 5
buffer = queue.Queue(maxsize=N)

def producer():
    for i in range(10):
        buffer.put(i)  # blocks if full
        print(f"P1 produced {i}")

def consumer():
    for _ in range(10):
        v = buffer.get()  # blocks if empty
        print(f"C1 consumed {v}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()`,
          java: `import java.util.concurrent.*;

public class ProducerConsumer {
    public static void main(String[] args) {
        BlockingQueue<Integer> buffer = new ArrayBlockingQueue<>(5);

        new Thread(() -> {
            try {
                for (int i = 0; i < 10; i++) {
                    buffer.put(i);
                    System.out.println("P1 produced " + i);
                }
            } catch (InterruptedException e) {}
        }).start();

        new Thread(() -> {
            try {
                for (int i = 0; i < 10; i++) {
                    int v = buffer.take();
                    System.out.println("C1 consumed " + v);
                }
            } catch (InterruptedException e) {}
        }).start();
    }
}`,
        },
      },

      { type: "h3", title: "2. Readers-Writers" },
      {
        type: "p",
        text: "Problem — একটি shared database। অনেক readers একসাথে read করতে পারে, কিন্তু একজন writer-কে exclusive access প্রয়োজন। দুটি variation আছে — First readers-writers problem (no reader starvation) যেখানে readers-এর priority এবং writers starve হতে পারে। Second readers-writers problem (writer priority) যেখানে writers-এর priority এবং readers starve হতে পারে।",
      },
      {
        type: "p",
        text: "Solution (first, with reader priority): তিনটি shared variables — rw_mutex = 1 (writer access), mutex = 1 (read_count protect করে), read_count = 0। Reader ঢোকার সময় mutex acquire করে read_count increment করে। যদি read_count == 1 হয় (first reader), rw_mutex acquire করে writers-কে lock করে। Last reader (read_count == 0) rw_mutex release করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি library book। অনেক মানুষ একই book একসাথে read করতে পারে (readers)। কিন্তু শুধু একজন মানুষ book update করতে পারবে (writer) — এবং update করার সময় কেউ half-written version read করবে না।",
      },

      { type: "h3", title: "3. Dining Philosophers" },
      {
        type: "p",
        text: "Problem — পাঁচজন philosopher একটি table-এ পাঁচটি chopstick (বা fork) সহ sit করে। প্রতিটি philosopher-কে eat করতে দুটি chopstick প্রয়োজন — left ও right। তারা think ও eat এর মধ্যে alternate করে। Challenge হলো deadlock ও starvation avoid করা।",
      },
      {
        type: "p",
        text: "Naïve solution deadlock হয় যদি সবাই একসাথে left chopstick pick up করে। Solution — একটি mutex use করে শুধু 4 philosophers-কে একসাথে table-এ allow করা। অথবা asymmetric (odd pick left then right, even pick right then left)। অথবা monitor use করা।",
      },
      {
        type: "p",
        text: "Real-life thinking — একদল বন্ধু একটি communal bowl of rice ও spoons share করছে। প্রত্যেকের serve করতে দুটি spoon প্রয়োজন। Coordination না থাকলে সবাই একটি spoon চিরকাল hold করে থাকবে (deadlock)।",
      },
      {
        type: "multi-code",
        filename: "dining_philosophers",
        codeSamples: {
          cpp: `#include <mutex>
#include <thread>
#include <vector>
#include <cstdio>

const int N = 5;
std::mutex chopsticks[N];
std::mutex table_mutex;  // prevent deadlock: allow only N-1 at table

void philosopher(int i) {
    int left = i;
    int right = (i + 1) % N;
    for (int meal = 0; meal < 3; meal++) {
        // think...
        {
            std::lock_guard<std::mutex> lk(table_mutex);
            std::lock(chopsticks[left], chopsticks[right]);
        }
        std::printf("P%d eating meal %d\\n", i, meal);
        chopsticks[left].unlock();
        chopsticks[right].unlock();
    }
}

int main() {
    std::vector<std::thread> ts;
    for (int i = 0; i < N; i++) ts.emplace_back(philosopher, i);
    for (auto& t : ts) t.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

const N = 5

func main() {
    var chopsticks [N]sync.Mutex
    var table sync.Mutex
    var wg sync.WaitGroup

    for i := 0; i < N; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            left := i
            right := (i + 1) % N
            for meal := 0; meal < 3; meal++ {
                table.Lock()
                chopsticks[left].Lock()
                chopsticks[right].Lock()
                table.Unlock()
                fmt.Printf("P%d eating meal %d\\n", i, meal)
                chopsticks[right].Unlock()
                chopsticks[left].Unlock()
            }
        }(i)
    }
    wg.Wait()
}`,
          python: `import threading

N = 5
chopsticks = [threading.Lock() for _ in range(N)]
table = threading.Lock()  # prevent deadlock

def philosopher(i):
    left, right = i, (i + 1) % N
    for meal in range(3):
        with table:
            chopsticks[left].acquire()
            chopsticks[right].acquire()
        print(f"P{i} eating meal {meal}")
        chopsticks[right].release()
        chopsticks[left].release()

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for t in threads: t.start()
for t in threads: t.join()`,
          java: `import java.util.concurrent.locks.*;

public class DiningPhilosophers {
    static final int N = 5;
    static ReentrantLock[] chopsticks = new ReentrantLock[N];
    static ReentrantLock table = new ReentrantLock();
    static {
        for (int i = 0; i < N; i++) chopsticks[i] = new ReentrantLock();
    }

    static void philosopher(int i) {
        int left = i, right = (i + 1) % N;
        for (int meal = 0; meal < 3; meal++) {
            table.lock();
            try {
                chopsticks[left].lock();
                chopsticks[right].lock();
            } finally { table.unlock(); }
            System.out.printf("P%d eating meal %d%n", i, meal);
            chopsticks[right].unlock();
            chopsticks[left].unlock();
        }
    }

    public static void main(String[] args) {
        Thread[] ts = new Thread[N];
        for (int i = 0; i < N; i++) {
            final int idx = i;
            ts[i] = new Thread(() -> philosopher(idx));
            ts[i].start();
        }
        for (Thread t : ts) {
            try { t.join(); } catch (InterruptedException e) {}
        }
    }
}`,
        },
      },

      { type: "h3", title: "4. Sleeping Barber" },
      {
        type: "p",
        text: "Problem — একটি barber shop একজন barber, একটি barber chair, এবং কিছু waiting chairs সহ। যদি কোনো customer না থাকে, barber sleep করে। একজন customer arrive করলে sleeping barber-কে wake করে। যদি barber busy হয়, customer একটি waiting chair-এ wait করে যদি available থাকে; নাহলে leave করে।",
      },
      {
        type: "p",
        text: "Solution তিনটি semaphores ও একটি integer use করে: customers = 0 (waiting customers), barber = 0 (barber ready), mutex = 1 (waiting count protect করে), waiting = 0 (number waiting), CHAIRS = 5। Barber wait(&customers) করে sleep করে। Customer arrive করলে waiting < CHAIRS হলে signal(&customers) করে barber-কে wake করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — ঠিক সেই described barber shop, যেখানে barber customers-এর মধ্যে nap করে। এই problem real-world resource management (server pools, thread pools, message queues) simulate করে।",
      },

      { type: "h2", id: "monitors", title: "Monitors ও Condition Variables" },
      {
        type: "p",
        text: "Monitor হলো একটি high-level abstraction যেটি clean, structured ভাবে synchronization achieve করতে দেয়। এটি একটি programming language construct (যেমন Java, C#-এ) বা library concept (যেমন C-এ pthread_cond)।",
      },
      {
        type: "list",
        items: [
          "Monitor shared variables ও তাদের operations-কে encapsulate করে।",
          "একই সময়ে শুধু একটি thread monitor-এর ভেতরে active থাকতে পারে (automatic mutual exclusion)।",
          "Condition variables একটি thread-কে monitor-এর ভেতরে একটি নির্দিষ্ট condition true হওয়ার জন্য wait করতে দেয়, সাময়িকভাবে monitor lock release করে।",
        ],
      },
      { type: "h3", title: "Condition variable operations" },
      {
        type: "list",
        items: [
          "wait(cond, mutex) — mutex release করে, cond-এ block করে, signal হলে mutex re-acquire করে।",
          "signal(cond) — একজন waiting thread-কে wake করে (যদি থাকে)।",
          "broadcast(cond) — সব waiting threads-কে wake করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restroom with একটি single key (monitor lock)। যদি restroom occupied হয়, আপনি একটি 'vacant' condition-এ wait করেন। Occupant leave করলে সে signal করে — একজন waiting person enter করে।",
      },

      { type: "h2", id: "pthreads", title: "Synchronization in POSIX Threads (Pthreads)" },
      {
        type: "p",
        text: "POSIX threads (pthreads) Unix-like systems-এ multithreading-এর জন্য একটি standard API provide করে। Common synchronization primitives হলো mutexes ও condition variables।",
      },
      { type: "h3", title: "Pthread Mutexes" },
      {
        type: "code",
        lang: "c",
        text: `#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

// In threads
pthread_mutex_lock(&mutex);
// critical section
pthread_mutex_unlock(&mutex);`,
      },
      {
        type: "p",
        text: "pthread_mutex_trylock() non-blocking lock acquisition attempt করে — যদি lock available না হয় immediately return করে। এটি deadlock-free algorithms-এ useful।",
      },
      { type: "h3", title: "Pthread Condition Variables" },
      {
        type: "p",
        text: "Condition variables সবসময় একটি mutex-এর সাথে use হয়। একটি thread যে condition হবে সেটির জন্য wait করে। অন্য thread সেই condition true করে signal করে। সবসময় while loop use করতে হয় (if নয়) কারণ spurious wakeups হতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি ticket booking system। Mutex double booking prevent করে। Condition variables একটি thread-কে seat available হওয়ার জন্য wait করতে দেয়।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Critical section — shared resources access করে এমন code segment যেটি mutually exclusive হতে হবে।",
          "Requirements — mutual exclusion, progress, bounded waiting।",
          "Peterson's algorithm — দুটি processes-এর জন্য software solution (pedagogical, practice-এ widely used নয়)।",
          "Hardware support — TAS, CAS atomic instructions যেগুলো lock implementation simplify করে।",
          "Mutex / Spinlock — Mutex block করে, spinlock busy-wait করে। Critical section-এর length অনুযায়ী choose করতে হবে।",
          "Semaphores — Counting semaphores resources manage করে; binary semaphores mutex-এর মতো কাজ করে।",
          "Classical problems — bounded buffer, readers-writers, dining philosophers, sleeping barber।",
          "Monitors — automatic mutual exclusion ও condition variables সহ language construct।",
          "Pthreads — Unix threading standard API with pthread_mutex ও pthread_cond।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Process synchronization বোঝা correct concurrent programs লেখার জন্য crucial। পরের chapter deadlock নিয়ে আলোচনা করবে — কী হয় যখন synchronization ভুল হয়।",
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

// ---- Ch 06 - Memory Management ----
  {
    id: "os-memory",
    subject: "os",
    title: "Ch 06 — Memory Management",
    bangla: "মেমোরি ম্যানেজমেন্ট",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Memory হলো একটি computer system-এর physical heart। Operating system-কে efficiently processes-এ memory allocate করতে হয়, এক process-কে অন্য থেকে protect করতে হয়, এবং একটি large, private address space-এর illusion তৈরি করতে হয়। এই chapter-এ hardware ও OS techniques ব্যাখ্যা করা হয়েছে যেগুলো modern memory management সম্ভব করে।",
    sections: [
      { type: "h2", id: "hierarchy", title: "Memory Hierarchy" },
      {
        type: "p",
        text: "সব memory সমান নয়। একটি typical computer-এ storage-এর একটি hierarchy আছে — fast ও expensive থেকে slow ও cheap পর্যন্ত।",
      },
      { type: "h3", title: "Memory hierarchy levels" },
      {
        type: "list",
        items: [
          "Registers — CPU internal, few hundred bytes, 0.2-0.5 ns access, compiler দ্বারা managed।",
          "Cache (L1, L2, L3) — SRAM, 32KB – 32MB, 1-10 ns, hardware দ্বারা managed।",
          "Main memory (RAM) — DRAM, 4GB – 512GB, 50-100 ns, OS দ্বারা managed।",
          "Swap space (disk) — SSD/HDD, 100GB – 2TB, 0.1-10 ms, OS দ্বারা managed।",
          "File storage — SSD/HDD, 256GB – multiple TB, ms – seconds, User/OS দ্বারা managed।",
        ],
      },
      {
        type: "p",
        text: "OS-এর memory manager এই complexity hide করে, main memory-কে একটি uniform, linear array of bytes হিসেবে দেখায়, এবং optionally disk পর্যন্ত extend করে (virtual memory, Chapter 7-এ covered)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি desk (registers) যেখানে আপনি এখন কাজ করছেন তা hold করে। একটি nearby bookshelf (cache) reference books hold করে। একটি filing cabinet (RAM) current projects hold করে। একটি warehouse (disk) archived files hold করে। আপনি actively প্রয়োজন হলে data কে hierarchy-তে উপরে move করেন।",
      },

      { type: "h2", id: "binding", title: "Address Binding" },
      {
        type: "p",
        text: "Programs addresses use করে memory reference করে। এই symbolic addresses-কে actual physical memory locations-এ bind করা বিভিন্ন সময়ে হতে পারে।",
      },
      { type: "h3", title: "Three Binding Times" },
      {
        type: "list",
        items: [
          "Compile time — addresses compilation-এ fixed। Example: absolute code (যেমন MS-DOS .COM)। Fast কিন্তু inflexible; program একটি নির্দিষ্ট address-এ load হতে হবে।",
          "Load time — loader দ্বারা program load-এ relocation। Example: relocatable code (যেমন .exe with base address)। Flexible; কিন্তু একবার load হলে, address move করতে পারে না।",
          "Execution time — binding runtime পর্যন্ত delay; MMU use করে। Modern OSes (Linux, Windows)। Maximum flexibility; swapping ও paging allow করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Compile time হলো একটি train timetable যেটা exact platform numbers-এ fixed। Load time হলো একটি conference seating plan — seats আপনি arrive করার সময় assign করা হয়, কিন্তু পরে move করতে পারবেন না। Execution time হলো একটি taxi — আপনার pickup location যখন call করেন তখন determine হয় (runtime)।",
      },

      { type: "h2", id: "logical-physical", title: "Logical vs Physical Address Space" },
      {
        type: "p",
        text: "Logical address (virtual address) — CPU দ্বারা generate হয় যখন program execute হয়। Program শুধু এই address space দেখে। Physical address — RAM hardware-এ actual location। OS ও MMU logical-কে physical-এ translate করে।",
      },
      { type: "h3", title: "Memory Management Unit (MMU)" },
      {
        type: "p",
        text: "MMU হলো hardware যেটি runtime address translation perform করে। একটি simple MMU একটি base (relocation) register use করে: physical address = logical address + base register। একটি bounds (limit) register সহ, OS processes protect করতে পারে — যদি logical address >= limit, OS-এ trap হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hotel room key যেখানে 'Room 412' (logical address) label করা। Hotel-এর internal map (MMU) সেটিকে third floor-এ actual physical room 1012-তে translate করে। আপনাকে physical location জানার দরকার নেই।",
      },

      { type: "h2", id: "allocation", title: "Memory Allocation" },
      {
        type: "p",
        text: "যখন একটি process create হয়, OS তার code, data, ও stack-এর জন্য memory allocate করতে হয়। দুটি main approach আছে — contiguous allocation ও paging।",
      },

      { type: "h3", title: "Contiguous Allocation" },
      {
        type: "p",
        text: "প্রতিটি process physical memory-এ একটি single contiguous block occupy করে। দুটি প্রকার — fixed partitions ও dynamic partitions।",
      },
      { type: "h3", title: "Fixed Partitions (Static)" },
      {
        type: "p",
        text: "Memory কে boot time-এ fixed-size regions-এ ভাগ করা হয়। একটি process তাকে hold করার মতো বড় partition-এ load করা হয়। Pros — simple, কোনো external fragmentation নেই। Cons — internal fragmentation (partition-এর ভেতরে wasted space), limited number of active processes।",
      },
      { type: "h3", title: "Dynamic Partitions (Variable)" },
      {
        type: "p",
        text: "Partitions dynamically create করা হয় যাতে exactly process-এর size match করে। OS free holes-এর একটি list maintain করে। Placement algorithms গুলো হলো — First-fit (first hole যেটা যথেষ্ট বড়, fast, সাধারণত ভালো)। Best-fit (smallest hole যেটা fit করে, কিন্তু tiny useless holes তৈরি করে)। Worst-fit (largest hole, যা বড় remaining holes রেখে যায়)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি busy street-এ parking (dynamic partitions)। First-fit — যে প্রথম spot দেখেন নেন। Best-fit — প্রতিটি spot measure করেন আপনার car-এর সাথে exactly fit করে এমন একটা খুঁজে বের করতে — সময় নষ্ট।",
      },

      { type: "h3", title: "Placement Algorithm Demo" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় first-fit, best-fit, ও worst-fit placement algorithms দেখানো হলো।",
      },
      {
        type: "multi-code",
        filename: "placement_algo",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// holes: list of free hole sizes
int firstFit(const vector<int>& holes, int size) {
    for (int i = 0; i < (int)holes.size(); i++)
        if (holes[i] >= size) return i;
    return -1;
}

int bestFit(const vector<int>& holes, int size) {
    int best = -1;
    for (int i = 0; i < (int)holes.size(); i++)
        if (holes[i] >= size &&
            (best == -1 || holes[i] < holes[best])) best = i;
    return best;
}

int worstFit(const vector<int>& holes, int size) {
    int worst = -1;
    for (int i = 0; i < (int)holes.size(); i++)
        if (holes[i] >= size &&
            (worst == -1 || holes[i] > holes[worst])) worst = i;
    return worst;
}

int main() {
    vector<int> holes = {10, 4, 20, 8, 7};
    int size = 6;
    cout << "first-fit: hole " << firstFit(holes, size)  << '\\n';  // 2
    cout << "best-fit:  hole " << bestFit(holes,  size)  << '\\n';  // 4
    cout << "worst-fit: hole " << worstFit(holes, size)  << '\\n';  // 2
}`,
          go: `package main

import "fmt"

func firstFit(holes []int, size int) int {
    for i, h := range holes {
        if h >= size { return i }
    }
    return -1
}

func bestFit(holes []int, size int) int {
    best := -1
    for i, h := range holes {
        if h >= size && (best == -1 || h < holes[best]) { best = i }
    }
    return best
}

func worstFit(holes []int, size int) int {
    worst := -1
    for i, h := range holes {
        if h >= size && (worst == -1 || h > holes[worst]) { worst = i }
    }
    return worst
}

func main() {
    holes := []int{10, 4, 20, 8, 7}
    size := 6
    fmt.Println("first-fit: hole", firstFit(holes, size))  // 2
    fmt.Println("best-fit:  hole", bestFit(holes, size))   // 4
    fmt.Println("worst-fit: hole", worstFit(holes, size))  // 2
}`,
          python: `def first_fit(holes, size):
    for i, h in enumerate(holes):
        if h >= size:
            return i
    return -1

def best_fit(holes, size):
    best = -1
    for i, h in enumerate(holes):
        if h >= size and (best == -1 or h < holes[best]):
            best = i
    return best

def worst_fit(holes, size):
    worst = -1
    for i, h in enumerate(holes):
        if h >= size and (worst == -1 or h > holes[worst]):
            worst = i
    return worst

holes = [10, 4, 20, 8, 7]
size = 6
print("first-fit: hole", first_fit(holes, size))  # 2
print("best-fit:  hole", best_fit(holes, size))   # 4
print("worst-fit: hole", worst_fit(holes, size))  # 2`,
          java: `import java.util.*;

public class PlacementAlgo {
    static int firstFit(int[] holes, int size) {
        for (int i = 0; i < holes.length; i++)
            if (holes[i] >= size) return i;
        return -1;
    }
    static int bestFit(int[] holes, int size) {
        int best = -1;
        for (int i = 0; i < holes.length; i++)
            if (holes[i] >= size && (best == -1 || holes[i] < holes[best])) best = i;
        return best;
    }
    static int worstFit(int[] holes, int size) {
        int worst = -1;
        for (int i = 0; i < holes.length; i++)
            if (holes[i] >= size && (worst == -1 || holes[i] > holes[worst])) worst = i;
        return worst;
    }
    public static void main(String[] args) {
        int[] holes = {10, 4, 20, 8, 7};
        int size = 6;
        System.out.println("first-fit: hole " + firstFit(holes, size));
        System.out.println("best-fit:  hole " + bestFit(holes, size));
        System.out.println("worst-fit: hole " + worstFit(holes, size));
    }
}`,
        },
      },

      { type: "h2", id: "fragmentation", title: "Fragmentation" },
      { type: "h3", title: "Two types of fragmentation" },
      {
        type: "list",
        items: [
          "Internal fragmentation — একটি allocated partition-এর ভেতরে wasted space। উদাহরণ: fixed partition size 8MB, process 5MB চায় → 3MB waste। Fixed partitions ও paging-এ page alignment-এর কারণে হয়।",
          "External fragmentation — total free memory একটি request satisfy করতে যথেষ্ট, কিন্তু কোনো single contiguous block large enough না। Dynamic partitioning-এ হয় — holes scattered হয়ে যায়।",
        ],
      },
      { type: "h3", title: "Compaction" },
      {
        type: "p",
        text: "Memory contents shuffle করে ছোট holes-কে combine করে একটি বড় hole তৈরি করা। শুধু dynamic (execution-time) binding সহ possible। Expensive কারণ processes-কে move করতে হয়। এটা একটি trade-off — এটা করলে memory utilization ভালো হবে কিন্তু CPU সময় নষ্ট হবে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি wardrobe-এ ছোট ছোট free gaps আছে। সব জামা একদিকে push করলে একদিকে একটি বড় gap তৈরি হয় (compaction)। কিন্তু সব জামা move করতে সময় লাগে।",
      },

      { type: "h2", id: "paging", title: "Paging" },
      {
        type: "p",
        text: "Paging external fragmentation solve করে physical memory-কে fixed-size blocks (frames, সাধারণত 4KB) ও logical memory-কে same-size blocks (pages) এ ভাগ করে। একটি process-এর pages অসংখ্য non-contiguous frames-এ scattered হতে পারে।",
      },
      { type: "h3", title: "Key idea" },
      {
        type: "p",
        text: "Logical address = (page number, page offset)। OS page number-কে frame number-এ একটি page table দিয়ে map করে।",
      },
      { type: "h3", title: "Address Translation" },
      {
        type: "p",
        text: "m-bit logical address, page size 2^n bytes হলে — Page number (p) = top (m - n) bits। Page offset (d) = lower n bits। উদাহরণ: 32-bit address, 4KB pages (2^12)। Page number = bits 31-12, offset = bits 11-0।",
      },
      { type: "h3", title: "Page Table Entry (PTE)" },
      {
        type: "list",
        items: [
          "Frame number — physical frame যেখানে page reside করে।",
          "Valid (present) bit — page memory-তে আছে (1) বা disk-এ swapped (0)।",
          "Dirty (modified) bit — page-এ লেখা হয়েছে (eviction-এ disk-এ write-back প্রয়োজন)।",
          "Reference (accessed) bit — page read বা write হয়েছে (page replacement algorithms-এর জন্য use হয়)।",
          "Protection bits — read, write, execute permissions।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Paging হলো একটি filing system যেখানে প্রতিটি file (page) যেকোনো drawer (frame)-এ store করা যায়, একটি index (page table) সহ। TLB হলো আপনার desk-এ একটি ছোট sticky note যেখানে most-used file locations লেখা, যাতে প্রতিবার বড় index না খুলতে হয়।",
      },
      {
        type: "multi-code",
        filename: "page_table",
        codeSamples: {
          cpp: `#include <iostream>
#include <unordered_map>

class MMU {
    std::unordered_map<int, int> pageTable;   // page -> frame
    int pageSize;
public:
    MMU(std::unordered_map<int,int> pt, int ps = 4096)
        : pageTable(pt), pageSize(ps) {}

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
    MMU mmu({ {0, 5}, {1, 9}, {2, 3} });
    std::cout << "0x0     -> " << mmu.translate(0)    << '\\n';   // 20480
    std::cout << "0x1001  -> " << mmu.translate(4097) << '\\n';   // 37401
    std::cout << "0x5000  -> " << mmu.translate(20480) << '\\n';   // -1 (page fault)
}`,
          go: `package main

import "fmt"

type MMU struct {
    pageTable map[int]int
    pageSize  int
}

func (m *MMU) translate(vaddr int) int {
    page := vaddr / m.pageSize
    off  := vaddr % m.pageSize
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
    fmt.Println("0x0    ->", m.translate(0))
    fmt.Println("0x1001 ->", m.translate(4097))
    fmt.Println("0x5000 ->", m.translate(20480))
}`,
          python: `class MMU:
    def __init__(self, page_table, page_size=4096):
        self.page_table = page_table
        self.page_size = page_size

    def translate(self, vaddr):
        page = vaddr // self.page_size
        off  = vaddr %  self.page_size
        if page not in self.page_table:
            print(f"PAGE FAULT: page {page}")
            return -1
        return self.page_table[page] * self.page_size + off

mmu = MMU({0: 5, 1: 9, 2: 3})
print("0x0    ->", mmu.translate(0))
print("0x1001 ->", mmu.translate(4097))
print("0x5000 ->", mmu.translate(20480))`,
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
        MMU mmu = new MMU(Map.of(0, 5, 1, 9, 2, 3), 4096);
        System.out.println("0x0    -> " + mmu.translate(0));
        System.out.println("0x1001 -> " + mmu.translate(4097));
        System.out.println("0x5000 -> " + mmu.translate(20480));
    }
}`,
        },
      },

      { type: "h3", title: "Multi-level Page Tables" },
      {
        type: "p",
        text: "64-bit address space-এর জন্য single page table impossibly large হবে (2^64 / page size entries)। Multi-level page tables memory overhead reduce করে শুধু সেই levels allocate করে যেগুলো actually use হয়।",
      },
      {
        type: "p",
        text: "উদাহরণ: x86-32 তে 2-level page table (10+10+12 bits)। Virtual address split: Level 1 (page directory index) — 10 bits, একটি page directory entry select করে যেটি একটি page table-এ point করে। Level 2 (page table index) — 10 bits, সেই table-এ একটি PTE select করে। Offset — 12 bits। Advantage — sparse address spaces-এ খুব কম memory waste হয়, শুধু directory ও actually-used page tables।",
      },

      { type: "h3", title: "Inverted Page Table" },
      {
        type: "p",
        text: "Per-process page table-এর বদলে একটি inverted page table-এ প্রতিটি physical frame-এর জন্য একটি entry থাকে। প্রতিটি entry (process ID, page number) mapping store করে। PowerPC, UltraSPARC, ও কিছু IBM systems-এ use হয়।",
      },
      {
        type: "list",
        items: [
          "Size — (physical memory size / frame size) entries, fixed ও small।",
          "Lookup — (PID, page number) pair hash করে entry find করা। Multi-level tables-এর চেয়ে slow।",
        ],
      },

      { type: "h3", title: "Translation Lookaside Buffer (TLB)" },
      {
        type: "p",
        text: "Page tables RAM-এ store থাকে। Memory access করতে হলে দুটি RAM access প্রয়োজন (page table + actual data) — অনেক slow। TLB হলো একটি hardware cache যেটি recently used page-to-frame translations store করে।",
      },
      {
        type: "list",
        items: [
          "TLB hit — translation TLB-এ পাওয়া গেছে, single memory access।",
          "TLB miss — page table walk করতে হবে (RAM-এ), দুই বা ততোধিক access, তারপর mapping cache করা হয়।",
          "Typical TLB — 32-512 entries, fully associative বা set-associative।",
          "TLB coverage — TLB entries × page size = maximum memory যেটা page table walk ছাড়া access করা যায়। 4KB pages ও 64 TLB entries-এর জন্য = 256KB।",
        ],
      },
      {
        type: "p",
        text: "Large pages (যেমন 2MB বা 1GB) TLB coverage improve করে এবং memory-intensive workloads (databases, virtual machines)-এ use হয়।",
      },
      { type: "h3", title: "Context switch ও TLB" },
      {
        type: "p",
        text: "যখন process switch হয়, TLB-এ পুরোনো process-এর entries থাকে। দুটি solution — Flush TLB (costly), বা Tagged TLB যেখানে প্রতিটি entry একটি Address Space ID (ASID) include করে processes differentiate করার জন্য।",
      },
      {
        type: "p",
        text: "Real-life thinking — TLB হলো আপনার desk-এ একটি ছোট sticky note যেখানে সবচেয়ে ব্যবহৃত file locations লেখা। যখন আপনি অন্য project শুরু করেন, sticky note পুরোনো entries দেখায় — flush করতে হয় (নতুন notes লিখতে হয়)।",
      },

      { type: "h2", id: "segmentation", title: "Segmentation" },
      {
        type: "p",
        text: "Segmentation programmer-কে memory-এর একটি view দেয় যেখানে variable-sized segments আছে — code, data, stack, heap, ইত্যাদি — প্রতিটির নিজস্ব base ও limit সহ।",
      },
      { type: "h3", title: "Segment Table" },
      {
        type: "p",
        text: "প্রতিটি process-এর একটি segment table আছে। একটি logical address হলো <segment-number, offset>। Segment table entry-তে থাকে: Base (segment-এর starting physical address), Limit (segment-এর length)। MMU check করে offset < limit, তারপর physical = base + offset compute করে।",
      },
      {
        type: "multi-code",
        filename: "segmentation",
        codeSamples: {
          cpp: `#include <iostream>
#include <stdexcept>
#include <vector>

struct SegEntry { int base, limit; };

class SegmentMMU {
    std::vector<SegEntry> table;
public:
    SegmentMMU(std::vector<SegEntry> t) : table(std::move(t)) {}

    int translate(int seg, int offset) {
        if (seg < 0 || seg >= (int)table.size())
            throw std::runtime_error("Invalid segment");
        const auto& e = table[seg];
        if (offset >= e.limit)
            throw std::runtime_error("Segmentation fault");
        return e.base + offset;
    }
};

int main() {
    SegmentMMU mmu({ {1000, 500}, {2000, 800}, {5000, 200} });
    try {
        std::cout << "seg 0 off 100  -> " << mmu.translate(0, 100)  << '\\n';  // 1100
        std::cout << "seg 1 off 50   -> " << mmu.translate(1, 50)   << '\\n';  // 2050
        std::cout << "seg 2 off 250  -> " << mmu.translate(2, 250)  << '\\n';  // throws
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\\n';
    }
    return 0;
}`,
          go: `package main

import (
    "errors"
    "fmt"
)

type SegEntry struct{ base, limit int }

type SegmentMMU struct{ table []SegEntry }

func (m *SegmentMMU) translate(seg, offset int) (int, error) {
    if seg < 0 || seg >= len(m.table) {
        return 0, errors.New("invalid segment")
    }
    e := m.table[seg]
    if offset >= e.limit {
        return 0, errors.New("segmentation fault")
    }
    return e.base + offset, nil
}

func main() {
    mmu := &SegmentMMU{table: []SegEntry{
        {1000, 500}, {2000, 800}, {5000, 200},
    }}

    if v, err := mmu.translate(0, 100); err == nil {
        fmt.Println("seg 0 off 100 ->", v)   // 1100
    }
    if v, err := mmu.translate(1, 50); err == nil {
        fmt.Println("seg 1 off 50  ->", v)    // 2050
    }
    if _, err := mmu.translate(2, 250); err != nil {
        fmt.Println("Error:", err)            // segmentation fault
    }
}`,
          python: `class SegmentMMU:
    def __init__(self, table):
        self.table = table  # list of (base, limit)

    def translate(self, seg, offset):
        if seg < 0 or seg >= len(self.table):
            raise ValueError("Invalid segment")
        base, limit = self.table[seg]
        if offset >= limit:
            raise ValueError("Segmentation fault")
        return base + offset

mmu = SegmentMMU([(1000, 500), (2000, 800), (5000, 200)])
try:
    print("seg 0 off 100 ->", mmu.translate(0, 100))  # 1100
    print("seg 1 off 50  ->", mmu.translate(1, 50))   # 2050
    print("seg 2 off 250 ->", mmu.translate(2, 250))  # raises
except ValueError as e:
    print("Error:", e)`,
          java: `import java.util.*;

public class SegmentMMU {
    static class SegEntry { int base, limit; SegEntry(int b, int l){base=b;limit=l;} }
    List<SegEntry> table;
    SegmentMMU(List<SegEntry> t) { table = t; }

    int translate(int seg, int offset) {
        if (seg < 0 || seg >= table.size())
            throw new RuntimeException("Invalid segment");
        SegEntry e = table.get(seg);
        if (offset >= e.limit)
            throw new RuntimeException("Segmentation fault");
        return e.base + offset;
    }
    public static void main(String[] args) {
        SegmentMMU mmu = new SegmentMMU(Arrays.asList(
            new SegEntry(1000, 500),
            new SegEntry(2000, 800),
            new SegEntry(5000, 200)));
        System.out.println("seg 0 off 100 -> " + mmu.translate(0, 100));
        System.out.println("seg 1 off 50  -> " + mmu.translate(1, 50));
        try {
            mmu.translate(2, 250);
        } catch (RuntimeException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}`,
        },
      },

      { type: "h3", title: "Segmentation-র Advantages ও Disadvantages" },
      {
        type: "list",
        items: [
          "Advantages: segments separately grow ও shrink করতে পারে (যেমন stack expansion)। Per-segment protection (code=read-only, data=read-write)। Sharing: দুটি processes একটি code segment share করতে পারে একই base/limit reference করে।",
          "Disadvantage: external fragmentation — segments contiguous variable-sized blocks।",
        ],
      },

      { type: "h3", title: "Segmentation with Paging (Intel x86)" },
      {
        type: "p",
        text: "x86 architecture (এবং অনেক others) segmentation ও paging combine করে: segmentation multiple logical address spaces provide করে, এবং প্রতিটি segment pages-এ ভাগ করা হয়।",
      },
      {
        type: "list",
        items: [
          "১. Logical address → <selector, offset>।",
          "২. Segment descriptor (Global Descriptor Table বা Local Descriptor Table থেকে) segment-এর base ও limit দেয়। OS segment base কে 0 set করে effectively segmentation disable করতে পারে।",
          "৩. Resulting linear address (আগে virtual address বলা হতো) paging দ্বারা physical address-এ translate হয় (multi-level page tables)।",
        ],
      },
      {
        type: "p",
        text: "এই two-step approach complex কিন্তু flexibility দেয়। বেশির ভাগ modern OSes (Linux, Windows) একটি flat memory model use করে — একটি (বা কয়েকটি) segment সম্পূর্ণ address space cover করে, প্রায় পুরোপুরি paging-এর উপর rely করে protection ও translation-এর জন্য।",
      },
      {
        type: "p",
        text: "Real-life thinking — Segmentation alone হলো আলাদা boxes (code box, data box, stack box) বিভিন্ন sizes-এ। Boxes কে warehouse-এ rearrange করা যায়। Segmentation + paging হলো boxes, কিন্তু প্রতিটি box আরও ছোট standard-size containers (pages)-এ ভাগ করা যেগুলো warehouse-এ বিভিন্ন shelves-এ store করা যায়।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Memory hierarchy — registers → cache → RAM → swap → storage; speed vs size trade-off।",
          "Address binding — compile time, load time, বা execution time (most modern) হতে পারে।",
          "Logical vs physical — logical = program-এর view; physical = প্রকৃত RAM; MMU translate করে।",
          "Contiguous allocation — fixed বা dynamic partitions; fragmentation-এ ভোগে।",
          "Fragmentation — internal (block-এর ভেতরে waste) ও external (scattered holes)।",
          "Paging — fixed-size pages ও frames; external fragmentation eliminate করে; page table pages-কে frames-এ map করে।",
          "Page table entries — frame number, valid, dirty, reference bits contain করে।",
          "Multi-level page tables — sparse address spaces-এর জন্য memory overhead reduce করে।",
          "Inverted page table — প্রতিটি physical frame-এ একটি entry; কিছু architectures-এ use হয়।",
          "TLB — address translations-এর জন্য hardware cache; performance-এর জন্য critical।",
          "Segmentation — variable-sized segments (code, data, stack) protection ও sharing সহ।",
          "x86 combination — segmentation base/limit provide করে, তারপর paging fine-grain translation-এর জন্য।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Memory management বোঝা fundamental — কারণ এটি paging, swapping, ও virtual memory-র ভিত্তি, যা পরের chapter-এর বিষয়।",
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
    est: "2 hr",
    summary:
      "Virtual memory হলো এমন একটি technique যেটা একটি process-এর logical address space-কে physical memory থেকে separate করে। এটা programs-কে physical RAM-এর চেয়ে বড় হতে allow করে, efficient sharing enable করে, এবং memory management simplify করে। এই chapter-এ ব্যাখ্যা করা হয়েছে virtual memory কীভাবে কাজ করে, OS কীভাবে page faults handle করে, এবং কোন pages memory-তে থাকবে সেই decide করার algorithms কী।",
    sections: [
      { type: "h2", id: "demand-paging", title: "Demand Paging" },
      {
        type: "p",
        text: "Demand paging হলো এমন একটি approach যেখানে pages-কে শুধু তখনই physical memory-তে load করা হয় যখন সেগুলো access করা হয় (on demand), process শুরু হওয়ার সময় নয়। এটা memory usage reduce করে এবং process startup কে speed up করে।",
      },
      {
        type: "p",
        text: "Demand paging-এর অধীনে page table-এ প্রতিটি entry-তে একটি valid-invalid bit থাকে। Valid (1) মানে page টি physical memory-তে আছে (frame allocated)। Invalid (0) মানে page টি memory-তে নেই — হয় কখনো load হয়নি বা disk-এ swap করা হয়েছে (swap space)। যখন program একটি invalid page access করার চেষ্টা করে, hardware OS-এ trap করে — এটাই page fault।",
      },
      { type: "h3", title: "Lazy swapper (pager)" },
      {
        type: "p",
        text: "Lazy swapper বা pager হলো সেই OS যেটি শুধু তখনই pages-কে memory-তে আনে যখন দরকার। এটি whole processes-কে move করা swapper-এর বিপরীত — যেহেতু pager page-level এ কাজ করে, সেহেতু অনেক বেশি fine-grained।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি university library যেটা প্রতিটি book কে storage থেকে reading room-এ একসাথে আনে না। শুধু যখন আপনি একটি book request করেন (page fault), তখনই একজন librarian সেটি basement থেকে fetch করে। এটাই demand paging-এর মূল ভাবনা।",
      },

      { type: "h2", id: "page-fault", title: "Page Fault Handling" },
      {
        type: "p",
        text: "যখন একটি page fault হয়, OS কয়েকটি ধাপ অনুসরণ করে:",
      },
      {
        type: "list",
        items: [
          "১. Hardware OS kernel-এ trap করে, program counter ও process state save করে।",
          "২. OS determine করে কোন virtual page access করা হয়েছিল (faulting address থেকে)।",
          "৩. OS check করে access legal কিনা (address space-এর ভেতরে, correct permissions)। যদি illegal হয়, process terminate হয় (segmentation fault)।",
          "৪. OS একটি free physical frame খোঁজে। যদি না থাকে, একটি page replacement algorithm একটি victim frame select করে।",
          "৫. OS একটি disk read schedule করে যাতে প্রয়োজনীয় page টি swap space থেকে chosen frame-এ আসে।",
          "৬. Disk I/O চলাকালীন, process block হয়। OS অন্য process-এ context-switch করতে পারে।",
          "৭. যখন disk I/O complete হয়, OS page table entry update করে — valid bit = 1, frame number set করে।",
          "৮. OS faulting instruction restart করে, যেটি এখন successfully page access করে।",
        ],
      },
      {
        type: "p",
        text: "Demand paging-এর performance — Effective access time = (1 − p) × memory access time + p × page fault time। এমনকি একটি ছোট page fault rate (p ≈ 0.0001) system-কে significantly slow করে দিতে পারে কারণ disk access RAM-এর চেয়ে ~10⁶ গুণ slow।",
      },

      { type: "h2", id: "cow", title: "Copy-on-Write (COW)" },
      {
        type: "p",
        text: "fork() system call traditionally parent-এর সম্পূর্ণ address space child-এ copy করত — expensive ও slow। Copy-on-write copying defer করে — parent ও child একই physical pages share করে যেগুলো read-only হিসেবে mark করা। যখন কেউ একটি page-এ লেখার চেষ্টা করে, একটি page fault হয়, এবং OS writing process-এর জন্য সেই page-এর একটি private copy তৈরি করে।",
      },
      {
        type: "list",
        items: [
          "Advantage — খুব fast fork। Unmodified pages কখনো copy হয় না।",
          "Use case — fork-এর পর common case হলো child সাথে সাথে exec() call করে — একেবারে কোনো copy হয় না।",
          "Implementation — Page table entries-এ একটি COW flag থাকে। Write fault হলে, page copy করা হয়, উভয় page table update হয় read-write-তে (অথবা original read-only রাখা হয়)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একজন teacher দুজন student-কে একই textbook দেন। যতক্ষণ কেউ লেখে না, তারা share করে। যখন একজন একটি sentence underline করতে চায়, সেই student সেই page-এর একটি photocopy পায় (copy-on-write)।",
      },

      { type: "h2", id: "replacement", title: "Page Replacement Algorithms" },
      {
        type: "p",
        text: "যখন একটি page fault হয় এবং কোনো free frame নেই, OS অবশ্যই memory থেকে একটি page evict করবে। Page replacement algorithms-এর লক্ষ্য হলো সেই page select করা যেটা ভবিষ্যতে সবচেয়ে কম faults cause করবে।",
      },

      { type: "h3", title: "1. FIFO (First-In, First-Out)" },
      {
        type: "p",
        text: "যে page টি memory-তে সবচেয়ে বেশি সময় ধরে আছে সেটিকে evict করো। একটি circular queue হিসেবে implement করা হয়। Advantage — simple। Disadvantage — poor performance; Belady's anomaly-তে ভোগে যেখানে frames-এর সংখ্যা বাড়ালে page faults-ও বাড়তে পারে।",
      },
      {
        type: "p",
        text: "Belady's anomaly উদাহরণ (reference string: 1,2,3,4,1,2,5,1,2,3,4,5): 3 frames → 9 faults। 4 frames → 10 faults (worse!)। এটা counterintuitive — কিন্তু FIFO-তে ঘটে।",
      },
      {
        type: "multi-code",
        filename: "fifo_replace",
        codeSamples: {
          cpp: `#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;

int fifo(const vector<int>& refs, int frames) {
    unordered_set<int> in_mem;
    queue<int> order;
    int faults = 0;
    for (int p : refs) {
        if (in_mem.count(p)) continue;
        faults++;
        if ((int)in_mem.size() == frames) {
            int victim = order.front(); order.pop();
            in_mem.erase(victim);
        }
        in_mem.insert(p);
        order.push(p);
    }
    return faults;
}

int main() {
    vector<int> refs = {1,2,3,4,1,2,5,1,2,3,4,5};
    cout << "3 frames: " << fifo(refs, 3) << " faults\\n";  // 9
    cout << "4 frames: " << fifo(refs, 4) << " faults\\n";  // 10 (Belady!)
    return 0;
}`,
          go: `package main

import "fmt"

func fifo(refs []int, frames int) int {
    inMem := map[int]bool{}
    var order []int
    faults := 0
    for _, p := range refs {
        if inMem[p] { continue }
        faults++
        if len(inMem) == frames {
            victim := order[0]
            order = order[1:]
            delete(inMem, victim)
        }
        inMem[p] = true
        order = append(order, p)
    }
    return faults
}

func main() {
    refs := []int{1,2,3,4,1,2,5,1,2,3,4,5}
    fmt.Println("3 frames:", fifo(refs, 3), "faults")  // 9
    fmt.Println("4 frames:", fifo(refs, 4), "faults")  // 10 (Belady!)
}`,
          python: `from collections import deque

def fifo(refs, frames):
    in_mem = set()
    order = deque()
    faults = 0
    for p in refs:
        if p in in_mem:
            continue
        faults += 1
        if len(in_mem) == frames:
            victim = order.popleft()
            in_mem.discard(victim)
        in_mem.add(p)
        order.append(p)
    return faults

refs = [1,2,3,4,1,2,5,1,2,3,4,5]
print("3 frames:", fifo(refs, 3), "faults")   # 9
print("4 frames:", fifo(refs, 4), "faults")   # 10 (Belady!)`,
          java: `import java.util.*;

public class FIFOReplace {
    static int fifo(int[] refs, int frames) {
        Set<Integer> inMem = new HashSet<>();
        Queue<Integer> order = new LinkedList<>();
        int faults = 0;
        for (int p : refs) {
            if (inMem.contains(p)) continue;
            faults++;
            if (inMem.size() == frames) {
                int victim = order.poll();
                inMem.remove(victim);
            }
            inMem.add(p);
            order.add(p);
        }
        return faults;
    }
    public static void main(String[] args) {
        int[] refs = {1,2,3,4,1,2,5,1,2,3,4,5};
        System.out.println("3 frames: " + fifo(refs, 3) + " faults");
        System.out.println("4 frames: " + fifo(refs, 4) + " faults");
    }
}`,
        },
      },

      { type: "h3", title: "2. Optimal Algorithm (MIN, OPT, বা Belady's)" },
      {
        type: "p",
        text: "যে page টি ভবিষ্যতে সবচেয়ে দীর্ঘ সময় ধরে use হবে না সেটিকে evict করো। এটি page faults minimise করার জন্য provably optimal। Advantage — best possible performance (lower bound)। Disadvantage — practice-এ implement করা impossible — ভবিষ্যৎ জানা দরকার। শুধু অন্যান্য algorithms-এর সাথে compare করার জন্য benchmark হিসেবে use হয়।",
      },

      { type: "h3", title: "3. LRU (Least Recently Used)" },
      {
        type: "p",
        text: "যে page টি সবচেয়ে বেশি সময় ধরে use হয়নি সেটিকে evict করো (past behaviour-এর উপর ভিত্তি করে)। এটি OPT-কে approximate করে এই assumption দিয়ে যে সাম্প্রতিক use হওয়া pages শীঘ্রই আবার use হবে (temporal locality)।",
      },
      { type: "h3", title: "LRU implementation approaches" },
      {
        type: "list",
        items: [
          "Counters — প্রতিটি page table entry-তে একটি last-use time field থাকে; প্রতিটি memory access-এ, time update করা হয়। Eviction-এর সময় smallest time খোঁজা হয়। Expensive।",
          "Stack — page references-এর একটি stack maintain করা হয়; accessed page-কে top-এ move করা হয়। Bottom page-টি LRU। Fast updates-এর জন্য hardware support প্রয়োজন।",
        ],
      },
      {
        type: "p",
        text: "LRU তে Belady's anomaly হয় না; এটি একটি stack algorithm। এটি একটি strong theoretical property — যেহেতু LRU-র সবগুলো কার্যকরী instance একটি stack structure মেনে চলে, frames বাড়ালে কখনো faults বাড়ে না।",
      },
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
    list<int> cache;   // front = LRU
    unordered_map<int, list<int>::iterator> pos;
    int faults = 0;
    for (int p : refs) {
        if (pos.count(p)) {
            cache.erase(pos[p]);
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
    cout << lru({7,0,1,2,0,3,0,4,2,3,0,3,2}, 3) << '\\n';  // 7 (no Belady)
    return 0;
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
    cache = OrderedDict()  # tail = MRU
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
        // tail = MRU; access-order mode
        LinkedHashMap<Integer, Boolean> cache =
            new LinkedHashMap<>(16, 0.75f, true);
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

      { type: "h3", title: "4. Clock (Second-Chance) Algorithm" },
      {
        type: "p",
        text: "LRU-র একটি practical approximation যেটি প্রতিটি page-এর জন্য একটি reference bit (accessed bit) use করে। Pages গুলো একটি circular list-এ arrange করা থাকে; একটি hand pointer ঘুরতে থাকে। যদি page-এর reference bit = 1 হয়, clear করো (second chance দাও) এবং hand move করো। যদি reference bit = 0 হয়, সেই page-টি evict করো।",
      },
      { type: "h3", title: "Enhanced Clock (NUR — Not Used Recently)" },
      {
        type: "p",
        text: "Reference bit ও dirty bit উভয় use করো। Disk-এ লেখা এড়াতে clean (not dirty) pages-কে evict করা prefer করো। চারটি class তৈরি হয় — (ref=0, dirty=0) সবচেয়ে ভালো victim; (ref=0, dirty=1); (ref=1, dirty=0); (ref=1, dirty=1) সবচেয়ে খারাপ।",
      },
      {
        type: "multi-code",
        filename: "clock_algo",
        codeSamples: {
          cpp: `#include <iostream>
#include <vector>
using namespace std;

int clock(const vector<int>& refs, int frames) {
    vector<int> mem(frames, -1);          // pages in memory
    vector<bool> ref(frames, false);      // reference bits
    int hand = 0, faults = 0, count = 0;
    for (int p : refs) {
        // check if p is in memory
        bool hit = false;
        for (int i = 0; i < count; i++) if (mem[i] == p) {
            ref[i] = true; hit = true; break;
        }
        if (hit) continue;
        faults++;
        if (count < frames) {
            mem[count] = p; ref[count] = true; count++;
            continue;
        }
        // find victim using clock hand
        while (ref[hand]) {
            ref[hand] = false;
            hand = (hand + 1) % frames;
        }
        mem[hand] = p; ref[hand] = true;
        hand = (hand + 1) % frames;
    }
    return faults;
}

int main() {
    cout << clock({7,0,1,2,0,3,0,4,2,3,0,3,2}, 3) << '\\n';  // ~8-10
}`,
          go: `package main

func clockAlgo(refs []int, frames int) int {
    mem := make([]int, frames)
    for i := range mem { mem[i] = -1 }
    ref := make([]bool, frames)
    hand, faults, count := 0, 0, 0

    for _, p := range refs {
        hit := false
        for i := 0; i < count; i++ {
            if mem[i] == p { ref[i] = true; hit = true; break }
        }
        if hit { continue }
        faults++
        if count < frames {
            mem[count] = p; ref[count] = true; count++
            continue
        }
        for ref[hand] {
            ref[hand] = false
            hand = (hand + 1) % frames
        }
        mem[hand] = p; ref[hand] = true
        hand = (hand + 1) % frames
    }
    return faults
}

func main() {
    println(clockAlgo([]int{7,0,1,2,0,3,0,4,2,3,0,3,2}, 3))
}`,
          python: `def clock_algo(refs, frames):
    mem = [-1] * frames    # pages in memory
    ref = [False] * frames  # reference bits
    hand = 0
    faults = 0
    count = 0
    for p in refs:
        # check if p is in memory
        hit = any(mem[i] == p for i in range(count))
        if hit:
            for i in range(count):
                if mem[i] == p:
                    ref[i] = True
                    break
            continue
        faults += 1
        if count < frames:
            mem[count] = p
            ref[count] = True
            count += 1
            continue
        # find victim using clock hand
        while ref[hand]:
            ref[hand] = False
            hand = (hand + 1) % frames
        mem[hand] = p
        ref[hand] = True
        hand = (hand + 1) % frames
    return faults

print(clock_algo([7,0,1,2,0,3,0,4,2,3,0,3,2], 3))`,
          java: `public class ClockAlgo {
    static int clock(int[] refs, int frames) {
        int[] mem = new int[frames];
        boolean[] ref = new boolean[frames];
        for (int i = 0; i < frames; i++) mem[i] = -1;
        int hand = 0, faults = 0, count = 0;
        for (int p : refs) {
            boolean hit = false;
            for (int i = 0; i < count; i++) {
                if (mem[i] == p) { ref[i] = true; hit = true; break; }
            }
            if (hit) continue;
            faults++;
            if (count < frames) {
                mem[count] = p; ref[count] = true; count++;
                continue;
            }
            while (ref[hand]) {
                ref[hand] = false;
                hand = (hand + 1) % frames;
            }
            mem[hand] = p; ref[hand] = true;
            hand = (hand + 1) % frames;
        }
        return faults;
    }
    public static void main(String[] args) {
        System.out.println(clock(new int[]{7,0,1,2,0,3,0,4,2,3,0,3,2}, 3));
    }
}`,
        },
      },

      { type: "h3", title: "5. LFU (Least Frequently Used) ও MFU (Most Frequently Used)" },
      {
        type: "list",
        items: [
          "LFU — smallest access count যুক্ত page কে evict করে। Assumes যে pages অনেক বার use হয়েছে সেগুলো আবার use হবে।",
          "MFU — largest access count যুক্ত page কে evict করে। Assumes যে pages-এ count বেশি সেগুলো already cached এবং শীঘ্রই দরকার হবে না।",
        ],
      },
      {
        type: "p",
        text: "উভয়ই implementation overhead-এ ভোগে (counters বড় হতে পারে)। এছাড়া LFU সেই pages-কে retain করতে পারে যেগুলো early-তে heavily use হয়েছিল কিন্তু আর কখনো না (no aging)। একটি modified version (LFU with aging) সময়ের সাথে counters decay করে।",
      },

      { type: "h3", title: "Algorithms-এর Comparison" },
      {
        type: "list",
        items: [
          "FIFO — implementation complexity very low, performance poor (Belady anomaly), শুধু very simple systems-এ use।",
          "Optimal — implementation not feasible, performance best (theoretical), শুধু benchmark হিসেবে।",
          "LRU — implementation high (hardware বা costly), performance very good, practice-এ use হয় যদি hardware support থাকে।",
          "Clock — implementation low (reference bit সহ software), performance good (LRU-র কাছাকাছি), বেশির ভাগ OSes-এ most common।",
          "LFU — implementation medium, performance fair (obsolete pages cache হতে পারে), rare use।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — FIFO হলো একটি ticket counter-এর queue; যিনি প্রথমে এসেছিলেন তাকে আগে serve করা হয়, এমনকি তিনি জটিল ticket কিনছেন। LRU হলো একটি bookshelf যেখানে আপনি পড়া books গুলো left-এ রাখেন; rightmost book-টি সবচেয়ে বেশি সময় ধরে untouched। Clock হলো একজন security guard যে একটি building এ ঘুরে বেড়ায়, প্রতিটি room-এর 'recently used' light check করে; যদি light অন থাকে, সে সেটা off করে এগিয়ে যায়; যদি off থাকে, সে room টি evict করে।",
      },

      { type: "h2", id: "thrashing", title: "Thrashing ও Working Set Model" },
      {
        type: "p",
        text: "Thrashing তখন হয় যখন একটি process executing এর চেয়ে বেশি সময় page faulting করে। Disk bottleneck হয়ে যায়; CPU utilisation dramatically drop করে।",
      },
      { type: "h3", title: "Cause" },
      {
        type: "p",
        text: "Process-এর কাছে তার locality hold করার জন্য যথেষ্ট physical frames নেই — locality হলো সেই pages গুলো যেগুলো সে actively use করে। OS বারবার সেই pages-কে evict করে যেগুলো শীঘ্রই আবার দরকার হবে।",
      },
      { type: "h3", title: "Working Set Model (Denning, 1968)" },
      {
        type: "p",
        text: "Time t-তে একটি process-এর working set হলো গত Δ references (বা time interval)-এ referenced pages গুলোর set। যদি একটি process-এর working set size available frames-এর চেয়ে বেশি হয়, thrashing হয়।",
      },
      { type: "h3", title: "Thrashing prevent করার strategies" },
      {
        type: "list",
        items: [
          "Working set algorithm — প্রতিটি process-এর working set track করো; শুধু তখনই একটি process-কে run allow করো যদি তার working set memory-তে fit করে।",
          "Page Fault Frequency (PFF) — allowed page fault rates-এ upper ও lower bounds set করো। যদি একটি process খুব বেশি fault করে, তাকে আরও frames দাও; যদি fault rate খুব কম হয়, frames কেড়ে নাও।",
          "Suspend a process — যদি working sets-এর যোগফল total memory-কে exceed করে, একটি process-কে entirely swap out করো।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একজন chef যার কাছে শুধু 2 sq ft counter space আছে, একটি 10-ingredient dish prepare করার চেষ্টা করছে। সে সারাক্ষণ pots কে stove-এ ঢুকায় আর নামায় (thrashing) আর খুব কম রান্না হয়। Solution — তাকে আরও counter space (frames) দাও অথবা recipe (working set) কমাও।",
      },

      { type: "h2", id: "page-size", title: "Page Size Selection" },
      {
        type: "p",
        text: "Page size choose করায় trade-offs আছে। বেশির ভাগ system 4 KB, 8 KB, বা 16 KB pages use করে (অথবা বড়, যেমন 2 MB huge pages)।",
      },
      { type: "h3", title: "Small vs Large pages" },
      {
        type: "list",
        items: [
          "Internal fragmentation — small pages: কম (page boundary-তে waste); large pages: বেশি (process-এর শেষ page)।",
          "Page table size — small pages: বড় (বেশি entries); large pages: ছোট।",
          "I/O overhead — small pages: বেশি transfers; large pages: কম, বড় transfers।",
          "Locality — small pages: ভালো (rarely used parts-এ waste কম); large pages: খারাপ (extra unused data আনে)।",
          "TLB coverage — small pages: কম (fixed TLB entries); large pages: বেশি (প্রতিটি entry বেশি memory map করে)।",
        ],
      },
      {
        type: "p",
        text: "Modern OSes multiple page sizes support করে (superpages, huge pages) যাতে applications (যেমন databases, VMs) ভালো TLB performance-এর জন্য বড় pages request করতে পারে।",
      },

      { type: "h2", id: "tlb-reach", title: "TLB Reach ও Coverage" },
      {
        type: "p",
        text: "TLB reach = (number of TLB entries) × (page size)। এটি হলো সেই memory-র পরিমাণ যেটা TLB একসাথে map করতে পারে। যদি একটি program-এর active working set TLB reach-এর মধ্যে fit করে, TLB misses rare।",
      },
      {
        type: "p",
        text: "উদাহরণ — 64 TLB entries × 4 KB page = 256 KB TLB reach। একটি database যার 10 MB working set, TLB-কে thrash করবে।",
      },
      { type: "h3", title: "Solutions" },
      {
        type: "list",
        items: [
          "Page size বাড়াও (যেমন 2 MB huge pages → 64 entries × 2 MB = 128 MB reach)।",
          "TLB size বাড়াও (বেশি entries, hardware-এ expensive)।",
          "Multiple TLB levels use করো (L1 ও L2 TLBs)।",
        ],
      },
      {
        type: "p",
        text: "TLB coverage বলতে memory accesses-এর সেই অনুপাতকে বোঝায় যেগুলো page table walk ছাড়া handle হয়। High coverage performance improve করে।",
      },

      { type: "h2", id: "mmap", title: "Memory-Mapped Files" },
      {
        type: "p",
        text: "Memory-mapped files disk-এর একটি file-কে একটি process-এর virtual address space-এ directly map করতে allow করে। সেই memory region-এ reads ও writes automatically file-এ reflect হয় (page caching সহ)।",
      },
      { type: "h3", title: "How it works" },
      {
        type: "list",
        items: [
          "১. OS mapped range-এর জন্য page table entries set up করে।",
          "২. Initially, সব pages invalid (বা demand-paged) হিসেবে mark করা।",
          "৩. যখন process একটি page access করে, একটি page fault হয়।",
          "৪. OS corresponding file block-কে disk থেকে একটি physical frame-এ read করে।",
          "৫. যদি page modify করা হয় (dirty), OS সেটি file-এ write back করে যখন page evict হয় বা file unmap হয়।",
        ],
      },
      { type: "h3", title: "System calls" },
      {
        type: "list",
        items: [
          "mmap() (Unix)।",
          "CreateFileMapping() + MapViewOfFile() (Windows)।",
        ],
      },
      { type: "h3", title: "Advantages" },
      {
        type: "list",
        items: [
          "File I/O simplify করে — file কে memory হিসেবে treat করো (কোনো explicit read বা write calls নেই)।",
          "Efficient sharing — একাধিক processes একই file map করতে পারে এবং pages share করতে পারে।",
          "OS automatically caching ও I/O handle করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি office-এ একটি shared whiteboard। প্রত্যেকে (process) একই board content (file) দেখে। যখন কেউ তাতে লেখে (memory write), সবাই change দেখে যখন তাকিয়ে দেখে। Cleaner (OS) সেই board কে periodically একটি photo (disk)-এ save করে।",
      },
      {
        type: "multi-code",
        filename: "mmap_demo",
        codeSamples: {
          cpp: `#include <fcntl.h>
#include <iostream>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    int fd = open("hello.txt", O_RDWR | O_CREAT, 0644);
    write(fd, "hello, mmap!", 12);

    // map the file into memory
    char* mapped = (char*) mmap(nullptr, 12,
        PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    if (mapped == MAP_FAILED) { perror("mmap"); return 1; }

    // read by accessing memory
    std::cout << "byte 0 = " << mapped[0] << '\\n';

    // write by modifying memory
    mapped[7] = 'M';   // changes file on disk

    munmap(mapped, 12);
    close(fd);
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os"
    "syscall"
    "unsafe"
)

func main() {
    f, _ := os.OpenFile("hello.txt",
        os.O_RDWR|os.O_CREATE, 0644)
    defer f.Close()
    f.Write([]byte("hello, mmap!"))

    // map the file into memory
    data, err := syscall.Mmap(int(f.Fd()), 0, 12,
        syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
    if err != nil { fmt.Println("err:", err); return }
    defer syscall.Munmap(data)

    fmt.Printf("byte 0 = %c\\n", data[0])
    data[7] = 'M'   // changes file on disk
}`,
          python: `import mmap
import os

# create or open file
with open("hello.txt", "w+b") as f:
    f.write(b"hello, mmap!")
    f.flush()
    # map the file into memory
    mm = mmap.mmap(f.fileno(), 0)
    print(f"byte 0 = {chr(mm[0])}")
    mm[7] = ord('M')   # changes file on disk
    mm.close()`,
          java: `import java.nio.*;
import java.nio.channels.*;
import java.nio.file.*;

public class MmapDemo {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("hello.txt");
        Files.writeString(p, "hello, mmap!");

        try (FileChannel fc = FileChannel.open(p,
                StandardOpenOption.READ, StandardOpenOption.WRITE)) {
            MappedByteBuffer mb = fc.map(
                FileChannel.MapMode.READ_WRITE, 0, 12);
            System.out.println("byte 0 = " + (char) mb.get(0));
            mb.put(7, (byte) 'M');   // changes file on disk
        }
    }
}`,
        },
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Demand paging — শুধু তখনই pages load করো যখন access হয়; memory usage reduce করে।",
          "Page fault — invalid page access করার সময় trap; OS page-কে memory-তে আনে।",
          "Copy-on-write — fork() করা processes-এর মধ্যে pages share করো যতক্ষণ না write হয়।",
          "Page replacement — FIFO (simple, Belady anomaly), Optimal (unimplementable), LRU (good কিন্তু costly), Clock (practical), LFU/MFU (rare)।",
          "Thrashing — working set-এর জন্য অপর্যাপ্ত frames-এর কারণে অতিরিক্ত paging।",
          "Working set model — একটি process-এর active pages; thrashing তখন হয় যখন working set > available frames।",
          "Page size trade-off — small pages: কম fragmentation, বড় page tables; large pages: ভালো TLB reach, বেশি internal waste।",
          "TLB reach — entries × page size; ভালো performance-এর জন্য working set cover করতে হবে।",
          "Memory-mapped files — file কে address space-এ map করো; I/O page faults-এ automatically হয়।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Virtual memory memory management-এর চিত্র সম্পূর্ণ করে। পরের chapter I/O ও file systems-এ যায়, যেখানে এই principles গুলো storage devices-এ apply হয়।",
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
    est: "2 hr",
    summary:
      "File system হলো OS component যেটা manage করে data persistent storage devices-এ (disks, SSDs) কীভাবে store, organize, ও retrieve হবে। এই chapter-এ file concepts, directory structures, allocation methods, free space management, disk scheduling, ও real-world file system designs cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "file-concept", title: "File Concept" },
      {
        type: "p",
        text: "File হলো সম্পর্কিত information-এর একটি named collection যেটা secondary storage device-এ store থাকে। এটি হলো storage-এর logical unit, যেটা disk-এর physical details hide করে।",
      },
      { type: "h3", title: "File Attributes" },
      {
        type: "list",
        items: [
          "Name — human-readable identifier (যেমন report.txt)।",
          "Identifier — unique number (inode number) যেটা OS internally use করে।",
          "Type — format indicate করে (যেমন .c, .pdf, executable)।",
          "Location — pointer যেটা বলে file টি disk-এর কোথায় store আছে।",
          "Size — বর্তমান size in bytes (এবং possibly maximum)।",
          "Protection — access permissions (read, write, execute owner/group/others-এর জন্য)।",
          "Timestamps — creation, last modification, last access times।",
          "User ID / Owner — কোন user file টি own করে।",
        ],
      },
      { type: "h3", title: "File Operations" },
      {
        type: "list",
        items: [
          "create — একটি নতুন file তৈরি করো (space allocate করো, directory entry যোগ করো)।",
          "open — file কে use-এর জন্য prepare করো — একটি file descriptor return করে।",
          "read — file থেকে memory-তে bytes transfer করো।",
          "write — memory থেকে file-এ bytes transfer করো।",
          "seek — file pointer move করো (random access)।",
          "close — buffers flush করো, resources release করো।",
          "delete — file কে disk ও directory থেকে remove করো।",
          "truncate — existing content discard করো, file keep করো।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি file হলো filing cabinet-এর ভেতরের একটি physical document। এর attributes হলো — document title (name), drawer number (location), তার size, এবং কে এটি read করতে পারবে (protection)।",
      },
      {
        type: "multi-code",
        filename: "file_ops",
        codeSamples: {
          cpp: `#include <fcntl.h>
#include <iostream>
#include <unistd.h>

int main() {
    // create & write
    int fd = open("hello.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    write(fd, "hello, fs!\\n", 12);
    close(fd);

    // read back
    fd = open("hello.txt", O_RDONLY);
    char buf[64];
    int n = read(fd, buf, sizeof(buf) - 1);
    buf[n] = '\\0';
    std::cout << "Read: " << buf;
    close(fd);
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os"
)

func main() {
    // create & write
    err := os.WriteFile("hello.txt",
        []byte("hello, fs!\\n"), 0644)
    if err != nil { panic(err) }

    // read back
    data, err := os.ReadFile("hello.txt")
    if err != nil { panic(err) }
    fmt.Printf("Read: %s", data)
}`,
          python: `# create & write
with open("hello.txt", "w") as f:
    f.write("hello, fs!\\n")

# read back
with open("hello.txt", "r") as f:
    print("Read:", f.read(), end="")`,
          java: `import java.nio.file.*;

public class FileOps {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("hello.txt");
        // create & write
        Files.writeString(p, "hello, fs!\\n");
        // read back
        System.out.print("Read: " + Files.readString(p));
    }
}`,
        },
      },

      { type: "h2", id: "directory", title: "Directory Structure" },
      {
        type: "p",
        text: "Directory হলো একটি container যেটা file names ও তাদের associated metadata (বা metadata-তে pointers) store করে। Directories files কে hierarchically organize করে।",
      },
      { type: "h3", title: "Single-Level Directory" },
      {
        type: "p",
        text: "সব files একটি directory-তে। Simple কিন্তু name collisions ও multiuser systems-এ poor organization-এ ভোগে। উদাহরণ: MS-DOS floppy disks (শুধু root)।",
      },
      { type: "h3", title: "Two-Level Directory" },
      {
        type: "p",
        text: "Per user আলাদা directory — master file directory (MFD) user directories ধারণ করে, প্রতিটি user-এর নিজস্ব user file directory (UFD) আছে। বিভিন্ন users-এর একই নামের files থাকতে পারে।",
      },
      { type: "h3", title: "Tree-Structured Directory" },
      {
        type: "p",
        text: "একটি general hierarchy — directories-এ subdirectories থাকতে পারে। Users unlimited nesting create করতে পারে। Current working directory pathnames-কে simplify করে।",
      },
      {
        type: "list",
        items: [
          "Absolute path — root থেকে (যেমন /home/user/file.txt)।",
          "Relative path — current directory থেকে (যেমন ./file.txt)।",
        ],
      },
      { type: "h3", title: "Acyclic-Graph Directory" },
      {
        type: "p",
        text: "Links (shortcuts, aliases) এর মাধ্যমে files বা subdirectories share করতে allow করে। দুটি প্রকার — Hard link (multiple directory entries একই file-কে point করে — একই inode; file systems cross করতে পারে না)। Soft link (symbolic link — একটি special file যেটা target-এর path ধারণ করে; file systems cross করতে পারে)। Problem — file delete করা জটিল হয় (reference counts প্রয়োজন)।",
      },
      { type: "h3", title: "General Graph Directory" },
      {
        type: "p",
        text: "Cycles allow করে (directory এমন একটি subdirectory ধারণ করে যেটা তার parent-এ link করে)। Directories traverse করায় সমস্যা হয় (infinite loops)। Solutions — garbage collection, references সহ files remove করতে অস্বীকার করা, বা cycles disallow করা।",
      },
      {
        type: "p",
        text: "Real-life thinking — Single-level হলো একটি বড় drawer যার ভেতরে সব files। Tree-structured হলো একটি filing cabinet folders ও subfolders সহ। Acyclic graph হলো একাধিক folder labels যেগুলো একই physical file-কে point করে (যেমন একটি box-এর উপর sticky notes)।",
      },

      { type: "h2", id: "mounting", title: "File System Mounting" },
      {
        type: "p",
        text: "Mounting হলো একটি file system-কে (disk partition, USB drive, CD-ROM থেকে) main file system tree-এর একটি existing directory path-এ attach করা। Directory যেখানে attach করা হয় সেটি mount point।",
      },
      { type: "h3", title: "Mounting-এর ধাপ" },
      {
        type: "list",
        items: [
          "১. OS check করে device-এ একটি valid file system আছে কিনা (superblock)।",
          "২. OS mount point-কে একটি mount table-এ record করে।",
          "৩. Mount point path-এ access mounted file system-এর root-এ redirect হয়।",
        ],
      },
      {
        type: "p",
        text: "উদাহরণ (Unix): mount /dev/sdb1 /mnt/usb। Real-life thinking — একটি bookshelf (main file system) যাতে empty slots (mount points) আছে। আপনি একটি labelled binder (USB drive থেকে file system) একটি slot-এ রাখেন। যখন আপনি সেই slot-এ তাকান, আপনি binder-এর contents দেখেন।",
      },

      { type: "h2", id: "allocation", title: "File Allocation Methods" },
      {
        type: "p",
        text: "OS কীভাবে disk blocks-কে files-এ allocate করবে সেটা decide করতে হয়। তিনটি classic method আছে।",
      },

      { type: "h3", title: "1. Contiguous Allocation" },
      {
        type: "p",
        text: "প্রতিটি file disk-এ contiguous blocks-এর একটি set occupy করে। Directory entry start block ও length store করে। Pros — simple, fast sequential ও random access (শুধু একটি seek)। Cons — external fragmentation (holes); file growth difficult (pre-allocate বা move করতে হয়)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি cinema যেখানে reserved seats আছে — সব seats একটি row-তে। যদি আরও seats দরকার হয়, অন্য row-তে move করতে হয়।",
      },

      { type: "h3", title: "2. Linked Allocation" },
      {
        type: "p",
        text: "প্রতিটি file হলো disk blocks-এর একটি linked list। Directory entry first block pointer store করে। প্রতিটি block পরবর্তী block-এর pointer ধারণ করে (বা একটি file allocation table)। Pros — কোনো external fragmentation নেই; file সহজে grow করতে পারে। Cons — poor random access (pointers traverse করতে হয়); reliability issue (একটি lost pointer বাকিগুলো নষ্ট করে দেয়)।",
      },
      { type: "h3", title: "File Allocation Table (FAT)" },
      {
        type: "p",
        text: "একটি separate table (partition-এর শুরুতে) সব blocks-এর pointers ধারণ করে। Directory entry first block number store করে। প্রতিটি block-এর FAT entry পরবর্তীতে point করে। Random access-এ এখনও chain follow করতে হয় (কিন্তু memory-তে cache করা যায়)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি treasure hunt যেখানে প্রতিটি clue (block) বলে পরবর্তী clue কোথায়। ৫০তম clue খুঁজতে ৪৯টি পূর্ববর্তী clue follow করতে হয়।",
      },

      { type: "h3", title: "3. Indexed Allocation" },
      {
        type: "p",
        text: "প্রতিটি file-এর নিজস্ব index block আছে — সব file-এর data blocks-এর pointers-এর একটি array। Directory entry index block-কে point করে। Pros — direct random access (index block lookup, তারপর data block)। কোনো external fragmentation নেই। Cons — index block-এর overhead; ছোট files space waste করে যদি index block fixed size হয় (যেমন 512 entries)।",
      },
      { type: "h3", title: "Unix inode extensions" },
      {
        type: "list",
        items: [
          "Direct pointers (10-12 pointers)।",
          "Single indirect pointer (একটি block of pointers-কে point করে)।",
          "Double indirect pointer (একটি block of single indirect blocks-কে point করে)।",
          "Triple indirect pointer (খুব বড় files-এর জন্য)।",
        ],
      },
      {
        type: "p",
        text: "এই scheme বিশাল files support করে ছোট files-এর জন্য minimal overhead সহ। Real-life thinking — একটি library card catalogue। Card (index block) বলে প্রতিটি chapter (data block) library-তে কোথায় আছে।",
      },

      { type: "h2", id: "free-space", title: "Free Space Management" },
      {
        type: "p",
        text: "OS কোন disk blocks গুলো free সেটা track করতে হয় এবং দরকার হলে allocate করতে হয়।",
      },
      { type: "h3", title: "Bit Vector (Bitmap)" },
      {
        type: "p",
        text: "প্রতিটি block-এ একটি bit (1 = free, 0 = allocated)। Bit vector moderate-sized disks-এর জন্য memory-তে fit করে (যেমন 1 TB 4 KB blocks সহ: 1 TB / 4 KB = 2²⁸ blocks → 256 MB bitmap — বড় কিন্তু manageable)। Free block খুঁজতে একটি 1-bit-এর জন্য scan করা হয়।",
      },
      { type: "h3", title: "Linked List" },
      {
        type: "p",
        text: "Free blocks একসাথে linked করা থাকে। First free block pointer store করা হয়। প্রতিটি free block পরবর্তী free block-এর pointer ধারণ করে। Pros — simple, কোনো extra space নেই (প্রতিটি free block-এ শুধু pointer)। Cons — list traverse করতে blocks read করতে হয় (disk I/O)। Allocate করতে একটি block read করতে হয়।",
      },
      { type: "h3", title: "Grouping" },
      {
        type: "p",
        text: "অনেক free blocks-এর addresses একটি block-এ store করা হয়। শেষ free block পরবর্তী group-এ point করে। Traversal reads reduce করে।",
      },
      { type: "h3", title: "Counting" },
      {
        type: "p",
        text: "Free blocks প্রায়ই contiguous runs-এ appear হয় (বিশেষত file deletion-এর পর)। First free block ও contiguous free blocks count-এর addresses record করা হয়। (address, count) pairs-এর list compact হয়।",
      },

      { type: "h2", id: "disk-scheduling", title: "Disk Scheduling" },
      {
        type: "p",
        text: "OS (বা disk driver) read/write requests কে order করে seek time minimise এবং throughput improve করতে।",
      },
      { type: "h3", title: "Common Algorithms" },
      {
        type: "list",
        items: [
          "FCFS — First-come, first-served। Fair, simple। Poor performance (wild seeks)।",
          "SSTF — Shortest seek time first। Better throughput। May starve far-away requests।",
          "SCAN (elevator) — arm এক end থেকে অন্য end-এ move করে, requests service করে। Fair, কোনো starvation নেই। End-এর requests গুলো বেশি wait করে।",
          "C-SCAN — Circular SCAN — শুধু এক direction, তারপর jump back। Uniform waiting time। Extra jump time (jump-এ কোনো I/O নেই)।",
          "LOOK — SCAN-এর মতো কিন্তু শেষ request-এ stop করে (end-এ যায় না)। Less wasted motion। Still biased।",
          "C-LOOK — C-SCAN-এর মতো কিন্তু শেষ request-এ stop করে। Both-এর best। Slightly বেশি complex।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — FCFS হলো একটি elevator যে মানুষের button press order অনুযায়ী service করে (up ও down করে wild ভাবে)। SCAN হলো একটি lift যে bottom থেকে top-এ যায়, তারপর top থেকে bottom-এ, pending requests-এর floors-এ stop করে। LOOK একই কিন্তু top floor-এ যায় না যদি কেউ সেটা request না করে।",
      },
      {
        type: "multi-code",
        filename: "disk_scheduling",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// SCAN (elevator) — service requests moving towards high end,
// then reverse.
int scan(int head, vector<int> reqs) {
    sort(reqs.begin(), reqs.end());
    int total = 0;
    auto it = lower_bound(reqs.begin(), reqs.end(), head);
    // move towards high end
    for (auto p = it; p != reqs.end(); ++p) {
        total += *p - head;
        head = *p;
    }
    // reverse direction
    for (auto p = it - 1; p >= reqs.begin(); --p) {
        total += head - *p;
        head = *p;
    }
    return total;
}

int main() {
    cout << scan(53, {98, 183, 37, 122, 14, 124, 65, 67})
         << " cylinders moved\\n";
}`,
          go: `package main

import "sort"

func scan(head int, reqs []int) int {
    sort.Ints(reqs)
    total := 0
    i := 0
    for i < len(reqs) && reqs[i] < head { i++ }
    // move towards high end
    for ; i < len(reqs); i++ {
        total += reqs[i] - head
        head = reqs[i]
    }
    // reverse direction
    for i--; i >= 0; i-- {
        total += head - reqs[i]
        head = reqs[i]
    }
    return total
}

func main() {
    println(scan(53, []int{98, 183, 37, 122, 14, 124, 65, 67}))
}`,
          python: `def scan(head, reqs):
    reqs = sorted(reqs)
    total = 0
    # split into higher and lower halves
    higher = [r for r in reqs if r >= head]
    lower  = [r for r in reqs if r <  head][::-1]
    # move towards high end first
    for r in higher:
        total += r - head
        head = r
    # then reverse direction
    for r in lower:
        total += head - r
        head = r
    return total

print(scan(53, [98, 183, 37, 122, 14, 124, 65, 67]))`,
          java: `import java.util.*;

public class DiskSched {
    static int scan(int head, int[] reqs) {
        Arrays.sort(reqs);
        int total = 0;
        int i = 0;
        while (i < reqs.length && reqs[i] < head) i++;
        // towards high end
        for (; i < reqs.length; i++) {
            total += reqs[i] - head;
            head = reqs[i];
        }
        // reverse direction
        for (i--; i >= 0; i--) {
            total += head - reqs[i];
            head = reqs[i];
        }
        return total;
    }
    public static void main(String[] args) {
        System.out.println(scan(53,
            new int[]{98, 183, 37, 122, 14, 124, 65, 67}));
    }
}`,
        },
      },

      { type: "h2", id: "fs-layout", title: "File System Layout" },
      {
        type: "p",
        text: "একটি typical Unix-like file system disk-এ blocks-এ ভাগ করা থাকে। Common structure:",
      },
      {
        type: "list",
        items: [
          "Block 0 — Boot block — bootstrap loader (OS boot করার code) ধারণ করে।",
          "Block 1 — Superblock — file system metadata: block size, number of blocks, free block count, inode table size, magic number।",
          "Blocks 2..N — Inode table — inodes-এর array, প্রতিটি একটি file বর্ণনা করে (metadata + pointers)।",
          "Rest — Data blocks — actual file content ও directory entries।",
        ],
      },
      { type: "h3", title: "Additional structures" },
      {
        type: "list",
        items: [
          "Block bitmap বা inode bitmap — free space tracking-এর জন্য (প্রায়ই superblock-এর পরে place করা হয়)।",
          "Journal বা log area — journaling file systems-এর জন্য।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি warehouse (disk) যার entrance-এ একটি map (superblock), একটি catalogue (inode table) প্রতিটি box-এর details দেয়, এবং shelves (data blocks) যেখানে boxes store করা থাকে।",
      },

      { type: "h2", id: "journaling-lfs", title: "Journaling ও Log-Structured File Systems" },
      { type: "h3", title: "Journaling (Write-ahead logging)" },
      {
        type: "p",
        text: "File system structures modify করার আগে, OS intended changes-এর একটি journal (log) write করে। Journal safely disk-এ থাকার পর, actual changes করা হয়। Crash হলে, OS journal replay করে consistency restore করে।",
      },
      { type: "h3", title: "Journaling levels" },
      {
        type: "list",
        items: [
          "Writeback — শুধু metadata, data inconsistent হতে পারে।",
          "Ordered — metadata journaled; data journal commit-এর আগে written।",
          "Data — full data journaling — safe কিন্তু slow।",
        ],
      },
      {
        type: "p",
        text: "Examples: ext3, ext4 (ordered), NTFS (metadata journaling), XFS। Real-life thinking — একজন pilot-এর checklist — takeoff-এর আগে, আপনি একটি log-এ 'flaps up' লেখেন (journal), তারপর সেটা করেন। Interrupt হলে, log থেকে resume করতে পারবেন।",
      },
      { type: "h3", title: "Log-Structured File System (LFS)" },
      {
        type: "p",
        text: "Files in-place overwrite করার বদলে, LFS সব changes sequentially একটি circular log-এর শেষে write করে (একটি tape-এর মতো)। File system index (inode map) ও periodically written হয়। Old blocks garbage-collected হয়।",
      },
      {
        type: "list",
        items: [
          "Pros — excellent write performance (sequential writes), fast crash recovery।",
          "Cons — read-এ log scan করতে হয়; garbage collection overhead।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একজন journalist-এর notebook — প্রতিটি নতুন fact শেষে লেখা হয়, কখনো erase করা হয় না। Back-এ একটি index প্রতিটি topic-এর latest version-এ point করে।",
      },

      { type: "h2", id: "examples", title: "File System Examples" },
      { type: "h3", title: "FAT32 (File Allocation Table)" },
      {
        type: "list",
        items: [
          "Origins — MS-DOS, Windows 95/98, এখনও USB drives-এ used।",
          "Structure — boot sector, FAT table (two copies), root directory (fixed location), data area।",
          "Limitations — max file size 4 GB, max volume 8 TB (practical 2 TB)। কোনো permissions নেই, কোনো journaling নেই।",
          "Advantage — simple, widely compatible।",
        ],
      },
      { type: "h3", title: "NTFS (New Technology File System)" },
      {
        type: "list",
        items: [
          "Windows default — NT 3.1 থেকে।",
          "Features — journaling ($LogFile), security (ACLs), compression, encryption (EFS), file-size limit 16 EB, hard links, reparse points (symlinks, mount points)।",
          "Structure — Master File Table (MFT) — প্রতিটি file-এর এক বা একাধিক MFT records আছে; ছোট files সরাসরি MFT-তে store হয় ('resident')।",
          "Performance — large volumes-এর জন্য ভালো; disk quotas support করে।",
        ],
      },
      { type: "h3", title: "ext4 (Fourth Extended File System)" },
      {
        type: "list",
        items: [
          "Linux default — অনেক distributions-এ।",
          "Features — journaling, extents (বড় files-এর জন্য block mapping replace করে), delayed allocation, 1 EB max volume, subdirectory limits up to 64,000 (বা dir_index সহ বেশি)।",
          "Backward compatibility — ext2/ext3 mount করতে পারে।",
          "Tools — mkfs.ext4, tune2fs।",
        ],
      },
      { type: "h3", title: "Comparison Table" },
      {
        type: "list",
        items: [
          "Max file size — FAT32: 4 GB; NTFS: 16 EB; ext4: 16 TB (theoretically 1 EB)।",
          "Max volume size — FAT32: 2 TB (64KB clusters সহ 8 TB); NTFS: 16 EB; ext4: 1 EB।",
          "Journaling — FAT32: না; NTFS: yes (metadata); ext4: yes (metadata, optional data)।",
          "Permissions — FAT32: না; NTFS: ACLs (yes); ext4: POSIX (yes)।",
          "Compression — FAT32: না; NTFS: yes; ext4: না (ecryptfs use করতে পারে)।",
          "Default OS — FAT32: legacy Windows, USB drives; NTFS: Windows; ext4: Linux।",
        ],
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "File attributes — name, ID, size, protection, timestamps, owner।",
          "File operations — create, open, read, write, close, delete, truncate।",
          "Directory structures — single-level, two-level, tree, acyclic graph (links সহ), general graph।",
          "Mounting — file system কে directory path-এ attach করা।",
          "Contiguous allocation — simple কিন্তু fragmentation cause করে।",
          "Linked allocation (FAT) — growth-এর জন্য ভালো, poor random access।",
          "Indexed allocation (inode) — direct + indirect pointers; large files support করে।",
          "Free space management — bitmap, linked list, grouping, counting।",
          "Disk scheduling — FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK।",
          "File system layout — boot block, superblock, inode table, data blocks।",
          "Journaling — changes-এর আগে log লেখো; crash-এর পর recover করো।",
          "Examples — FAT32 (simple, universal), NTFS (feature-rich, Windows), ext4 (Linux standard)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: File systems হলো OS ও persistent storage-এর মধ্যে bridge। পরের chapter I/O systems ও device management cover করে।",
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
    est: "2 hr",
    summary:
      "Input/Output (I/O) হলো সেই উপায় যেটা দিয়ে computer বাইরের দুনিয়ার সাথে communicate করে। এই chapter-এ hardware ও software cover করা হয়েছে যেগুলো I/O সম্ভব করে — device controllers থেকে interrupt handling, DMA, ও disk arrays পর্যন্ত।",
    sections: [
      { type: "h2", id: "hardware", title: "I/O Hardware: Ports, Buses, Controllers" },
      {
        type: "p",
        text: "I/O devices computer-এর সাথে hardware components-এর একটি hierarchy এর মাধ্যমে connect হয়। তিনটি main component হলো — ports, buses, ও controllers।",
      },
      { type: "h3", title: "Ports" },
      {
        type: "p",
        text: "Port হলো computer-এর একটি physical connector (যেমন USB port, Ethernet port, HDMI)। এটি একটি device-এর জন্য electrical ও logical interface provide করে। প্রতিটি port এক বা একাধিক I/O addresses-এর সাথে associated।",
      },
      { type: "h3", title: "Buses" },
      {
        type: "p",
        text: "Bus হলো wires-এর একটি set যেটা একাধিক devices share করে। Common buses — PCIe (graphics cards, NVMe SSDs, several GB/s), SATA (hard disks, SSDs, 6 Gb/s), USB (keyboards, mice, flash drives, up to 40 Gb/s USB4), Memory bus (CPU ↔ RAM, very high 50-100 GB/s)।",
      },
      {
        type: "p",
        text: "System bus CPU, memory, ও I/O bridges-কে connect করে। I/O bus (যেমন PCIe) I/O controllers-কে connect করে।",
      },
      { type: "h3", title: "Controllers (Adapters)" },
      {
        type: "p",
        text: "Controller হলো একটি chip বা circuit যেটা একটি নির্দিষ্ট ধরনের device manage করে। এটি low-level protocols, buffering, ও error correction handle করে। OS controller-এর সাথে registers (control, status, data) এর মাধ্যমে communicate করে। উদাহরণ — একটি disk controller read/write commands receive করে, logical block addresses-কে physical locations-এ translate করে, এবং data transfer করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি shipping port। Ship (device) একটি নির্দিষ্ট berth (port)-এ dock করে। Cranes ও customs officers (controller) cargo unload ও inspect করে। Road network (bus) goods কে city-তে transport করে।",
      },

      { type: "h2", id: "polling-interrupts", title: "Polling vs Interrupts" },
      {
        type: "p",
        text: "CPU কে জানতে হবে কখন একটি I/O device data-এর জন্য ready অথবা একটি operation complete করেছে। দুটি basic strategy আছে।",
      },
      { type: "h3", title: "Polling" },
      {
        type: "p",
        text: "CPU একটি loop-এ device-এর status register continuously check করে। যখন status 'ready' indicate করে, CPU I/O perform করে। Pros — simple, কোনো hardware overhead নেই। Cons — CPU cycles waste করে (busy waiting), বিশেষত যদি devices slow হয়।",
      },
      { type: "h3", title: "Interrupts" },
      {
        type: "p",
        text: "Device attention প্রয়োজন হলে CPU-কে একটি hardware interrupt signal পাঠায়। CPU current instruction finish করে, state save করে, এবং interrupt handler (interrupt service routine, ISR)-এ jump করে। Handling করার পর interrupted process-এ return করে।",
      },
      {
        type: "p",
        text: "Pros — CPU device busy থাকা অবস্থায় অন্য কাজ free হয়ে করতে পারে। Cons — state save/restore এর overhead; interrupt storms system-কে overwhelm করতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — Polling হলো একজন chef যে প্রতি সেকেন্ডে oven-এ দেখে cake প্রস্তুত হয়েছে কিনা। Interrupt হলো oven করে বিপ করে যখন cake তৈরি হয়; ততক্ষণ chef সবজি কাটতে থাকে।",
      },
      {
        type: "p",
        text: "Trade-off — খুব fast devices-এর জন্য polling use করো (যেমন always-ready data সহ network card) interrupt overhead এড়াতে। Slow devices-এর জন্য interrupts use করো (disks, keyboards)।",
      },
      {
        type: "multi-code",
        filename: "polling_vs_interrupt",
        codeSamples: {
          cpp: `#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>

// Simulate polling vs interrupt (event-driven) wait.
// 'ready' is set to true after 100ms by a "device" thread.

std::atomic<bool> ready{false};

// === POLLING ===
void polling_wait() {
    while (!ready.load()) {
        // busy wait — wastes CPU
    }
    std::cout << "[polling] device ready!\\n";
}

// === INTERRUPT (event-driven) ===
void interrupt_wait() {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    ready = true;       // simulate "device interrupt"
}

int main() {
    std::thread t(interrupt_wait);
    polling_wait();
    t.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
    "time"
)

// === POLLING ===
func pollingWait(ready *bool, mu *sync.Mutex) {
    for {
        mu.Lock()
        if *ready { mu.Unlock(); break }
        mu.Unlock()
        // busy wait — wastes CPU
    }
    fmt.Println("[polling] device ready!")
}

// === INTERRUPT (channel) ===
func interruptWait(done chan<- struct{}) {
    time.Sleep(100 * time.Millisecond)
    close(done)   // simulate "device interrupt"
}

func main() {
    var ready bool
    var mu sync.Mutex
    done := make(chan struct{})

    go pollingWait(&ready, &mu)
    go interruptWait(done)

    <-done
    mu.Lock()
    ready = true
    mu.Unlock()

    time.Sleep(50 * time.Millisecond)
}`,
          python: `import threading
import time

ready = False

# === POLLING ===
def polling_wait():
    while not ready:
        pass  # busy wait — wastes CPU
    print("[polling] device ready!")

# === INTERRUPT (event) ===
def device_interrupt():
    time.sleep(0.1)        # simulate device work
    global ready
    ready = True          # set the "interrupt"

t = threading.Thread(target=device_interrupt)
t.start()
polling_wait()
t.join()`,
          java: `import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class PollingVsInterrupt {
    static AtomicBoolean ready = new AtomicBoolean(false);

    // === POLLING ===
    static void pollingWait() {
        while (!ready.get()) {
            // busy wait
            Thread.onSpinWait();
        }
        System.out.println("[polling] device ready!");
    }

    // === INTERRUPT (event-driven) ===
    static void interruptWait() throws InterruptedException {
        Thread.sleep(100);             // simulate device work
        ready.set(true);                // fire "interrupt"
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(() -> {
            try { interruptWait(); } catch (InterruptedException e) {}
        });
        t.start();
        pollingWait();
        t.join();
    }
}`,
        },
      },

      { type: "h2", id: "dma", title: "Direct Memory Access (DMA)" },
      {
        type: "p",
        text: "DMA ছাড়া, CPU কে প্রতিটি byte device থেকে memory-তে copy করতে হয় (Programmed I/O – PIO)। এটি large transfers-এর জন্য CPU-কে tie করে রাখে।",
      },
      {
        type: "p",
        text: "DMA controller হলো special hardware যেটা device ও memory-এর মধ্যে directly data transfer করে CPU-এর involvement ছাড়া। CPU transfer set up করে (source, destination, count), তারপর অন্য কাজ continue করে। Transfer complete হলে DMA controller একটি interrupt পাঠায়।",
      },
      { type: "h3", title: "DMA-র ধাপ" },
      {
        type: "list",
        items: [
          "১. CPU DMA controller-কে program করে — memory address, device, transfer size, direction।",
          "২. DMA controller data move করে (word by word বা block by block) bus-এর উপর দিয়ে।",
          "৩. DMA controller complete হলে interrupt assert করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি moving company। DMA (PIO) ছাড়া আপনি প্রতিটি box নিজে carry করেন (CPU-bound)। DMA দিয়ে, আপনি movers hire করেন — তাদের বলেন 'room A থেকে room B-তে সব মুভ করো' এবং তারা সেটা করে যখন আপনি অন্য কিছু করেন; কাজ শেষ হলে তারা bell বাজায়।",
      },

      { type: "h2", id: "layers", title: "I/O Software Layers" },
      {
        type: "p",
        text: "Modern operating systems I/O-কে hierarchical layers-এ organize করে, complexity hide করে এবং uniform interfaces provide করে।",
      },
      { type: "h3", title: "১. Interrupt Handlers" },
      {
        type: "p",
        text: "Lowest layer। একটি interrupt হলে, handler — registers save করে, interrupt acknowledge করে, একটি callback schedule করে বা একটি waiting process wake করে, context restore করে এবং return করে।",
      },
      { type: "h3", title: "২. Device Drivers" },
      {
        type: "p",
        text: "Driver হলো একটি kernel module যেটা কীভাবে একটি নির্দিষ্ট device-এর সাথে talk করতে হয় তা জানে। এটি generic OS commands (যেমন read block 123) কে device-specific register writes-এ translate করে। প্রতিটি driver একটি standard interface implement করে (open, read, write, ioctl)। Linux, Windows-এ প্রায় 70% OS code drivers-এ থাকতে পারে।",
      },
      { type: "h3", title: "৩. Device-Independent I/O Layer" },
      {
        type: "p",
        text: "সব devices-এ common services provide করে:",
      },
      {
        type: "list",
        items: [
          "Uniform naming — /dev/sda, C:\\।",
          "Protection — কে কোন device access করতে পারবে।",
          "Buffering — data flow smooth করার জন্য temporary storage।",
          "Error handling — retry, report, বা ignore failures।",
          "Allocation — shared devices manage করা (যেমন tape drives)।",
        ],
      },
      { type: "h3", title: "৪. User-Space I/O" },
      {
        type: "p",
        text: "Library functions (যেমন printf, fread) যেগুলো system calls (read, write) call করে। কিছু I/O সম্পূর্ণভাবে user space-এ হতে পারে (যেমন memory-mapped files, microkernels-এ user-mode drivers)।",
      },
      {
        type: "p",
        text: "Real-life thinking — Interrupt handler হলো fire alarm bell — immediate action। Driver হলো building-এর electrician যে জানে ঠিক কোন wire কোন light control করে। Device-independent layer হলো building codes ও safety standards যা সব electrical work-এ apply হয়। User-space হলো আপনি light switch press করা।",
      },

      { type: "h2", id: "buffering-caching-spooling", title: "Buffering, Caching, Spooling" },
      {
        type: "p",
        text: "এই techniques গুলো I/O performance improve করে এবং speed mismatches handle করে।",
      },
      { type: "h3", title: "Buffering" },
      {
        type: "p",
        text: "Buffer হলো একটি memory area যেটা temporarily data hold করে যখন দুটি entity-এর মধ্যে (যেমন device ও application) transfer হয়। Buffers producer ও consumer speeds-কে decouple করে।",
      },
      {
        type: "list",
        items: [
          "Single buffer — OS data কে kernel buffer-এ read করে, তারপর user space-এ copy করে।",
          "Double buffering — দুটি buffers use করো — একটি fill হয় যখন অপরটি process হয়।",
          "Circular buffer — একটি ring-এ একাধিক buffers।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bread factory (fast producer) ও একটি toaster (slow consumer)। একটি delivery table (buffer) loaves collect করে; toaster ready হলে সেগুলো pick up করে।",
      },
      { type: "h3", title: "Caching" },
      {
        type: "p",
        text: "Cache recently used data কে faster storage-এ hold করে যাতে repeated slower I/O reduce হয়। Caching এবং buffering আলাদা — cache সম্ভাব্য reuse-এর জন্য already used data store করে; buffer in-transit data store করে। উদাহরণ — Linux-এ page cache, recently read disk blocks কে free memory-তে keep করা হয়।",
      },
      { type: "h3", title: "Spooling (Simultaneous Peripheral Operation On-Line)" },
      {
        type: "p",
        text: "Spool হলো একটি buffer যেটা slow device-এর জন্য output hold করে (যেমন printer)। প্রতিটি process তার output কে disk-এ একটি spool file-এ write করে। একটি background daemon (printer daemon) পরে files print করে। Advantage — processes printer-এর জন্য wait করে না; তারা immediately continue করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন receptionist-এর inbox — মানুষ messages drop করে (spool) এবং receptionist সেগুলো একে একে deliver করে।",
      },

      { type: "h2", id: "block-char", title: "Block ও Character Devices" },
      {
        type: "list",
        items: [
          "Block device — fixed-size blocks, random access (যেমন disk, SSD, USB drive)। Interface: read(), write(), seek()।",
          "Character device — byte stream, কোনো seek নেই (যেমন keyboard, mouse, serial port)। Interface: getchar(), putchar()।",
        ],
      },
      {
        type: "p",
        text: "Unix-এ block devices /dev-এ files হিসেবে appear করে। Character devices-ও appear করে (যেমন /dev/tty)। কিছু devices (যেমন network interfaces) কোনোটাই না — তারা socket interface use করে।",
      },

      { type: "h2", id: "disk-structure", title: "Disk Structure" },
      {
        type: "p",
        text: "Magnetic hard disks (HDDs) এখনও widely used; তাদের geometry বোঝা file systems optimize করতে help করে।",
      },
      { type: "h3", title: "Components" },
      {
        type: "list",
        items: [
          "Platters — circular metal/glass disks যেগুলো magnetic material দ্বারা coated।",
          "Spindle — platters rotate করে (5400, 7200, 10000 RPM)।",
          "Read/write heads — platter surface প্রতি একটি, একটি arm-এ mounted।",
          "Actuator — arm কে platter জুড়ে move করে।",
        ],
      },
      { type: "h3", title: "Geometric terms" },
      {
        type: "list",
        items: [
          "Track — platter surface-এ একটি concentric circle।",
          "Cylinder — সব platters জুড়ে একই arm position-এ tracks-এর set।",
          "Sector — smallest addressable unit (traditionally 512 bytes, এখন 4 KB)।",
          "Head — একটি surface-এর জন্য read/write mechanism।",
        ],
      },
      {
        type: "p",
        text: "Capacity = (bytes per sector) × (sectors per track) × (tracks per cylinder) × (cylinders) × (platters)। Real-life thinking — একটি vinyl record player। Record (platter) spin করে। Needle (head) radial ভাবে বিভিন্ন grooves (tracks)-এ move করে। একই groove position multiple records-এ vertically stack করা হলে সেটি cylinder।",
      },

      { type: "h2", id: "raid", title: "RAID Levels" },
      {
        type: "p",
        text: "RAID (Redundant Array of Independent Disks) একাধিক physical disks-কে একটি logical unit-এ combine করে performance, reliability, বা দুটোর জন্য।",
      },
      { type: "h3", title: "RAID 0 (Striping)" },
      {
        type: "p",
        text: "Data গুলো blocks-এ disks-এ stripe করা হয়। কোনো redundancy নেই। Pros — high performance (parallel I/O)। Cons — যেকোনো disk failure সব data হারায়। Use — temporary data, high-performance scratch space।",
      },
      { type: "h3", title: "RAID 1 (Mirroring)" },
      {
        type: "p",
        text: "প্রতিটি write দুটি (বা ততোধিক) disks-এ যায়। Reads যেকোনো একটি থেকে হতে পারে। Pros — excellent fault tolerance; good read performance। Cons — 2× storage cost। Use — OS disks, critical databases।",
      },
      { type: "h3", title: "RAID 5 (Striping with Parity)" },
      {
        type: "p",
        text: "Blocks ও parity সব disks-এ striped হয়। Parity distributed (একটি disk-এ না)। একটি disk failure tolerate করতে পারে। Pros — good read performance; efficient storage (1/N overhead)। Cons — slow writes (read-modify-write penalty)। Use — file servers, general-purpose storage।",
      },
      {
        type: "multi-code",
        filename: "raid5_parity",
        codeSamples: {
          cpp: `#include <iostream>
#include <vector>
using namespace std;

// Simulate RAID 5 parity across N disks.
// XOR all the data blocks of a stripe to get the parity.
int raid5_parity(const vector<int>& stripe_data) {
    int p = 0;
    for (int v : stripe_data) p ^= v;   // XOR = parity
    return p;
}

int main() {
    // 4 disks, block A on disk 0, B on 1, C on 2, P on 3
    vector<int> stripe = {0xAB, 0xCD, 0xEF};
    int parity = raid5_parity(stripe);
    cout << "Parity block: 0x" << hex << parity << '\\n';  // 0x123

    // Simulate disk 1 failure (lose block B). Reconstruct:
    int recovered = parity ^ stripe[0] ^ stripe[2];
    cout << "Recovered block B: 0x" << recovered << '\\n';   // 0xCD
}`,
          go: `package main

import "fmt"

// RAID 5 parity across N disks = XOR of all data blocks.
func raid5Parity(stripe []int) int {
    p := 0
    for _, v := range stripe {
        p ^= v
    }
    return p
}

func main() {
    stripe := []int{0xAB, 0xCD, 0xEF}
    parity := raid5Parity(stripe)
    fmt.Printf("Parity block: 0x%x\\n", parity)   // 0x123

    // Lose block on disk 1 (B). Reconstruct:
    recovered := parity ^ stripe[0] ^ stripe[2]
    fmt.Printf("Recovered block B: 0x%x\\n", recovered)  // 0xcd
}`,
          python: `# RAID 5 parity across N disks = XOR of all data blocks
def raid5_parity(stripe):
    p = 0
    for v in stripe:
        p ^= v
    return p

stripe = [0xAB, 0xCD, 0xEF]
parity = raid5_parity(stripe)
print(f"Parity block: 0x{parity:x}")  # 0x123

# Lose block on disk 1 (B). Reconstruct:
recovered = parity ^ stripe[0] ^ stripe[2]
print(f"Recovered block B: 0x{recovered:x}")  # 0xcd`,
          java: `public class RAID5 {
    // XOR of all data blocks
    static int raid5Parity(int[] stripe) {
        int p = 0;
        for (int v : stripe) p ^= v;
        return p;
    }

    public static void main(String[] args) {
        int[] stripe = {0xAB, 0xCD, 0xEF};
        int parity = raid5Parity(stripe);
        System.out.printf("Parity block: 0x%x%n", parity);   // 0x123

        // Lose disk 1 (block B). Reconstruct:
        int recovered = parity ^ stripe[0] ^ stripe[2];
        System.out.printf("Recovered block B: 0x%x%n", recovered);  // 0xcd
    }
}`,
        },
      },
      { type: "h3", title: "RAID 6" },
      {
        type: "p",
        text: "RAID 5-এর মতো কিন্তু দুটি parity blocks সহ (ভিন্ন algorithms)। দুটি disk failures tolerate করতে পারে। Pros — very high fault tolerance। Cons — আরও slow writes; 2/N overhead। Use — large capacity systems, archival storage।",
      },
      { type: "h3", title: "RAID 10 (1+0)" },
      {
        type: "p",
        text: "Striped mirrors — প্রথমে mirror, তারপর mirror pairs-এর উপর stripe (অথবা stripe তারপর mirror — দুটোই exist করে)। RAID 0 performance ও RAID 1 fault tolerance combine করে। Pros — excellent performance ও fault tolerance (প্রতিটি mirror pair-এ একটি disk lose করতে পারে)। Cons — expensive (2× storage)। Use — high-performance databases, virtualization hosts।",
      },
      { type: "h3", title: "RAID Levels Comparison" },
      {
        type: "list",
        items: [
          "RAID 0 — min 2 disks, fault tolerance none, read perf high, write perf high, capacity N × disk।",
          "RAID 1 — min 2 disks, 1 disk fault tolerance, read high, write medium, capacity N/2 × disk।",
          "RAID 5 — min 3 disks, 1 disk tolerance, read high, write low, capacity (N-1) × disk।",
          "RAID 6 — min 4 disks, 2 disks tolerance, read high, write very low, capacity (N-2) × disk।",
          "RAID 10 — min 4 disks, up to 2 (one per pair), read very high, write high, capacity N/2 × disk।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — RAID 0 হলো দুজন relay runners যারা অর্ধেক message ধারণ করে — fast, কিন্তু একজন পড়লে পুরো message হারায়। RAID 1 হলো দুজন student একই notes লেখে — একজন notebook হারালেও অপরজনের কাছে complete info আছে। RAID 5 হলো ৪ জন friend-এর একটি group যারা তাদের shared document-এর জন্য checksum calculate করে। একজন friend leave করলে বাকিরা checksum থেকে missing parts reconstruct করতে পারে।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "I/O hardware — ports (connectors), buses (communication paths), controllers (device managers)।",
          "Polling — CPU continuously device status check করে — simple কিন্তু cycles waste করে।",
          "Interrupts — device ready হলে CPU signal করে — slow devices-এর জন্য efficient।",
          "DMA — hardware CPU ছাড়া data transfer করে; শুধু setup ও completion interrupt।",
          "I/O software layers — interrupt handlers → device drivers → device-independent I/O → user-space I/O।",
          "Buffering — in-transit data-র জন্য temporary storage (speed mismatches smooth করে)।",
          "Caching — ভবিষ্যত fast access-এর জন্য reused data store করা।",
          "Spooling — slow devices-এর জন্য output buffer (printers)।",
          "Block vs character — block devices: random access, fixed blocks; character: byte stream।",
          "Disk structure — tracks, cylinders, sectors — geometry scheduling-কে affect করে।",
          "RAID levels — 0 (striping, no redundancy), 1 (mirroring), 5 (parity, one fault), 6 (two faults), 10 (mirrored stripes)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: I/O systems OS puzzle complete করে, internal abstractions-কে physical world-এর সাথে bridge করে। এই chapter-এ operating systems fundamentals-এর journey conclude হয়।",
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
    est: "2 hr",
    summary:
      "Security ও protection যেকোনো operating system-এ fundamental। এই chapter-এ security-এর goals, authentication methods, access control models, protection mechanisms, common attacks, ও encryption techniques cover করা হয়েছে যেগুলো data ও resources safeguard করে।",
    sections: [
      { type: "h2", id: "cia", title: "Security Goals: Confidentiality, Integrity, Availability" },
      {
        type: "p",
        text: "CIA triad information security-এর core objectives define করে। তিনটি goal একসাথে থাকা জরুরি — একটি দুর্বল হলে পুরো system দুর্বল হয়ে যায়।",
      },
      { type: "h3", title: "CIA Triad" },
      {
        type: "list",
        items: [
          "Confidentiality — unauthorised access prevent করা information-এ। Failure example: hacker password file steal করে।",
          "Integrity — ensure করা যে data tamper বা permission ছাড়া modify করা হবে না। Failure example: malware system binaries alter করে।",
          "Availability — ensure করা যে systems ও data দরকার হলে accessible। Failure example: Denial-of-service (DoS) attack website-কে unreachable করে দেয়।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bank vault। Confidentiality — শুধু authorised staff ভেতর দেখতে পারে। Integrity — stored money alter করা যায় না (counterfeiting prevented)। Availability — vault business hours-এ accessible।",
      },

      { type: "h2", id: "authentication", title: "Authentication" },
      {
        type: "p",
        text: "Authentication একটি user বা process-এর identity verify করে। তিনটি common factor আছে — something you know, something you have, ও something you are।",
      },
      { type: "h3", title: "১. Something you know (passwords, PINs)" },
      {
        type: "p",
        text: "Most common, কিন্তু guessing, theft, phishing-এ vulnerable। Password storage-এ modern OSes plaintext-এর বদলে hashed passwords store করে (bcrypt, SHA-256 with salt সহ)। Salt হলো একটি random value যেটা প্রতিটি password-এ যোগ করা হয় hashing-এর আগে rainbow table attacks prevent করতে।",
      },
      {
        type: "multi-code",
        filename: "password_hashing",
        codeSamples: {
          cpp: `#include <iostream>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <string>
#include <vector>

// Generate a random salt, then hash password+salt with SHA-256.
std::vector<unsigned char> hash_password(
    const std::string& pw, std::vector<unsigned char>& salt) {
    salt.resize(16);
    RAND_bytes(salt.data(), 16);

    EVP_MD_CTX* ctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(ctx, EVP_sha256(), nullptr);
    EVP_DigestUpdate(ctx, pw.data(), pw.size());
    EVP_DigestUpdate(ctx, salt.data(), salt.size());

    std::vector<unsigned char> hash(EVP_MAX_MD_SIZE);
    unsigned int len;
    EVP_DigestFinal_ex(ctx, hash.data(), &len);
    hash.resize(len);
    EVP_MD_CTX_free(ctx);
    return hash;
}

int main() {
    std::vector<unsigned char> salt;
    auto hash = hash_password("hunter2", salt);
    std::cout << "Hash length: " << hash.size() << " bytes\\n";
    return 0;
}
// Compile: g++ password.cpp -lcrypto`,
          go: `package main

import (
    "crypto/rand"
    "crypto/sha256"
    "fmt"
)

// Generate a random salt, then hash password+salt with SHA-256.
func hashPassword(pw string) (hash, salt []byte) {
    salt = make([]byte, 16)
    rand.Read(salt)
    h := sha256.New()
    h.Write([]byte(pw))
    h.Write(salt)
    hash = h.Sum(nil)
    return
}

func main() {
    hash, salt := hashPassword("hunter2")
    fmt.Printf("Hash: %x\\nSalt: %x\\n", hash, salt)
}`,
          python: `import hashlib
import os

# Generate a random salt, then hash password+salt with SHA-256.
def hash_password(pw):
    salt = os.urandom(16)
    h = hashlib.sha256()
    h.update(pw.encode())
    h.update(salt)
    return h.digest(), salt

pw_hash, salt = hash_password("hunter2")
print(f"Hash: {pw_hash.hex()}")
print(f"Salt: {salt.hex()}")`,
          java: `import java.security.*;
import java.util.*;

public class PasswordHashing {
    public static void main(String[] args) throws Exception {
        // Generate a random salt
        byte[] salt = new byte[16];
        SecureRandom.getInstanceStrong().nextBytes(salt);

        // Hash password + salt with SHA-256
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update("hunter2".getBytes());
        md.update(salt);
        byte[] hash = md.digest();

        System.out.println("Hash: " + Base64.getEncoder().encodeToString(hash));
        System.out.println("Salt: " + Base64.getEncoder().encodeToString(salt));
    }
}`,
        },
      },
      { type: "h3", title: "২. Something you have (smart card, security token, phone)" },
      {
        type: "p",
        text: "একটি second factor যোগ করে; সাধারণত password-এর সাথে combine করা হয় (two-factor authentication – 2FA)। Hardware tokens — YubiKey, RSA SecurID। Software tokens — TOTP (Google Authenticator) – time-based one-time password।",
      },
      { type: "h3", title: "৩. Something you are (biometrics)" },
      {
        type: "p",
        text: "Fingerprint, iris scan, face recognition, voice। Pros — hard to forge, convenient। Cons — compromised হলে change করা যায় না; false positives/negatives হতে পারে।",
      },
      { type: "h3", title: "Multi-factor Authentication (MFA)" },
      {
        type: "p",
        text: "দুটি বা ততোধিক factors combine করে। যেমন password (knowledge) + SMS code (possession)। Security greatly increase করে। Real-life thinking — একটি secure building-এ প্রবেশ করা। Password = door-এ keycode। Security token = keycard। Biometric = fingerprint scanner। MFA = keycard + PIN।",
      },

      { type: "h2", id: "access-control", title: "Access Control" },
      {
        type: "p",
        text: "Authenticate হওয়ার পর, OS decide করতে হবে একটি user কোন resources access করতে পারবে এবং কোন operations allowed। তিনটি classic model আছে।",
      },
      { type: "h3", title: "DAC (Discretionary Access Control)" },
      {
        type: "p",
        text: "একটি resource-এর owner decide করে কে access করতে পারবে। General-purpose OSes-এ common (Unix permissions, Windows ACLs)। Unix permissions — read, write, execute for owner, group, others। Problem — users accidentally excessive permissions grant করতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি একটি house own করছেন; আপনি friends কে keys দেন যেমন চান।",
      },
      { type: "h3", title: "MAC (Mandatory Access Control)" },
      {
        type: "p",
        text: "System (OS) একটি global policy enforce করে যা users override করতে পারে না। High-security environments-এ use হয় (military, SELinux, AppArmor)। Labels — প্রতিটি resource ও user-এর একটি security label আছে (যেমন 'Top Secret', 'Secret', 'Unclassified')। Rules — একজন user একটি resource access করতে পারবে শুধু যদি তার clearance resource-এর label-কে dominate করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — Military document classification — একজন 'Secret' clearance holder 'Top Secret' documents read করতে পারবে না, তার ইচ্ছা যাই হোক না কেন।",
      },
      { type: "h3", title: "RBAC (Role-Based Access Control)" },
      {
        type: "p",
        text: "Permissions roles-এ assign করা হয়, এবং users roles-এ assign করা হয়। Roles job functions reflect করে (যেমন 'Doctor', 'Nurse', 'Accountant')। Advantage — administration simplify করে; per-user এর বদলে role permissions change করুন। Examples — database systems, enterprise applications, Windows groups।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hospital — doctors-এর prescription rights আছে; nurses-এর patient care rights আছে; receptionists শুধু appointments schedule করতে পারে। Users roles-এ assign করা হয়।",
      },

      { type: "h2", id: "matrix", title: "Protection Mechanisms: Capabilities ও Access Matrix" },
      {
        type: "p",
        text: "OS-এর internal structures প্রয়োজন access control enforce করতে।",
      },
      { type: "h3", title: "Access Matrix" },
      {
        type: "p",
        text: "একটি conceptual table যেখানে rows subjects (users, processes) represent করে এবং columns objects (files, devices) represent করে। প্রতিটি cell allowed operations (read, write, execute, delete) ধারণ করে।",
      },
      {
        type: "p",
        text: "Implementation — Access Control Lists (ACLs): প্রতিটি object-এর সাথে একটি list attach করো (matrix-এর column)। Windows NTFS, POSIX ACLs। Capabilities: প্রতিটি subject-এর সাথে একটি list attach করো (matrix-এর row)। প্রতিটি capability একটি unforgeable token যেটা একটি নির্দিষ্ট object-এ নির্দিষ্ট rights সহ access grant করে।",
      },
      {
        type: "multi-code",
        filename: "acl_capability",
        codeSamples: {
          cpp: `#include <iostream>
#include <unordered_map>
#include <string>

enum class Perm { NONE = 0, READ = 1, WRITE = 2, EXEC = 4 };

inline Perm operator|(Perm a, Perm b) {
    return static_cast<Perm>(static_cast<int>(a) | static_cast<int>(b));
}
inline bool has(Perm s, Perm p) {
    return (static_cast<int>(s) & static_cast<int>(p)) != 0;
}

// ACL: file -> user -> permission
std::unordered_map<std::string,
    std::unordered_map<std::string, Perm>> acl = {
    {"secret.txt", { {"alice", Perm::READ | Perm::WRITE},
                      {"bob",   Perm::READ} }},
};

bool check_acl(const std::string& file,
               const std::string& user, Perm need) {
    auto it = acl.find(file);
    if (it == acl.end()) return false;
    auto& fileAcl = it->second;
    auto u = fileAcl.find(user);
    if (u == fileAcl.end()) return false;
    return has(u->second, need);
}

int main() {
    std::cout << "alice read:  " << check_acl("secret.txt", "alice", Perm::READ)  << '\\n';
    std::cout << "alice write: " << check_acl("secret.txt", "alice", Perm::WRITE) << '\\n';
    std::cout << "alice exec:  " << check_acl("secret.txt", "alice", Perm::EXEC)  << '\\n';
    std::cout << "bob write:   " << check_acl("secret.txt", "bob",   Perm::WRITE) << '\\n';
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

// ACL: file -> user -> permission
var acl = map[string]map[string]Perm{
    "secret.txt": {
        "alice": Read | Write,
        "bob":   Read,
    },
}

func checkACL(file, user string, need Perm) bool {
    fileAcl, ok := acl[file]
    if !ok { return false }
    p, ok := fileAcl[user]
    return ok && p.Has(need)
}

func main() {
    fmt.Println("alice read: ", checkACL("secret.txt", "alice", Read))
    fmt.Println("alice write:", checkACL("secret.txt", "alice", Write))
    fmt.Println("alice exec: ", checkACL("secret.txt", "alice", Exec))
    fmt.Println("bob write:  ", checkACL("secret.txt", "bob",   Write))
}`,
          python: `from enum import Flag, auto

class Perm(Flag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    EXEC = auto()

# ACL: file -> user -> permission
acl = {
    "secret.txt": {
        "alice": Perm.READ | Perm.WRITE,
        "bob":   Perm.READ,
    },
}

def check_acl(file, user, need):
    file_acl = acl.get(file, {})
    p = file_acl.get(user)
    if p is None:
        return False
    return bool(p & need)

print("alice read: ", check_acl("secret.txt", "alice", Perm.READ))
print("alice write:", check_acl("secret.txt", "alice", Perm.WRITE))
print("alice exec: ", check_acl("secret.txt", "alice", Perm.EXEC))
print("bob write:  ", check_acl("secret.txt", "bob",   Perm.WRITE))`,
          java: `import java.util.*;

public class ACL {
    enum Perm { NONE, READ, WRITE, EXEC }
    static class PermSet {
        final Set<Perm> perms;
        PermSet(Perm... ps) {
            perms = EnumSet.noneOf(Perm.class);
            for (Perm p : ps) if (p != Perm.NONE) perms.add(p);
        }
        boolean has(Perm p) { return perms.contains(p); }
    }

    // ACL: file -> user -> permission set
    static Map<String, Map<String, PermSet>> acl = Map.of(
        "secret.txt", Map.of(
            "alice", new PermSet(Perm.READ, Perm.WRITE),
            "bob",   new PermSet(Perm.READ)
        )
    );

    static boolean checkACL(String file, String user, Perm need) {
        Map<String, PermSet> fileAcl = acl.get(file);
        if (fileAcl == null) return false;
        PermSet p = fileAcl.get(user);
        return p != null && p.has(need);
    }

    public static void main(String[] args) {
        System.out.println("alice read:  " + checkACL("secret.txt", "alice", Perm.READ));
        System.out.println("alice write: " + checkACL("secret.txt", "alice", Perm.WRITE));
        System.out.println("alice exec:  " + checkACL("secret.txt", "alice", Perm.EXEC));
        System.out.println("bob write:   " + checkACL("secret.txt", "bob",   Perm.WRITE));
    }
}`,
        },
      },
      { type: "h3", title: "Capability" },
      {
        type: "p",
        text: "Capability হলো একটি ticket যেটা একটি process-কে permission দেয় একটি object-এ নির্দিষ্ট operations perform করার জন্য। প্রায়ই একটি protected, kernel-managed reference হিসেবে implement করা হয়। Advantage — easy to delegate; fine-grained। Disadvantage — capabilities revoke করা complex হতে পারে। Examples — early research OS (Hydra, KeyKOS), কিছু microkernels (seL4)।",
      },
      {
        type: "p",
        text: "Real-life thinking — ACL হলো একটি club-এ bouncer-এর list — প্রতিটি club-এর নিজস্ব allowed guests list। Capability হলো একটি wristband — আপনি এটি show করেন প্রবেশ করতে; বিভিন্ন colors বিভিন্ন access দেয়।",
      },

      { type: "h2", id: "least-privilege", title: "Principle of Least Privilege" },
      {
        type: "p",
        text: "Principle of least privilege বলে যে একটি process (বা user)-কে শুধু ততটুকু privilege grant করা উচিত যতটুকু তার task perform করার জন্য প্রয়োজন, এবং শুধু ততটুকু সময়ের জন্য যতটুকু দরকার।",
      },
      {
        type: "p",
        text: "Benefit — bugs বা attacks থেকে damage limit করে। Examples — Unix setuid programs initial setup-এর পর privileges drop করে। Web browsers tabs-কে sandboxes-এ চালায় limited file access সহ। Linux capabilities: root privileges-কে ছোট pieces-এ ভাগ করে (CAP_NET_ADMIN, CAP_SYS_ADMIN)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন hotel valet — তারা আপনার car park করতে পারে কিন্তু আপনার room safe খুলতে পারবে না।",
      },

      { type: "h2", id: "malware", title: "Malicious Software (Malware)" },
      {
        type: "p",
        text: "Malware হলো এমন software যেটা harm বা infiltrate করার জন্য design করা। বিভিন্ন প্রকার আছে।",
      },
      {
        type: "list",
        items: [
          "Virus — legitimate programs-এ attach হয়; user action প্রয়োজন (infected program run করা)। File infection-এ propagate হয়। Payload: corruption, theft, backdoor।",
          "Worm — networks-এ user action ছাড়া self-replicate করে। Network exploits, emails-এ propagate হয়। Payload: resource exhaustion, backdoor।",
          "Trojan — legitimate software হিসেবে disguised; self-replicate করে না। Social engineering-এ propagate হয়। Payload: data theft, ransomware।",
          "Rootkit — OS থেকে তার presence (files, processes, network connections) hide করে। Initial compromise-এর পর install হয়। Payload: stealth, persistent backdoor।",
          "Ransomware — user files encrypt করে এবং payment demand করে। Trojan, worm, exploit-এ propagate হয়। Payload: file encryption।",
          "Spyware — secretly user information collect করে। Freeware-এর সাথে bundled হয়। Payload: keylogging, browsing data।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Virus হলো একটি contagious disease touch দ্বারা spread হয়। Worm হলো একটি airborne pathogen যেটা ventilation systems-এর মাধ্যমে নিজে ছড়ায়। Trojan হলো একটি delivery box 'gift' label করা যেটার ভেতরে bomb। Rootkit হলো একজন spy যে security camera footage delete করতে পারে যাতে আপনি জানতেই না সে ছিল।",
      },

      { type: "h2", id: "buffer-overflow", title: "Buffer Overflow Attacks ও Defenses" },
      {
        type: "p",
        text: "Buffer overflow তখন হয় যখন একটি program allocated buffer bounds-এর বাইরে data write করে, adjacent memory overwrite করে। Attackers এটিকে exploit করে malicious code inject করতে বা execution flow change করতে।",
      },
      { type: "h3", title: "Classic stack overflow" },
      {
        type: "code",
        lang: "c",
        text: `void vulnerable(char *str) {
    char buffer[64];
    strcpy(buffer, str);   // no bounds check
}`,
      },
      {
        type: "p",
        text: "str যদি 64 bytes-এর বেশি হয়, সেটা stack-এ return address overwrite করে। একজন attacker এমন input craft করে যেটা attacker code (shellcode) place করে এবং return address-কে সেটি point করতে set করে।",
      },
      { type: "h3", title: "Defenses" },
      {
        type: "list",
        items: [
          "Non-executable stack (NX bit) — stack memory কে non-executable mark করো। Shellcode execution prevent করে। Bypass হয় return-to-libc বা ROP দিয়ে।",
          "Address Space Layout Randomization (ASLR) — stack, heap, libraries-এর base addresses randomise করো। Attacker return address location জানতে পারবে না। Effective; 32-bit-এ brute-force possible।",
          "Stack canaries — return address-এর আগে একটি secret value (canary) place করো। Overflow এটি overwrite করলে program abort হয়। Very effective; GCC দ্বারা use হয় (-fstack-protector)।",
          "Bounds checking — compile-time বা runtime checks (যেমন Rust, Safe C extensions)। Most thorough, কিন্তু performance cost।",
          "Control Flow Integrity (CFI) — program jumps-কে একটি precomputed set of valid targets-এ restrict করো। Emerging standard (যেমন Intel CET)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hotel keycard system। Buffers হলো mail slots-এর মতো — যদি আপনি একটি লম্বা package shove করেন, এটা room door push করে open করতে পারে। Defenses হলো slot-কে খুব narrow করা (little canary) বা key যে door open করে সেটা randomise করা (ASLR)।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: একটি single defense পর্যাপ্ত না। Modern systems defense-in-depth use করে — NX + ASLR + stack canaries একসাথে। তবুও ROP (Return-Oriented Programming) এর মতো advanced attacks থেকে যায়।",
      },

      { type: "h2", id: "encryption", title: "Encryption Basics for OS Security" },
      {
        type: "p",
        text: "Encryption data transform করে unauthorised reading prevent করতে। Modern OSes encryption use করে data at rest (disk) ও in transit (network) protect করতে।",
      },
      { type: "h3", title: "Symmetric Encryption" },
      {
        type: "p",
        text: "একই key encrypt ও decrypt করে। Algorithms — AES (Advanced Encryption Standard), ChaCha20। Use — full-disk encryption (FDE), file encryption, network session encryption (TLS)। একই key দুই পক্ষ share করে, তাই key distribution একটি সমস্যা।",
      },
      { type: "h3", title: "Asymmetric Encryption (Public Key)" },
      {
        type: "p",
        text: "দুটি keys — public key (encrypt করে), private key (decrypt করে)। Public থেকে private derive করা infeasible। Algorithms — RSA, ECC (Elliptic Curve Cryptography)। Use — key exchange, digital signatures, authentication।",
      },
      { type: "h3", title: "Full-Disk Encryption (FDE)" },
      {
        type: "p",
        text: "Entire storage device encrypt করে (boot block ছাড়া)। OS on-the-fly decrypt করে একটি key দিয়ে যেটা passphrase, TPM (Trusted Platform Module), বা USB token থেকে derive হয়।",
      },
      {
        type: "list",
        items: [
          "Examples — Windows BitLocker, macOS FileVault, Linux LUKS (dm-crypt)।",
          "Threat model — device-এর physical theft থেকে protect করে; compromised running system থেকে protect করে না।",
        ],
      },
      { type: "h3", title: "How LUKS works (simplified)" },
      {
        type: "list",
        items: [
          "১. User passphrase enter করে।",
          "২. Passphrase LUKS header-এ stored master key-কে decrypt করে।",
          "৩. Master key disk blocks-কে on-the-fly decrypt করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি safe (encrypted disk) যার combination lock (passphrase) আছে। একজন thief safe steal করলেও combination ছাড়া ভেতরের documents read করতে পারবে না।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Security goals — Confidentiality, Integrity, Availability (CIA triad)।",
          "Authentication — something you know (password), have (token), are (biometric); MFA factors combine করে।",
          "Access control — DAC (owner decide করে), MAC (system decide করে), RBAC (roles)।",
          "Protection mechanisms — Access matrix; ACLs (per object) বা capabilities (per subject) হিসেবে implement করা।",
          "Least privilege — minimal rights minimal time-এর জন্য grant করো damage limit করতে।",
          "Malware types — viruses (attach), worms (self-spread), trojans (disguised), rootkits (hide), ransomware (encrypt)।",
          "Buffer overflow defenses — NX bit, ASLR, stack canaries, bounds checking, CFI।",
          "Encryption for OS — Full-disk encryption (BitLocker, FileVault, LUKS) physical theft থেকে protect করে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Security একটি product না, একটি continuous process। OS-level mechanisms বোঝা trustworthy systems build ও maintain করার প্রথম ধাপ।",
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
    est: "2 hr",
    summary:
      "Virtualization software-কে underlying hardware থেকে decouple করে, যাতে একাধিক operating systems একটি single physical machine-এ চলতে পারে। Cloud computing virtualization-এর উপর built হয়ে computing resources-কে on-demand services হিসেবে deliver করে। এই chapter-এ hypervisors, containers, cloud models, ও তাদের trade-offs ব্যাখ্যা করা হয়েছে।",
    sections: [
      { type: "h2", id: "vm-hypervisors", title: "Virtual Machine Concepts: Hypervisors" },
      {
        type: "p",
        text: "Virtual machine (VM) হলো একটি physical computer-এর software implementation যেটা একটি operating system ও applications run করে। Hypervisor (বা virtual machine monitor, VMM) হলো সেই software layer যেটা VMs create ও manage করে।",
      },
      { type: "h3", title: "Type 1 Hypervisor (Bare-Metal)" },
      {
        type: "p",
        text: "সরাসরি physical hardware-এ চালে কোনো host OS ছাড়া। Hardware resources-এ direct access আছে। Examples — VMware ESXi, Microsoft Hyper-V, KVM (Linux kernel-based), Xen। Pros — high performance, low overhead, better security। Cons — সব devices-এর জন্য hardware drivers প্রয়োজন; বেশি complex management।",
      },
      { type: "h3", title: "Type 2 Hypervisor (Hosted)" },
      {
        type: "p",
        text: "একটি host operating system-এর উপরে application হিসেবে চালে। Host OS physical hardware manage করে। Examples — Oracle VirtualBox, VMware Workstation, QEMU (KVM acceleration ছাড়া)। Pros — install করা সহজ, development ও testing-এর জন্য ভালো। Cons — বেশি overhead (calls host OS দিয়ে যায়), lower performance।",
      },
      {
        type: "p",
        text: "Real-life thinking — Type 1 হলো একটি high-rise apartment building যেখানে property manager on-site থাকেন (hypervisor directly elevators, electricity control করে)। Type 2 হলো একটি rental agency যেটা একটি বড় office building-এর ভেতরে চলে — আপনি একটি room rent করেন, কিন্তু building-এর নিজস্ব facilities manager (host OS) infrastructure control করে।",
      },

      { type: "h2", id: "virt-vs-emulation", title: "Virtualization vs Emulation" },
      {
        type: "p",
        text: "Virtualization-এ guest ও host-এর একই instruction set architecture (ISA) থাকা জরুরি — তাহলে guest instructions directly CPU-তে run হয়। Emulation যেকোনো architecture-এর software run করতে পারে প্রতিটি instruction interpret বা translate করে।",
      },
      { type: "h3", title: "Virtualization vs Emulation — Comparison" },
      {
        type: "list",
        items: [
          "Guest instructions — Virtualization: directly CPU-তে run করে (যদি same architecture হয়); Emulation: software-এ simulate করা হয়।",
          "Performance — Virtualization: near-native (hardware support সহ); Emulation: খুব slow (10-100× slowdown)।",
          "Guest OS modification — Virtualization: প্রয়োজন নেই (full virtualization) বা minimal (para-virtualization); Emulation: কিছু প্রয়োজন নেই।",
          "Use case — Virtualization: x86 Windows-এ x86 Linux run করা; Emulation: x86-এ ARM software run করা, retro-gaming।",
        ],
      },
      {
        type: "p",
        text: "Example — QEMU একটি ARM CPU কে x86 host-এ emulate করতে পারে (emulation)। QEMU + KVM একটি x86 guest কে x86 host-এ virtualize করতে পারে (virtualization)। Real-life thinking — Virtualization হলো একটি movie theatre যেখানে films তাদের native format-এ দেখানো হয় (digital projector digital files play করে)। Emulation হলো একজন translator যে একটি French script কে English-এ aloud পড়ে — প্রতিটি word process হয়।",
      },

      { type: "h2", id: "para-vs-hw-assisted", title: "Para-Virtualization ও Hardware-Assisted Virtualization" },
      { type: "h3", title: "Para-Virtualization" },
      {
        type: "p",
        text: "Guest OS-কে modify করা হয় যাতে সে hypervisor সম্পর্কে aware হয়। Privileged instructions trap করার বদলে (যেটা emulate করা slow), guest explicit hypercalls hypervisor-এ করে। Pros — high performance (trapping overhead reduce করে)। Cons — guest OS modify করা প্রয়োজন (Windows-এর জন্য possible না)। Example — Xen-এর early approach (paravirtualized Linux, NetBSD)।",
      },
      { type: "h3", title: "Hardware-Assisted Virtualization" },
      {
        type: "p",
        text: "Modern CPUs (Intel VT-x, AMD-V) virtualization-এর জন্য hardware support যোগ করে — নতুন CPU modes (VMX root for hypervisor, VMX non-root for guest)। Extended Page Tables (EPT) / Nested Page Tables (NPT) — hardware-assisted virtual memory translation (shadow page table overhead reduce করে)। VMCS (Virtual Machine Control Structure) — guest state, exit reasons store করে।",
      },
      {
        type: "list",
        items: [
          "Benefits — Full virtualization guest modification ছাড়া। Near-native performance। Simpler hypervisor implementation।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Para-virtualization হলো একজন foreign tourist যে কয়েকটি local customs learn করে (modified OS) যাতে airport security দ্রুত pass করতে পারে। Hardware-assisted হলো immigration-এ একটি express lane যেটাতে automated passport scanners (CPU support) আছে — সবাই special training ছাড়া use করতে পারে।",
      },

      { type: "h2", id: "containers-vs-vms", title: "Containers vs Virtual Machines" },
      {
        type: "p",
        text: "Containers (যেমন Docker, LXC, Podman) OS level-এ virtualize করে, hardware level-এ না। তারা host kernel share করে কিন্তু processes কে namespaces-এ isolate করে।",
      },
      { type: "h3", title: "Containers vs VMs — Comparison" },
      {
        type: "list",
        items: [
          "Isolation — VM: strong (separate kernels); Container: moderate (shared kernel, namespaced)।",
          "Startup time — VM: seconds থেকে minutes (OS boot); Container: milliseconds (শুধু process start)।",
          "Disk footprint — VM: GBs (full OS + apps); Container: MBs (app + dependencies)।",
          "Performance overhead — VM: small (Type 1) বা moderate (Type 2); Container: very low (near-native)।",
          "Kernel — VM: প্রতিটি VM-এর নিজস্ব kernel; Container: সব containers host kernel share করে।",
          "Guest OS — VM: যেকোনো OS (Linux, Windows, BSD); Container: host kernel-এর সাথে match করতে হবে।",
        ],
      },
      { type: "h3", title: "Container primitives (Linux)" },
      {
        type: "list",
        items: [
          "Namespaces — views isolate করে (PID, network, mount, UTS, IPC, user)।",
          "Cgroups (control groups) — resource usage limit করে (CPU, memory, disk I/O)।",
          "Union filesystems (OverlayFS, AUFS) — efficient, layered images।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Virtual machines হলো detached houses — প্রতিটির নিজস্ব plumbing, electricity, foundation। খুব isolated কিন্তু expensive ও build করতে slow। Containers হলো একই building-এর apartments — central heating, water, elevator (host kernel) share করে, কিন্তু আলাদা doors (namespaces) ও rent control (cgroups) আছে।",
      },
      {
        type: "multi-code",
        filename: "pid_namespace",
        codeSamples: {
          cpp: `#include <iostream>
#include <sched.h>
#include <sys/wait.h>
#include <unistd.h>

// Run a child in a NEW PID namespace (Linux only, needs CAP_SYS_ADMIN).
// The child becomes PID 1 inside its own namespace.
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child: try to enter a new PID + mount namespace
        if (unshare(CLONE_NEWPID | CLONE_NEWNS) == -1) {
            perror("unshare failed");
            _exit(1);
        }
        // After unshare, re-exec ourselves — now PID 1 in new ns
        execl("/bin/echo", "echo", "I am isolated", nullptr);
        _exit(1);
    } else {
        int status;
        waitpid(pid, &status, 0);
        std::cout << "child status=" << status << '\\n';
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
    cmd := exec.Command("/bin/echo", "I am isolated")
    // Ask kernel for a new PID + mount namespace for this child
    cmd.SysProcAttr = &syscall.SysProcAttr{
        Cloneflags: syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
    }
    out, err := cmd.Output()
    if err != nil {
        fmt.Println("err:", err)
        return
    }
    fmt.Println(string(out))
}`,
          python: `import subprocess

# Linux only — child gets its own PID + mount namespace.
# Requires root or CAP_SYS_ADMIN.
proc = subprocess.Popen(
    ["/bin/echo", "I am isolated"],
    stdout=subprocess.PIPE,
    start_new_session=True,  # new session, but not a full namespace
)
out, _ = proc.communicate()
print(out.decode(), end="")`,
          java: `// Java standard library doesn't expose namespace flags.
// Real containers are launched via the Docker / containerd API.
import java.io.*;

public class PidNamespace {
    public static void main(String[] args) throws Exception {
        ProcessBuilder pb = new ProcessBuilder(
            "docker", "run", "--rm", "--pid=host",
            "alpine:3", "echo", "I am isolated");
        pb.inheritIO();
        Process p = pb.start();
        System.out.println("exit=" + p.waitFor());
    }
}`,
        },
      },

      { type: "h2", id: "cloud-models", title: "Cloud Computing Models" },
      {
        type: "p",
        text: "Cloud computing internet-এর মাধ্যমে computing resources deliver করে pay-per-use basis-এ। তিনটি main service model আছে।",
      },
      { type: "h3", title: "IaaS (Infrastructure as a Service)" },
      {
        type: "p",
        text: "Virtual machines, storage, networks, ও অন্যান্য fundamental computing resources provide করে। আপনি OS, applications, ও middleware control করেন। Examples — AWS EC2, Google Compute Engine, Microsoft Azure VMs। Customer responsibility — OS patches, security, application data।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি plot of land rent করা — আপনি যা খুশি build করেন।",
      },
      { type: "h3", title: "PaaS (Platform as a Service)" },
      {
        type: "p",
        text: "একটি platform provide করে যেখানে আপনি applications deploy করেন underlying infrastructure (OS, runtime, middleware, databases) manage না করে। Examples — AWS Elastic Beanstalk, Google App Engine, Heroku। Customer responsibility — application code ও data।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি fully equipped kitchen rent করা — আপনি শুধু ingredients আনেন এবং cook করেন।",
      },
      { type: "h3", title: "SaaS (Software as a Service)" },
      {
        type: "p",
        text: "Internet-এর মাধ্যমে ready-to-use applications provide করে। কোনো installation নেই, infrastructure বা platform manage করা নেই। Examples — Google Workspace (Gmail, Docs), Salesforce, Microsoft 365। Customer responsibility — শুধু user data ও configuration।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant-এ খাওয়া — আপনি শুধু order করেন এবং consume করেন।",
      },
      { type: "h3", title: "Deployment models" },
      {
        type: "list",
        items: [
          "Public cloud — internet-এর উপর shared infrastructure।",
          "Private cloud — একটি organization-এর জন্য dedicated infrastructure।",
          "Hybrid cloud — public ও private clouds combined।",
          "Multi-cloud — একাধিক public cloud providers use করা।",
        ],
      },

      { type: "h2", id: "challenges", title: "Challenges: Isolation, Performance, Security" },
      { type: "h3", title: "Isolation" },
      {
        type: "p",
        text: "VMs strong isolation provide করে (separate kernels)। তবে side-channel attacks (যেমন Spectre, Meltdown) একই physical host-এর VMs-এর মধ্যে information leak করতে পারে।",
      },
      {
        type: "p",
        text: "Containers host kernel share করে। একটি kernel bug বা container escape অন্য containers-কে compromise করতে পারে। Mitigations — seccomp, SELinux, AppArmor, user namespaces, gVisor (sandboxed container runtime)। Real-life thinking — Apartment walls (containers) এর sound isolation separate houses (VMs) এর চেয়ে কম। একটি apartment-এ loud party প্রতিবেশীদের বিরক্ত করে।",
      },
      {
        type: "multi-code",
        filename: "cgroup_limit",
        codeSamples: {
          cpp: `#include <iostream>
#include <fstream>

// Set a memory limit (1 MB) on the current process via cgroups v2.
// Needs root or delegation. Path may vary by distro.
int main() {
    const std::string path =
        "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max";
    std::ofstream f(path);
    if (!f) {
        std::cerr << "Cannot open " << path << '\\n';
        return 1;
    }
    f << "1048576";   // 1 MB limit
    std::cout << "Memory limit set to 1 MB\\n";
    return 0;
}`,
          go: `package main

import "os"

// Set a memory limit (1 MB) on the current process via cgroups v2.
func main() {
    path := "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max"
    err := os.WriteFile(path, []byte("1048576"), 0644)
    if err != nil {
        println("err:", err.Error())
        return
    }
    println("Memory limit set to 1 MB")
}`,
          python: `# Set a memory limit (1 MB) on the current process via cgroups v2.
# Needs root or delegation. Path may vary by distro.
path = "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max"
try:
    with open(path, "w") as f:
        f.write("1048576")   # 1 MB limit
    print("Memory limit set to 1 MB")
except PermissionError as e:
    print("err:", e)`,
          java: `import java.nio.file.*;

// Set a memory limit (1 MB) on the current process via cgroups v2.
public class CgroupLimit {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("/sys/fs/cgroup/user.slice/user-1000.slice/memory.max");
        Files.writeString(p, "1048576");
        System.out.println("Memory limit set to 1 MB");
    }
}`,
        },
      },
      { type: "h3", title: "Performance" },
      {
        type: "list",
        items: [
          "CPU (native) — VMs: ~0-5% (hardware assist সহ); Containers: ~0-1%।",
          "Memory — VMs: fixed per VM (static); Containers: dynamic, copy-on-write।",
          "I/O (disk, network) — VMs: higher (double-buffering); Containers: near-native।",
          "Boot time — VMs: long (OS boot); Containers: instant (process start)।",
        ],
      },
      {
        type: "p",
        text: "Considerations — VMs: mixed-trust workloads, legacy apps, different OSes-এর জন্য ভালো। Containers: microservices, CI/CD, high density-র জন্য ভালো।",
      },
      { type: "h3", title: "Security" },
      {
        type: "p",
        text: "Shared risks (VMs ও containers উভয়ের জন্য) — hypervisor বা kernel vulnerabilities। Misconfigured networking (exposed ports)। Insecure images বা base OS।",
      },
      {
        type: "list",
        items: [
          "VM-specific — hypervisor attacks (VM escape), resource exhaustion (fork bombs অন্যদের affect করে)।",
          "Container-specific — container থেকে host-এ privilege escalation, environment variables-এর মাধ্যমে secret leakage, image supply chain attacks (malicious layers)।",
        ],
      },
      { type: "h3", title: "Best practices" },
      {
        type: "list",
        items: [
          "Hypervisor/host kernel patched রাখো।",
          "Minimal base images use করো (Alpine, Distroless)।",
          "Containers কে non-root হিসেবে run করো, read-only root filesystems সহ।",
          "Secure secrets management use করো (HashiCorp Vault, Kubernetes secrets)।",
          "Micro-segmentation-এর জন্য network policies।",
        ],
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Hypervisor Type 1 — bare-metal, সরাসরি hardware-এ চালে (ESXi, KVM, Hyper-V)।",
          "Hypervisor Type 2 — host OS-এ app হিসেবে চালে (VirtualBox, Workstation)।",
          "Virtualization vs emulation — Virtualization: same ISA, near-native; Emulation: different ISA, slow।",
          "Para-virtualization — guest hypercalls use করতে modify করা; বেশি efficient (Xen)।",
          "Hardware-assisted virt — CPU extensions (VT-x, AMD-V) hypervisors simplify করে এবং performance improve করে।",
          "Containers — OS-level virtualization, host kernel share করে, lightweight (Docker, LXC)।",
          "VMs vs containers — VMs: strong isolation, slower; containers: fast, dense, shared kernel risk।",
          "Cloud IaaS — Infrastructure – VMs, storage, networks (AWS EC2)।",
          "Cloud PaaS — Platform – OS manage না করে apps deploy করা (Heroku, App Engine)।",
          "Cloud SaaS — Software – ready-to-use apps (Gmail, Office 365)।",
          "Challenges — Isolation (side-channel, container escape), performance trade-offs, security hardening।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Virtualization ও cloud computing software build ও deploy করার পদ্ধতিকে transform করেছে। এই concepts বোঝা traditional OS knowledge-কে modern DevOps practices-এর সাথে bridge করে।",
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
        type: "p",
        text: "Real-life thinking — একজন interpreter সহ একটি phone call। আপনি English-এ কথা বলেন (local call); interpreter Japanese-এ translate করে (message), অন্য ব্যক্তি answer করে; interpreter ফিরিয়ে translate করে। আপনাকে language বা phone network details জানতে হবে না।",
      },
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

// ---- Ch 13 - Advanced Topics ----
  {
    id: "os-advanced",
    subject: "os",
    title: "Ch 13 — Advanced Topics",
    bangla: "অ্যাডভান্সড টপিকস",
    difficulty: "Medium",
    est: "Coming Soon",
    summary:
      "এই chapter-এ আলোচনা করা হবে real-time operating systems (RTOS), embedded OS, mobile OS, multicore scheduling, GPU computing, ও energy-aware scheduling। Content এখন প্রস্তুত হচ্ছে — শীঘ্রই আসছে।",
    sections: [
      {
        type: "p",
        text: "🚧 এই chapter-এর content এখন প্রস্তুত হচ্ছে। আমরা শীঘ্রই এখানে real-time operating systems (RTOS), embedded OS, mobile OS, multicore scheduling, GPU computing, ও energy-aware scheduling নিয়ে বিস্তারিত আলোচনা যোগ করব — Bangla + English technical terms এ, real-life examples ও multi-language code (C++/Go/Python/Java) সহ।",
      },
      {
        type: "p",
        text: "প্রতিটি chapter-এর মতো এখানেও একই format থাকবে — Maximum Bangla + English technical terms, real-life human-thinking examples, এবং প্রতিটি কোড sample চারটি ভাষায়। আপাতত নিচের একটি overview দেখুন এই chapter-এ যা যা থাকবে।",
      },
      { type: "h3", title: "এই chapter-এ যা যা থাকবে" },
      {
        type: "list",
        items: [
          "Real-Time Operating Systems (RTOS) — VxWorks, FreeRTOS, Zephyr, QNX। Hard vs soft real-time, Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF)।",
          "Embedded Operating Systems — Embedded Linux, NuttX, TinyOS। Small footprint, low power, resource-constrained devices।",
          "Mobile Operating Systems — Android, iOS। Power-aware, touch-centric, app sandboxing।",
          "Multicore / NUMA-aware OS — Linux CFS + scheduler domains, EEVDF (Linux 6.6+)।",
          "GPU / Heterogeneous Computing — CUDA runtime, ROCm, GPU scheduling।",
          "Energy-Aware Scheduling — DVFS (Dynamic Voltage and Frequency Scaling), big.LITTLE, EAS (Energy Aware Scheduling)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: এই chapter-টি শীঘ্রই আসছে। ততক্ষণ আগের চ্যাপ্টারগুলো (Ch 01 – Ch 12) ভালোভাবে পড়ুন — এই advanced topics গুলো সেই fundamentals-এর উপর built।",
      },
    ],
  },
];
