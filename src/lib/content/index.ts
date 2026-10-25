// BitsToBytes content system — barrel export
// This file re-exports everything so imports stay the same:
//   import { TOPICS, PROJECTS, getTopicById } from "@/lib/content";

// Types
export type {
  SubjectId,
  CheatsheetId,
  Subject,
  TopicSection,
  CodeSamples,
  Topic,
  Project,
  Cheatsheet,
} from "./types";

// Subjects
export { SUBJECTS, SUBJECT_COLORS } from "./subjects";

// Topics (combined)
export { DSA_TOPICS } from "./dsa";
export { DB_TOPICS } from "./database";
export { NETWORKING_TOPICS } from "./networking";
export { OS_TOPICS } from "./os";

// Projects
export { PROJECTS } from "./projects";

// Cheatsheets
export { CHEATSHEETS } from "./cheatsheets";

// ============ Combined TOPICS array ============
import { DSA_TOPICS } from "./dsa";
import { DB_TOPICS } from "./database";
import { NETWORKING_TOPICS } from "./networking";
import { OS_TOPICS } from "./os";
import type { Topic, SubjectId, CheatsheetId, Project, Cheatsheet } from "./types";
import { SUBJECTS, SUBJECT_COLORS } from "./subjects";
import { PROJECTS } from "./projects";
import { CHEATSHEETS } from "./cheatsheets";

export const TOPICS: Topic[] = [
  ...DSA_TOPICS,
  ...DB_TOPICS,
  ...NETWORKING_TOPICS,
  ...OS_TOPICS,
];

// ============ Helper functions ============
export function getTopicById(id: string): Topic | undefined {
  return TOPICS.find((t) => t.id === id);
}

export function getTopicsForSubject(subject: SubjectId): Topic[] {
  return TOPICS.filter((t) => t.subject === subject);
}

export function getProjectById(id: string): Project | undefined {
  return PROJECTS.find((p) => p.id === id);
}

export function getCheatsheetById(id: CheatsheetId): Cheatsheet | undefined {
  return CHEATSHEETS.find((c) => c.id === id);
}

export function getSubjectById(id: SubjectId) {
  return SUBJECTS.find((s) => s.id === id);
}
