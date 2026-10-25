#!/usr/bin/env python3
"""
Rewrite Ch 07 (Virtual Memory) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch7_marker_start = "// ---- Ch 07 - Virtual Memory ----"
ch8_marker_start = "// ---- Ch 08 - File System ----"

start_idx = text.find(ch7_marker_start)
assert start_idx != -1, "Ch 07 marker not found"
end_idx = text.find(ch8_marker_start, start_idx)
assert end_idx != -1, "Ch 08 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH7 = r'''// ---- Ch 07 - Virtual Memory ----
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

'''

new_text = before + NEW_CH7 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 07 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
