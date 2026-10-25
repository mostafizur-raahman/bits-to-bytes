import type { SubjectId, Subject, CheatsheetId } from "./types";

export const SUBJECTS: Subject[] = [
  {
    id: "dsa",
    name: "DSA Fundamentals",
    bangla: "ডাটা স্ট্রাকচার ও অ্যালগরিদম",
    color: "lime",
    blurb: "Arrays, trees, graphs, recursion, dynamic programming & Big-O.",
  },
  {
    id: "db",
    name: "Database Fundamentals",
    bangla: "ডেটাবেস",
    color: "sky",
    blurb: "SQL, joins, normalization, indexing, transactions & ACID.",
  },
  {
    id: "net",
    name: "Networking Fundamentals",
    bangla: "নেটওয়ার্কিং",
    color: "pink",
    blurb: "OSI / TCP-IP, routing, DNS, HTTP, sockets & TCP handshake.",
  },
  {
    id: "os",
    name: "OS Fundamentals",
    bangla: "অপারেটিং সিস্টেম",
    color: "amber",
    blurb:
      "13 chapters covering OS fundamentals — intro, process mgmt, scheduling, sync, deadlocks, memory, VM, FS, I/O, security, virtualization, distributed OS, advanced.",
  },
];

export const SUBJECT_COLORS: Record<SubjectId, "lime" | "sky" | "pink" | "amber"> =
  {
    dsa: "lime",
    db: "sky",
    net: "pink",
    os: "amber",
  };