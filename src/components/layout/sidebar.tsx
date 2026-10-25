"use client";

import { useNav } from "@/lib/store";
import { useProgress } from "@/lib/store";
import {
  SUBJECTS,
  getTopicsForSubject,
  CHEATSHEETS,
  type SubjectColor,
} from "@/lib/content";
import { ChevronRight, ChevronDown, FileText, Hash } from "lucide-react";
import { useState } from "react";
import { cn } from "@/lib/utils";

const COLOR_ACTIVE: Record<SubjectColor, string> = {
  lime: "active-glow-lime",
  sky: "active-glow-sky",
  pink: "active-glow-pink",
  amber: "active-glow-amber",
};

const COLOR_TEXT: Record<SubjectColor, string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};

export function Sidebar() {
  const view = useNav((s) => s.view);
  const currentSubject = useNav((s) => s.subject);
  const currentTopicId = useNav((s) => s.topicId);
  const openTopic = useNav((s) => s.openTopic);
  const openCheatsheet = useNav((s) => s.openCheatsheet);
  const cheatsheetId = useNav((s) => s.cheatsheetId);
  const goHome = useNav((s) => s.goHome);

  const progress = useProgress((s) => s.status);

  const initialOpen = currentSubject ?? "dsa";
  const [open, setOpen] = useState<Record<string, boolean>>({
    [initialOpen]: true,
  });

  const toggle = (id: string) =>
    setOpen((o) => ({ ...o, [id]: !o[id] }));

  return (
    <aside className="thin-scroll sticky top-14 hidden h-[calc(100vh-3.5rem)] w-64 shrink-0 overflow-y-auto border-r border-border bg-surface/40 px-3 py-4 lg:block">
      {/* Home */}
      <button
        onClick={goHome}
        className={cn(
          "mb-2 flex w-full items-center gap-2 rounded-md px-2 py-1.5 text-left text-sm transition-colors focus-ring",
          view === "home"
            ? "bg-secondary text-foreground"
            : "text-muted-foreground hover:bg-secondary/60 hover:text-foreground"
        )}
      >
        <span className="font-mono text-[10px] uppercase">~</span>
        Home
      </button>

      {/* Subjects */}
      <div className="mb-1 px-2 font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
        subjects
      </div>
      <nav className="space-y-0.5">
        {SUBJECTS.map((subject) => {
          const topics = getTopicsForSubject(subject.id);
          const isOpen = !!open[subject.id];
          const doneCount = topics.filter(
            (t) => progress[t.id] === "done"
          ).length;

          return (
            <div key={subject.id}>
              <button
                onClick={() => toggle(subject.id)}
                className="flex w-full items-center gap-1.5 rounded-md px-2 py-1.5 text-left text-sm text-foreground transition-colors hover:bg-secondary focus-ring"
              >
                {isOpen ? (
                  <ChevronDown className="h-3.5 w-3.5 text-muted-foreground" />
                ) : (
                  <ChevronRight className="h-3.5 w-3.5 text-muted-foreground" />
                )}
                <span className={cn("font-mono text-[10px] uppercase", COLOR_TEXT[subject.color])}>
                  /{subject.name.toLowerCase()}
                </span>
                <span className="flex-1">{subject.name}</span>
                {doneCount > 0 && (
                  <span className="font-mono text-[10px] text-muted-foreground">
                    {doneCount}/{topics.length}
                  </span>
                )}
              </button>

              {isOpen && (
                <ul className="ml-4 mt-0.5 space-y-0.5 border-l border-border pl-2">
                  {topics.map((topic) => {
                    const isActive =
                      currentTopicId === topic.id &&
                      currentSubject === subject.id;
                    const status = progress[topic.id];
                    return (
                      <li key={topic.id}>
                        <button
                          onClick={() => openTopic(subject.id, topic.id)}
                          className={cn(
                            "flex w-full items-center gap-2 rounded-md px-2 py-1.5 text-left text-[13px] transition-colors focus-ring",
                            isActive
                              ? `${COLOR_ACTIVE[subject.color]} text-foreground`
                              : "text-muted-foreground hover:bg-secondary/60 hover:text-foreground",
                            !isActive && status === "done" && "text-lime/80"
                          )}
                        >
                          <FileText className="h-3 w-3 shrink-0 opacity-70" />
                          <span className="flex-1 truncate">{topic.title}</span>
                          {status === "done" && (
                            <span className="font-mono text-[10px] text-lime">
                              ✓
                            </span>
                          )}
                          {status === "learning" && (
                            <span className="font-mono text-[10px] text-amber">
                              …
                            </span>
                          )}
                        </button>
                      </li>
                    );
                  })}
                </ul>
              )}
            </div>
          );
        })}
      </nav>

      {/* Cheatsheets */}
      <div className="mb-1 mt-6 px-2 font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
        cheatsheets
      </div>
      <nav className="space-y-0.5">
        {CHEATSHEETS.map((c) => {
          const isActive = view === "cheatsheet" && cheatsheetId === c.id;
          const subject = SUBJECTS.find((s) => s.id === c.subject)!;
          return (
            <button
              key={c.id}
              onClick={() => openCheatsheet(c.id)}
              className={cn(
                "flex w-full items-center gap-2 rounded-md px-2 py-1.5 text-left text-[13px] transition-colors focus-ring",
                isActive
                  ? `${COLOR_ACTIVE[subject.color]} text-foreground`
                  : "text-muted-foreground hover:bg-secondary/60 hover:text-foreground"
              )}
            >
              <Hash
                className={cn("h-3 w-3 shrink-0 opacity-70", COLOR_TEXT[subject.color])}
              />
              <span className="flex-1 truncate">{c.title}</span>
            </button>
          );
        })}
      </nav>

      <div className="mt-6 px-2 py-2 text-[10px] text-muted-foreground">
        <p>
          <span className="font-mono">tip:</span> Press{" "}
          <kbd className="rounded border border-border bg-secondary px-1 py-0.5 font-mono">
            ⌘K
          </kbd>{" "}
          to search.
        </p>
      </div>
    </aside>
  );
}
