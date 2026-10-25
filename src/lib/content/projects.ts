import type { Project } from "./types";

export const PROJECTS: Project[] = [
  {
    id: "pg-big-lab",
    title: "PostgreSQL Big Data Lab",
    tagline: "Partitioning, replication & sharding at real scale with Docker",
    description:
      "A hands-on PostgreSQL lab that generates tens of millions of rows and practices partitioning, BRIN indexes, replication, benchmarking, and sharding at real scale. Covers beginner to advanced levels — from basic queries to multi-server sharding with Citus. Follow the step-by-step guide below to build this project yourself.",
    banglaDescription:
      "একটি hands-on PostgreSQL lab যেখানে কোটি কোটি rows generate করে partitioning, BRIN indexes, replication, benchmarking, ও sharding practice করা যায়। Beginner থেকে advanced level পর্যন্ত — basic queries থেকে multi-server sharding (Citus) পর্যন্ত। নিচের step-by-step guide follow করে নিজে project টি build করুন।",
    status: "shipped",
    tech: ["PostgreSQL", "Docker", "Citus", "pgbench", "Go", "Next.js"],
    features: [
      "BEGINNER: Install Docker, create PostgreSQL container, load 1 million users",
      "BEGINNER: Measure & fix slow queries with EXPLAIN ANALYZE + indexes (1000x faster!)",
      "BEGINNER: Two-table joins, pagination traps (keyset vs OFFSET), index cost analysis",
      "INTERMEDIATE: Build replicas with pg_basebackup, watch replication lag live",
      "INTERMEDIATE: Failover with pg_promote(), understand split-brain risks",
      "INTERMEDIATE: Partitioning by date, partition pruning, instant DROP for retention",
      "ADVANCED: BRIN indexes for time-series data (1000x smaller than B-tree)",
      "ADVANCED: Benchmarking with pgbench (TPS, latency, read/write splitting)",
      "ADVANCED: Sharding with Citus — single-shard vs all-shard queries, hot shards, rebalancing",
      "PRINCIPLES: Decision guide — when to use indexes vs replicas vs partitioning vs sharding",
    ],
    demoUrl: "https://demo.bittobytes.dev",
    githubUrl: "https://github.com/bittobytes/pg-big-lab",
    accent: "sky",
    cover: "PGQL",
    sections: [
      { type: "h2", id: "big-ideas", title: "Lesson 0 — The Big Ideas" },
      { type: "p", text: "ধরো তোমার database হলো একটি library যেখানে একজন librarian আছে। Database-কে fast করার প্রতিটি উপায় হলো সেই librarian-কে help করার একটি ভিন্ন উপায়।" },
      { type: "h3", title: "Index — the catalog" },
      { type: "p", text: "Catalog ছাড়া librarian প্রতিটি shelf পার হয়ে একটি book খুঁজে বের করে। Catalog থাকলে সে সরাসরি সঠিক shelf-এ যায়। Index হলো প্রথম ও সবচেয়ে সস্তা fix, এবং এটি বেশির ভাগ speed problems solve করে।" },
      { type: "h3", title: "Replica — more librarians with photocopies" },
      { type: "p", text: "তুমি আরও librarians hire করো, এবং প্রত্যেকে সব book-এর একটি full photocopy পায়। এখন অনেক মানুষ একসাথে read করতে পারে। কিন্তু নতুন book (write) সবসময় main librarian-এর কাছে যায়। Replicas অনেক reads handle করতে help করে এবং main server die করলে backup হিসেবে কাজ করে।" },
      { type: "h3", title: "Partitioning — rooms inside one library" },
      { type: "p", text: "Books গুলো year অনুযায়ী rooms-এ organize করা হয়। এখনও একটি building, কিন্তু '2026 সালের books' খুঁজতে শুধু একটি room check করলেই হয়। একই server, ছোট pieces।" },
      { type: "h3", title: "Sharding — separate libraries in different cities" },
      { type: "p", text: "Users A থেকে M একটি library-তে থাকে, N থেকে Z অন্য library-তে। প্রতিটি library কম store করে ও কম কাজ করে। এটি powerful, কিন্তু 'মোট কয়টি book?' এর মতো প্রশ্নে এখন সব library-তে call করতে হয়। এটি সবচেয়ে complex option।" },
      { type: "callout", calloutTone: "tip", text: "Golden rule: measure first, then split। Split করো কারণ একটি measured problem আছে, row count-এর কারণে নয়। ১ মিলিয়ন users-এ তোমাকে কিছু split করতে হবে না।" },

      { type: "h2", id: "setup", title: "Lesson 1 — Install Docker & Load 1M Users" },
      { type: "p", text: "প্রথমে Docker install করো। Windows বা Mac-এ Docker Desktop download করো docker.com থেকে। Ubuntu Linux-এ: curl -fsSL https://get.docker.com | sh। Check করো: docker --version।" },
      { type: "h3", title: "PostgreSQL container তৈরি করো" },
      { type: "code", lang: "bash", text: 'docker run --name mypg -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres:17\n\ndocker ps\n\ndocker exec -it mypg psql -U postgres' },
      { type: "h3", title: "Database ও table তৈরি করো, 1M users load করো" },
      { type: "code", lang: "sql", text: "CREATE DATABASE shop;\n\\c shop\n\nCREATE TABLE users (\n    id bigserial PRIMARY KEY,\n    email text NOT NULL,\n    name text,\n    country text,\n    created_at timestamptz\n);\n\n-- ১ মিলিয়ন fake users insert করো\nINSERT INTO users (email, name, country, created_at)\nSELECT 'user' || g || '@example.com',\n       'User ' || g,\n       (ARRAY['IN','US','UK','DE','BR'])[1 + g % 5],\n       now() - random() * interval '730 days'\nFROM generate_series(1, 1000000) g;\n\nSELECT count(*) FROM users;  -- 1000000" },
      { type: "p", text: "INSERT কীভাবে কাজ করে — generate_series(1, 1000000) g দিয়ে ১ থেকে ১০ লক্ষ পর্যন্ত numbers তৈরি হয়। 'user' || g || '@example.com' দিয়ে email তৈরি হয়। (ARRAY[...])[1 + g % 5] দিয়ে ৫টি country rotate হয়। now() - random() * interval '730 days' দিয়ে গত ২ বছরের মধ্যে random date তৈরি হয়।" },

      { type: "h2", id: "slow-queries", title: "Lesson 2 — Measure & Fix Slow Queries" },
      { type: "p", text: "Timing on করো এবং একটি search চালাও। তারপর EXPLAIN ANALYZE দিয়ে দেখো PostgreSQL কীভাবে query চালিয়েছে। Seq Scan দেখলে বুঝবে সে পুরো table পড়েছে — এটাই slow। Index যোগ করলে Index Scan হবে — হাজার গুণ fast।" },
      { type: "code", lang: "sql", text: "-- Timing on\n\\timing on\n\n-- Email দিয়ে search — slow (Seq Scan)\nSELECT * FROM users WHERE email = 'user777777@example.com';\n\n-- দেখো কীভাবে চালানো হয়েছে\nEXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user777777@example.com';\n-- Seq Scan — ১ মিলিয়ন row পড়েছে! ~50-150ms\n\n-- Index তৈরি করো\nCREATE INDEX idx_users_email ON users(email);\n\n-- আবার চালাও — এখন Index Scan!\nEXPLAIN ANALYZE SELECT * FROM users WHERE email = 'user777777@example.com';\n-- Index Scan — ~0.05ms — 1000x faster!" },
      { type: "p", text: "Real-life thinking — index ছাড়া librarian প্রতিটি shelf খুঁজছে। Index থাকলে সে সরাসরি সঠিক shelf-এ যায়। এক line SQL ১০০০ গুণ fast করতে পারে — এটিই database performance-এর সবচেয়ে important lesson।" },

      { type: "h2", id: "joins", title: "Lesson 3 — Two Tables, Joins & Pagination" },
      { type: "code", lang: "sql", text: "-- Orders table তৈরি করো (৩ মিলিয়ন rows)\nCREATE TABLE orders (\n    id bigserial PRIMARY KEY,\n    user_id bigint REFERENCES users(id),\n    amount numeric(10,2),\n    status text,\n    created_at timestamptz\n);\n\nINSERT INTO orders (user_id, amount, status, created_at)\nSELECT 1 + floor(random() * 1000000)::bigint,\n       round((random() * 500)::numeric, 2),\n       (ARRAY['paid','pending','refunded'])[1 + floor(random() * 3)::int],\n       now() - random() * interval '365 days'\nFROM generate_series(1, 3000000);\n\nANALYZE;\n\n-- 'My Orders' page query — slow!\nEXPLAIN ANALYZE\nSELECT * FROM orders WHERE user_id = 42 ORDER BY created_at DESC LIMIT 10;\n-- Seq Scan! Foreign key index স্বয়ংক্রিয়ভাবে তৈরি হয় না!\n\n-- Composite index যোগ করো\nCREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);\nEXPLAIN ANALYZE\nSELECT * FROM orders WHERE user_id = 42 ORDER BY created_at DESC LIMIT 10;\n-- Index Scan — fast! Column order matters!" },
      { type: "p", text: "কেন দুটি columns? Phone book-এর কথা ভাবো — last name তারপর first name sort করা। PostgreSQL user 42-এর সব orders খুঁজে পায়, এবং সেগুলো already date অনুযায়ী sorted, তাই extra sort লাগে না।" },
      { type: "h3", title: "Pagination trap" },
      { type: "code", lang: "sql", text: "-- SLOW: deep pages-এ ৯০০,০০০ rows পড়ে ফেলে\nSELECT id, email FROM users ORDER BY id LIMIT 20 OFFSET 900000;\n\n-- FAST: keyset pagination — শেষ shown id-এর পর থেকে\nSELECT id, email FROM users WHERE id > 900000 ORDER BY id LIMIT 20;" },

      { type: "h2", id: "replication", title: "Lesson 4 — Replication: Build Your First Replica" },
      { type: "p", text: "Replica হলো একটি দ্বিতীয় PostgreSQL server যা primary-এর সব data-এর live copy রাখে। প্রতিটি change প্রথমে WAL (write-ahead log)-এ লেখা হয় — এটি একটি diary। Primary এই diary প্রতিটি connected replica-তে stream করে। Replicas read-only।" },
      { type: "code", lang: "bash", text: "# Docker network তৈরি করো\ndocker network create pgnet\ndocker network connect pgnet mypg\n\n# Replication user তৈরি করো\ndocker exec -it mypg psql -U postgres \\\n  -c \"CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'replpass';\"\n\n# pg_hba.conf-এ replication allow করো\ndocker exec mypg bash -c \\\n  'echo \"host replication replicator all scram-sha-256\" >> \"$PGDATA/pg_hba.conf\"'\ndocker exec mypg psql -U postgres -c \"SELECT pg_reload_conf();\"\n\n# Primary-এর full copy নাও\ndocker run --rm --network pgnet \\\n  -v replica-data:/var/lib/postgresql/data \\\n  -e PGPASSWORD=replpass \\\n  postgres:17 \\\n  pg_basebackup -h mypg -U replicator -D /var/lib/postgresql/data -R -X stream -P\n\n# Replica চালু করো\ndocker run -d --name mypg-replica --network pgnet -p 5433:5432 \\\n  -v replica-data:/var/lib/postgresql/data postgres:17" },
      { type: "code", lang: "sql", text: "-- Primary-এ user insert করো\nINSERT INTO users (email, name, country, created_at)\nVALUES ('rahim@example.com', 'Rahim', 'BD', now());\n\n-- Replica-তে check করো — Rahim already সেখানে!\nSELECT * FROM users WHERE email = 'rahim@example.com';\n\n-- Replica-তে insert error: cannot execute INSERT in a read-only transaction\n\n-- Replication health check (primary-এ):\nSELECT client_addr, state, sent_lsn, replay_lsn FROM pg_stat_replication;\n-- state = 'streaming' = সব ঠিক আছে" },
      { type: "p", text: "Real-life thinking — replica হলো একটি photocopy machine। Primary একটি document change করলে, replica সেই change সাথে সাথে copy করে। তুমি photocopy থেকে read করতে পারো, কিন্তু change করতে পারো না।" },

      { type: "h2", id: "failover", title: "Lesson 5 — Failover: When the Primary Dies" },
      { type: "p", text: "Servers crash করে। Primary die করলে তুমি একটি replica-কে promote করো যাতে সে নতুন primary হয়ে যায়। একে failover বলে।" },
      { type: "code", lang: "bash", text: "# Primary বন্ধ করো (crash simulate)\ndocker stop mypg\n\n# Replica-তে যাও এবং promote করো\ndocker exec -it mypg-replica psql -U postgres -d shop\nSELECT pg_promote();\nSELECT pg_is_in_recovery();  -- now 'f' = I am a primary!\n\n-- এখন insert কাজ করবে!\nINSERT INTO users (email, name, country, created_at)\nVALUES ('after-failover@example.com', 'New Primary', 'BD', now());" },
      { type: "callout", calloutTone: "warn", text: "Warning: পুরোনো mypg আবার চালু করলে তোমার কাছে দুটি primary থাকবে — split brain! Production-এ Patroni-এর মতো tools এটি safely handle করে।" },

      { type: "h2", id: "partitioning", title: "Lesson 6 — Partitioning: Split a Big Table" },
      { type: "p", text: "Partitioning একটি বড় table-কে একই server-এ ছোট tables-এ ভাগ করে। PostgreSQL সেই partitions skip করে যেগুলোতে তোমার চাওয়া rows থাকতে পারে না।" },
      { type: "code", lang: "sql", text: "-- Date অনুযায়ী partitioned table তৈরি করো\nCREATE TABLE orders_p (\n    id bigint,\n    user_id bigint,\n    amount numeric(10,2),\n    status text,\n    created_at timestamptz NOT NULL,\n    PRIMARY KEY (id, created_at)\n) PARTITION BY RANGE (created_at);\n\nCREATE TABLE orders_2025 PARTITION OF orders_p\nFOR VALUES FROM ('2025-01-01') TO ('2026-01-01');\nCREATE TABLE orders_2026 PARTITION OF orders_p\nFOR VALUES FROM ('2026-01-01') TO ('2027-01-01');\nCREATE TABLE orders_other PARTITION OF orders_p DEFAULT;\n\n-- Data copy করো এবং index তৈরি করো\nINSERT INTO orders_p SELECT * FROM orders;\nCREATE INDEX ON orders_p (user_id, created_at DESC);\nANALYZE orders_p;\n\n-- Partition pruning দেখো\nEXPLAIN ANALYZE\nSELECT count(*) FROM orders_p WHERE created_at >= '2026-06-01';\n-- শুধু orders_2026 partition দেখা হয়! বাকিগুলো skip!\n\n-- পুরোনো data instant delete (DROP!)\nALTER TABLE orders_p DETACH PARTITION orders_2025;\nDROP TABLE orders_2025;" },
      { type: "p", text: "Real-life thinking — partitioning হলো একটি library-কে rooms-এ ভাগ করা। '2026 সালের books' খুঁজতে শুধু 2026-এর room-এ যাও। পুরোনো room delete করা মাত্র মিলিসেকেন্ড — এটি কারণ logs ও events সবসময় time-এ partitioned হয়।" },

      { type: "h2", id: "sharding", title: "Lesson 7 — Sharding with Citus: Split Data Across Servers" },
      { type: "p", text: "Replicas সব data প্রতিটি server-এ copy করে। Sharding data-কেই split করে — কিছু users server A-তে, বাকিগুলো server B-তে। Citus হলো একটি open-source PostgreSQL extension যা এটি তোমার জন্য করে।" },
      { type: "code", lang: "sql", text: "-- Workers register করো\nSELECT citus_set_coordinator_host('coordinator', 5432);\nSELECT citus_add_node('worker1', 5432);\nSELECT citus_add_node('worker2', 5432);\nSELECT * FROM citus_get_active_worker_nodes();\n\n-- Distributed tables তৈরি করো (shard key = user_id)\nSELECT create_distributed_table('users', 'id');\nSELECT create_distributed_table('orders', 'user_id', colocate_with => 'users');\n\n-- Single-shard query — একটি worker-ে যায় (Task Count: 1)\nEXPLAIN SELECT * FROM orders WHERE user_id = 42;\n\n-- All-shard query — সব 32 shards-এ যায় (Task Count: 32)\nEXPLAIN SELECT count(*) FROM orders;" },
      { type: "p", text: "Real-life thinking — sharding হলো users-কে আলাদা library-তে ভাগ করা। User 42-এর data শুধু একটি library-তে — query fast। কিন্তু 'মোট কয়জন user?' এর জন্য সব library-তে call করতে হয়।" },
      { type: "callout", calloutTone: "warn", text: "Warning: CREATE UNIQUE INDEX ON users (email) fail করবে! কারণ কোনো single worker সব shards-এ email uniqueness check করতে পারে না।" },

      { type: "h2", id: "app-integration", title: "Lesson 8 — Using Primary & Replicas from Your App" },
      { type: "p", text: "তোমার app দুটি connections রাখে — writes primary-তে যায়, reads replica-তে। এটি read/write splitting বলে।" },
      {
        type: "multi-code",
        filename: "app_rw_split",
        codeSamples: {
          cpp: '// C++ with libpqxx — read/write splitting\n#include <pqxx/pqxx>\n#include <iostream>\n\nint main() {\n    pqxx::connection write_db(\n        \"dbname=shop user=postgres password=secret host=localhost port=5432\");\n    pqxx::work txn(write_db);\n    txn.exec_params(\n        \"INSERT INTO users (email, name, country, created_at) \"\n        \"VALUES ($1, $2, \\\'BD\\\', now())\",\n        \"app-test@example.com\", \"App Test\");\n    txn.commit();\n    std::cout << \"User created on primary\\n\";\n\n    pqxx::connection read_db(\n        \"dbname=shop user=postgres password=secret host=localhost port=5433\");\n    pqxx::work read_txn(read_db);\n    auto row = read_db.exec(\"SELECT name FROM users \"\n                            \"WHERE email = \\\'app-test@example.com\\\'\");\n    if (!row.empty()) {\n        std::cout << \"Found on replica: \" << row[0][\"name\"].c_str() << \"\\n\";\n    }\n    return 0;\n}',
          go: 'package main\n\nimport (\n    \"database/sql\"\n    \"fmt\"\n    _ \"github.com/lib/pq\"\n)\n\nfunc main() {\n    writeDB, _ := sql.Open(\"postgres\",\n        \"dbname=shop user=postgres password=secret host=localhost port=5432 sslmode=disable\")\n    writeDB.Exec(\"INSERT INTO users (email, name, country, created_at) VALUES ($1, $2, \\\'BD\\\', now())\",\n        \"app-test@example.com\", \"App Test\")\n    fmt.Println(\"User created on primary\")\n\n    readDB, _ := sql.Open(\"postgres\",\n        \"dbname=shop user=postgres password=secret host=localhost port=5433 sslmode=disable\")\n    var name string\n    readDB.QueryRow(\"SELECT name FROM users WHERE email = $1\",\n        \"app-test@example.com\").Scan(&name)\n    fmt.Println(\"Found on replica:\", name)\n}',
          python: 'import psycopg\n\n# Write to primary (port 5432)\nwrite_db = psycopg.connect(\n    \"dbname=shop user=postgres password=secret host=localhost port=5432\")\nwith write_db.cursor() as cur:\n    cur.execute(\n        \"INSERT INTO users (email, name, country, created_at) \"\n        \"VALUES (%s, %s, \\\'BD\\\', now()) RETURNING id\",\n        (\"app-test@example.com\", \"App Test\"))\n    new_id = cur.fetchone()[0]\n    write_db.commit()\n    print(f\"User created on primary, id={new_id}\")\n\n# Read from replica (port 5433)\nread_db = psycopg.connect(\n    \"dbname=shop user=postgres password=secret host=localhost port=5433\")\nwith read_db.cursor() as cur:\n    cur.execute(\"SELECT name FROM users WHERE email = %s\",\n                (\"app-test@example.com\",))\n    print(f\"Found on replica: {cur.fetchone()[0]}\")',
          java: 'import java.sql.*;\n\npublic class AppRW {\n    public static void main(String[] args) throws Exception {\n        Connection writeDb = DriverManager.getConnection(\n            \"jdbc:postgresql://localhost:5432/shop\", \"postgres\", \"secret\");\n        PreparedStatement ps = writeDb.prepareStatement(\n            \"INSERT INTO users (email, name, country, created_at) \" +\n            \"VALUES (?, ?, \\\'BD\\\', now()) RETURNING id\");\n        ps.setString(1, \"app-test@example.com\");\n        ps.setString(2, \"App Test\");\n        ResultSet rs = ps.executeQuery();\n        rs.next();\n        System.out.println(\"User created, id=\" + rs.getInt(1));\n\n        Connection readDb = DriverManager.getConnection(\n            \"jdbc:postgresql://localhost:5433/shop\", \"postgres\", \"secret\");\n        PreparedStatement readPs = readDb.prepareStatement(\n            \"SELECT name FROM users WHERE email = ?\");\n        readPs.setString(1, \"app-test@example.com\");\n        ResultSet rs2 = readPs.executeQuery();\n        rs2.next();\n        System.out.println(\"Found on replica: \" + rs2.getString(1));\n    }\n}',
        },
      },

      { type: "h2", id: "big-data-scale", title: "Big Data Lab — At Scale (50M+ Rows)" },
      { type: "p", text: "যখন data RAM-এর চেয়ে বড় হয়, PostgreSQL-কে disk থেকে read করতে হয়। Full table scan মিলিসেকেন্ডের বদলে মিনিট নেয়। সেখানে partitioning, BRIN indexes, ও sharding matter করতে শুরু করে।" },
      { type: "code", lang: "sql", text: "-- ৫০ মিলিয়ন orders generate করো\nCALL create_order_partitions(36);  -- 36 monthly partitions\nCALL load_users(5000000);           -- 5M users\nCALL load_orders(50000000, 5000000); -- 50M orders\n\n-- count(*) slow — planner estimate use করো\nSELECT count(*) FROM orders;  -- slow\nSELECT sum(reltuples)::bigint AS estimated_orders\nFROM pg_class WHERE relname ~ \'^orders_\' AND relkind = \'r\';  -- instant!\n\n-- BRIN index — B-tree-এর চেয়ে হাজার গুণ ছোট\nCREATE INDEX idx_events_brin ON events USING BRIN (event_time);\n-- BRIN: কয়েক KB, B-tree: কয়েক MB!\n-- BRIN works perfectly on time-ordered data (events), useless on unordered (orders)" },
      { type: "callout", calloutTone: "tip", text: "Tip: BRIN use করো append-only, time-ordered data-র জন্য (logs, events, sensor readings)। B-tree use করো বাকি সবার জন্য।" },

      { type: "h2", id: "decision-guide", title: "Decision Guide — What to Use When" },
      { type: "list", items: [
        "কয়েকটা query slow → Indexes, query rewrites, EXPLAIN ANALYZE (সবসময় এটা আগে try করো)।",
        "Server CPU busy with reads → Top queries fix করো, caching যোগ করো → Read replicas।",
        "High availability দরকার → একটি replica + tested failover → Automatic failover (Patroni)।",
        "Big tables date অনুযায়ী query → Time partitioning → pg_partman দিয়ে automate করো।",
        "Append-only time-series data → BRIN index on time column → Daily/monthly partitions।",
        "Data বা writes largest server-এও fit করছে না → Sharding (Citus) → এমন shard key বেছে নাও যেটা প্রায় প্রতিটি query-তে আছে।",
        "Multi-tenant SaaS with uneven customers → Shard by tenant id → Biggest tenants-কে isolate করো।",
      ]},
      { type: "p", text: "Realistic growth path — বেশির ভাগ apps এভাবে grow করে — এক server with good indexes → এক replica for safety ও reads → partitioning for few huge time-based tables → এবং অনেক পরে sharding। অনেক large companies অনেক দিন এক primary ও replicas নিয়ে চলে। Sharding powerful, কিন্তু এটি প্রতিটি schema change, query, ও operation কে বেশি complex করে, তাই এটি এমন একটি problem solve করুক যেটা তুমি actually measure করেছ।" },
    ]
},
];