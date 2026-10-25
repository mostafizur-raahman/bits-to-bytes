#!/usr/bin/env python3
"""
Rewrite Ch 09 (I/O System) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch9_marker_start = "// ---- Ch 09 - I/O System ----"
ch10_marker_start = "// ---- Ch 10 - Protection & Security ----"

start_idx = text.find(ch9_marker_start)
assert start_idx != -1, "Ch 09 marker not found"
end_idx = text.find(ch10_marker_start, start_idx)
assert end_idx != -1, "Ch 10 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH9 = r'''// ---- Ch 09 - I/O System ----
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

'''

new_text = before + NEW_CH9 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 09 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
