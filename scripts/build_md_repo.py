#!/usr/bin/env python3
"""
Generate a Markdown-based content repo from content.ts.

Each topic becomes a single Markdown file under content/<subject>/<topic-id>.md
with frontmatter (id, title, subject, difficulty, est, summary) and the full
body content rendered as readable Markdown — including code samples in all
4 languages (C++, Go, Python, Java) fenced with ```cpp, ```go, etc.

Also generates:
- README.md (main readme with contribution guide)
- CONTRIBUTING.md (detailed contribution rules + Markdown spec)
- CONTENT_FORMAT.md (the Markdown schema documentation)
- content/index.md (table of contents)
- cheatsheets/*.md (one per cheatsheet)
- projects/*.md (one per project)
"""
import json
import re
import shutil
from pathlib import Path

# Re-implement the topic loader by importing content.ts as a module is hard
# (it's TypeScript). Instead, we'll parse it with regex / simple state machine.
# Actually, the simpler approach: re-use the TypeScript runtime via a tiny
# Node script that dumps JSON, then read that JSON.

ROOT = Path("/home/z/my-project")
REPO_DIR = ROOT / "download" / "learnhub-repo"

# Step 1: Dump content.ts to JSON using a small Node script.
dump_script = ROOT / "scripts" / "dump_content.ts"
dump_script.write_text("""
// Tiny dump script — imports content.ts and prints JSON.
import { SUBJECTS, TOPICS, PROJECTS, CHEATSHEETS } from "../src/lib/content";
console.log(JSON.stringify({ SUBJECTS, TOPICS, PROJECTS, CHEATSHEETS }, null, 2));
""")
# Run it with bun (no transpile needed; bun handles .ts natively)
import subprocess
result = subprocess.run(
    ["bun", "run", str(dump_script)],
    capture_output=True, text=True, cwd=str(ROOT)
)
if result.returncode != 0:
    print("STDERR:", result.stderr)
    raise SystemExit("Failed to dump content.ts")

data = json.loads(result.stdout)
subjects = data["SUBJECTS"]
topics = data["TOPICS"]
projects = data["PROJECTS"]
cheatsheets = data["CHEATSHEETS"]

print(f"Loaded {len(topics)} topics, {len(projects)} projects, {len(cheatsheets)} cheatsheets")

# ---------- Helpers ----------

def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def render_section(s: dict) -> str:
    t = s.get("type")
    if t == "h2":
        return f"\n## {s.get('title', '')}\n" + (f"<a id=\"{s.get('id')}\"></a>\n" if s.get("id") else "")
    if t == "h3":
        return f"\n### {s.get('title', '')}\n"
    if t == "p":
        return f"\n{s.get('text', '')}\n"
    if t == "list":
        items = "\n".join(f"- {it}" for it in s.get("items", []))
        return f"\n{items}\n"
    if t == "code":
        lang = s.get("lang", "text")
        return f"\n```{lang}\n{s.get('text', '')}\n```\n"
    if t == "multi-code":
        out = "\n"
        samples = s.get("codeSamples", {}) or {}
        # Write each available language as a separate fenced block
        for lang in ["cpp", "go", "python", "java"]:
            code = samples.get(lang)
            if code and code.strip():
                out += f"```{lang}\n{code}\n```\n\n"
        filename = s.get("filename")
        if filename:
            out = f"\n> **File:** `{filename}`\n" + out
        return out
    if t == "callout":
        tone = s.get("calloutTone", "info")
        text = s.get("text", "")
        label_map = {"info": "ℹ️ NOTE", "warn": "⚠️ WARNING", "tip": "💡 TIP"}
        label = label_map.get(tone, "ℹ️ NOTE")
        return f"\n> **{label}**\n>\n> {text}\n"
    if t == "diagram":
        d = s.get("diagram")
        if d == "sorting":
            return "\n> *[Interactive sorting visualizer — visit the live site to play]*\n"
        if d == "tcp-handshake":
            return "\n> *[Interactive TCP handshake diagram — visit the live site to play]*\n"
        return ""
    return ""

# ---------- Build subject directories and topic files ----------

subject_meta = {s["id"]: s for s in subjects}

# Clear existing content (so re-runs are clean)
for sub_dir in (REPO_DIR / "content").iterdir():
    if sub_dir.is_dir():
        for f in sub_dir.glob("*.md"):
            f.unlink()

# Map subject IDs to directory names
SUBJECT_DIR = {
    "dsa": "dsa",
    "db": "db",
    "net": "networking",
    "os": "os",
}

# Group topics by subject
topics_by_subject = {s["id"]: [] for s in subjects}
for t in topics:
    topics_by_subject[t["subject"]].append(t)

# Write each topic as a Markdown file
for subject_id, subject_topics in topics_by_subject.items():
    sub_dir = REPO_DIR / "content" / SUBJECT_DIR[subject_id]
    sub_dir.mkdir(parents=True, exist_ok=True)

    for t in subject_topics:
        sm = subject_meta[subject_id]
        out = []
        # Frontmatter
        out.append("---")
        out.append(f"id: {t['id']}")
        out.append(f"title: {t['title']}")
        out.append(f"bangla: {t['bangla']}")
        out.append(f"subject: {subject_id}")
        out.append(f"subject_name: {sm['name']}")
        out.append(f"difficulty: {t['difficulty']}")
        out.append(f"est: {t['est']}")
        out.append(f"summary: {json.dumps(t['summary'], ensure_ascii=False)}")
        out.append("---\n")
        # Title + bangla
        out.append(f"# {t['title']}")
        out.append(f"\n*{t['bangla']}*\n")
        # Summary as blockquote
        out.append(f"> {t['summary']}\n")
        # Metadata badges
        out.append(f"**Difficulty:** {t['difficulty']}  |  **Est. time:** {t['est']}  |  **Subject:** {sm['name']}\n")
        # Sections
        for s in t["sections"]:
            out.append(render_section(s))
        # Write
        (sub_dir / f"{t['id']}.md").write_text("\n".join(out))
    print(f"Wrote {len(subject_topics)} topics for {subject_id}")

# ---------- Cheatsheets ----------
(REPO_DIR / "cheatsheets").mkdir(parents=True, exist_ok=True)
for f in (REPO_DIR / "cheatsheets").glob("*.md"):
    f.unlink()
for c in cheatsheets:
    out = []
    out.append("---")
    out.append(f"id: {c['id']}")
    out.append(f"title: {c['title']}")
    out.append(f"bangla: {c['bangla']}")
    out.append(f"subject: {c['subject']}")
    out.append(f"description: {json.dumps(c['description'], ensure_ascii=False)}")
    out.append("---\n")
    out.append(f"# {c['title']}")
    out.append(f"\n*{c['bangla']}*\n")
    out.append(f"> {c['description']}\n")
    # Build markdown table
    out.append("| " + " | ".join(c["columns"]) + " |")
    out.append("| " + " | ".join(["---"] * len(c["columns"])) + " |")
    for row in c["rows"]:
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    (REPO_DIR / "cheatsheets" / f"{c['id']}.md").write_text("\n".join(out))
print(f"Wrote {len(cheatsheets)} cheatsheets")

# ---------- Projects ----------
(REPO_DIR / "projects").mkdir(parents=True, exist_ok=True)
for f in (REPO_DIR / "projects").glob("*.md"):
    f.unlink()
for p in projects:
    out = []
    out.append("---")
    out.append(f"id: {p['id']}")
    out.append(f"title: {p['title']}")
    out.append(f"tagline: {json.dumps(p['tagline'], ensure_ascii=False)}")
    out.append(f"status: {p['status']}")
    out.append(f"accent: {p['accent']}")
    out.append(f"tech: [{', '.join(json.dumps(t) for t in p['tech'])}]")
    out.append(f"demoUrl: {p.get('demoUrl', '')}")
    out.append(f"githubUrl: {p.get('githubUrl', '')}")
    out.append("---\n")
    out.append(f"# {p['title']}")
    out.append(f"\n> {p['tagline']}\n")
    out.append(f"**Status:** {p['status']}\n")
    out.append("## Description\n")
    out.append(p["description"])
    out.append(f"\n*{p['banglaDescription']}*\n")
    out.append("## Tech Stack\n")
    for t in p["tech"]:
        out.append(f"- {t}")
    out.append("\n## Features\n")
    for f in p["features"]:
        out.append(f"- {f}")
    out.append("")
    (REPO_DIR / "projects" / f"{p['id']}.md").write_text("\n".join(out))
print(f"Wrote {len(projects)} projects")

# ---------- content/index.md (table of contents) ----------
out = []
out.append("# LearnHub Content Index\n")
out.append("All learning content in this repo. Click a topic to read it.\n")
for s in subjects:
    out.append(f"## {s['name']}")
    out.append(f"\n*{s['bangla']}*\n")
    out.append(f"{s['blurb']}\n")
    sub_topics = topics_by_subject[s["id"]]
    out.append("| # | Topic | Difficulty | Time |")
    out.append("|---|-------|-----------|------|")
    for i, t in enumerate(sub_topics, 1):
        rel_path = f"{SUBJECT_DIR[s['id']]}/{t['id']}.md"
        out.append(f"| {i} | [{t['title']}]({rel_path}) | {t['difficulty']} | {t['est']} |")
    out.append("")
(REPO_DIR / "content" / "index.md").write_text("\n".join(out))
print("Wrote content/index.md")

print("\n✓ Done. Markdown repo is at /home/z/my-project/download/learnhub-repo/")
