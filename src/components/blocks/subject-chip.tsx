"use client";

import { cn } from "@/lib/utils";
import type { SubjectColor } from "@/lib/content";

interface SubjectChipProps {
  color: SubjectColor;
  children: React.ReactNode;
  size?: "sm" | "md" | "lg";
  className?: string;
}

const COLOR_MAP: Record<
  SubjectColor,
  { text: string; bg: string; border: string }
> = {
  lime: {
    text: "text-lime",
    bg: "bg-lime-soft",
    border: "border-lime/40",
  },
  sky: {
    text: "text-sky",
    bg: "bg-sky-soft",
    border: "border-sky/40",
  },
  pink: {
    text: "text-pink",
    bg: "bg-pink-soft",
    border: "border-pink/40",
  },
  amber: {
    text: "text-amber",
    bg: "bg-amber-soft",
    border: "border-amber/40",
  },
};

export function SubjectChip({
  color,
  children,
  size = "md",
  className,
}: SubjectChipProps) {
  const c = COLOR_MAP[color];
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md border font-mono uppercase tracking-wider",
        c.text,
        c.bg,
        c.border,
        size === "sm" && "px-1.5 py-0.5 text-[10px]",
        size === "md" && "px-2 py-0.5 text-[11px]",
        size === "lg" && "px-3 py-1 text-xs",
        className
      )}
    >
      {children}
    </span>
  );
}
