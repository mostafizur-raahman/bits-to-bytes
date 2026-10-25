"use client";

import { useEffect, useRef, useState } from "react";
import { Play, Pause, RotateCcw, SkipForward } from "lucide-react";
import { cn } from "@/lib/utils";

const ALGOS = ["bubble", "selection", "insertion"] as const;
type Algo = (typeof ALGOS)[number];

const ALGO_LABEL: Record<Algo, string> = {
  bubble: "Bubble",
  selection: "Selection",
  insertion: "Insertion",
};

function* bubbleSort(arr: number[]) {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length - i - 1; j++) {
      yield { arr: [...a], comparing: [j, j + 1], swaps: 0 };
      if (a[j] > a[j + 1]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        yield { arr: [...a], comparing: [j, j + 1], swaps: 1 };
      }
    }
  }
  yield { arr: [...a], comparing: [], swaps: 0, done: true };
}

function* selectionSort(arr: number[]) {
  const a = [...arr];
  for (let i = 0; i < a.length; i++) {
    let min = i;
    for (let j = i + 1; j < a.length; j++) {
      yield { arr: [...a], comparing: [min, j], swaps: 0 };
      if (a[j] < a[min]) min = j;
    }
    if (min !== i) {
      [a[i], a[min]] = [a[min], a[i]];
      yield { arr: [...a], comparing: [i, min], swaps: 1 };
    }
  }
  yield { arr: [...a], comparing: [], swaps: 0, done: true };
}

function* insertionSort(arr: number[]) {
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    let j = i;
    while (j > 0 && a[j - 1] > a[j]) {
      yield { arr: [...a], comparing: [j - 1, j], swaps: 0 };
      [a[j], a[j - 1]] = [a[j - 1], a[j]];
      yield { arr: [...a], comparing: [j - 1, j], swaps: 1 };
      j--;
    }
  }
  yield { arr: [...a], comparing: [], swaps: 0, done: true };
}

const GENERATORS: Record<Algo, (a: number[]) => Generator<any>> = {
  bubble: bubbleSort,
  selection: selectionSort,
  insertion: insertionSort,
};

const initial = () =>
  Array.from({ length: 16 }, () => Math.floor(Math.random() * 90) + 10);

export function SortingVisualizer() {
  const [algo, setAlgo] = useState<Algo>("bubble");
  const [data, setData] = useState<number[]>(initial);
  const [comparing, setComparing] = useState<number[]>([]);
  const [playing, setPlaying] = useState(false);
  const [done, setDone] = useState(false);
  const genRef = useRef<Generator<any> | null>(null);

  const reset = (newAlgo: Algo = algo, newData: number[] = data) => {
    genRef.current = GENERATORS[newAlgo](newData);
    setDone(false);
    setComparing([]);
    setPlaying(false);
  };

  // Build generator on mount and whenever algo/data changes
  useEffect(() => {
    genRef.current = GENERATORS[algo](data);
  }, [algo, data]);

  const pickAlgo = (a: Algo) => {
    setAlgo(a);
    reset(a, data);
  };

  const reshuffle = () => {
    const next = initial();
    setData(next);
    reset(algo, next);
  };

  // Step loop
  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => {
      const next = genRef.current?.next();
      if (!next || next.done) {
        setPlaying(false);
        return;
      }
      const v = next.value;
      setData(v.arr);
      setComparing(v.comparing ?? []);
      if (v.done) {
        setPlaying(false);
        setDone(true);
        setComparing([]);
      }
    }, 220);
    return () => clearInterval(id);
  }, [playing]);

  const step = () => {
    const next = genRef.current?.next();
    if (!next || next.done) {
      setDone(true);
      return;
    }
    const v = next.value;
    setData(v.arr);
    setComparing(v.comparing ?? []);
    if (v.done) {
      setDone(true);
      setComparing([]);
    }
  };

  const max = Math.max(...data);

  return (
    <div className="my-6 overflow-hidden rounded-lg border border-border bg-surface-sunken p-4">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-1 rounded-md border border-border bg-surface p-0.5">
          {ALGOS.map((a) => (
            <button
              key={a}
              onClick={() => pickAlgo(a)}
              className={cn(
                "rounded px-2.5 py-1 font-mono text-[11px] uppercase transition-colors",
                algo === a
                  ? "bg-lime text-background"
                  : "text-muted-foreground hover:text-foreground"
              )}
            >
              {ALGO_LABEL[a]}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-1">
          <button
            onClick={step}
            className="rounded-md border border-border bg-surface p-1.5 text-muted-foreground transition-colors hover:text-foreground focus-ring"
            aria-label="Step"
          >
            <SkipForward className="h-3.5 w-3.5" />
          </button>
          <button
            onClick={() => setPlaying((p) => !p)}
            disabled={done}
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
            onClick={reshuffle}
            className="rounded-md border border-border bg-surface p-1.5 text-muted-foreground transition-colors hover:text-foreground focus-ring"
            aria-label="Reset"
          >
            <RotateCcw className="h-3.5 w-3.5" />
          </button>
        </div>
      </div>

      <div className="flex h-44 items-end justify-between gap-0.5 rounded-md bg-background/40 p-3">
        {data.map((v, i) => {
          const isCompare = comparing.includes(i);
          return (
            <div
              key={i}
              className={cn(
                "flex-1 rounded-t-sm transition-all",
                done
                  ? "bg-lime"
                  : isCompare
                  ? "bg-pink"
                  : "bg-foreground/30"
              )}
              style={{ height: `${(v / max) * 100}%` }}
              title={String(v)}
            />
          );
        })}
      </div>

      <div className="mt-3 flex items-center gap-4 font-mono text-[11px] text-muted-foreground">
        <span className="flex items-center gap-1.5">
          <span className="inline-block h-2 w-2 rounded-sm bg-pink" />
          comparing
        </span>
        <span className="flex items-center gap-1.5">
          <span className="inline-block h-2 w-2 rounded-sm bg-lime" />
          sorted
        </span>
        <span className="ml-auto">{ALGO_LABEL[algo]} sort · O(n²)</span>
      </div>
    </div>
  );
}
