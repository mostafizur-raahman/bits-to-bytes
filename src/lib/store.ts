"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";

export type View =
  | "home"
  | "topic"
  | "projects"
  | "project-detail"
  | "cheatsheet";

export type SubjectId = "dsa" | "db" | "net" | "os";
export type CheatsheetId =
  | "big-o"
  | "sql-joins"
  | "osi-layers"
  | "linux-cmds";

interface NavState {
  view: View;
  subject: SubjectId | null;
  topicId: string | null;
  projectId: string | null;
  cheatsheetId: CheatsheetId | null;
  searchOpen: boolean;

  goHome: () => void;
  openTopic: (subject: SubjectId, topicId: string) => void;
  openProjects: () => void;
  openProject: (projectId: string) => void;
  openCheatsheet: (id: CheatsheetId) => void;
  setSearchOpen: (open: boolean) => void;
}

export const useNav = create<NavState>()(
  persist(
    (set) => ({
      view: "home",
      subject: null,
      topicId: null,
      projectId: null,
      cheatsheetId: null,
      searchOpen: false,

      goHome: () =>
        set({
          view: "home",
          subject: null,
          topicId: null,
          projectId: null,
          cheatsheetId: null,
        }),
      openTopic: (subject, topicId) =>
        set({
          view: "topic",
          subject,
          topicId,
          projectId: null,
          cheatsheetId: null,
        }),
      openProjects: () =>
        set({
          view: "projects",
          subject: null,
          topicId: null,
          projectId: null,
          cheatsheetId: null,
        }),
      openProject: (projectId) =>
        set({
          view: "project-detail",
          projectId,
          subject: null,
          topicId: null,
          cheatsheetId: null,
        }),
      openCheatsheet: (cheatsheetId) =>
        set({
          view: "cheatsheet",
          cheatsheetId,
          subject: null,
          topicId: null,
          projectId: null,
        }),
      setSearchOpen: (searchOpen) => set({ searchOpen }),
    }),
    {
      name: "bittobytes-nav",
      partialize: (state) => ({
        view: state.view,
        subject: state.subject,
        topicId: state.topicId,
        projectId: state.projectId,
        cheatsheetId: state.cheatsheetId,
      }),
    }
  )
);

/* Progress tracker store */
type ProgressStatus = "todo" | "learning" | "done" | "review";

interface ProgressState {
  status: Record<string, ProgressStatus>;
  setStatus: (topicId: string, status: ProgressStatus) => void;
  cycleStatus: (topicId: string) => void;
}

const CYCLE: ProgressStatus[] = ["todo", "learning", "done", "review"];

export const useProgress = create<ProgressState>()(
  persist(
    (set, get) => ({
      status: {},
      setStatus: (topicId, status) =>
        set((s) => ({ status: { ...s.status, [topicId]: status } })),
      cycleStatus: (topicId) => {
        const current = get().status[topicId] ?? "todo";
        const next = CYCLE[(CYCLE.indexOf(current) + 1) % CYCLE.length];
        set((s) => ({ status: { ...s.status, [topicId]: next } }));
      },
    }),
    { name: "bittobytes-progress" }
  )
);
