#!/usr/bin/env python3
"""
Replace Networking Ch 02 (OSI Model) with detailed Network Models (OSI + TCP/IP) content.
Maximum Bangla + English technical terms pattern, with real-life analogies.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Find net-osi topic (which is currently the Ch 02 — OSI Model)
# It starts at `id: "net-osi"` and ends at the closing `},`
# Look for the start: the line `  {` before `id: "net-osi"`
# And the end: the closing `},` after the last section of net-osi
# We need to find net-tcp to know where net-osi ends

net_osi_marker = 'id: "net-osi"'
net_tcp_marker = 'id: "net-tcp"'

osi_idx = text.find(net_osi_marker)
assert osi_idx != -1, "net-osi marker not found"

tcp_idx = text.find(net_tcp_marker, osi_idx)
assert tcp_idx != -1, "net-tcp marker not found"

# Walk back from osi_idx to find the opening `  {`
# The topic starts at the line `  {` before `id: "net-osi"`
osi_start = text.rfind("  {\n", 0, osi_idx)
assert osi_start != -1, "Opening brace of net-osi not found"

# Walk forward from tcp_idx to find the start of the topic block (the `  {` before `id: "net-tcp"`)
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

# Now we have:
# - osi_start: the `  {` that opens net-osi
# - tcp_start: the `  {` that opens net-tcp (which is the next topic after net-osi)
# We want to replace text[osi_start:tcp_start] with our new content.

before = text[:osi_start]
after = text[tcp_start:]

NEW_CH2 = r'''  {
    id: "net-osi",
    subject: "net",
    title: "Ch 02 — Network Models (OSI & TCP/IP)",
    bangla: "নেটওয়ার্ক মডেলস (OSI ও TCP/IP)",
    difficulty: "Medium",
    est: "1.5 hr",
    summary:
      "এই chapter-এ আমরা দুটি important model শিখব যেগুলো networks কীভাবে কাজ করে তা বুঝতে help করে — OSI Model ও TCP/IP Model। এই models গুলো network communication কে ছোট, simpler layers-এ ভাগ করে। প্রতিটি layer-এর নির্দিষ্ট কাজ আছে। আমরা দেখব data কীভাবে wrap (encapsulate) ও unwrap (decapsulate) হয় যখন সেটা travel করে।",
    sections: [
      { type: "h2", id: "why-models", title: "Why Do We Need Network Models?" },
      {
        type: "p",
        text: "একটি letter পাঠানোর কথা ভাবুন। আপনি শুধু paper throw করেন না — আপনি সেটাকে envelope-এ রাখেন, address লেখেন, stamp যোগ করেন, mailbox-এ drop করেন, এবং postal service বাকি সব handle করে। Network models ঠিক একইভাবে কাজ করে — তারা কাজকে steps (layers)-এ ভাগ করে। প্রতিটি layer শুধু তার উপরের ও নিচের layer-এর সাথে কথা বলে। এটি network design কে সহজ করে, এবং এক layer-এর changes অন্যদের affect করে না।",
      },
      {
        type: "p",
        text: "Real-life thinking — restaurant-এ food order করা। Customer (application) শুধু order দেয়। Waiter (transport) order kitchen-এ নিয়ে যায়। Kitchen (network) food prepare করে। Delivery (data link) food পৌঁছে দেয়। প্রতিটি role আলাদা, এবং এক role পরিবর্তন হলে অন্যটি affect হয় না।",
      },

      { type: "h2", id: "osi-model", title: "The OSI Model (Open Systems Interconnection)" },
      {
        type: "p",
        text: "OSI model-এ ৭টি layers আছে। এটি International Organization for Standardization (ISO) দ্বারা তৈরি একটি theoretical model যেটা vendors ও developers-কে interoperable network products create করতে help করে।",
      },
      { type: "h3", title: "৭টি Layers — Bottom থেকে Top" },
      {
        type: "p",
        text: "আমরা bottom (physical hardware-এর কাছে) থেকে শুরু করে application (user-এর কাছে) পর্যন্ত যাব।",
      },
      {
        type: "list",
        items: [
          "Layer 1 — Physical। Raw bits (0s ও 1s) একটি physical medium (cable, radio, fiber)-এর উপর transmit করে।",
          "Layer 2 — Data Link। Bits গুলোকে frames-এ organize করে। Physical addressing (MAC addresses) handle করে। Error detection করে।",
          "Layer 3 — Network। Packets গুলোকে source থেকে destination-এ multiple networks জুড়ে route করে। Logical addressing (IP addresses) use করে।",
          "Layer 4 — Transport। Reliable বা unreliable data delivery provide করে। Error recovery, flow control। Port numbers use করে।",
          "Layer 5 — Session। Applications-এর মধ্যে sessions (dialogues) manage করে। Connections establish, maintain, ও terminate করে।",
          "Layer 6 — Presentation। Data formats translate করে (encryption, compression, character encoding)।",
          "Layer 7 — Application। User applications-কে directly network services provide করে (যেমন web browser, email client)।",
        ],
      },
      {
        type: "p",
        text: "Mnemonic মনে রাখার জন্য (নিচ থেকে উপরে): Please Do Not Throw Sausage Pizza Away — Physical, Data Link, Network, Transport, Session, Presentation, Application।",
      },

      { type: "h2", id: "osi-details", title: "প্রতিটি Layer-এর Detailed Functions" },
      { type: "h3", title: "Layer 1 — Physical Layer" },
      {
        type: "p",
        text: "Bits কে electrical signals, light pulses, বা radio waves-এ convert করে। Cables, connectors, voltage levels, ও data rates define করে। Examples — Ethernet (physical part), USB, Bluetooth radio, fiber optics, DSL।",
      },
      {
        type: "p",
        text: "Real-life thinking — actual road বা train track যার উপর vehicles (bits) travel করে।",
      },

      { type: "h3", title: "Layer 2 — Data Link Layer" },
      {
        type: "p",
        text: "Bits কে frames-এ group করে। Source ও destination-এর MAC address (hardware address) যোগ করে। Transmission errors detect (এবং কখনো correct) করে। Physical medium-এ access control করে (যেমন Ethernet-এর জন্য CSMA/CD)। দুটি sublayer আছে — LLC (Logical Link Control) ও MAC (Media Access Control)। Examples — Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), PPP।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি single city-র ভেতরের postal service। সে জানে কীভাবে একটি letter সেই street-এর একটি নির্দিষ্ট house-এ (MAC address) deliver করতে হয়।",
      },

      { type: "h3", title: "Layer 3 — Network Layer" },
      {
        type: "p",
        text: "Packets গুলোকে বিভিন্ন networks জুড়ে route করে। IP addresses (logical addresses) use করে best path খোঁজে। বড় packets কে fragment করে যদি প্রয়োজন হয়। Examples — IP (Internet Protocol — IPv4 ও IPv6), ICMP (ping), RIP, OSPF (routing protocols)।",
      },
      {
        type: "p",
        text: "Real-life thinking — interstate highway system ও GPS। সে New York থেকে Los Angeles-এর best route বের করে, শুধু একটি city-র ভেতরে নয়।",
      },

      { type: "h3", title: "Layer 4 — Transport Layer" },
      {
        type: "p",
        text: "Applications-এর মধ্যে end-to-end communication provide করে। Port numbers use করে (যেমন 80 web-এর জন্য, 443 secure web-এর জন্য)। দুটি main protocol — TCP (Transmission Control Protocol) যেটা reliable, connection-oriented, error-checked, ordered delivery দেয়। UDP (User Datagram Protocol) যেটা fast, connectionless, কোনো guarantee নেই (streaming, gaming-এর জন্য used)।",
      },
      {
        type: "p",
        text: "Real-life thinking — registered mail service যেটা আপনার package track করে, lost হলে resend করে (TCP) বনাম একটি regular postcard যেটা lost হতে পারে কিন্তু fast (UDP)।",
      },

      { type: "h3", title: "Layer 5 — Session Layer" },
      {
        type: "p",
        text: "Applications-এর মধ্যে sessions (conversations) set up, manage, ও end করে। Dialog control করে — কে কখন কথা বলতে পারবে। বড় data transfers-এর জন্য checkpoints যোগ করে (যাতে transfer fail হলে একটি checkpoint থেকে resume হয়)। Examples — NetBIOS, RPC (Remote Procedure Call), PPTP (VPN tunnel control)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন meeting moderator যিনি decide করেন কে কখন কথা বলবেন এবং meeting কখন start/end হবে।",
      },

      { type: "h3", title: "Layer 6 — Presentation Layer" },
      {
        type: "p",
        text: "Application format ও network format-এর মধ্যে data translate করে। Encryption/decryption, compression, ও character encoding (যেমন ASCII, UTF-8, EBCDIC) handle করে। Examples — SSL/TLS (cryptography), JPEG, GIF, ASCII, EBCDIC।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন translator যে English-কে French-এ convert করে এবং message-কে একটি secret code-এ encrypt করে।",
      },

      { type: "h3", title: "Layer 7 — Application Layer" },
      {
        type: "p",
        text: "User-এর software-কে (যেমন web browser, email client, file transfer) directly network services provide করে। এটি সেই layer যেটার সাথে user interact করে। Examples — HTTP (web), HTTPS, FTP (file transfer), SMTP (email sending), POP3/IMAP (email receiving), DNS (domain name resolution), Telnet, SSH।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি যে letter লেখেন — communication-এর actual content।",
      },

      { type: "h2", id: "encapsulation", title: "Encapsulation ও Decapsulation" },
      {
        type: "p",
        text: "যখন data sender থেকে receiver-এ যায়, প্রতিটি layer তার নিজস্ব header (এবং কখনো trailer) যোগ করে। এই process কে encapsulation বলে। Receiving side-এ প্রতিটি layer তার header remove করে — এটি decapsulation।",
      },
      { type: "h3", title: "Example: HTTP দিয়ে 'Hello' পাঠানো" },
      {
        type: "list",
        items: [
          "১. Application layer (HTTP) — 'Hello' হলো user data।",
          "২. Presentation layer — optionally compress/encrypt করে (এখনও 'Hello')।",
          "৩. Session layer — session ID যোগ করে (যেমন 'session 123')।",
          "৪. Transport layer (TCP) — source port (যেমন 5000) ও destination port (80) যোগ করে। একটি TCP segment create হয়।",
          "৫. Network layer (IP) — source IP (192.168.1.2) ও destination IP (8.8.8.8) যোগ করে। একটি IP packet create হয়।",
          "৬. Data Link layer (Ethernet) — source MAC (AA:BB:CC:DD:EE:FF) ও destination MAC (next hop router) যোগ করে। Error check (FCS) সহ একটি trailer যোগ করে। একটি Ethernet frame create হয়।",
          "৭. Physical layer — bits গুলোকে electrical pulses হিসেবে পাঠায়।",
        ],
      },
      {
        type: "p",
        text: "Receiver-এ প্রতিটি layer তার header strip করে এবং বাকিটা উপরের layer-এ pass করে। Real-life thinking — একটি Russian nesting doll। প্রতিটি doll-এর ভেতরে আরেকটি doll। Sender একটি ছোট doll নেয় ও প্রতিটি layer-এ একটি বড় doll পরিয়ে দেয়। Receiver প্রতিটি doll খুলে ভেতরের doll বের করে।",
      },

      { type: "h2", id: "osi-protocols", title: "OSI Model-এ প্রতিটি Layer-এর Protocols" },
      {
        type: "list",
        items: [
          "Layer 7 – Application — HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, SSH, Telnet, SNMP।",
          "Layer 6 – Presentation — SSL/TLS (প্রায়ই এখানে), JPEG, MPEG, ASCII, EBCDIC।",
          "Layer 5 – Session — NetBIOS, RPC, PPTP, SMB (partly session)।",
          "Layer 4 – Transport — TCP, UDP, SCTP, DCCP।",
          "Layer 3 – Network — IPv4, IPv6, ICMP, IGMP, ARP (প্রায়ই L2/L3-এ), OSPF, RIP।",
          "Layer 2 – Data Link — Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC, Frame Relay, Token Ring।",
          "Layer 1 – Physical — Ethernet (cables, repeaters), DSL, SONET/SDH, Bluetooth radio, USB।",
        ],
      },

      { type: "h2", id: "tcpip-model", title: "The TCP/IP Model" },
      {
        type: "p",
        text: "TCP/IP model হলো একটি practical, simpler model যেটা real Internet-এ used হয়। এতে ৪টি layers আছে (কখনো ৫টি, আপনি কীভাবে count করেন তার উপর নির্ভর করে)। এটি U.S. Department of Defense (ARPANET) দ্বারা developed।",
      },
      { type: "h3", title: "TCP/IP Layers vs OSI Layers" },
      {
        type: "list",
        items: [
          "Application layer — OSI-র Application, Presentation, ও Session layers কে combine করে। প্রতিটি functionality এক layer-এ।",
          "Transport layer — OSI-র Transport layer-এর সমান। TCP ও UDP এখানে কাজ করে।",
          "Internet layer — OSI-র Network layer-এর সমান। IP, ICMP, ARP এখানে কাজ করে।",
          "Network Access layer (Link Layer) — OSI-র Data Link ও Physical layers কে combine করে। Ethernet, Wi-Fi এখানে কাজ করে।",
        ],
      },

      { type: "h3", title: "প্রতিটি TCP/IP Layer-এর Functions" },
      {
        type: "list",
        items: [
          "Application — User applications-কে network services provide করে। OSI layers 5, 6, 7 কে combine করে। Examples: HTTP, HTTPS, FTP, SMTP, DNS, SSH।",
          "Transport — End-to-end reliability, flow control, multiplexing (port numbers)। OSI Transport layer-এর সমান। Examples: TCP, UDP।",
          "Internet — Packets গুলোকে networks জুড়ে route করে, logical addressing (IP)। OSI Network layer-এর সমান। Examples: IPv4, IPv6, ICMP, ARP (কখনো)।",
          "Network Access (Link Layer) — Frames কে physical medium-এর উপর পাঠায়, hardware addressing। OSI Data Link + Physical-এর সমান। Examples: Ethernet, Wi-Fi, PPP, DSL।",
        ],
      },

      { type: "h2", id: "comparison", title: "OSI vs TCP/IP Comparison" },
      {
        type: "list",
        items: [
          "Number of layers — OSI: 7; TCP/IP: 4 (বা ৫ যদি physical আলাদা করেন)।",
          "Developed by — OSI: ISO (International Org); TCP/IP: DARPA (U.S. DoD)।",
          "Theoretical / Practical — OSI: theoretical (reference model); TCP/IP: practical (Internet-এ used)।",
          "Session & Presentation — OSI: separate layers; TCP/IP: Application layer-এ included।",
          "Physical & Data Link — OSI: separate layers; TCP/IP: Network Access layer-এ combined।",
          "Protocol dependencies — OSI: protocols থেকে independent; TCP/IP: TCP ও IP-এর চারপাশে built।",
          "Popularity — OSI: teaching ও documentation-এ used; TCP/IP: real devices ও networks-এ used।",
        ],
      },

      { type: "h2", id: "why-both", title: "Why Both Models Matter Today" },
      {
        type: "p",
        text: "OSI model আপনাকে network functions layer by layer understand করতে help করে। এটি learning, troubleshooting, ও designing networks-এর জন্য একটি দারুণ tool। TCP/IP model হলো সেটা যেটা আসলে Internet-এ run করে। যখন আপনি একটি website browse করেন, email পাঠানে, বা video stream করেন, আপনি TCP/IP use করছেন।",
      },
      {
        type: "p",
        text: "যখন network engineers 'Layer 2 switches' বা 'Layer 3 routers' নিয়ে কথা বলে, তারা OSI layers (Data Link ও Network) বোঝাচ্ছে। একইভাবে, 'TCP port 80' TCP/IP-এর Transport layer থেকে এসেছে।",
      },
      {
        type: "p",
        text: "Real-life thinking — OSI model হলো একটি detailed recipe book যেখানে প্রতিটি step আলাদা বোঝানো আছে। TCP/IP model হলো একজন home cook-এর সংক্ষিপ্ত version — fewer steps কিন্তু একই food তৈরি হয়।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "OSI model-এ ৭টি layers আছে — Physical, Data Link, Network, Transport, Session, Presentation, Application।",
          "প্রতিটি layer-এর নির্দিষ্ট কাজ আছে, এবং প্রতিটি layer-এ protocols operate করে।",
          "Encapsulation প্রতিটি layer-এ headers যোগ করে sender side-এ; decapsulation সেগুলো remove করে receiver-এ।",
          "TCP/IP model-এ ৪টি layers আছে — Network Access, Internet, Transport, Application। এটি Internet-এ used real model।",
          "দুটি model-ই আমাদের networks design, understand, ও troubleshoot করতে help করে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: পরের chapter-এ আমরা Physical Layer-এর details-এ dive করব — cables, connectors, signaling, এবং bits আসলে কীভাবে travel করে।",
      },
    ],
  },

'''

new_text = before + NEW_CH2 + after

# Verify
assert 'id: "net-osi"' in new_text, "net-osi missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'id: "net-intro"' in new_text, "net-intro missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 02 (OSI + TCP/IP) replaced. File size: {len(new_text)} bytes")
