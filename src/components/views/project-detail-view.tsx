"use client";

import { useNav } from "@/lib/store";
import { getProjectById, type SubjectColor } from "@/lib/content";
import { CodeBlock } from "@/components/blocks/code-block";
import { MultiLangCode } from "@/components/blocks/multi-lang-code";
import { MonoLabel } from "@/components/blocks/mono-label";
import type { TopicSection } from "@/lib/content";
import { ArrowLeft, Check, CircleDot, Circle, Sparkles, Info, AlertTriangle, Lightbulb } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  AsteriskShape,
  SpikyShape,
  SquiggleShape,
  TriangleShape,
} from "@/components/blocks/decorative-shapes";

const COLOR_TEXT: Record<SubjectColor, string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};

const COLOR_BORDER: Record<SubjectColor, string> = {
  lime: "border-lime/40",
  sky: "border-sky/40",
  pink: "border-pink/40",
  amber: "border-amber/40",
};

const STATUS_META = {
  shipped: { label: "Shipped", color: "text-lime", icon: Check },
  wip: { label: "Work in progress", color: "text-amber", icon: CircleDot },
  planned: { label: "Planned", color: "text-muted-foreground", icon: Circle },
} as const;

function SectionBlock({ section }: { section: TopicSection }) {
  switch (section.type) {
    case "h2":
      return (
        <h2 id={section.id} className="font-display text-2xl font-semibold tracking-tight">
          {section.title}
        </h2>
      );
    case "h3":
      return (
        <h3 className="font-display text-lg font-semibold tracking-tight">
          {section.title}
        </h3>
      );
    case "p":
      return <p className="text-foreground/85">{section.text}</p>;
    case "list":
      return (
        <ul className="space-y-1.5">
          {section.items?.map((it, i) => (
            <li key={i} className="flex gap-2.5 text-foreground/85">
              <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-muted-foreground" />
              <span>{it}</span>
            </li>
          ))}
        </ul>
      );
    case "code":
      return <CodeBlock code={section.text ?? ""} lang={section.lang} />;
    case "multi-code":
      return (
        <MultiLangCode
          samples={section.codeSamples ?? {}}
          filename={section.filename}
        />
      );
    case "callout": {
      const tone = section.calloutTone ?? "info";
      const meta = {
        info: { icon: Info, color: "text-sky", bg: "bg-sky-soft", border: "border-sky/30", label: "NOTE" },
        warn: { icon: AlertTriangle, color: "text-amber", bg: "bg-amber-soft", border: "border-amber/30", label: "WARNING" },
        tip: { icon: Lightbulb, color: "text-lime", bg: "bg-lime-soft", border: "border-lime/30", label: "TIP" },
      }[tone];
      const Icon = meta.icon;
      return (
        <div className={cn("my-5 flex gap-3 rounded-lg border bg-surface p-4", meta.border)}>
          <Icon className={cn("h-4 w-4 shrink-0 mt-0.5", meta.color)} />
          <div className="flex-1">
            <div className={cn("mb-1 font-mono text-[10px] uppercase tracking-wider", meta.color)}>
              {meta.label}
            </div>
            <p className="text-sm text-foreground/85">{section.text}</p>
          </div>
        </div>
      );
    }
    default:
      return null;
  }
}

export function ProjectDetailView() {
  const projectId = useNav((s) => s.projectId);
  const openProjects = useNav((s) => s.openProjects);

  const project = projectId ? getProjectById(projectId) : undefined;

  if (!project) {
    return (
      <div className="view-in mx-auto max-w-2xl px-6 py-20 text-center text-muted-foreground">
        Project not found.
        <button
          onClick={openProjects}
          className="mt-4 block w-full text-lime underline"
        >
          ← back to projects
        </button>
      </div>
    );
  }

  const statusMeta = STATUS_META[project.status];
  const StatusIcon = statusMeta.icon;

  return (
    <article className="view-in mx-auto max-w-3xl px-6 py-10 sm:px-10">
      {/* Breadcrumb */}
      <div className="mb-8 flex items-center gap-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
        <button
          onClick={openProjects}
          className="flex items-center gap-1 hover:text-foreground focus-ring rounded"
        >
          <ArrowLeft className="h-3 w-3" />
          back
        </button>
        <span>/</span>
        <span className="text-foreground">{project.title.toLowerCase()}</span>
      </div>

      {/* Header */}
      <header className="relative mb-8">
        <AsteriskShape className="absolute -top-2 right-0 h-6 w-6 text-sky/70" />
        <SpikyShape className="absolute -top-3 right-14 hidden h-6 w-6 text-lime/70 sm:block" />

        <div className="flex items-center gap-3">
          <span
            className={cn(
              "grid h-16 w-20 place-items-center rounded-md border bg-surface-sunken font-mono text-base",
              COLOR_BORDER[project.accent],
              COLOR_TEXT[project.accent]
            )}
          >
            {project.cover}
          </span>
          <div>
            <h1 className="font-display text-3xl font-bold tracking-tight sm:text-4xl">
              {project.title}
            </h1>
            <p className="mt-1 text-sm text-muted-foreground">{project.tagline}</p>
          </div>
        </div>

        <div className="mt-5 flex flex-wrap items-center gap-2">
          <span
            className={cn(
              "flex items-center gap-1.5 rounded-md border border-border bg-surface px-2 py-1 font-mono text-[11px] uppercase tracking-wider",
              statusMeta.color
            )}
          >
            <StatusIcon className="h-3 w-3" />
            {statusMeta.label}
          </span>
          {project.tech.map((t) => (
            <span
              key={t}
              className="rounded-md border border-border bg-surface px-2 py-1 font-mono text-[11px] text-muted-foreground"
            >
              {t}
            </span>
          ))}
        </div>
      </header>

      {/* Overview */}
      <section className="mb-8">
        <MonoLabel color={project.accent}>overview</MonoLabel>
        <div className="prose-learn mt-4 space-y-4">
          <p>{project.description}</p>
          <p className="text-muted-foreground">{project.banglaDescription}</p>
        </div>
      </section>

      {/* Features */}
      <section className="mb-8">
        <div className="mb-4 flex items-center gap-2">
          <Sparkles className={cn("h-4 w-4", COLOR_TEXT[project.accent])} />
          <MonoLabel color={project.accent}>key features</MonoLabel>
        </div>
        <div className="grid gap-3 sm:grid-cols-2">
          {project.features.map((f, i) => (
            <div key={i} className="rounded-lg border border-border bg-surface p-4 card-hover">
              <div className="flex items-start gap-3">
                <span className={cn("mt-0.5 grid h-5 w-5 shrink-0 place-items-center rounded font-mono text-[10px] border", COLOR_TEXT[project.accent], COLOR_BORDER[project.accent])}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <p className="text-sm text-foreground/85">{f}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Step-by-step Guide (Book-like reading sections) */}
      {project.sections && project.sections.length > 0 && (
        <section className="mb-8">
          <MonoLabel color={project.accent}>step-by-step guide</MonoLabel>
          <div className="prose-learn mt-4 space-y-4">
            {project.sections.map((s, i) => (
              <SectionBlock key={`proj-${i}-${s.type}`} section={s} />
            ))}
          </div>
        </section>
      )}

      {/* Tech stack */}
      <section className="mb-8">
        <MonoLabel color={project.accent}>tech stack</MonoLabel>
        <div className="mt-4 flex flex-wrap gap-2">
          {project.tech.map((t) => (
            <span key={t} className={cn("rounded-md border px-3 py-1.5 font-mono text-xs bg-surface", COLOR_BORDER[project.accent], COLOR_TEXT[project.accent])}>
              {t}
            </span>
          ))}
        </div>
      </section>

      {/* Footer */}
      <div className="mt-16 flex items-center gap-3 border-t border-border pt-6">
        <SquiggleShape className="h-3 w-20 text-muted-foreground/60" />
        <TriangleShape className="h-3 w-3 text-amber/60" />
        <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
          end of project
        </span>
      </div>
    </article>
  );
}
