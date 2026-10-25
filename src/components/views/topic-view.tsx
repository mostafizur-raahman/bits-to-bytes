"use client";

import { useNav } from "@/lib/store";
import {
  getTopicById,
  getSubjectById,
  getTopicsForSubject,
  type Topic,
  type TopicSection,
} from "@/lib/content";
import { CodeBlock } from "@/components/blocks/code-block";
import { MultiLangCode } from "@/components/blocks/multi-lang-code";
import { SubjectChip } from "@/components/blocks/subject-chip";
import { MonoLabel } from "@/components/blocks/mono-label";
import { ProgressTracker } from "@/components/blocks/progress-tracker";
import { SortingVisualizer } from "@/components/diagrams/sorting-visualizer";
import { TCPHandshake } from "@/components/diagrams/tcp-handshake";
import { ArrowLeft, Clock, Gauge, Info, AlertTriangle, Lightbulb } from "lucide-react";
import { cn } from "@/lib/utils";

function SectionBlock({ section, index = 0 }: { section: TopicSection; index?: number }) {
  switch (section.type) {
    case "h2":
      return (
        <h2 id={section.id ?? `sec-${index}`} className="font-display text-2xl font-semibold tracking-tight scroll-mt-20">
          {section.title}
        </h2>
      );
    case "h3":
      return (
        <h3 id={`sec-${index}`} className="font-display text-lg font-semibold tracking-tight scroll-mt-20">
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
        info: {
          icon: Info,
          color: "text-sky",
          bg: "bg-sky-soft",
          border: "border-sky/30",
          label: "NOTE",
        },
        warn: {
          icon: AlertTriangle,
          color: "text-amber",
          bg: "bg-amber-soft",
          border: "border-amber/30",
          label: "WARNING",
        },
        tip: {
          icon: Lightbulb,
          color: "text-lime",
          bg: "bg-lime-soft",
          border: "border-lime/30",
          label: "TIP",
        },
      }[tone];
      const Icon = meta.icon;
      return (
        <div
          className={cn(
            "my-5 flex gap-3 rounded-lg border bg-surface p-4",
            meta.border
          )}
        >
          <Icon className={cn("h-4 w-4 shrink-0 mt-0.5", meta.color)} />
          <div className="flex-1">
            <div
              className={cn(
                "mb-1 font-mono text-[10px] uppercase tracking-wider",
                meta.color
              )}
            >
              {meta.label}
            </div>
            <p className="text-sm text-foreground/85">{section.text}</p>
          </div>
        </div>
      );
    }
    case "diagram":
      if (section.diagram === "sorting") return <SortingVisualizer />;
      if (section.diagram === "tcp-handshake") return <TCPHandshake />;
      return null;
    default:
      return null;
  }
}

export function TopicView() {
  const topicId = useNav((s) => s.topicId);
  const subjectId = useNav((s) => s.subject);
  const openTopic = useNav((s) => s.openTopic);
  const goHome = useNav((s) => s.goHome);

  if (!topicId || !subjectId) {
    return (
      <div className="view-in mx-auto max-w-2xl px-6 py-20 text-center text-muted-foreground">
        Topic not found.
      </div>
    );
  }

  const topic = getTopicById(topicId);
  const subject = getSubjectById(subjectId);

  if (!topic) {
    return (
      <div className="view-in mx-auto max-w-2xl px-6 py-20 text-center text-muted-foreground">
        Topic not found.
      </div>
    );
  }

  if (!subject) {
    return (
      <div className="view-in mx-auto max-w-2xl px-6 py-20 text-center text-muted-foreground">
        Subject not found.
      </div>
    );
  }

  // Find next topic in same subject
  const subjectTopics = getTopicsForSubject(subjectId);
  const idx = subjectTopics.findIndex((t) => t.id === topicId);
  const next = subjectTopics[idx + 1];

  return (
    <article className="view-in mx-auto max-w-3xl px-6 py-10 sm:px-10">
      {/* Breadcrumb */}
      <div className="mb-6 flex items-center gap-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
        <button onClick={goHome} className="hover:text-foreground focus-ring rounded">
          ~
        </button>
        <span>/</span>
        <span className="text-foreground">{subject.name.toLowerCase()}</span>
        <span>/</span>
        <span className="text-foreground">{topic.title.toLowerCase()}</span>
      </div>

      {/* Header */}
      <header className="mb-8">
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <SubjectChip color={subject.color} size="md">
            {subject.name}
          </SubjectChip>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            · {topic.difficulty}
          </span>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            · ~{topic.est}
          </span>
        </div>
        <h1 className="font-display text-3xl font-bold tracking-tight sm:text-4xl">
          {topic.title}
        </h1>
        <p className="mt-1 font-mono text-sm text-muted-foreground">
          {topic.bangla}
        </p>
        <p className="mt-4 max-w-2xl text-base leading-relaxed text-muted-foreground">
          {topic.summary}
        </p>

        <div className="mt-6 flex flex-wrap items-center gap-3">
          <ProgressTracker topicId={topic.id} />
          <div className="flex items-center gap-1.5 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            <Clock className="h-3 w-3" />
            {topic.est}
          </div>
          <div className="flex items-center gap-1.5 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            <Gauge className="h-3 w-3" />
            {topic.difficulty}
          </div>
        </div>
      </header>

      {/* Sections */}
      <div className="prose-learn space-y-4">
        {topic.sections.map((s, i) => (
          <SectionBlock key={`${topic.id}-${i}-${s.type}`} section={s} index={i} />
        ))}
      </div>

      {/* Next */}
      {next && (
        <div className="mt-16 border-t border-border pt-6">
          <MonoLabel color={subject.color}>next up</MonoLabel>
          <button
            onClick={() => openTopic(subjectId, next.id)}
            className="card-hover mt-3 flex w-full items-center justify-between rounded-lg border border-border bg-surface p-4 text-left focus-ring"
          >
            <div>
              <div className="font-display text-base font-semibold">
                {next.title}
              </div>
              <div className="mt-0.5 font-mono text-[11px] text-muted-foreground">
                {next.bangla} · {next.est}
              </div>
            </div>
            <ArrowLeft className="h-4 w-4 rotate-180 text-muted-foreground" />
          </button>
        </div>
      )}
    </article>
  );
}
