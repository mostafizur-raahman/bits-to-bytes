// Types for BitsToBytes content system
// All interfaces and type definitions live here

export interface Subject {
  id: SubjectId;
  name: string;
  bangla: string;
  color: "lime" | "sky" | "pink" | "amber";
  blurb: string;
}

export type CodeSamples = {
  cpp?: string;
  go?: string;
  python?: string;
  java?: string;
};

export interface TopicSection {
  type:
    | "h2"
    | "h3"
    | "p"
    | "code"
    | "multi-code"
    | "callout"
    | "list"
    | "diagram";
  id?: string;
  title?: string;
  text?: string;
  lang?: string;
  items?: string[];
  diagram?: "sorting" | "tcp-handshake";
  calloutTone?: "info" | "warn" | "tip";
  codeSamples?: CodeSamples;
  filename?: string;
}

export interface Topic {
  id: string;
  subject: SubjectId;
  title: string;
  bangla: string;
  difficulty: "Easy" | "Medium" | "Hard";
  est: string;
  summary: string;
  sections: TopicSection[];
}

export interface Project {
  id: string;
  title: string;
  tagline: string;
  description: string;
  banglaDescription: string;
  status: "shipped" | "wip" | "planned";
  tech: string[];
  features: string[];
  demoUrl?: string;
  githubUrl?: string;
  accent: "lime" | "sky" | "pink" | "amber";
  cover: string; // emoji or ascii
  sections?: TopicSection[]; // book-like content from PDFs
}

export interface Cheatsheet {
  id: CheatsheetId;
  title: string;
  bangla: string;
  subject: SubjectId;
  description: string;
  columns: string[];
  rows: string[][];
}