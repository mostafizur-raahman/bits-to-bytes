"use client";

import { useNav } from "@/lib/store";
import {
  getCheatsheetById,
  getSubjectById,
  getTopicsForSubject,
} from "@/lib/content";
import { MonoLabel } from "@/components/blocks/mono-label";
import { SubjectChip } from "@/components/blocks/subject-chip";
import { ArrowLeft } from "lucide-react";
import { cn } from "@/lib/utils";
import { AsteriskShape, SpikyShape } from "@/components/blocks/decorative-shapes";

export function CheatsheetView() {
  const cheatsheetId = useNav((s) => s.cheatsheetId);
  const openTopic = useNav((s) => s.openTopic);
  const goHome = useNav((s) => s.goHome);

  const c = cheatsheetId ? getCheatsheetById(cheatsheetId) : undefined;

  if (!c) {
    return (
      <div className="view-in mx-auto max-w-2xl px-6 py-20 text-center text-muted-foreground">
        Cheatsheet not found.
      </div>
    );
  }

  const subject = getSubjectById(c.subject)!;
  const COLOR_TEXT = {
    lime: "text-lime",
    sky: "text-sky",
    pink: "text-pink",
    amber: "text-amber",
  } as const;
  const COLOR_BORDER = {
    lime: "border-lime/30",
    sky: "border-sky/30",
    pink: "border-pink/30",
    amber: "border-amber/30",
  } as const;
  const COLOR_HEADER_BG = {
    lime: "bg-lime-soft",
    sky: "bg-sky-soft",
    pink: "bg-pink-soft",
    amber: "bg-amber-soft",
  } as const;

  return (
    <div className="view-in mx-auto max-w-4xl px-6 py-10 sm:px-10">
      {/* Breadcrumb */}
      <div className="mb-6 flex items-center gap-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
        <button onClick={goHome} className="hover:text-foreground focus-ring rounded">
          ~
        </button>
        <span>/</span>
        <span className="text-foreground">cheatsheets</span>
        <span>/</span>
        <span className="text-foreground">{c.title.toLowerCase()}</span>
      </div>

      {/* Header */}
      <header className="relative mb-8">
        <AsteriskShape className="absolute -top-2 right-0 h-5 w-5 text-sky/70" />
        <SpikyShape className="absolute -top-2 right-10 hidden h-6 w-6 text-lime/70 sm:block" />

        <div className="mb-3 flex flex-wrap items-center gap-2">
          <SubjectChip color={subject.color} size="md">
            {subject.name}
          </SubjectChip>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            · {c.rows.length} rows
          </span>
        </div>

        <h1 className="font-display text-3xl font-bold tracking-tight sm:text-4xl">
          {c.title}
        </h1>
        <p className="mt-1 font-mono text-sm text-muted-foreground">{c.bangla}</p>
        <p className="mt-4 max-w-2xl text-sm leading-relaxed text-muted-foreground">
          {c.description}
        </p>
      </header>

      {/* Table */}
      <div
        className={cn(
          "overflow-hidden rounded-lg border bg-surface",
          COLOR_BORDER[subject.color]
        )}
      >
        <div className="overflow-x-auto thin-scroll">
          <table className="w-full text-left text-sm">
            <thead>
              <tr
                className={cn(
                  "border-b border-border",
                  COLOR_HEADER_BG[subject.color]
                )}
              >
                {c.columns.map((col, i) => (
                  <th
                    key={i}
                    className={cn(
                      "px-4 py-3 font-mono text-[11px] font-semibold uppercase tracking-wider",
                      COLOR_TEXT[subject.color],
                      i === 0 ? "text-left" : "text-left"
                    )}
                  >
                    {col}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {c.rows.map((row, ri) => (
                <tr
                  key={ri}
                  className="border-b border-border/60 last:border-b-0 transition-colors hover:bg-secondary/40"
                >
                  {row.map((cell, ci) => (
                    <td
                      key={ci}
                      className={cn(
                        "px-4 py-3 align-top",
                        ci === 0
                          ? cn("font-medium", COLOR_TEXT[subject.color])
                          : "text-foreground/80",
                        ci > 0 && "font-mono text-[13px]"
                      )}
                    >
                      {cell}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Related topic */}
      <div className="mt-10 border-t border-border pt-6">
        <MonoLabel color={subject.color}>deep dive</MonoLabel>
        <p className="mt-2 text-sm text-muted-foreground">
          এই cheatsheet-এর বিষয়বস্তু বিস্তারিতভাবে শিখতে চাইলে{" "}
          <span className={COLOR_TEXT[subject.color]}>
            {subject.name}
          </span>{" "}
          track-এর টপিকগুলো দেখুন।
        </p>
        <button
          onClick={() => {
            const firstTopicId = getTopicsForSubject(subject.id)[0]?.id;
            if (firstTopicId) openTopic(subject.id, firstTopicId);
          }}
          className="mt-3 flex items-center gap-2 rounded-md border border-border bg-surface px-3 py-1.5 text-sm text-foreground transition-colors hover:border-foreground/30 focus-ring"
        >
          <ArrowLeft className="h-3.5 w-3.5 rotate-180" />
          Open {subject.name} track
        </button>
      </div>
    </div>
  );
}
