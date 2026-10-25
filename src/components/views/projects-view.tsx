"use client";

import { useNav } from "@/lib/store";
import { PROJECTS, type SubjectColor } from "@/lib/content";
import { MonoLabel } from "@/components/blocks/mono-label";
import { ArrowRight, Cpu, CheckCircle2, Circle, CircleDot } from "lucide-react";
import { cn } from "@/lib/utils";
import { SpikyShape, AsteriskShape, TriangleShape } from "@/components/blocks/decorative-shapes";

const COLOR_TEXT: Record<SubjectColor, string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};

const COLOR_HOVER_BORDER: Record<SubjectColor, string> = {
  lime: "hover:border-lime/60",
  sky: "hover:border-sky/60",
  pink: "hover:border-pink/60",
  amber: "hover:border-amber/60",
};

const STATUS_META = {
  shipped: { label: "shipped", color: "text-lime", icon: CheckCircle2 },
  wip: { label: "wip", color: "text-amber", icon: CircleDot },
  planned: { label: "planned", color: "text-muted-foreground", icon: Circle },
} as const;

export function ProjectsView() {
  const openProject = useNav((s) => s.openProject);

  return (
    <div className="view-in mx-auto max-w-5xl px-6 py-10 sm:px-10 sm:py-16">
      {/* Header */}
      <section className="relative">
        <AsteriskShape className="absolute -top-2 right-0 h-6 w-6 text-sky/70" />
        <SpikyShape className="absolute -top-3 right-12 hidden h-7 w-7 text-lime/70 sm:block" />

        <MonoLabel color="sky">/ projects</MonoLabel>
        <h1 className="mt-3 font-pixel text-xl leading-relaxed text-foreground sm:text-2xl">
          BUILT WITH <span className="text-sky">NEXT.JS</span>
        </h1>
        <p className="mt-6 max-w-2xl text-base leading-relaxed text-muted-foreground">
          এই প্রজেক্টগুলো শেখা কনসেপ্টগুলোকে বাস্তবে রূপ দেওয়ার জায়গা — প্রতিটি
          প্রজেক্ট একটি নির্দিষ্ট সাবজেক্টের (DSA / DB / Net / OS) সাথে যুক্ত।
          Live demo ও source code সব জায়গায় আছে।
        </p>

        <TriangleShape className="mt-6 h-3 w-3 text-amber/70" />
      </section>

      {/* Project grid */}
      <section className="mt-12">
        <div className="mb-4 flex items-center justify-between">
          <MonoLabel color="lime">all projects</MonoLabel>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            {PROJECTS.length} total
          </span>
        </div>

        <div className="grid gap-4 md:grid-cols-2">
          {PROJECTS.map((p) => {
            const statusMeta = STATUS_META[p.status];
            const StatusIcon = statusMeta.icon;
            return (
              <button
                key={p.id}
                onClick={() => openProject(p.id)}
                className={cn(
                  "card-hover group relative overflow-hidden rounded-xl border border-border bg-surface p-6 text-left focus-ring",
                  COLOR_HOVER_BORDER[p.accent]
                )}
              >
                <div
                  className={cn(
                    "absolute -right-12 -top-12 h-32 w-32 rounded-full opacity-30 blur-3xl",
                    p.accent === "lime" && "bg-lime",
                    p.accent === "sky" && "bg-sky",
                    p.accent === "pink" && "bg-pink",
                    p.accent === "amber" && "bg-amber"
                  )}
                />

                <div className="relative">
                  <div className="mb-4 flex items-start justify-between">
                    <div
                      className={cn(
                        "grid h-14 w-16 place-items-center rounded-md border border-border bg-surface-sunken font-mono text-sm",
                        COLOR_TEXT[p.accent]
                      )}
                    >
                      {p.cover}
                    </div>
                    <span
                      className={cn(
                        "flex items-center gap-1 font-mono text-[10px] uppercase tracking-wider",
                        statusMeta.color
                      )}
                    >
                      <StatusIcon className="h-3 w-3" />
                      {statusMeta.label}
                    </span>
                  </div>

                  <h3 className="font-display text-xl font-semibold tracking-tight">
                    {p.title}
                  </h3>
                  <p className="mt-1 text-xs text-muted-foreground">
                    {p.banglaDescription.slice(0, 80)}…
                  </p>
                  <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                    {p.tagline}
                  </p>

                  <div className="mt-4 flex flex-wrap gap-1.5">
                    {p.tech.map((t) => (
                      <span
                        key={t}
                        className="rounded border border-border bg-surface-sunken px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground"
                      >
                        {t}
                      </span>
                    ))}
                  </div>

                  <div
                    className={cn(
                      "mt-5 flex items-center gap-1.5 font-mono text-[11px] uppercase tracking-wider transition-colors",
                      COLOR_TEXT[p.accent]
                    )}
                  >
                    open project
                    <ArrowRight className="h-3 w-3 transition-transform group-hover:translate-x-0.5" />
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </section>

      {/* Footer note */}
      <section className="mt-16 rounded-lg border border-border bg-surface p-5">
        <div className="flex items-center gap-3">
          <Cpu className="h-5 w-5 text-amber" />
          <div>
            <div className="font-display text-sm font-semibold">
              Want to contribute a project?
            </div>
            <p className="mt-1 text-xs text-muted-foreground">
              প্রতিটি প্রজেক্ট একটি subject track-এর সাথে যুক্ত — DSA, DB,
              Networking, বা OS. নতুন idea থাকলে GitHub-এ issue খুলুন।
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
