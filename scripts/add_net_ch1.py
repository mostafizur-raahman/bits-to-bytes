#!/usr/bin/env python3
"""
Add Networking Ch 01 — Introduction to Computer Networks (Maximum Bangla + English terms).
Insert it at the beginning of the Networking section (before net-osi).
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Insert the new chapter right after the NETWORKING marker
network_marker = "/* ============== NETWORKING ============== */"
idx = text.find(network_marker)
assert idx != -1, "Networking marker not found"

# Find the next newline after the marker, then insert the new topic there
# We need to insert AFTER the marker line.
newline_after = text.find("\n", idx) + 1

new_chapter = r'''  {
    id: "net-intro",
    subject: "net",
    title: "Ch 01 — Introduction to Networks",
    bangla: "কম্পিউটার নেটওয়ার্ক পরিচিতি",
    difficulty: "Easy",
    est: "1 hr",
    summary:
      "Computer network হলো দুটি বা ততোধিক computers (বা printers, smartphones, game consoles এর মতো devices)-এর একটি group যেগুলো একসাথে connected থাকে যাতে তারা information ও resources share করতে পারে। এই chapter-এ আমরা শিখব computer networks কী, কেন আমরা সেগুলো use করি, কীভাবে তাদের quality judge করতে হয়, এবং তাদের বিভিন্ন shapes ও styles কী কী।",
    sections: [
      { type: "h2", id: "definition", title: "Definition ও Goals of Computer Networks" },
      {
        type: "p",
        text: "Computer network হলো দুটি বা ততোধিক computers (বা printers, smartphones, game consoles এর মতো devices)-এর একটি group যেগুলো একসাথে connected থাকে যাতে তারা information ও resources share করতে পারে। এটিকে ভাবতে পারেন roads দ্বারা connected একটি neighborhood of houses — roads people-দের একে অপরকে visit করতে, news exchange করতে, বা tools share করতে দেয়। একইভাবে, network computers-কে data back and forth পাঠাতে দেয়।",
      },
      { type: "h3", title: "Computer network-র main goals" },
      {
        type: "list",
        items: [
          "Resource sharing — hardware (printers, scanners), software (applications), ও files (documents, photos) অনেক computers জুড়ে share করা। Example: একটি office-তে ১০ জন মানুষ একটি networked printer use করতে পারে ১০টি printer কেনার বদলে।",
          "Communication — মানুষ emails, chat, video calls, বা documents-এ একসাথে কাজ করতে পারে। Example: Zoom calls বা WhatsApp messages networks-এর উপর travel করে।",
          "Cost reduction — expensive devices share করা ও centralizing data storage টাকা বাঁচায়। Example: একটি school সব student records একটি central server-এ store করে প্রতিটি teacher-এর PC-তে রাখার বদলে।",
          "Reliability — যদি একটি computer fail করে, অন্যরা take over করতে পারে (backup systems সহ)। Example: Google-এর মতো large websites হাজার হাজার servers use করে যাতে কয়েকটা break হলেও site কাজ করে।",
          "Scalability — existing network না ভেঙে আরও computers বা devices যোগ করতে পারা। Example: আপনার home Wi-Fi আজ ২টা phones সহ কাজ করে এবং পরের মাসে ৫টা phones সহ — শুধু সেগুলো connect করুন।",
        ],
      },

      { type: "h2", id: "criteria", title: "Network Criteria — Network কীভাবে judge করবেন" },
      {
        type: "p",
        text: "সব networks সমানভাবে ভালো নয়। আমরা সেগুলো তিনটি main criteria দিয়ে judge করি — Performance, Reliability, ও Security।",
      },
      { type: "h3", title: "1. Performance" },
      {
        type: "list",
        items: [
          "Throughput — per second কত data send করা যায় (Mbps বা Gbps-এ measured)।",
          "Delay (Latency) — এক piece data source থেকে destination-এ যেতে কত সময় নেয়।",
          "Jitter — delay-এর variation। Voice/video calls-এর জন্য low jitter গুরুত্বপূর্ণ।",
          "Number of users — বেশি users network share করলে সাধারণত সেটা slow হয়।",
        ],
      },
      { type: "h3", title: "2. Reliability" },
      {
        type: "list",
        items: [
          "Fault tolerance — কিছু parts fail করলেও network কাজ চালিয়ে যায়।",
          "Error rate — transmission-এর সময় data কতবার corrupt হয়।",
          "Uptime — network কত শতাংশ সময় available থাকে।",
        ],
      },
      { type: "h3", title: "3. Security" },
      {
        type: "list",
        items: [
          "Confidentiality — শুধু authorized মানুষ data দেখতে পারে।",
          "Integrity — data accidentally বা intentionally change হয় না।",
          "Availability — authorized মানুষ দরকার হলে network access করতে পারে।",
          "Authentication — verify করা যে একজন user বা device যে সে claim করছে সে-ই।",
        ],
      },

      { type: "h2", id: "types", title: "Types of Networks" },
      {
        type: "p",
        text: "Networks size ও range অনুযায়ী বিভিন্ন প্রকারের হয়। মূল পাঁচটি প্রকার হলো — PAN, LAN, MAN, WAN, ও WLAN।",
      },
      { type: "h3", title: "Network types এর overview" },
      {
        type: "list",
        items: [
          "PAN (Personal Area Network) — কয়েক meters range। Phone, laptop, smartwatch connect করতে ব্যবহৃত।",
          "LAN (Local Area Network) — একটি building বা campus range। Office-এ files, printers, internet share করতে।",
          "MAN (Metropolitan Area Network) — একটি city range। একটি university-এর একাধিক buildings কে city জুড়ে connect করতে।",
          "WAN (Wide Area Network) — countries বা continents range। Internet, বা global offices-এর সাথে একটি company।",
          "WLAN (Wireless Local Area Network) — LAN-এর মতোই, কিন্তু wireless। Home Wi-Fi, airport Wi-Fi।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — PAN হলো আপনার নিজের শরীরের আশেপাশের ব্যাগ্গুলো (phone, watch)। LAN হলো আপনার বাড়ি বা office building। MAN হলো আপনার city। WAN হলো পুরো দেশ বা দুনিয়া। WLAN হলো LAN-এর মতোই কিন্তু wireless।",
      },

      { type: "h2", id: "topologies", title: "Network Topologies" },
      {
        type: "p",
        text: "Network topology হলো network-এর layout — devices গুলো কীভাবে connected। পাঁচটি main topology আছে।",
      },
      { type: "h3", title: "1. Bus Topology" },
      {
        type: "p",
        text: "সব devices একটি single central cable (bus) share করে। Data দুই দিকে travel করে; প্রতিটি device data দেখে, কিন্তু শুধু intended recipient accept করে। Advantages — cheap, install করা সহজ, কম cable লাগে। Disadvantages — bus-এ একটি break পুরো network নামিয়ে দেয়। এক সময়ে শুধু একটি device send করতে পারে। Example — খুব পুরোনো Ethernet networks, আজকে কদাচিৎ used।",
      },
      { type: "h3", title: "2. Star Topology" },
      {
        type: "p",
        text: "সব devices একটি central switch বা hub-এ connect হয়। প্রতিটি message center-এর মধ্য দিয়ে যায়। Advantages — একটি cable fail হলে শুধু সেই device affected হয়। Devices যোগ করা সহজ। Faults খুঁজে পাওয়া সহজ। Disadvantages — central switch fail হলে পুরো network নেমে যায়। Bus-এর চেয়ে বেশি cable প্রয়োজন। Example — আজকের বেশির ভাগ home ও office networks (Ethernet switches, Wi-Fi access points)।",
      },
      { type: "h3", title: "3. Ring Topology" },
      {
        type: "p",
        text: "Devices একটি closed loop-এ connected। Data এক দিকে (বা কিছু rings-এ উভয় দিকে) device থেকে device-এ travel করে। Advantages — orderly data flow (কোনো collisions নেই)। প্রতিটি device signal repeat করতে পারে, যা longer distances allow করে। Disadvantages — ring-এ একটি break বা failed device পুরো network নামিয়ে দিতে পারে (যদি না dual ring হয়)। Example — পুরোনো IBM Token Ring networks, কিছু fiber optic rings (SONET)।",
      },
      { type: "h3", title: "4. Mesh Topology" },
      {
        type: "p",
        text: "প্রতিটি device প্রতিটি অন্য device-এর সাথে connected। এটি অনেক redundant paths দেয়। Advantages — খুব reliable; অনেক alternative paths। কোনো single point of failure নেই। Disadvantages — expensive; অনেক cables ও ports প্রয়োজন। Set up করা complex। Example — Internet-এর backbone, military networks, large data centers।",
      },
      { type: "h3", title: "5. Hybrid Topology" },
      {
        type: "p",
        text: "দুটি বা ততোধিক basic topologies combine করে (যেমন bus backbone দ্বারা connected stars)। Advantages — flexible, specific needs-এ fit করতে design করা যায়। Disadvantages — complex design, বেশি expensive, troubleshoot করা কঠিন। Example — large corporate networks (প্রতিটি department একটি star, একটি ring বা bus backbone দ্বারা linked)।",
      },
      {
        type: "p",
        text: "Real-life thinking — Bus হলো একটি একলা রাস্তা যেখানে সব বাড়ি এক line-এ। Star হলো একটি central roundabout যেখানে সব roads মিলিত হয়। Ring হলো একটি circular road যেখানে traffic ঘুরে বেড়ায়। Mesh হলো এমন একটি city যেখানে প্রতিটি বাড়ি প্রতিটি অন্য বাড়ির সাথে সরাসরি রাস্তা দিয়ে connected। Hybrid হলো একটি city যেখানে বিভিন্ন neighborhoods বিভিন্ন topology ব্যবহার করে।",
      },

      { type: "h2", id: "models", title: "Network Models" },
      {
        type: "p",
        text: "দুটি main network model আছে — Client-Server ও Peer-to-Peer (P2P)। প্রতিটির নিজস্ব strengths ও weaknesses।",
      },
      { type: "h3", title: "1. Client-Server Model" },
      {
        type: "p",
        text: "Server হলো একটি powerful computer (বা software) যেটা services provide করে। Client হলো যেকোনো device যেটা server-এর কাছে কিছু চায়। কীভাবে কাজ করে — client একটি request পাঠায় ('আমাকে file.pdf দাও')। Server সেটি process করে এবং answer ফিরে পাঠায়। Examples — web browsing, email, online banking।",
      },
      {
        type: "list",
        items: [
          "Advantages — centralized management, access control সহজ, powerful servers।",
          "Disadvantages — server single point of failure; expensive; administrator প্রয়োজন।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant। Client হলো customer যে waiter-কে order দেয়। Server হলো kitchen যেটা food prepare করে। সব communication waiter-এর মাধ্যমে হয়, customer directly kitchen-এ যায় না।",
      },
      { type: "h3", title: "2. Peer-to-Peer (P2P) Model" },
      {
        type: "p",
        text: "প্রতিটি computer (peer) সমান। প্রতিটি peer client (চাওয়া) ও server (share করা) উভয় হিসেবে act করতে পারে। কোনো central server নেই। Examples — BitTorrent, পুরোনো file-sharing apps, ছোট home বা office workgroups।",
      },
      {
        type: "list",
        items: [
          "Advantages — কোনো expensive server নেই, set up করা সহজ, খুব scalable।",
          "Disadvantages — security risks, কোনো central backup নেই, performance slowest peer-এর উপর depend করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একদল বন্ধু যারা একে অপরের সাথে directly books share করে। কোনো library বা librarian নেই; প্রত্যেকে একই সময়ে একজন reader ও একজন lender।",
      },
      { type: "h3", title: "Client-Server vs Peer-to-Peer — Comparison" },
      {
        type: "list",
        items: [
          "Central control — Client-Server: yes (server); P2P: না।",
          "Cost — Client-Server: higher (server প্রয়োজন); P2P: lower।",
          "Security — Client-Server: better (central policies); P2P: weaker।",
          "Reliability — Client-Server: single point of failure; P2P: কোনো single failure point নেই (কিন্তু peers leave করতে পারে)।",
          "Example — Client-Server: web, email, databases; P2P: BitTorrent, Windows Workgroup।",
        ],
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Computer network — devices কে connect করে resources share ও communicate করতে।",
          "Three key criteria — performance, reliability, security।",
          "Types of networks — PAN (ছোট) থেকে WAN (বিশাল); LAN ও WLAN সবচেয়ে common।",
          "Topologies — layout describe করে: Bus, Star, Ring, Mesh, Hybrid। Star আজকে সবচেয়ে popular।",
          "Network models — Client-Server (centralized) বা Peer-to-Peer (decentralized)। প্রতিটির নিজস্ব strengths।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: এই foundation টা ভালোভাবে বোঝার পরেই পরের chapter (layers, protocols, addressing) পড়া সহজ হবে। পরের chapter-এ আমরা দেখব data কীভাবে এই networks-এর উপর দিয়ে আসলে পাঠানো হয়।",
      },
    ],
  },

'''

# Insert the new chapter right after the network marker
new_text = text[:newline_after] + new_chapter + text[newline_after:]

# Verify
assert 'id: "net-intro"' in new_text, "New chapter not added"
assert new_text.count('id: "net-') == 4, f"Expected 4 net topics, got {new_text.count('id: \"net-')}"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 01 added. File size: {len(new_text)} bytes")
