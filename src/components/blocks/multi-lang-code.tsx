"use client";

import { useState } from "react";
import { Check, Copy } from "lucide-react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import { cn } from "@/lib/utils";

export type Lang = "cpp" | "go" | "python" | "java";

export interface CodeSamples {
  cpp?: string;
  go?: string;
  python?: string;
  java?: string;
}

const LANG_LABEL: Record<Lang, string> = {
  cpp: "C++",
  go: "Go",
  python: "Python",
  java: "Java",
};

const LANG_PRISM: Record<Lang, string> = {
  cpp: "cpp",
  go: "go",
  python: "python",
  java: "java",
};

const LANG_ACTIVE_BG: Record<Lang, string> = {
  cpp: "bg-sky-soft text-sky",
  go: "bg-sky-soft text-sky",
  python: "bg-amber-soft text-amber",
  java: "bg-pink-soft text-pink",
};

// Force no wrapping: long lines get horizontal scroll, like VS Code
const NO_WRAP_PRE_STYLE = {
  margin: 0,
  background: "transparent",
  padding: "1rem",
  fontSize: "13.5px",
  lineHeight: "1.65",
  fontFamily: "var(--font-mono), ui-monospace, monospace",
  overflowX: "auto" as const,
  overflowY: "hidden" as const,
  whiteSpace: "pre" as const,
  wordBreak: "normal" as const,
  overflowWrap: "normal" as const,
  wordWrap: "normal" as const,
  display: "block" as const,
  width: "100%" as const,
};

const NO_WRAP_CODE_STYLE = {
  fontFamily: "var(--font-mono), ui-monospace, monospace",
  whiteSpace: "pre" as const,
  wordBreak: "normal" as const,
  overflowWrap: "normal" as const,
  wordWrap: "normal" as const,
  display: "block" as const,
};

interface MultiLangCodeProps {
  samples: CodeSamples;
  filename?: string;
}

export function MultiLangCode({ samples, filename }: MultiLangCodeProps) {
  const availableLangs = (Object.keys(samples) as Lang[]).filter(
    (l) => samples[l] && samples[l]!.trim().length > 0
  );

  const [active, setActive] = useState<Lang>(availableLangs[0] ?? "python");
  const [copied, setCopied] = useState(false);

  if (availableLangs.length === 0) return null;

  const code = samples[active] ?? "";
  const copy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 1400);
    } catch {
      // ignore
    }
  };

  return (
    <div className="my-6 overflow-hidden rounded-lg border border-border bg-surface-sunken">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-border bg-surface px-3 py-2">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-pink/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-amber/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-lime/70" />
          </div>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            {filename ?? "example"}
          </span>
        </div>
        <button
          onClick={copy}
          className="flex items-center gap-1 rounded-md px-2 py-1 font-mono text-[11px] text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground focus-ring"
          aria-label="Copy code"
        >
          {copied ? (
            <>
              <Check className="h-3 w-3 text-lime" />
              <span className="text-lime">copied</span>
            </>
          ) : (
            <>
              <Copy className="h-3 w-3" />
              <span>copy</span>
            </>
          )}
        </button>
      </div>

      {/* Language tabs */}
      <div className="flex items-center gap-0 border-b border-border bg-surface/60 px-2 py-1">
        {availableLangs.map((l) => (
          <button
            key={l}
            onClick={() => setActive(l)}
            className={cn(
              "rounded-md px-2.5 py-1 font-mono text-[11px] uppercase tracking-wider transition-colors",
              active === l
                ? LANG_ACTIVE_BG[l]
                : "text-muted-foreground hover:bg-secondary hover:text-foreground"
            )}
          >
            {LANG_LABEL[l]}
          </button>
        ))}
        <span className="ml-auto font-mono text-[10px] text-muted-foreground">
          {availableLangs.length} lang
        </span>
      </div>

      {/* Code body — syntax highlighted, NO wrapping (horizontal scroll like VS Code) */}
      <SyntaxHighlighter
        language={LANG_PRISM[active]}
        style={oneDark}
        customStyle={NO_WRAP_PRE_STYLE}
        codeTagProps={{ style: NO_WRAP_CODE_STYLE }}
        wrapLongLines={false}
        PreTag="pre"
      >
        {code}
      </SyntaxHighlighter>
    </div>
  );
}
