"use client";

import { useState } from "react";
import { Check, Copy } from "lucide-react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface CodeBlockProps {
  code: string;
  lang?: string;
  filename?: string;
}

// Map our common lang names to Prism language aliases
const LANG_ALIASES: Record<string, string> = {
  cpp: "cpp",
  "c++": "cpp",
  cc: "cpp",
  cxx: "cpp",
  h: "cpp",
  hpp: "cpp",
  go: "go",
  golang: "go",
  python: "python",
  py: "python",
  java: "java",
  javascript: "javascript",
  js: "javascript",
  jsx: "jsx",
  typescript: "typescript",
  ts: "typescript",
  tsx: "tsx",
  bash: "bash",
  sh: "bash",
  shell: "bash",
  zsh: "bash",
  sql: "sql",
  http: "http",
  json: "json",
  yaml: "yaml",
  yml: "yaml",
  html: "markup",
  xml: "markup",
  md: "markdown",
  text: "text",
  plaintext: "text",
  "": "text",
};

function resolveLang(lang?: string): string {
  if (!lang) return "text";
  return LANG_ALIASES[lang.toLowerCase()] ?? "text";
}

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

export function CodeBlock({ code, lang = "text", filename }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 1400);
    } catch {
      // ignore
    }
  };

  const resolvedLang = resolveLang(lang);
  const displayLabel = filename ?? lang;

  return (
    <div className="my-6 overflow-hidden rounded-lg border border-border bg-surface-sunken">
      <div className="flex items-center justify-between border-b border-border bg-surface px-3 py-2">
        <div className="flex items-center gap-2">
          <div className="flex gap-1.5">
            <span className="h-2.5 w-2.5 rounded-full bg-pink/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-amber/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-lime/70" />
          </div>
          <span className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
            {displayLabel}
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
      <SyntaxHighlighter
        language={resolvedLang}
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
