import type { Metadata } from "next";
import { Press_Start_2P, Space_Grotesk, Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { ThemeProvider } from "@/components/theme-provider";

const pixel = Press_Start_2P({
  variable: "--font-pixel",
  subsets: ["latin"],
  weight: "400",
  display: "swap",
});

const grotesk = Space_Grotesk({
  variable: "--font-grotesk",
  subsets: ["latin"],
  display: "swap",
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const mono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "BitsToBytes — DSA · DB · Networking · OS",
  description:
    "A premium learning hub for Data Structures & Algorithms, Databases, Networking and Operating Systems fundamentals. Bangla + English, reading-first, code-heavy.",
  keywords: [
    "DSA",
    "Database",
    "Networking",
    "Operating Systems",
    "BitsToBytes",
    "CS fundamentals",
    "Bangla",
  ],
  authors: [{ name: "BitsToBytes" }],
  icons: {
    icon: "https://z-cdn.chatglm.cn/z-ai/static/logo.svg",
  },
  openGraph: {
    title: "BitsToBytes — DSA · DB · Networking · OS",
    description: "Premium learning hub for CS fundamentals. Bangla + English.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${pixel.variable} ${grotesk.variable} ${inter.variable} ${mono.variable} antialiased bg-background text-foreground`}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem={false}
          disableTransitionOnChange
        >
          {children}
          <Toaster />
        </ThemeProvider>
      </body>
    </html>
  );
}
