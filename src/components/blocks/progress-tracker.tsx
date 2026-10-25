"use client";

import { useProgress, type ProgressStatus } from "@/lib/store";
import { cn } from "@/lib/utils";
import { Circle, Loader2, Check, RotateCcw } from "lucide-react";

const STATUS_META: Record<
  ProgressStatus,
  { label: string; icon: typeof Circle; color: string }
> = {
  todo: { label: "Todo", icon: Circle, color: "text-muted-foreground" },
  learning: { label: "Learning", icon: Loader2, color: "text-amber" },
  done: { label: "Done", icon: Check, color: "text-lime" },
  review: { label: "Review", icon: RotateCcw, color: "text-sky" },
};

export function ProgressTracker({ topicId }: { topicId: string }) {
  const status = useProgress((s) => s.status[topicId] ?? "todo");
  const cycle = useProgress((s) => s.cycleStatus);
  const meta = STATUS_META[status];
  const Icon = meta.icon;

  return (
    <button
      onClick={() => cycle(topicId)}
      className="flex items-center gap-2 rounded-md border border-border bg-surface px-3 py-1.5 text-xs font-medium transition-colors hover:border-foreground/30 focus-ring"
    >
      <Icon
        className={cn(
          "h-3.5 w-3.5",
          meta.color,
          status === "learning" && "animate-spin"
        )}
      />
      <span>{meta.label}</span>
      <span className="text-muted-foreground">/ click to cycle</span>
    </button>
  );
}
