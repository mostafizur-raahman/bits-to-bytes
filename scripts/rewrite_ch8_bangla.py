#!/usr/bin/env python3
"""
Rewrite Ch 08 (File System) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch8_marker_start = "// ---- Ch 08 - File System ----"
ch9_marker_start = "// ---- Ch 09 - I/O System ----"

start_idx = text.find(ch8_marker_start)
assert start_idx != -1, "Ch 08 marker not found"
end_idx = text.find(ch9_marker_start, start_idx)
assert end_idx != -1, "Ch 09 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH8 = r'''// ---- Ch 08 - File System ----
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

'''

new_text = before + NEW_CH8 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 08 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
