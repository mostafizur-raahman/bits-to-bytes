"use client";

import { useNav } from "@/lib/store";
import { useProgress } from "@/lib/store";
import {
  SUBJECTS,
  PROJECTS,
  CHEATSHEETS,
  TOPICS,
  getTopicsForSubject,
  type SubjectColor,
} from "@/lib/content";
import { SubjectChip } from "@/components/blocks/subject-chip";
import { MonoLabel } from "@/components/blocks/mono-label";
import {
  AsteriskShape,
  SpikyShape,
  SquiggleShape,
  ZigzagArrow,
  TriangleShape,
} from "@/components/blocks/decorative-shapes";
import { ArrowRight, Folder, Hash, FileText } from "lucide-react";
import { cn } from "@/lib/utils";

const COLOR_TEXT: Record<SubjectColor, string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};

const COLOR_BG_SOFT: Record<SubjectColor, string> = {
  lime: "bg-lime-soft",
  sky: "bg-sky-soft",
  pink: "bg-pink-soft",
  amber: "bg-amber-soft",
};

const COLOR_HOVER_BORDER: Record<SubjectColor, string> = {
  lime: "hover:border-lime/60",
  sky: "hover:border-sky/60",
  pink: "hover:border-pink/60",
  amber: "hover:border-amber/60",
};

export function HomeView() {
  const openTopic = useNav((s) => s.openTopic);
  const openProjects = useNav((s) => s.openProjects);
  const openProject = useNav((s) => s.openProject);
  const openCheatsheet = useNav((s) => s.openCheatsheet);
  const progress = useProgress((s) => s.status);

  const totalDone = Object.values(progress).filter((s) => s === "done").length;
  const totalTopics = TOPICS.length;

  return (
    <div className="view-in mx-auto max-w-5xl px-6 py-10 sm:px-10 sm:py-16">
      {/* ============== HERO ============== */}
      <section className="relative">
        {/* Decorative shapes */}
        <AsteriskShape className="absolute -top-2 right-0 h-6 w-6 text-sky/80 sm:right-12" />
        <SpikyShape className="absolute -top-4 right-24 hidden h-8 w-8 text-lime/70 sm:block" />
        <SquiggleShape className="absolute top-32 -left-4 hidden h-6 w-16 text-pink/60 lg:block" />
        <TriangleShape className="absolute top-44 right-2 hidden h-4 w-4 text-amber/70 lg:block" />

        <div className="mb-6 flex flex-wrap items-center gap-3">
          <SubjectChip color="lime" size="sm">
            DSA FUNDAMENTALS
          </SubjectChip>
          <SubjectChip color="sky" size="sm">
            DATABASE FUNDAMENTALS
          </SubjectChip>
          <SubjectChip color="pink" size="sm">
            NETWORKING FUNDAMENTALS
          </SubjectChip>
          <SubjectChip color="amber" size="sm">
            OS FUNDAMENTALS
          </SubjectChip>
        </div>

        <h1 className="font-pixel text-2xl leading-[1.5] text-foreground sm:text-[28px] md:text-3xl lg:text-4xl">
          START FROM
          <br />
          <span className="text-lime">M</span>
          <span className="text-sky">I</span>
          <span className="text-pink">N</span>
          <span className="text-amber">U</span>
          <span className="text-lime">S</span>{" "}
          <span className="text-sky">O</span>
          <span className="text-pink">N</span>
          <span className="text-amber">E</span>
          <span className="blink ml-2 font-pixel text-lime">_</span>
        </h1>

        <p className="mt-8 max-w-2xl text-base leading-relaxed text-muted-foreground sm:text-lg">
          চারটি কোর সাবজেক্ট — <span className="text-lime">DSA Fundamentals</span>,{" "}
          <span className="text-sky">Database Fundamentals</span>,{" "}
          <span className="text-pink">Networking Fundamentals</span>,{" "}
          <span className="text-amber">OS Fundamentals</span> — বাংলা ও English
          একসাথে, reading-first layout-এ। প্রতিটি টপিকে কোড ব্লক (C++/Go/Python/Java),
          interactive diagram, এবং cheatsheet সহ। শেখা শুরু হয় zero থেকে নয়,
          minus one থেকে — কারণ প্রথমে বুঝতে হবে কেন আমরা শিখছি।
        </p>

        <div className="mt-8 flex flex-wrap items-center gap-4">
          <button
            onClick={() => openTopic("dsa", "dsa-arrays")}
            className="group flex items-center gap-2 rounded-md bg-lime px-4 py-2.5 text-sm font-medium text-background transition-all hover:bg-lime/90 focus-ring"
          >
            শুরু করো — From Minus One
            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
          </button>
          <button
            onClick={openProjects}
            className="flex items-center gap-2 rounded-md border border-border bg-surface px-4 py-2.5 text-sm font-medium text-foreground transition-colors hover:border-foreground/30 focus-ring"
          >
            <Folder className="h-4 w-4" />
            View Projects
          </button>
          <div className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            {totalDone}/{totalTopics} topics done
          </div>
        </div>

        <ZigzagArrow className="mt-10 h-3 w-32 text-lime/60" />
      </section>

      {/* ============== SUBJECTS GRID ============== */}
      <section className="mt-16">
        <div className="mb-6 flex items-baseline justify-between">
          <MonoLabel color="lime">subjects</MonoLabel>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            4 tracks
          </span>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          {SUBJECTS.map((subject) => {
            const topics = getTopicsForSubject(subject.id);
            const topicIds = topics.map((t) => t.id);
            const doneCount = topicIds.filter(
              (id) => progress[id] === "done"
            ).length;

            return (
              <button
                key={subject.id}
                onClick={() => topicIds[0] && openTopic(subject.id, topicIds[0])}
                className={cn(
                  "card-hover group relative overflow-hidden rounded-lg border border-border bg-surface p-5 text-left focus-ring",
                  COLOR_HOVER_BORDER[subject.color]
                )}
              >
                <div
                  className={cn(
                    "absolute -right-6 -top-6 h-20 w-20 rounded-full opacity-50 blur-2xl",
                    COLOR_BG_SOFT[subject.color]
                  )}
                />
                <div className="relative">
                  <div className="mb-3 flex items-center justify-between">
                    <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
                      /{subject.name.toLowerCase()}
                    </span>
                    <span
                      className={cn(
                        "font-mono text-[11px]",
                        COLOR_TEXT[subject.color]
                      )}
                    >
                      {doneCount}/{topicIds.length}
                    </span>
                  </div>
                  <h3
                    className={cn(
                      "font-display text-xl font-semibold tracking-tight",
                      COLOR_TEXT[subject.color]
                    )}
                  >
                    {subject.name}
                  </h3>
                  <p className="mt-1 text-xs text-muted-foreground">
                    {subject.bangla}
                  </p>
                  <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                    {subject.blurb}
                  </p>
                  <div className="mt-4 flex items-center gap-1.5 font-mono text-[11px] uppercase tracking-wider text-muted-foreground transition-colors group-hover:text-foreground">
                    open track
                    <ArrowRight className="h-3 w-3 transition-transform group-hover:translate-x-0.5" />
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </section>

      {/* ============== FEATURED PROJECTS ============== */}
      <section className="mt-20">
        <div className="mb-6 flex items-baseline justify-between">
          <MonoLabel color="sky">featured projects</MonoLabel>
          <button
            onClick={openProjects}
            className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground transition-colors hover:text-foreground"
          >
            view all →
          </button>
        </div>

        <div className="grid gap-4 md:grid-cols-3">
          {PROJECTS.slice(0, 3).map((p) => (
            <button
              key={p.id}
              onClick={() => openProject(p.id)}
              className={cn(
                "card-hover group rounded-lg border border-border bg-surface p-5 text-left focus-ring",
                COLOR_HOVER_BORDER[p.accent]
              )}
            >
              <div className="mb-3 flex items-center justify-between">
                <span
                  className={cn(
                    "grid h-10 w-12 place-items-center rounded-md border border-border bg-surface-sunken font-mono text-xs",
                    COLOR_TEXT[p.accent]
                  )}
                >
                  {p.cover}
                </span>
                <span
                  className={cn(
                    "font-mono text-[10px] uppercase tracking-wider",
                    p.status === "shipped"
                      ? "text-lime"
                      : p.status === "wip"
                      ? "text-amber"
                      : "text-muted-foreground"
                  )}
                >
                  {p.status}
                </span>
              </div>
              <h4 className="font-display text-base font-semibold">
                {p.title}
              </h4>
              <p className="mt-1 text-xs text-muted-foreground">{p.tagline}</p>
              <div className="mt-3 flex flex-wrap gap-1">
                {p.tech.slice(0, 3).map((t) => (
                  <span
                    key={t}
                    className="rounded border border-border bg-surface-sunken px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground"
                  >
                    {t}
                  </span>
                ))}
              </div>
            </button>
          ))}
        </div>
      </section>

      {/* ============== CHEATSHEETS ============== */}
      <section className="mt-20">
        <div className="mb-6 flex items-baseline justify-between">
          <MonoLabel color="pink">quick cheatsheets</MonoLabel>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            bilingual tables
          </span>
        </div>

        <div className="grid gap-3 sm:grid-cols-2">
          {CHEATSHEETS.map((c) => {
            const subject = SUBJECTS.find((s) => s.id === c.subject)!;
            return (
              <button
                key={c.id}
                onClick={() => openCheatsheet(c.id)}
                className="card-hover group flex items-center gap-4 rounded-lg border border-border bg-surface p-4 text-left focus-ring"
              >
                <div
                  className={cn(
                    "grid h-10 w-10 shrink-0 place-items-center rounded-md",
                    COLOR_BG_SOFT[subject.color]
                  )}
                >
                  <Hash className={cn("h-4 w-4", COLOR_TEXT[subject.color])} />
                </div>
                <div className="min-w-0 flex-1">
                  <div className="flex items-center gap-2">
                    <span className="font-display text-sm font-semibold">
                      {c.title}
                    </span>
                    <span className="font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
                      · {subject.name}
                    </span>
                  </div>
                  <div className="mt-0.5 truncate text-xs text-muted-foreground">
                    {c.bangla}
                  </div>
                </div>
                <ArrowRight className="h-3.5 w-3.5 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
              </button>
            );
          })}
        </div>
      </section>

      {/* ============== FOOTER ============== */}
      <footer className="mt-24 border-t border-border pt-6 pb-12">
        <div className="flex flex-col items-start justify-between gap-4 sm:flex-row sm:items-center">
          <div className="flex items-center gap-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            <FileText className="h-3.5 w-3.5" />
            bittobytes · cs fundamentals · bangla + english
          </div>
          <div className="font-mono text-[11px] text-muted-foreground">
            built with{" "}
            <span className="text-lime">next.js</span> ·{" "}
            <span className="text-sky">tailwind</span> ·{" "}
            <span className="text-pink">shadcn</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
