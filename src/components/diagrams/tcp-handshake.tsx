"use client";

import { useEffect, useRef, useState } from "react";
import { Play, Pause, RotateCcw, SkipForward } from "lucide-react";
import { cn } from "@/lib/utils";

type Step = {
  from: "client" | "server";
  to: "client" | "server";
  flags: string;
  seq: string;
  ack: string;
  note: string;
};

const STEPS: Step[] = [
  {
    from: "client",
    to: "server",
    flags: "SYN",
    seq: "seq=x",
    ack: "",
    note: "Client initiates. Picks a random sequence number x.",
  },
  {
    from: "server",
    to: "client",
    flags: "SYN, ACK",
    seq: "seq=y",
    ack: "ack=x+1",
    note: "Server acknowledges with x+1 and sends its own seq y.",
  },
  {
    from: "client",
    to: "server",
    flags: "ACK",
    seq: "seq=x+1",
    ack: "ack=y+1",
    note: "Client acknowledges y+1. Connection is now ESTABLISHED.",
  },
];

export function TCPHandshake() {
  const [step, setStep] = useState(0);
  const [playing, setPlaying] = useState(false);
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (!playing) return;
    timerRef.current = setInterval(() => {
      setStep((s) => {
        if (s >= STEPS.length) {
          setPlaying(false);
          return s;
        }
        return s + 1;
      });
    }, 1300);
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [playing]);

  const reset = () => {
    setStep(0);
    setPlaying(false);
  };

  return (
    <div className="my-6 overflow-hidden rounded-lg border border-border bg-surface-sunken p-4">
      <div className="mb-4 flex items-center justify-between">
        <div className="font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
          / tcp 3-way handshake
        </div>
        <div className="flex items-center gap-1">
          <button
            onClick={() => setStep((s) => Math.min(s + 1, STEPS.length))}
            className="rounded-md border border-border bg-surface p-1.5 text-muted-foreground transition-colors hover:text-foreground focus-ring"
            aria-label="Step"
          >
            <SkipForward className="h-3.5 w-3.5" />
          </button>
          <button
            onClick={() => setPlaying((p) => !p)}
            disabled={step >= STEPS.length}
            className="rounded-md border border-border bg-surface p-1.5 text-muted-foreground transition-colors hover:text-foreground focus-ring disabled:opacity-40"
            aria-label={playing ? "Pause" : "Play"}
          >
            {playing ? (
              <Pause className="h-3.5 w-3.5" />
            ) : (
              <Play className="h-3.5 w-3.5" />
            )}
          </button>
          <button
            onClick={reset}
            className="rounded-md border border-border bg-surface p-1.5 text-muted-foreground transition-colors hover:text-foreground focus-ring"
            aria-label="Reset"
          >
            <RotateCcw className="h-3.5 w-3.5" />
          </button>
        </div>
      </div>

      {/* Diagram */}
      <div className="relative h-56 rounded-md bg-background/40 p-4">
        {/* Two vertical lines */}
        <div className="absolute left-[20%] top-4 bottom-4 w-px bg-border" />
        <div className="absolute right-[20%] top-4 bottom-4 w-px bg-border" />

        {/* Labels */}
        <div className="absolute left-[20%] -translate-x-1/2 top-1 font-mono text-[11px] text-sky">
          client
        </div>
        <div className="absolute right-[20%] translate-x-1/2 top-1 font-mono text-[11px] text-pink">
          server
        </div>

        {/* Packets */}
        <div className="absolute inset-0 flex flex-col justify-center gap-8 px-[20%] py-6">
          {STEPS.map((s, i) => {
            const isShown = i < step;
            const isActive = i === step - 1;
            const isClientToServer = s.from === "client";
            return (
              <div
                key={i}
                className={cn(
                  "relative flex items-center transition-opacity duration-500",
                  isShown ? "opacity-100" : "opacity-25"
                )}
              >
                <div
                  className={cn(
                    "flex flex-1 items-center gap-2",
                    isClientToServer ? "flex-row" : "flex-row-reverse"
                  )}
                >
                  <div
                    className={cn(
                      "rounded border px-2 py-1 font-mono text-[10px] transition-colors",
                      isActive
                        ? isClientToServer
                          ? "border-sky/60 bg-sky-soft text-sky"
                          : "border-pink/60 bg-pink-soft text-pink"
                        : "border-border bg-surface text-muted-foreground"
                    )}
                  >
                    {s.flags} · {s.seq}
                    {s.ack && ` · ${s.ack}`}
                  </div>
                  <span
                    className={cn(
                      "text-muted-foreground",
                      isClientToServer ? "" : "rotate-180"
                    )}
                  >
                    →
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Note */}
      <div className="mt-3 min-h-[2.5rem] rounded-md border border-border bg-surface px-3 py-2 text-xs text-muted-foreground">
        {step > 0 && step <= STEPS.length ? (
          <span>
            <span className="font-mono text-[10px] uppercase tracking-wider text-foreground">
              step {step}/{STEPS.length} ·{" "}
            </span>
            {STEPS[step - 1].note}
          </span>
        ) : step === 0 ? (
          <span className="font-mono text-[10px] uppercase tracking-wider">
            press play to begin
          </span>
        ) : (
          <span className="font-mono text-[10px] uppercase tracking-wider text-lime">
            ✓ connection established
          </span>
        )}
      </div>
    </div>
  );
}
