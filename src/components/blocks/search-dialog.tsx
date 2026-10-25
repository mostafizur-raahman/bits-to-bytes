"use client";

import { useEffect, useMemo, useState } from "react";
import { useNav } from "@/lib/store";
import {
  TOPICS,
  PROJECTS,
  CHEATSHEETS,
  SUBJECTS,
  type SubjectId,
} from "@/lib/content";
import { Search, X, CornerDownLeft, Hash, Folder, FileText } from "lucide-react";
import { cn } from "@/lib/utils";

interface Result {
  kind: "topic" | "project" | "cheatsheet";
  id: string;
  title: string;
  sub: string;
  subject?: SubjectId;
  accent: "lime" | "sky" | "pink" | "amber";
}

const ALL_RESULTS: Result[] = [
  ...TOPICS.map<Result>((t) => {
    const subject = SUBJECTS.find((s) => s.id === t.subject)!;
    return {
      kind: "topic",
      id: t.id,
      title: t.title,
      sub: t.bangla,
      subject: t.subject,
      accent: subject.color,
    };
  }),
  ...PROJECTS.map<Result>((p) => ({
    kind: "project",
    id: p.id,
    title: p.title,
    sub: p.tagline,
    accent: p.accent,
  })),
  ...CHEATSHEETS.map<Result>((c) => {
    const subject = SUBJECTS.find((s) => s.id === c.subject)!;
    return {
      kind: "cheatsheet",
      id: c.id,
      title: c.title,
      sub: c.bangla,
      subject: c.subject,
      accent: subject.color,
    };
  }),
];

function score(query: string, target: string): number {
  if (!query) return 0;
  const q = query.toLowerCase();
  const t = target.toLowerCase();
  if (t.startsWith(q)) return 100 - (t.length - q.length);
  if (t.includes(q)) return 50;
  return 0;
}

const accentTextMap: Record<Result["accent"], string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};
const accentDotMap: Record<Result["accent"], string> = {
  lime: "bg-lime",
  sky: "bg-sky",
  pink: "bg-pink",
  amber: "bg-amber",
};

/** Inner dialog — local state resets automatically when remounted (via key) */
function SearchDialogInner() {
  const setOpen = useNav((s) => s.setSearchOpen);
  const openTopic = useNav((s) => s.openTopic);
  const openProject = useNav((s) => s.openProject);
  const openCheatsheet = useNav((s) => s.openCheatsheet);

  const [q, setQ] = useState("");
  const [active, setActive] = useState(0);

  const results = useMemo(() => {
    if (!q.trim()) return ALL_RESULTS.slice(0, 8);
    return ALL_RESULTS.map((r) => ({
      r,
      s: Math.max(score(q, r.title), score(q, r.sub), score(q, r.kind)),
    }))
      .filter((x) => x.s > 0)
      .sort((a, b) => b.s - a.s)
      .slice(0, 10)
      .map((x) => x.r);
  }, [q]);

  const pick = (r: Result) => {
    if (r.kind === "topic" && r.subject) openTopic(r.subject, r.id);
    else if (r.kind === "project") openProject(r.id);
    else if (r.kind === "cheatsheet")
      openCheatsheet(r.id as "big-o" | "sql-joins" | "osi-layers" | "linux-cmds");
    setOpen(false);
  };

  // Arrow-key navigation
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        setActive((a) => Math.min(a + 1, results.length - 1));
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        setActive((a) => Math.max(a - 1, 0));
      } else if (e.key === "Enter" && results[active]) {
        e.preventDefault();
        pick(results[active]);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [results, active]);

  return (
    <div
      className="fixed inset-0 z-50 flex items-start justify-center bg-background/70 p-4 backdrop-blur-sm sm:pt-[12vh]"
      onClick={() => setOpen(false)}
    >
      <div
        className="view-in w-full max-w-xl overflow-hidden rounded-xl border border-border bg-surface shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-3 border-b border-border px-4 py-3">
          <Search className="h-4 w-4 text-muted-foreground" />
          <input
            autoFocus
            value={q}
            onChange={(e) => {
              setQ(e.target.value);
              setActive(0);
            }}
            placeholder="Search topics, projects, cheatsheets…"
            className="flex-1 bg-transparent text-sm text-foreground outline-none placeholder:text-muted-foreground"
          />
          <kbd className="hidden rounded border border-border bg-secondary px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground sm:inline">
            ESC
          </kbd>
          <button
            onClick={() => setOpen(false)}
            className="rounded p-1 text-muted-foreground hover:bg-secondary hover:text-foreground focus-ring"
            aria-label="Close"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        <ul className="thin-scroll max-h-[60vh] overflow-y-auto p-2">
          {results.length === 0 && (
            <li className="px-3 py-6 text-center text-sm text-muted-foreground">
              No matches for &ldquo;{q}&rdquo;
            </li>
          )}
          {results.map((r, i) => {
            const Icon =
              r.kind === "topic" ? FileText : r.kind === "project" ? Folder : Hash;
            return (
              <li key={`${r.kind}-${r.id}`}>
                <button
                  onClick={() => pick(r)}
                  onMouseEnter={() => setActive(i)}
                  className={cn(
                    "flex w-full items-center gap-3 rounded-md px-3 py-2 text-left transition-colors",
                    i === active ? "bg-secondary" : "hover:bg-secondary/50"
                  )}
                >
                  <span
                    className={cn(
                      "h-1.5 w-1.5 shrink-0 rounded-full",
                      accentDotMap[r.accent]
                    )}
                  />
                  <Icon
                    className={cn("h-4 w-4 shrink-0", accentTextMap[r.accent])}
                  />
                  <div className="flex-1 min-w-0">
                    <div className="truncate text-sm font-medium text-foreground">
                      {r.title}
                    </div>
                    <div className="truncate text-xs text-muted-foreground">
                      {r.sub}
                    </div>
                  </div>
                  <span className="font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                    {r.kind}
                  </span>
                  {i === active && (
                    <CornerDownLeft className="h-3.5 w-3.5 text-muted-foreground" />
                  )}
                </button>
              </li>
            );
          })}
        </ul>
        <div className="border-t border-border px-4 py-2 text-[11px] text-muted-foreground">
          <span className="font-mono">↑↓</span> navigate{" "}
          <span className="font-mono">↵</span> open{" "}
          <span className="font-mono">esc</span> close
        </div>
      </div>
    </div>
  );
}

export function SearchDialog() {
  const open = useNav((s) => s.searchOpen);

  // Cmd/Ctrl+K toggles, Esc closes
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        useNav.setState((s) => ({ searchOpen: !s.searchOpen }));
      } else if (e.key === "Escape" && useNav.getState().searchOpen) {
        useNav.setState({ searchOpen: false });
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  if (!open) return null;
  // key forces remount → local state (q, active) resets each time dialog opens
  return <SearchDialogInner key="search-dialog" />;
}
