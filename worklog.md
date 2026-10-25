---
Task ID: heap-expand
Agent: main (GLM)
Task: Expand the Heap / Priority Queue topic in src/lib/content/dsa.ts from overview-only to a full 5-problem NeetCode chapter (Brute force → Optimal) in C++ / Go / Python / Java with Max Bangla + English pattern.

Work Log:
- Located the existing overview-only Heap / Priority Queue topic at line 5355 in /home/z/my-project/src/lib/content/dsa.ts (originally ~13 lines).
- Studied the fully-built Backtracking topic (lines 4588–5353) to mirror the exact section structure: Overview → Problem N (h2 + p problem statement + h3 brute force + multi-code + h3 optimal + multi-code + h3 Complexity Comparison list) → Chapter Summary → tip callout.
- Persisted the generator script to /home/z/my-project/scripts/expand_heap_section.py (per Rule 9 — Script Persistence).
- Wrote 5 NeetCode Heap / Priority Queue problems with full brute-force AND optimal code in 4 languages each (40 code samples total):
  1. Kth Largest Element in a Stream (Easy) — min-heap of size k
  2. Last Stone Weight (Easy) — max-heap simulation, two extract + push diff
  3. K Closest Points to Origin (Medium) — max-heap of size k (opposite-heap pattern), plus Quickselect note
  4. Task Scheduler (Medium) — math formula (max_freq - 1) × (n + 1) + count_of_max_freq, plus heap+queue alternative
  5. Find Median from Data Stream (Hard) — Two-Heaps pattern (lower max-heap + upper min-heap)
- Each problem includes Max Bangla + English explanations, real-life analogies (ER queue, coin change style), key insight paragraphs, brute-force complexity, optimal complexity, and complexity comparison lists.
- Chapter Summary includes the core mantras: "top k → opposite heap of size k", "median/stream → two heaps balance".
- Ran the script; file grew from 5498 → 6227 lines.
- Verified no NEW TypeScript errors introduced (7 pre-existing TS2322 errors on sections arrays of prior topics — same pattern as Backtracking which already runs in production).

Stage Summary:
- Heap / Priority Queue topic now has full 5-problem coverage matching NeetCode roadmap.
- Content pattern consistent with existing Backtracking chapter (Brute → Optimal → Complexity Comparison per problem).
- Multi-language code (C++ / Go / Python / Java) with proper idiomatic heap APIs (priority_queue, container/heap, heapq, PriorityQueue).
- Remaining DSA topics still overview-only: Graphs, 1-D DP, Intervals, Greedy, Advanced Graphs, 2-D DP, Bit Manipulation, Math & Geometry (8 topics).
- Persisted generator script: /home/z/my-project/scripts/expand_heap_section.py (recoverable artifact for future tweaks).
