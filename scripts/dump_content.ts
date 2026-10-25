
// Tiny dump script — imports content.ts and prints JSON.
import { SUBJECTS, TOPICS, PROJECTS, CHEATSHEETS } from "../src/lib/content";
console.log(JSON.stringify({ SUBJECTS, TOPICS, PROJECTS, CHEATSHEETS }, null, 2));
