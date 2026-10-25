"use client";

import { useNav } from "@/lib/store";
import { TopNav } from "@/components/layout/top-nav";
import { Sidebar } from "@/components/layout/sidebar";
import { RightAnchors } from "@/components/layout/right-anchors";
import { SearchDialog } from "@/components/blocks/search-dialog";
import { HomeView } from "@/components/views/home-view";
import { TopicView } from "@/components/views/topic-view";
import { ProjectsView } from "@/components/views/projects-view";
import { ProjectDetailView } from "@/components/views/project-detail-view";
import { CheatsheetView } from "@/components/views/cheatsheet-view";

export default function Home() {
  const view = useNav((s) => s.view);
  const topicId = useNav((s) => s.topicId);
  const projectId = useNav((s) => s.projectId);
  const cheatsheetId = useNav((s) => s.cheatsheetId);

  const viewKey = `${view}-${topicId ?? ""}-${projectId ?? ""}-${cheatsheetId ?? ""}`;

  return (
    <div className="flex min-h-screen flex-col bg-background text-foreground">
      <TopNav />
      <div className="flex flex-1">
        <Sidebar />
        <main className="flex-1">
          <div key={viewKey}>
            {view === "home" && <HomeView />}
            {view === "topic" && <TopicView />}
            {view === "projects" && <ProjectsView />}
            {view === "project-detail" && <ProjectDetailView />}
            {view === "cheatsheet" && <CheatsheetView />}
          </div>
        </main>
        <RightAnchors />
      </div>
      <SearchDialog />
    </div>
  );
}
