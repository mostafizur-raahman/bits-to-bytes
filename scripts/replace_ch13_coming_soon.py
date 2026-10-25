#!/usr/bin/env python3
"""
Replace Ch 13 (Advanced Topics) with a 'Content Coming Soon' placeholder.
When user clicks Ch 13, they see a nicely designed 'coming soon' message
instead of actual content.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch13_marker_start = "// ---- Ch 13 - Advanced Topics ----"
# Ch 13 is the last topic, so we need to find the end of the TOPICS array
topics_end_marker = "\n];\n\nexport const PROJECTS"

start_idx = text.find(ch13_marker_start)
assert start_idx != -1, "Ch 13 marker not found"
end_idx = text.find(topics_end_marker, start_idx)
assert end_idx != -1, "TOPICS array end not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH13 = r'''// ---- Ch 13 - Advanced Topics ----
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
'''

new_text = before + NEW_CH13 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 13 replaced with 'Content Coming Soon' placeholder. File size: {len(new_text)} bytes")
