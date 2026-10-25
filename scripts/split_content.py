#!/usr/bin/env python3
"""
Split content.ts into separate files per section.
Creates: src/lib/content/
  - types.ts        (all interfaces)
  - subjects.ts     (SUBJECTS, SUBJECT_COLORS)
  - dsa.ts          (DSA topics)
  - database.ts     (Database topics)
  - networking.ts   (Networking topics)
  - os.ts           (OS topics)
  - projects.ts     (PROJECTS)
  - cheatsheets.ts  (CHEATSHEETS)
  - index.ts        (re-exports everything + helper functions)
"""
from pathlib import Path

SRC = Path("/home/z/my-project/src/lib/content.ts")
DEST_DIR = Path("/home/z/my-project/src/lib/content")
DEST_DIR.mkdir(parents=True, exist_ok=True)

text = SRC.read_text()

# ============ 1. Extract types ============
types_start = text.find("export interface Subject")
types_end = text.find("export const SUBJECTS")
types_content = text[types_start:types_end].strip()

# Fix: remove "export " prefix from interfaces since they'll be in types.ts
# Actually keep them exported

# Add SubjectId and CheatsheetId type imports
types_ts = """// Types for BitsToBytes content system
// All interfaces and type definitions live here

""" + types_content

(DEST_DIR / "types.ts").write_text(types_ts)
print("✓ types.ts")

# ============ 2. Extract SUBJECTS ============
subj_start = text.find("export const SUBJECTS: Subject[]")
subj_end = text.find("export const TOPICS: Topic[]")
subjects_content = text[subj_start:subj_end].strip()

subjects_ts = """import type { SubjectId, Subject, CheatsheetId } from "./types";

""" + subjects_content

# Also extract SUBJECT_COLORS
colors_start = text.find("export const SUBJECT_COLORS")
colors_end = text.find("export function getTopicById")
if colors_start > 0:
    colors_content = text[colors_start:colors_end].strip()
    subjects_ts += "\n\n" + colors_content

(DEST_DIR / "subjects.ts").write_text(subjects_ts)
print("✓ subjects.ts")

# ============ 3. Extract TOPICS ============
topics_start = text.find("export const TOPICS: Topic[]")
topics_end = text.find("export const PROJECTS: Project[]")
topics_content = text[topics_start:topics_end].strip()

# Split TOPICS by section markers
dsa_marker = "/* ============== DSA ============== */"
db_marker = "/* ============== DATABASE ============== */"
net_marker = "/* ============== NETWORKING ============== */"
os_marker = "/* ============== OS ============== */"

# Find section boundaries
dsa_idx = topics_content.find(dsa_marker)
db_idx = topics_content.find(db_marker)
net_idx = topics_content.find(net_marker)
os_idx = topics_content.find(os_marker)

# Determine end of topics array
topics_end_bracket = topics_content.rfind("];")

# Extract each section
dsa_content = topics_content[dsa_idx:db_idx] if db_idx > dsa_idx else ""
db_content = topics_content[db_idx:net_idx] if net_idx > db_idx else ""
net_content = topics_content[net_idx:os_idx] if os_idx > net_idx else ""
os_content = topics_content[os_idx:topics_end_bracket + 2] if os_idx > 0 else ""

# ============ 3a. DSA topics ============
dsa_ts = """import type { Topic } from "./types";

export const DSA_TOPICS: Topic[] = [
""" + dsa_content.replace(dsa_marker, "").strip() + """
];
"""

# Remove trailing comma before ];
dsa_ts = dsa_ts.replace(",\n];", "\n];")
(DEST_DIR / "dsa.ts").write_text(dsa_ts)
print("✓ dsa.ts")

# ============ 3b. Database topics ============
db_ts = """import type { Topic } from "./types";

export const DB_TOPICS: Topic[] = [
""" + db_content.replace(db_marker, "").strip() + """
];
"""

db_ts = db_ts.replace(",\n];", "\n];")
(DEST_DIR / "database.ts").write_text(db_ts)
print("✓ database.ts")

# ============ 3c. Networking topics ============
net_ts = """import type { Topic } from "./types";

export const NETWORKING_TOPICS: Topic[] = [
""" + net_content.replace(net_marker, "").strip() + """
];
"""

net_ts = net_ts.replace(",\n];", "\n];")
(DEST_DIR / "networking.ts").write_text(net_ts)
print("✓ networking.ts")

# ============ 3d. OS topics ============
os_ts = """import type { Topic } from "./types";

export const OS_TOPICS: Topic[] = [
""" + os_content.replace(os_marker, "").strip() + """
];
"""

os_ts = os_ts.replace(",\n];", "\n];")
(DEST_DIR / "os.ts").write_text(os_ts)
print("✓ os.ts")

# ============ 4. Extract PROJECTS ============
proj_start = text.find("export const PROJECTS: Project[]")
proj_end = text.find("export const CHEATSHEETS")
projects_content = text[proj_start:proj_end].strip()

projects_ts = """import type { Project } from "./types";

""" + projects_content

(DEST_DIR / "projects.ts").write_text(projects_ts)
print("✓ projects.ts")

# ============ 5. Extract CHEATSHEETS ============
cheat_start = text.find("export const CHEATSHEETS: Cheatsheet[]")
cheat_end = text.find("export const SUBJECT_COLORS")
if cheat_end < 0:
    cheat_end = text.find("export function getTopicById")
cheatsheets_content = text[cheat_start:cheat_end].strip()

cheatsheets_ts = """import type { Cheatsheet } from "./types";

""" + cheatsheets_content

(DEST_DIR / "cheatsheets.ts").write_text(cheatsheets_ts)
print("✓ cheatsheets.ts")

# ============ 6. Create index.ts ============
index_ts = """// BitsToBytes content system — barrel export
// This file re-exports everything so imports stay the same:
//   import { TOPICS, PROJECTS, getTopicById } from "@/lib/content";

// Types
export type {
  SubjectId,
  CheatsheetId,
  Subject,
  TopicSection,
  CodeSamples,
  Topic,
  Project,
  Cheatsheet,
} from "./types";

// Subjects
export { SUBJECTS, SUBJECT_COLORS } from "./subjects";

// Topics (combined)
export { DSA_TOPICS } from "./dsa";
export { DB_TOPICS } from "./database";
export { NETWORKING_TOPICS } from "./networking";
export { OS_TOPICS } from "./os";

// Projects
export { PROJECTS } from "./projects";

// Cheatsheets
export { CHEATSHEETS } from "./cheatsheets";

// ============ Combined TOPICS array ============
import { DSA_TOPICS } from "./dsa";
import { DB_TOPICS } from "./database";
import { NETWORKING_TOPICS } from "./networking";
import { OS_TOPICS } from "./os";
import type { Topic, SubjectId, CheatsheetId, Project, Cheatsheet } from "./types";
import { SUBJECTS, SUBJECT_COLORS } from "./subjects";
import { PROJECTS } from "./projects";
import { CHEATSHEETS } from "./cheatsheets";

export const TOPICS: Topic[] = [
  ...DSA_TOPICS,
  ...DB_TOPICS,
  ...NETWORKING_TOPICS,
  ...OS_TOPICS,
];

// ============ Helper functions ============
export function getTopicById(id: string): Topic | undefined {
  return TOPICS.find((t) => t.id === id);
}

export function getTopicsForSubject(subject: SubjectId): Topic[] {
  return TOPICS.filter((t) => t.subject === subject);
}

export function getProjectById(id: string): Project | undefined {
  return PROJECTS.find((p) => p.id === id);
}

export function getCheatsheetById(id: CheatsheetId): Cheatsheet | undefined {
  return CHEATSHEETS.find((c) => c.id === id);
}

export function getSubjectById(id: SubjectId) {
  return SUBJECTS.find((s) => s.id === id);
}
"""

(DEST_DIR / "index.ts").write_text(index_ts)
print("✓ index.ts")

# ============ 7. Rename old content.ts ============
old_path = Path("/home/z/my-project/src/lib/content.ts.bak")
SRC.rename(old_path)
print(f"✓ Old content.ts → content.ts.bak (backup)")

# ============ 8. Create redirect content.ts ============
# This ensures existing imports like `import { ... } from "@/lib/content"` still work
redirect_ts = """// This file re-exports from the content/ directory.
// All imports like `import { ... } from "@/lib/content"` still work.
export * from "./content";
"""

SRC.write_text(redirect_ts)
print("✓ content.ts (redirect)")

print("\n✅ Split complete! Files created:")
for f in sorted(DEST_DIR.iterdir()):
    lines = len(f.read_text().splitlines())
    print(f"  {f.name}: {lines} lines")
print(f"\n  content.ts: {len(redirect_ts.splitlines())} lines (redirect)")
