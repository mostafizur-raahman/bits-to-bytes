"use client";

import { cn } from "@/lib/utils";
import type { SubjectColor } from "@/lib/content";

interface MonoLabelProps {
  color?: SubjectColor;
  children: React.ReactNode;
  className?: string;
}

const COLOR_TEXT: Record<SubjectColor, string> = {
  lime: "text-lime",
  sky: "text-sky",
  pink: "text-pink",
  amber: "text-amber",
};

/** "/ SAVING TIME WHERE IT MATTERS" style label */
export function MonoLabel({ color = "lime", children, className }: MonoLabelProps) {
  return (
    <span className={cn("mono-label", COLOR_TEXT[color], className)}>
      / {children}
    </span>
  );
}
