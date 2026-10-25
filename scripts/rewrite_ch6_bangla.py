#!/usr/bin/env python3
"""
Rewrite Ch 06 (Memory Management) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch6_marker_start = "// ---- Ch 06 - Memory Management ----"
ch7_marker_start = "// ---- Ch 07 - Virtual Memory ----"

start_idx = text.find(ch6_marker_start)
assert start_idx != -1, "Ch 06 marker not found"
end_idx = text.find(ch7_marker_start, start_idx)
assert end_idx != -1, "Ch 07 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH6 = r'''// ---- Ch 06 - Memory Management ----
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

'''

new_text = before + NEW_CH6 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 06 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
