#!/usr/bin/env python3
"""
Replace entire DATABASE section with 5 new chapters (Maximum Bangla + English terms).
Also add a PostgreSQL Big Data Lab project.

Chapters:
  Ch 01 — Core Concepts & Architecture
  Ch 02 — Relational Database Concepts
  Ch 03 — Normalization & Database Design
  Ch 04 — Structured Query Language (SQL)
  Ch 05 — Transactions & Concurrency Control

Each chapter has SQL + MySQL code, real-life analogies in Bangla.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# ============ STEP 1: Replace DB section ============
db_marker = "/* ============== DATABASE ============== */"
net_marker = "/* ============== NETWORKING ============== */"

db_start = text.find(db_marker)
assert db_start != -1, "DB marker not found"
net_start = text.find(net_marker, db_start)
assert net_start != -1, "Networking marker not found"

before = text[:db_start]
after = text[net_start:]

NEW_DB_SECTION = r'''/* ============== DATABASE ============== */

  // ---- Ch 01 - Core Concepts & Architecture ----
  {
    id: "db-intro",
    subject: "db",
    title: "Ch 01 — Core Concepts & Architecture",
    bangla: "কোর কনসেপ্টস ও আর্কিটেকচার",
    difficulty: "Easy",
    est: "1.5 hr",
    summary:
      "এই chapter-এ database-এর fundamental concepts — data vs information, file systems vs DBMS, 3-schema architecture, data independence, ও data models cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "data-vs-info", title: "Data vs Information" },
      {
        type: "p",
        text: "Data হলো raw facts — unprocessed numbers, text, images যেগুলো একা অর্থবহ নয়। Information হলো processed data — data-কে organize ও interpret করে meaningful output তৈরি করা হয়। উদাহরণ — '25', 'Rahim', 'Dhaka' এগুলো data। কিন্তু 'Rahim, 25 বছর, Dhaka-তে থাকে' — এটি information কারণ এটি meaningful ও actionable।",
      },
      {
        type: "p",
        text: "Real-life thinking — data হলো কাঁচামালি (flour, sugar, eggs)। Information হলো তৈরি করা cake। কাঁচামালি একা খাওয়া যায় না, কিন্তু সেগুলো process করে cake বানালে সবাই খেতে পারে।",
      },

      { type: "h2", id: "file-vs-dbms", title: "File Systems vs DBMS" },
      {
        type: "p",
        text: "Flat-file systems-এ data text files বা spreadsheets-এ store থাকে। এর limitations গুলো হলো — Data redundancy (একই data একাধিক জায়গায় repeat হয়), Data inconsistency (এক place-এ update হলে অন্য place-এ update হয় না), Difficulty in accessing data (programming knowledge প্রয়োজন), ও No concurrency control (একাধিক users একসাথে modify করলে data corrupt হতে পারে)।",
      },
      {
        type: "p",
        text: "DBMS (Database Management System) এই সব problems solve করে। এটি centralized data storage, controlled access, ও data integrity provide করে। উদাহরণ — MySQL, PostgreSQL, Oracle, MongoDB।",
      },
      {
        type: "p",
        text: "Real-life thinking — file system হলো প্রতিটি room-এ আলাদা আলাদা notebook-এ লেখা। কেউ এক notebook-এ পুরোনো address update করলে, অন্য notebook-এ পুরোনো address থেকে যায় (inconsistency)। DBMS হলো একটি central filing cabinet — সব data এক জায়গায়, সব update একসাথে হয়।",
      },

      { type: "h2", id: "schema-arch", title: "3-Schema Architecture" },
      {
        type: "p",
        text: "Database design-এ তিনটি level আছে — Internal (physical) level: data কীভাবে disk-এ store হয় (file structures, indexes)। Conceptual (logical) level: সম্পূর্ণ database-এর logical structure (tables, relationships)। External (user view) level: প্রতিটি user বা application যা দেখে (specific views, reports)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant। Internal level হলো kitchen-এর layout (stove কোথায়, fridge কোথায়)। Conceptual level হলো menu (কোন dishes available)। External level হলো customer-এর order slip (শুধু তার order দেখে)।",
      },
      {
        type: "h2",
        id: "data-independence",
        title: "Data Independence",
      },
      {
        type: "p",
        text: "Physical data independence — internal schema change করলেও conceptual schema affected হয় না (যেমন index যোগ করলেও application code change করতে হবে না)। Logical data independence — conceptual schema change করলেও external schema affected হয় না (যেমন নতুন column যোগ করলেও পুরোনো views কাজ করবে)।",
      },
      {
        type: "h2",
        id: "data-models",
        title: "Data Models",
      },
      {
        type: "list",
        items: [
          "Hierarchical — tree structure, parent-child relationship (XML, early IBM IMS)।",
          "Network — graph structure, many-to-many relationships (early IDMS)।",
          "Relational — tables (relations), rows ও columns (MySQL, PostgreSQL, Oracle) — সবচেয়ে common।",
          "Object-Oriented — objects ও classes store (ObjectDB, db4o)।",
          "Hybrid/NoSQL — document, key-value, column-family, graph (MongoDB, Redis, Cassandra, Neo4j)।",
        ],
      },
      {
        type: "h2",
        id: "summary",
        title: "Chapter Summary",
      },
      {
        type: "list",
        items: [
          "Data = raw facts; Information = processed, meaningful output।",
          "File systems-এ redundancy ও inconsistency problem; DBMS solve করে।",
          "3-Schema Architecture — Internal (physical), Conceptual (logical), External (user view)।",
          "Data Independence — physical ও logical।",
          "Data Models — Hierarchical, Network, Relational (most common), Object-Oriented, NoSQL।",
        ],
      },
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
    summary:
      "এই chapter-ে relational database-এর core concepts — tables, keys, ER modeling, integrity constraints, ও relational algebra cover করা হয়েছে। SQL ও MySQL code সহ।",
    sections: [
      { type: "h2", id: "tables", title: "Tables & Structure" },
      {
        type: "p",
        text: "Relational database-এ data tables (relations)-এ store থাকে। Tuple (row) — একটি single record। Attribute (column) — একটি property বা field। Domain — একটি attribute-এর সম্ভাব্য values। Instance — একটি নির্দিষ্ট সময়ে table-এর সম্পূর্ণ data।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Table creation (Standard SQL / MySQL)
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    age INT CHECK (age >= 0),
    dept_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MySQL specific: ENGINE ও CHARSET
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    age INT,
    dept_id INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert data
INSERT INTO students (name, email, age, dept_id)
VALUES ('Rahim', 'rahim@example.com', 22, 1),
       ('Karim', 'karim@example.com', 23, 2),
       ('Fatima', 'fatima@example.com', 21, 1);

-- View all data
SELECT * FROM students;`,
      },
      {
        type: "p",
        text: "Real-life thinking — একটি spreadsheet। প্রতিটি sheet একটি table। প্রতিটি row একজন student-এর তথ্য। প্রতিটি column একটি property (name, email, age)। Domain হলো সম্ভাব্য values — age column-এ শুধু positive integers থাকতে পারে।",
      },

      { type: "h2", id: "keys", title: "Types of Keys" },
      {
        type: "list",
        items: [
          "Primary Key — প্রতিটি row কে uniquely identify করে (NOT NULL + UNIQUE)। যেমন id।",
          "Foreign Key — অন্য table-এর primary key-এর reference। যেমন dept_id departments table-কে refer করে।",
          "Candidate Key — যেকোনো attribute যা unique হতে পারে (email, id উভয়ই candidate)।",
          "Super Key — এক বা একাধিক attribute যা uniquely identify করে (id+name একটি super key)।",
          "Alternate Key — candidate key যা primary key হিসেবে choose করা হয়নি (email)।",
          "Composite Key — একাধিক column combine করে তৈরি key (dept_id + student_id)।",
          "Unique Key — UNIQUE constraint সহ column, NULL allowed।",
        ],
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Foreign key example (Standard SQL / MySQL)
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- MySQL: show table structure
DESCRIBE students;
-- Standard SQL equivalent
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'students';`,
      },
      {
        type: "p",
        text: "Real-life thinking — একটি school-এ প্রতিটি student-এর একটি roll number আছে (primary key)। প্রতিটি student একটি class-এ belong করে (foreign key যা class table-কে refer করে)। একজন student-কে email দিয়েও uniquely identify করা যায় (alternate key)।",
      },

      { type: "h2", id: "er-modeling", title: "Entity-Relationship (ER) Modeling" },
      {
        type: "p",
        text: "ER modeling হলো database design-এর একটি visual approach। Entity — একটি real-world object বা concept (Student, Course, Teacher)। Attribute — entity-এর property (name, email)। Relationship — entities-এর মধ্যে association (Student enrolls in Course)।",
      },
      { type: "h3", title: "Mapping Cardinalities" },
      {
        type: "list",
        items: [
          "1:1 (One-to-One) — একজন student-এর একটি library card।",
          "1:N (One-to-Many) — একটি department-এ অনেক students।",
          "N:M (Many-to-Many) — অনেক students অনেক courses নেয় (junction table দিয়ে implement)।",
        ],
      },
      {
        type: "code",
        lang: "sql",
        text: `-- 1:N relationship — department has many students
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- N:M relationship — students enroll in courses (junction table)
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- MySQL: insert data
INSERT INTO departments VALUES (1, 'CSE', 'Computer Science');
INSERT INTO students VALUES (101, 'Rahim', 1);
INSERT INTO courses VALUES (501, 'Database Systems');
INSERT INTO enrollments VALUES (101, 501, '2026-01-15');`,
      },

      { type: "h2", id: "integrity", title: "Integrity Constraints" },
      {
        type: "list",
        items: [
          "Entity Integrity — primary key NULL হতে পারবে না ও unique হতে হবে।",
          "Referential Integrity — foreign key শুধু এমন value নিতে পারে যা referenced table-এ exists করে, অথবা NULL।",
          "Domain Integrity — প্রতিটি attribute তার defined domain থেকে value নেবে (CHECK, NOT NULL, DEFAULT)।",
        ],
      },

      { type: "h2", id: "relational-algebra", title: "Relational Algebra" },
      {
        type: "list",
        items: [
          "Selection (σ) — rows filter করে condition দিয়ে (WHERE clause)।",
          "Projection (π) — specific columns select করে (SELECT col1, col2)।",
          "Union (∪) — দুটি table-এর সব rows combine করে (UNION)।",
          "Set Difference (−) — প্রথম table-এ আছে কিন্তু দ্বিতীয়-তে নেই (EXCEPT)।",
          "Cartesian Product (×) — দুটি table-এর সব combination (CROSS JOIN)।",
          "Join (⋈) — related rows combine করে (INNER JOIN, LEFT JOIN)।",
        ],
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Selection (σ) — filter rows
SELECT * FROM students WHERE age > 20;

-- Projection (π) — select columns
SELECT name, email FROM students;

-- Union (∪) — combine results
SELECT name FROM students WHERE dept_id = 1
UNION
SELECT name FROM students WHERE dept_id = 2;

-- Join (⋈) — combine related tables
SELECT s.name, d.dept_name
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id;

-- MySQL: multiple joins
SELECT s.name, c.course_name, e.enrollment_date
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE d.dept_name = 'CSE';  -- note: alias d not defined here`,
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Tables (relations) — rows (tuples) ও columns (attributes) নিয়ে গঠিত।",
          "Keys — Primary, Foreign, Candidate, Super, Alternate, Composite, Unique।",
          "ER Modeling — entities, attributes, relationships, cardinalities (1:1, 1:N, N:M)।",
          "Integrity Constraints — entity, referential, domain।",
          "Relational Algebra — selection, projection, union, set difference, Cartesian product, joins।",
        ],
      },
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
    summary:
      "এই chapter-ে functional dependency, normal forms (1NF, 2NF, 3NF, BCNF), ও denormalization cover করা হয়েছে। SQL ও MySQL code সহ।",
    sections: [
      { type: "h2", id: "functional-dep", title: "Functional Dependency" },
      {
        type: "p",
        text: "Functional dependency হলো দুটি attributes-এর মধ্যে relationship — যেখানে একটি attribute-এর value অন্য attribute-এর value determine করে। উদাহরণ — student_id → name (student_id জানলে name জানা যায়)।",
      },
      {
        type: "list",
        items: [
          "Full dependency — non-key attribute সম্পূর্ণ primary key-এর উপর depend করে (composite key-এর কোনো part-এ নয়)।",
          "Partial dependency — non-key attribute composite key-ের একটি part-এর উপর depend করে (2NF-এ remove করতে হবে)।",
          "Transitive dependency — A → B ও B → C, তাহলে A → C (3NF-এ remove করতে হবে)।",
        ],
      },

      { type: "h2", id: "normal-forms", title: "Normal Forms" },
      {
        type: "p",
        text: "Normalization হলো database-কে এমনভাবে design করা যাতে data redundancy ও update anomalies (insertion, deletion, modification) কমে।",
      },

      { type: "h3", title: "1NF (First Normal Form)" },
      {
        type: "p",
        text: "প্রতিটি column-এ atomic (single) value থাকতে হবে। কোনো repeating groups বা arrays নয়। প্রতিটি row unique হতে হবে (primary key প্রয়োজন)।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Before 1NF: phone column has multiple values
CREATE TABLE bad_students (
    id INT,
    name VARCHAR(100),
    phones VARCHAR(200)  -- "017xxx, 018xxx, 019xxx" — NOT atomic!
);

-- After 1NF: separate table for phones
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE student_phones (
    student_id INT,
    phone VARCHAR(15),
    PRIMARY KEY (student_id, phone),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- MySQL insert
INSERT INTO students VALUES (1, 'Rahim');
INSERT INTO student_phones VALUES (1, '01711111111'), (1, '01822222222');`,
      },

      { type: "h3", title: "2NF (Second Normal Form)" },
      {
        type: "p",
        text: "1NF-এ থাকতে হবে ও কোনো partial dependency নেই — অর্থাৎ সব non-key attributes সম্পূর্ণ primary key-এর উপর depend করে (composite key-ের কোনো part-এ নয়)।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Before 2NF: composite key (student_id, course_id), but
-- course_name depends only on course_id (partial dependency)
CREATE TABLE bad_enrollments (
    student_id INT,
    course_id INT,
    course_name VARCHAR(100),  -- depends on course_id only!
    student_name VARCHAR(100),  -- depends on student_id only!
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id)
);

-- After 2NF: separate tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);`,
      },

      { type: "h3", title: "3NF (Third Normal Form)" },
      {
        type: "p",
        text: "2NF-এ থাকতে হবে ও কোনো transitive dependency নেই — অর্থাৎ কোনো non-key attribute অন্য কোনো non-key attribute-এর উপর depend করে না।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Before 3NF: dept_name depends on dept_id, not directly on student_id
CREATE TABLE bad_students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    dept_name VARCHAR(50),  -- transitively depends on student_id via dept_id
    dept_location VARCHAR(100)  -- same
);

-- After 3NF: move department info to separate table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    dept_location VARCHAR(100)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);`,
      },

      { type: "h3", title: "BCNF (Boyce-Codd Normal Form)" },
      {
        type: "p",
        text: "3NF-এর একটি stricter version। প্রতিটি determinant একটি candidate key হতে হবে। উদাহরণ — যদি A → B হয়, তাহলে A অবশ্যই একটি super key হতে হবে। BCNF 3NF-এর চেয়ে কঠোর কিন্তু বাস্তবে কদাচিৎ 3NF-এর চেয়ে আলাদা হয়।",
      },

      { type: "h2", id: "denormalization", title: "Denormalization" },
      {
        type: "p",
        text: "Denormalization হলো normalization-এর উল্টো — ইচ্ছাকৃতভাবে redundancy যোগ করা read performance improve করার জন্য। যখন read-heavy workloads-এ অনেক joins expensive হয়, তখন denormalization strategically use করা যায়। trade-off — writes slower হয় কিন্তু reads faster।",
      },
      {
        type: "p",
        text: "Real-life thinking — normalization হলো প্রতিটি জিনিস তার সঠিক জায়গায় রাখা (kitchen-এ পাত্র, bedroom-এ বিছানা)। Denormalization হলো প্রায় ব্যবহৃত জিনিসগুলো কাছে রাখা (TV remote coffee table-এ)। বেশি কাজ করতে হয় ঠিক রাখতে কিন্তু ব্যবহার করতে সহজ।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Functional Dependency — full, partial, transitive।",
          "1NF — atomic values, no repeating groups।",
          "2NF — 1NF + no partial dependency।",
          "3NF — 2NF + no transitive dependency।",
          "BCNF — stricter 3NF, every determinant must be a candidate key।",
          "Denormalization — strategic redundancy for read performance।",
        ],
      },
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
    summary:
      "এই chapter-ে SQL-র সম্পূর্ণ overview — DDL, DML, DQL, DCL, TCL, joins, subqueries, ও aggregate functions cover করা হয়েছে। Standard SQL ও MySQL code সহ।",
    sections: [
      { type: "h2", id: "ddl", title: "DDL (Data Definition Language)" },
      {
        type: "p",
        text: "DDL database structure define ও modify করতে use হয়। Commands — CREATE, ALTER, DROP, TRUNCATE।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- CREATE: table, database, index
CREATE DATABASE IF NOT EXISTS university;
USE university;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    gpa DECIMAL(3,2) DEFAULT 0.00,
    enrolled DATE DEFAULT (CURRENT_DATE)
);

-- MySQL: specify engine
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    gpa DECIMAL(3,2) DEFAULT 0.00
) ENGINE=InnoDB;

-- ALTER: modify table structure
ALTER TABLE students ADD COLUMN phone VARCHAR(15);
ALTER TABLE students MODIFY COLUMN email VARCHAR(320);
ALTER TABLE students DROP COLUMN phone;
ALTER TABLE students RENAME TO university_students;

-- DROP: delete table (structure + data)
DROP TABLE IF EXISTS university_students;

-- TRUNCATE: delete all data, keep structure
TRUNCATE TABLE students;`,
      },

      { type: "h2", id: "dml", title: "DML (Data Manipulation Language)" },
      {
        type: "code",
        lang: "sql",
        text: `-- INSERT
INSERT INTO students (name, email, gpa)
VALUES ('Rahim', 'rahim@example.com', 3.75),
       ('Karim', 'karim@example.com', 3.50),
       ('Fatima', 'fatima@example.com', 3.90);

-- MySQL: INSERT ... ON DUPLICATE KEY UPDATE (upsert)
INSERT INTO students (id, name, email, gpa)
VALUES (1, 'Rahim', 'rahim@example.com', 3.80)
ON DUPLICATE KEY UPDATE gpa = 3.80;

-- UPDATE
UPDATE students SET gpa = 3.85 WHERE name = 'Rahim';
UPDATE students SET gpa = gpa + 0.1 WHERE gpa < 3.5;

-- DELETE
DELETE FROM students WHERE gpa < 2.0;
DELETE FROM students;  -- delete all (can rollback)`,
      },

      { type: "h2", id: "dql", title: "DQL (Data Query Language)" },
      {
        type: "code",
        lang: "sql",
        text: `-- SELECT with WHERE
SELECT name, email, gpa FROM students
WHERE gpa >= 3.5 AND enrolled > '2025-01-01';

-- ORDER BY
SELECT * FROM students ORDER BY gpa DESC, name ASC;

-- GROUP BY with aggregate
SELECT dept_id, COUNT(*) AS total, AVG(gpa) AS avg_gpa
FROM students
GROUP BY dept_id
HAVING AVG(gpa) > 3.0;

-- LIMIT (MySQL / PostgreSQL)
SELECT * FROM students ORDER BY gpa DESC LIMIT 10;

-- MySQL: LIMIT with offset for pagination
SELECT * FROM students ORDER BY id LIMIT 20 OFFSET 40;  -- page 3

-- DISTINCT
SELECT DISTINCT dept_id FROM students;

-- CASE expression
SELECT name,
    CASE
        WHEN gpa >= 3.7 THEN 'A'
        WHEN gpa >= 3.0 THEN 'B'
        WHEN gpa >= 2.0 THEN 'C'
        ELSE 'F'
    END AS grade
FROM students;`,
      },

      { type: "h2", id: "dcl-tcl", title: "DCL & TCL" },
      {
        type: "code",
        lang: "sql",
        text: `-- DCL (Data Control Language)
GRANT SELECT, INSERT ON university.students TO 'app_user'@'localhost';
REVOKE INSERT ON university.students FROM 'app_user'@'localhost';
GRANT ALL PRIVILEGES ON university.* TO 'admin'@'localhost';

-- MySQL: create user
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_pass';
GRANT SELECT, INSERT, UPDATE ON university.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;

-- TCL (Transaction Control Language)
START TRANSACTION;
INSERT INTO students (name, email, gpa) VALUES ('Sadia', 'sadia@example.com', 3.65);
UPDATE students SET gpa = gpa + 0.1 WHERE name = 'Karim';
COMMIT;  -- save changes

-- Or rollback if something went wrong
START TRANSACTION;
DELETE FROM students WHERE gpa < 1.0;
ROLLBACK;  -- undo the delete

-- SAVEPOINT: partial rollback
START TRANSACTION;
INSERT INTO students (name, email) VALUES ('Test1', 't1@example.com');
SAVEPOINT sp1;
INSERT INTO students (name, email) VALUES ('Test2', 't2@example.com');
ROLLBACK TO sp1;  -- undo only Test2
COMMIT;  -- Test1 stays`,
      },

      { type: "h2", id: "joins", title: "Joins & Subqueries" },
      {
        type: "code",
        lang: "sql",
        text: `-- INNER JOIN: matching rows only
SELECT s.name, d.dept_name
FROM students s
INNER JOIN departments d ON s.dept_id = d.dept_id;

-- LEFT JOIN: all from left, matching from right
SELECT s.name, d.dept_name
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id;
-- students without dept show NULL for dept_name

-- RIGHT JOIN: all from right, matching from left
SELECT s.name, d.dept_name
FROM students s
RIGHT JOIN departments d ON s.dept_id = d.dept_id;

-- FULL OUTER JOIN (Standard SQL)
SELECT s.name, d.dept_name
FROM students s
FULL OUTER JOIN departments d ON s.dept_id = d.dept_id;

-- MySQL does not support FULL OUTER JOIN directly.
-- Workaround: UNION of LEFT and RIGHT joins
SELECT s.name, d.dept_name
FROM students s
LEFT JOIN departments d ON s.dept_id = d.dept_id
UNION
SELECT s.name, d.dept_name
FROM students s
RIGHT JOIN departments d ON s.dept_id = d.dept_id;

-- Self join: employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Subquery (nested query)
SELECT name, gpa FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);

-- Correlated subquery
SELECT s.name,
    (SELECT COUNT(*) FROM enrollments e
     WHERE e.student_id = s.id) AS course_count
FROM students s;

-- EXISTS subquery
SELECT name FROM students s
WHERE EXISTS (
    SELECT 1 FROM enrollments e
    WHERE e.student_id = s.id
);`,
      },

      { type: "h2", id: "aggregates", title: "Aggregate Functions" },
      {
        type: "code",
        lang: "sql",
        text: `-- COUNT
SELECT COUNT(*) AS total_students FROM students;
SELECT COUNT(gpa) AS students_with_gpa FROM students;
SELECT COUNT(DISTINCT dept_id) AS departments FROM students;

-- SUM, AVG, MIN, MAX
SELECT
    SUM(gpa) AS total_gpa,
    AVG(gpa) AS avg_gpa,
    MIN(gpa) AS min_gpa,
    MAX(gpa) AS max_gpa
FROM students;

-- GROUP BY with HAVING
SELECT dept_id,
    COUNT(*) AS student_count,
    AVG(gpa) AS avg_gpa,
    MAX(gpa) AS top_gpa
FROM students
GROUP BY dept_id
HAVING COUNT(*) > 10
ORDER BY avg_gpa DESC;

-- MySQL: GROUP_CONCAT (aggregate strings)
SELECT dept_id, GROUP_CONCAT(name SEPARATOR ', ') AS all_names
FROM students
GROUP BY dept_id;`,
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "DDL — CREATE, ALTER, DROP, TRUNCATE (structure define করে)।",
          "DML — INSERT, UPDATE, DELETE (data manipulate করে)।",
          "DQL — SELECT, WHERE, ORDER BY, GROUP BY, HAVING (data query করে)।",
          "DCL — GRANT, REVOKE (access control)।",
          "TCL — COMMIT, ROLLBACK, SAVEPOINT (transaction control)।",
          "Joins — Inner, Left, Right, Full Outer, Self Join।",
          "Subqueries — nested ও correlated queries।",
          "Aggregate Functions — COUNT, SUM, AVG, MIN, MAX।",
        ],
      },
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
    summary:
      "এই chapter-ে ACID properties, concurrency issues (dirty reads, non-repeatable reads, phantom reads), ও locking/MVCC cover করা হয়েছে। SQL ও MySQL code সহ।",
    sections: [
      { type: "h2", id: "acid", title: "ACID Properties" },
      {
        type: "p",
        text: "ACID হলো transaction-এর চারটি fundamental property যা reliable database operations ensure করে।",
      },
      {
        type: "list",
        items: [
          "Atomicity — transaction সম্পূর্ণ হয় বা একেবারে না হয় (all-or-nothing)। যদি কোনো step fail করে, পুরো transaction rollback হয়।",
          "Consistency — transaction-এর পরে database একটি valid state-এ থাকে (সব constraints satisfied)।",
          "Isolation — concurrent transactions একে অপরকে interfere করে না। প্রতিটি transaction independent মনে হয়।",
          "Durability — একবার commit হওয়ার পর data permanently save থাকে, system crash হলেও।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bank transfer। Atomicity — টাকা আপনার account থেকে কমে ও প্রাপকের account-ে বাড়ে — দুটোই হবে বা কোনোটাই না। Consistency — transfer-এর পর total balance ঠিক থাকে। Isolation — দুটি concurrent transfer একে অপরকে affect করবে না। Durability — transfer হওয়ার পর system crash হলেও record থেকে যায়।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- Transaction example: bank transfer
START TRANSACTION;

-- Deduct from sender
UPDATE accounts SET balance = balance - 500
WHERE account_id = 1 AND balance >= 500;

-- Add to receiver
UPDATE accounts SET balance = balance + 500
WHERE account_id = 2;

-- Check if both updates affected rows
-- If either failed, rollback
COMMIT;
-- or ROLLBACK; if something went wrong

-- MySQL: isolation levels
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;  -- dirty read allowed
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;     -- no dirty reads
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;   -- MySQL default
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;      -- strictest

START TRANSACTION;
SELECT balance FROM accounts WHERE account_id = 1;
-- other transactions cannot modify this row
COMMIT;`,
      },

      { type: "h2", id: "concurrency-issues", title: "Concurrency Issues" },
      {
        type: "list",
        items: [
          "Dirty Read — Transaction A reads uncommitted data from Transaction B, যদি B rollback হয়, A invalid data read করেছে।",
          "Non-repeatable Read — Transaction A একই row দুবার read করে কিন্তু দুটি ভিন্ন values পায় (B modify করেছে মাঝখানে)।",
          "Phantom Read — Transaction A একই query দুবার চালায় কিন্তু দ্বিতীয়বার নতুন rows যোগ হয়ে যায় (B insert করেছে)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Dirty read হলো একজন student-এর পরীক্ষার script মূল্যায়ন করার আগে draft read করা। Non-repeatable read হলো একই book-এর দুটি copy পড়ে দেখা যে ভিন্ন — কেউ মাঝখানে পাতা পরিবর্তন করেছে। Phantom read হলো library-তে একই ক্যাটাগরিতে দুবার খুঁজে দেখা যে দ্বিতীয়বার নতুন books এসেছে।",
      },

      { type: "h2", id: "locking-mvcc", title: "Locking & MVCC" },
      {
        type: "h3", title: "Locking" },
      {
        type: "list",
        items: [
          "Shared Lock (S) — read lock। একাধিক transactions একসাথে read করতে পারে কিন্তু modify না।",
          "Exclusive Lock (X) — write lock। শুধু একটি transaction modify করতে পারে, অন্যরা read-ও করতে পারবে না।",
          "Two-Phase Locking (2PL) — growing phase (locks acquire) ও shrinking phase (locks release)। Deadlock prevent করার জন্য strict 2PL।",
        ],
      },
      {
        type: "code",
        lang: "sql",
        text: `-- MySQL: explicit locking
-- Shared lock (read lock)
SELECT * FROM accounts WHERE account_id = 1 LOCK IN SHARE MODE;

-- Exclusive lock (write lock)
SELECT * FROM accounts WHERE account_id = 1 FOR UPDATE;

-- Table-level lock (MySQL)
LOCK TABLES accounts WRITE;
-- do operations
UNLOCK TABLES;

-- MySQL: check locks
SELECT * FROM information_schema.innodb_locks;
SELECT * FROM performance_schema.data_locks;  -- MySQL 8.0+`,
      },
      { type: "h3", title: "MVCC (Multi-Version Concurrency Control)" },
      {
        type: "p",
        text: "MVCC হলো একটি concurrency control technique যেখানে প্রতিটি transaction একটি snapshot of data দেখে। Locking-এর বিপরীতে, readers writers-কে block করে না এবং writers readers-কে block করে না। প্রতিটি row-এর একাধিক versions থাকে। PostgreSQL ও MySQL InnoDB উভয়ই MVCC use করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — locking হলো একটি room-এ এক সময়ে একজন ঢুকতে পারে (door lock)। MVCC হলো প্রতিটি person তার নিজের photocopy পায় — সবাই একসাথে read করতে পারে, এবং কেউ modify করলে সে একটি নতুন version তৈরি করে যা others পরে দেখবে।",
      },
      {
        type: "code",
        lang: "sql",
        text: `-- MySQL InnoDB MVCC example
-- Transaction 1 (read)
START TRANSACTION;
SELECT balance FROM accounts WHERE account_id = 1;
-- sees balance = 1000

-- Transaction 2 (write, concurrent)
START TRANSACTION;
UPDATE accounts SET balance = 1500 WHERE account_id = 1;
COMMIT;

-- Transaction 1 reads again (REPEATABLE READ)
SELECT balance FROM accounts WHERE account_id = 1;
-- STILL sees balance = 1000 (snapshot from first read)
-- This is MVCC in action

-- Transaction 1 commits and reads again
COMMIT;
SELECT balance FROM accounts WHERE account_id = 1;
-- NOW sees balance = 1500

-- MySQL: check transaction isolation
SELECT @@transaction_isolation;
-- Default: REPEATABLE-READ (uses MVCC)`,
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "ACID — Atomicity, Consistency, Isolation, Durability।",
          "Concurrency Issues — dirty read, non-repeatable read, phantom read।",
          "Locking — shared (read) ও exclusive (write) locks।",
          "MVCC — multi-version snapshots, readers ও writers একে অপরকে block করে না।",
          "Isolation Levels — READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ (MySQL default), SERIALIZABLE।",
        ],
      },
    ],
  },

'''

# ============ STEP 2: Add PostgreSQL project ============
# Find the PROJECTS array and add the new project at the beginning

projects_marker = "export const PROJECTS: Project[] = ["
projects_idx = text.find(projects_marker)
if projects_idx == -1:
    # If we can't find it, skip project addition
    print("WARNING: PROJECTS marker not found, skipping project addition")
    new_text = before + NEW_DB_SECTION + after
else:
    # Find the opening bracket position
    bracket_idx = text.find("[", projects_idx)
    after_projects_marker = text[bracket_idx + 1:]

    NEW_PROJECT = r'''  {
    id: "pg-big-lab",
    title: "PostgreSQL Big Data Lab",
    tagline: "Partitioning, replication & sharding at real scale with Docker",
    description:
      "A hands-on PostgreSQL lab that generates tens of millions of rows and practices partitioning, BRIN indexes, replication, benchmarking, and sharding at real scale. Covers beginner to advanced levels — from basic queries to multi-server sharding with Citus.",
    banglaDescription:
      "একটি hands-on PostgreSQL lab যেখানে কোটি কোটি rows generate করে partitioning, BRIN indexes, replication, benchmarking, ও sharding practice করা যায়। Beginner থেকে advanced level পর্যন্ত — basic queries থেকে multi-server sharding (Citus) পর্যন্ত।",
    status: "shipped",
    tech: ["PostgreSQL", "Docker", "Citus", "pgbench", "Linux"],
    features: [
      "Beginner: Install Docker, load 1M users, measure & fix slow queries with indexes",
      "Beginner: Two-table joins, pagination traps, index cost analysis",
      "Intermediate: Build replicas with pg_basebackup, watch replication lag live",
      "Intermediate: Failover with pg_promote(), understand split-brain risks",
      "Intermediate: Partitioning by date, partition pruning, instant DROP for retention",
      "Advanced: BRIN indexes for time-series data (1000x smaller than B-tree)",
      "Advanced: Benchmarking with pgbench (TPS, latency, read/write splitting)",
      "Advanced: Sharding with Citus — single-shard vs all-shard queries, hot shards, rebalancing",
      "Decision guide: when to use indexes vs replicas vs partitioning vs sharding",
    ],
    demoUrl: "#",
    githubUrl: "#",
    accent: "sky",
    cover: "PGQL",
  },
'''

    # Reconstruct: before + NEW_DB_SECTION + after (networking onward)
    # Then in the projects section, add the new project at the beginning
    text_with_db = before + NEW_DB_SECTION + after

    # Now add the project
    bracket_idx2 = text_with_db.find("[", text_with_db.find(projects_marker))
    before_projects = text_with_db[:bracket_idx2 + 1]
    after_projects = text_with_db[bracket_idx2 + 1:]

    new_text = before_projects + "\n" + NEW_PROJECT + after_projects

# Verify
assert 'id: "db-intro"' in new_text, "db-intro missing"
assert 'id: "db-relational"' in new_text, "db-relational missing"
assert 'id: "db-normalization"' in new_text, "db-normalization missing"
assert 'id: "db-sql"' in new_text, "db-sql missing"
assert 'id: "db-transactions"' in new_text, "db-transactions missing"
assert 'id: "db-sql-basics"' not in new_text, "old db-sql-basics still present"
assert 'id: "db-joins"' not in new_text, "old db-joins still present"
assert 'id: "db-indexing"' not in new_text, "old db-indexing still present"
assert 'id: "pg-big-lab"' in new_text, "pg-big-lab project missing"
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Database section replaced with 5 chapters + PostgreSQL project added. File size: {len(new_text)} bytes")
