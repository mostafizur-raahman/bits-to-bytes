"use client";

import { useNav } from "@/lib/store";
import { ThemeToggle } from "@/components/theme-toggle";
import { Search, Command } from "lucide-react";

export function TopNav() {
  const goHome = useNav((s) => s.goHome);
  const openProjects = useNav((s) => s.openProjects);
  const setSearchOpen = useNav((s) => s.setSearchOpen);
  const view = useNav((s) => s.view);

  return (
    <header className="sticky top-0 z-40 flex h-14 items-center justify-between border-b border-border bg-background/85 px-4 backdrop-blur-md sm:px-6">
      <button
        onClick={goHome}
        className="flex items-center gap-2 focus-ring rounded"
        aria-label="Home"
      >
        <div className="grid h-7 w-7 place-items-center rounded-md bg-lime text-background">
          <span className="font-pixel text-[9px]">B</span>
        </div>
        <span className="font-display text-base font-semibold tracking-tight">
          BitsToBytes
        </span>
        <span className="hidden font-mono text-[10px] uppercase tracking-wider text-muted-foreground sm:inline">
          / bits to bytes
        </span>
      </button>

      <nav className="flex items-center gap-1 sm:gap-2">
        <button
          onClick={() => setSearchOpen(true)}
          className="flex items-center gap-2 rounded-md border border-border bg-surface px-2.5 py-1.5 text-xs text-muted-foreground transition-colors hover:border-foreground/30 hover:text-foreground focus-ring"
        >
          <Search className="h-3.5 w-3.5" />
          <span className="hidden sm:inline">Search</span>
          <kbd className="hidden items-center gap-0.5 rounded border border-border bg-secondary px-1 py-0.5 font-mono text-[10px] sm:flex">
            <Command className="h-2.5 w-2.5" />
            <span>K</span>
          </kbd>
        </button>

        <button
          onClick={openProjects}
          className={`rounded-md px-2.5 py-1.5 text-xs font-medium transition-colors focus-ring ${
            view === "projects" || view === "project-detail"
              ? "bg-secondary text-foreground"
              : "text-muted-foreground hover:bg-secondary hover:text-foreground"
          }`}
        >
          Projects
        </button>

        <ThemeToggle />
      </nav>
    </header>
  );
}
