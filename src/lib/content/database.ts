import type { Topic } from "./types";

export const DB_TOPICS: Topic[] = [
// ---- Ch 01 - Core Concepts & Architecture ----
  {
    id: "db-intro",
    subject: "db",
    title: "Ch 01 — Core Concepts & Architecture",
    bangla: "কোর কনসেপ্টস ও আর্কিটেকচার",
    difficulty: "Easy",
    est: "1.5 hr",
    summary: "Data vs information, file systems vs DBMS, 3-schema architecture, data independence, ও data models।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "এই chapter-এ database-এর fundamental concepts cover করা হয়েছে। Data vs Information, File Systems vs DBMS, 3-Schema Architecture, Data Independence, ও Data Models।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের chapter-এ relational database concepts নিয়ে আলোচনা করা হবে।" },
    ],
  },

  // ---- Ch 02 - Relational Database Concepts ----
  {
    id: "db-relational",
    subject: "db",
    title: "Ch 02 — Relational Database Concepts",
    bangla: "রিলেশনাল ডেটাবেস কনসেপ্টস",
    difficulty: "Medium",
    est: "2 hr",
    summary: "Tables, keys, ER modeling, integrity constraints, ও relational algebra।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Tables & Structure, Types of Keys, ER Modeling, Integrity Constraints, ও Relational Algebra। SQL ও MySQL code সহ।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের chapter-এ normalization ও database design নিয়ে আলোচনা করা হবে।" },
    ],
  },

  // ---- Ch 03 - Normalization & Database Design ----
  {
    id: "db-normalization",
    subject: "db",
    title: "Ch 03 — Normalization & Database Design",
    bangla: "নরমালাইজেশন ও ডেটাবেস ডিজাইন",
    difficulty: "Hard",
    est: "2 hr",
    summary: "Functional dependency, normal forms (1NF, 2NF, 3NF, BCNF), ও denormalization।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Functional Dependency, Normal Forms (1NF, 2NF, 3NF, BCNF), ও Denormalization। SQL ও MySQL code সহ।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের chapter-ে SQL-র সম্পূর্ণ overview নিয়ে আলোচনা করা হবে।" },
    ],
  },

  // ---- Ch 04 - Structured Query Language (SQL) ----
  {
    id: "db-sql",
    subject: "db",
    title: "Ch 04 — Structured Query Language (SQL)",
    bangla: "স্ট্রাকচার্ড কোয়েরি ল্যাঙ্গুয়েজ (SQL)",
    difficulty: "Medium",
    est: "3 hr",
    summary: "DDL, DML, DQL, DCL, TCL, joins, subqueries, ও aggregate functions।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "DDL (CREATE, ALTER, DROP, TRUNCATE), DML (INSERT, UPDATE, DELETE), DQL (SELECT, WHERE, ORDER BY, GROUP BY), DCL (GRANT, REVOKE), TCL (COMMIT, ROLLBACK), Joins, Subqueries, ও Aggregate Functions। Standard SQL ও MySQL code সহ।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের chapter-ে transactions ও concurrency control নিয়ে আলোচনা করা হবে।" },
    ],
  },

  // ---- Ch 05 - Transactions & Concurrency Control ----
  {
    id: "db-transactions",
    subject: "db",
    title: "Ch 05 — Transactions & Concurrency Control",
    bangla: "ট্রানজেকশনস ও কনকারেন্সি কন্ট্রোল",
    difficulty: "Hard",
    est: "2 hr",
    summary: "ACID properties, concurrency issues (dirty reads, non-repeatable reads, phantom reads), ও locking/MVCC।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "ACID Properties, Concurrency Issues (dirty read, non-repeatable read, phantom read), Locking (shared/exclusive), ও MVCC (Multi-Version Concurrency Control)। SQL ও MySQL code সহ।" },
      { type: "callout", calloutTone: "tip", text: "Tip: এই chapter-এর পরে database fundamentals-এর সম্পূর্ণ overview complete হয়।" },
    ],
  }
];
