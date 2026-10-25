"use client";

import { useNav } from "@/lib/store";
import { getTopicById } from "@/lib/content";
import { useEffect, useMemo, useState } from "react";

export function RightAnchors() {
  const topicId = useNav((s) => s.topicId);
  const view = useNav((s) => s.view);

  const anchors = useMemo(() => {
    if (view !== "topic" || !topicId) return [];
    const topic = getTopicById(topicId);
    if (!topic) return [];
    return topic.sections
      .map((s, index) => ({
        id: s.id ?? `section-${index}`,
        label: s.title ?? "",
        level: s.type === "h2" ? 2 : 3,
      }))
      .filter((s, index) => {
        const section = topic.sections[index];
        return section.type === "h2" || section.type === "h3";
      });
  }, [topicId, view]);

  const [activeAnchor, setActiveAnchor] = useState<string | null>(null);

  useEffect(() => {
    if (anchors.length === 0) return;
    const obs = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActiveAnchor(visible[0].target.id);
      },
      { rootMargin: "-80px 0px -65% 0px", threshold: 0 }
    );
    anchors.forEach((a) => {
      const el = document.getElementById(a.id);
      if (el) obs.observe(el);
    });
    return () => obs.disconnect();
  }, [anchors]);

  if (anchors.length === 0) return null;

  return (
    <aside className="hidden w-48 shrink-0 xl:block">
      <div className="sticky top-20">
        <div className="mb-2 font-mono text-[10px] uppercase tracking-wider text-muted-foreground">
          on this page
        </div>
        <ul className="space-y-1 border-l border-border">
          {anchors.map((a, i) => (
            <li key={`${a.id}-${i}`}>
              <a
                href={`#${a.id}`}
                onClick={(e) => {
                  e.preventDefault();
                  const el = document.getElementById(a.id);
                  if (el) {
                    el.scrollIntoView({ behavior: "smooth", block: "start" });
                    setActiveAnchor(a.id);
                  }
                }}
                className={`block border-l-2 py-1 text-xs transition-colors ${
                  a.level === 3 ? "pl-4" : "pl-3"
                } ${
                  activeAnchor === a.id
                    ? "border-lime text-foreground"
                    : "border-transparent text-muted-foreground hover:text-foreground"
                }`}
              >
                {a.label}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </aside>
  );
}
