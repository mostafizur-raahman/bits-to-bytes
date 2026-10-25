// Content barrel export — all imports from "@/lib/content" resolve here
// This file re-exports everything from the content/ subdirectory

export type {
  SubjectId,
  CheatsheetId,
  Subject,
  TopicSection,
  CodeSamples,
  Topic,
  Project,
  Cheatsheet,
} from "./content/types";

export { SUBJECTS, SUBJECT_COLORS } from "./content/subjects";
export { DSA_TOPICS } from "./content/dsa";
export { DB_TOPICS } from "./content/database";
export { NETWORKING_TOPICS } from "./content/networking";
export { OS_TOPICS } from "./content/os";
export { PROJECTS } from "./content/projects";
export { CHEATSHEETS } from "./content/cheatsheets";

// Combined TOPICS array
import { DSA_TOPICS } from "./content/dsa";
import { DB_TOPICS } from "./content/database";
import { NETWORKING_TOPICS } from "./content/networking";
import { OS_TOPICS } from "./content/os";
import type { Topic, SubjectId, CheatsheetId, Project, Cheatsheet } from "./content/types";
import { SUBJECTS, SUBJECT_COLORS } from "./content/subjects";
import { PROJECTS } from "./content/projects";
import { CHEATSHEETS } from "./content/cheatsheets";

export const TOPICS: Topic[] = [
  ...DSA_TOPICS,
  ...DB_TOPICS,
  ...NETWORKING_TOPICS,
  ...OS_TOPICS,
];

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
