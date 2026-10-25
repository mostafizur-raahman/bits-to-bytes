"use client";

interface ShapeProps {
  className?: string;
}

/** Cyan asterisk */
export function AsteriskShape({ className }: ShapeProps) {
  return (
    <svg
      viewBox="0 0 24 24"
      className={className}
      fill="none"
      stroke="currentColor"
      strokeWidth="2.5"
      strokeLinecap="round"
    >
      <path d="M12 2v20M2 12h20M5 5l14 14M19 5L5 19" />
    </svg>
  );
}

/** Green spiky flower / star */
export function SpikyShape({ className }: ShapeProps) {
  return (
    <svg viewBox="0 0 32 32" className={className} fill="currentColor">
      <path d="M16 0l3 9 9-3-3 9 9 3-9 3 3 9-9-3-3 9-3-9-9 3 3-9-9-3 9-3z" />
    </svg>
  );
}

/** Pink squiggle */
export function SquiggleShape({ className }: ShapeProps) {
  return (
    <svg
      viewBox="0 0 64 32"
      className={className}
      fill="none"
      stroke="currentColor"
      strokeWidth="3"
      strokeLinecap="round"
    >
      <path d="M4 16c4-10 8-10 12 0s8 10 12 0 8-10 12 0 8 10 12 0" />
    </svg>
  );
}

/** Pixel corner bracket */
export function PixelBracket({ className }: ShapeProps) {
  return (
    <svg viewBox="0 0 16 16" className={className} fill="currentColor">
      <rect x="0" y="0" width="6" height="2" />
      <rect x="0" y="0" width="2" height="6" />
      <rect x="10" y="14" width="6" height="2" />
      <rect x="14" y="10" width="2" height="6" />
    </svg>
  );
}

/** Green zigzag arrow */
export function ZigzagArrow({ className }: ShapeProps) {
  return (
    <svg
      viewBox="0 0 40 16"
      className={className}
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M2 8 L8 2 L14 8 L20 2 L26 8 L32 2" />
      <path d="M30 5 L34 2 L34 6" />
    </svg>
  );
}

/** Small triangle (amber) */
export function TriangleShape({ className }: ShapeProps) {
  return (
    <svg viewBox="0 0 24 24" className={className} fill="currentColor">
      <path d="M12 2l12 20H0z" />
    </svg>
  );
}
