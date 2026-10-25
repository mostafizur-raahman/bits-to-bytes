import type { Topic } from "./types";

export const NETWORKING_TOPICS: Topic[] = [
{
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

  {
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

  {
    id: "net-physical",
    subject: "net",
    title: "Ch 03 — Physical Layer",
    bangla: "ফিজিক্যাল লেয়ার",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Physical Layer হলো OSI model ও TCP/IP protocol suite-এর lowest layer। এটি raw bits কে একটি physical medium-এর উপর actual transmission-এর জন্য responsible। এই layer mechanical, electrical, procedural, ও functional specifications define করে — network devices-এর মধ্যে physical links activate, maintain, ও deactivate করার জন্য।",
    sections: [
      { type: "h2", id: "intro", title: "Introduction" },
      {
        type: "p",
        text: "Physical Layer হলো OSI (Open Systems Interconnection) model ও TCP/IP protocol suite-এর lowest layer। এটি raw bits কে একটি physical medium-এর উপর actual transmission-এর জন্য responsible। এই layer mechanical, electrical, procedural, ও functional specifications define করে — network devices-এর মধ্যে physical links activate, maintain, ও deactivate করার জন্য।",
      },
      { type: "h3", title: "Learning Objectives" },
      {
        type: "list",
        items: [
          "বিভিন্ন transmission media ও তাদের characteristics understand করা",
          "Analog ও digital signals-এর মধ্যে differentiate করা",
          "বিভিন্ন transmission modes comprehend করা",
          "Digital communication-এ used line coding techniques master করা",
          "Channel capacity calculate করার জন্য Nyquist ও Shannon theorems apply করা",
        ],
      },

      { type: "h2", id: "media", title: "Transmission Media" },
      {
        type: "p",
        text: "Transmission media হলো sender ও receiver-এর মধ্যে data transmission-এর জন্য physical pathway। এটি মূলত দুটি ভাগে বিভক্ত — guided (wired) ও unguided (wireless)।",
      },
      { type: "h3", title: "১.১ Guided Media (Wired)" },
      {
        type: "p",
        text: "Guided media একটি physical conduit provide করে যেটা signals কে একটি নির্দিষ্ট path ধরে direct করে। Signal medium-এর ভেতরে confined থাকে, যা wireless transmission-এর তুলনায় ভালো security ও reliability দেয়। তিনটি main প্রকার আছে — Twisted Pair, Coaxial Cable, ও Optical Fiber।",
      },
      { type: "h3", title: "Twisted Pair Cable" },
      {
        type: "p",
        text: "Twisted pair-এ দুটি insulated copper wires helical pattern-এ twisted থাকে। Twisting electromagnetic interference (EMI) ও crosstalk reduce করতে help করে। Categories গুলো হলো — Cat5e (100 MHz, Fast Ethernet), Cat6 (250 MHz, Gigabit Ethernet), Cat6a (500 MHz, 10 Gigabit Ethernet), Cat7 (600 MHz, Data Centers)।",
      },
      {
        type: "list",
        items: [
          "Advantages — low cost, install করা সহজ, flexible, lightweight, widely available।",
          "Disadvantages — fiber-এর তুলনায় limited bandwidth, EMI ও crosstalk-এ susceptible, distance বাড়লে attenuation বাড়ে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি office building-এর phone lines। প্রতিটি room-এ একটি phone jack, এবং সব cables একটি central closet-এ যায়। Cheap ও easy কিন্তু long distance-এ quality পড়ে যায়।",
      },
      { type: "h3", title: "Coaxial Cable" },
      {
        type: "p",
        text: "Coaxial cable-এ একটি central conductor থাকে যেটা insulation দ্বারা ঘেরা, তারপর একটি metallic shield, এবং outer jacket। এটি twisted pair-এর চেয়ে ভালো shielding দেয়। দুটি প্রকার — Baseband (digital, Ethernet 10Base2/10Base5, single channel) ও Broadband (analog, Cable TV/Internet, multiple channels)।",
      },
      {
        type: "list",
        items: [
          "Advantages — twisted pair-এর চেয়ে বেশি bandwidth, noise-এ ভালো immunity, দীর্ঘ transmission distances।",
          "Disadvantages — twisted pair-এর চেয়ে expensive, bulky ও less flexible, অনেক জায়গায় fiber দ্বারা replaced হচ্ছে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি garden hose। পানি (signal) hose-এর ভেতর দিয়ে যায়, বাইরের কিছু সহজে ঢুকতে পারে না। কিন্তু hose বেশ চওড়া ও ভারী।",
      },
      { type: "h3", title: "Optical Fiber" },
      {
        type: "p",
        text: "Optical fiber light pulses use করে data কে একটি glass বা plastic core-এর মাধ্যমে transmit করে, যা highest bandwidth ও longest transmission distances দেয়। দুটি প্রকার — Single-mode (SMF, 8-10 μm core, laser, up to 100 km, WAN/Telecom) ও Multi-mode (MMF, 50-62.5 μm core, LED/VCSEL, up to 2 km, LAN/Data Centers)।",
      },
      {
        type: "list",
        items: [
          "Advantages — extremely high bandwidth (Tbps range), খুব low attenuation, electromagnetic interference-এ immune, highly secure (tap করা কঠিন)।",
          "Disadvantages — high installation cost, fragile ও careful handling প্রয়োজন, complex splicing ও termination।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি laser pointer একটি long pipe-এর ভেতর দিয়ে। Light খুব দ্রুত যায়, কিছু দ্বারা interrupted হয় না, কিন্তু pipe সরল হতে হবে নাহলে light হারিয়ে যায়।",
      },

      { type: "h3", title: "১.২ Unguided Media (Wireless)" },
      {
        type: "p",
        text: "Unguided media electromagnetic waves কে air, vacuum, বা water-এর মাধ্যমে transmit করে কোনো physical conduit ছাড়া। তিনটি main প্রকার আছে।",
      },
      {
        type: "list",
        items: [
          "Radio Waves — 3 kHz থেকে 1 GHz, omnidirectional, walls penetrate করতে পারে। AM/FM radio, TV, mobile-এ used। Long range কিন্তু high interference।",
          "Microwaves — 1 GHz থেকে 300 GHz, unidirectional, line-of-sight প্রয়োজন। Satellite communication ও point-to-point links-এ used। Rain/fog-এ প্রভাবিত হয়।",
          "Infrared — 300 GHz থেকে 400 THz, short range, walls penetrate করতে পারে না। Remote controls, IrDA-তে used। High security (limited range)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Radio waves হলো একটি loudspeaker যা সব দিকে sound ছড়ায়। Microwaves হলো একটি flashlight beam — শুধু যেদিকে point করা সেদিকে যায়। Infrared হলো একটি TV remote — শুধু short distance-এ কাজ করে, wall-এর পিছে কিছু যায় না।",
      },

      { type: "h2", id: "signals", title: "Signal Types: Analog vs Digital" },
      {
        type: "p",
        text: "Analog ও digital signals-এর মধ্যে পার্থক্য বোঝা data transmission comprehend করার জন্য fundamental।",
      },
      { type: "h3", title: "Analog Signals" },
      {
        type: "p",
        text: "Analog signal হলো একটি continuous waveform যেটা সময়ের সাথে smoothly vary করে। এটি একটি given range-এর মধ্যে infinite সংখ্যক values নিতে পারে। Continuous time ও amplitude-এ। Physical quantities (sound, temperature, light) represent করে। Noise ও distortion-এ বেশি susceptible।",
      },
      {
        type: "p",
        text: "Examples — human voice, analog radio/TV signals, temperature sensors, traditional telephone systems। Real-life thinking — একটি dimmer switch। Brightness smoothly 0 থেকে 100% পর্যন্ত vary করে, যেকোনো value নিতে পারে।",
      },
      { type: "h3", title: "Digital Signals" },
      {
        type: "p",
        text: "Digital signal হলো একটি discrete signal যেটা specific values (সাধারণত binary 0 ও 1) use করে data represent করে। Steps-এ change হয়, continuously না। Discrete time ও amplitude-এ। Binary representation use করে (0s ও 1s)। Noise-এ কম affected। Store, process, ও transmit করা সহজ।",
      },
      { type: "h3", title: "Digital over Analog-এর Advantages" },
      {
        type: "list",
        items: [
          "Noise immunity — Analog: low; Digital: high।",
          "Error correction — Analog: difficult; Digital: easy।",
          "Storage — Analog: complex; Digital: simple।",
          "Processing — Analog: limited; Digital: extensive।",
          "Security — Analog: encrypt করা কঠিন; Digital: encrypt করা সহজ।",
          "Quality over distance — Analog: degrades; Digital: maintained।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Analog হলো একটি cassette tape। প্রতিবার copy করলে quality পড়ে যায়। Digital হলো একটি MP3 file। হাজার হাজার বার copy করলেও quality একই থাকে।",
      },

      { type: "h2", id: "modes", title: "Transmission Modes" },
      {
        type: "p",
        text: "Transmission mode দুটি communicating device-এর মধ্যে data flow-এর direction define করে। তিনটি mode আছে।",
      },
      { type: "h3", title: "১. Simplex Mode (Unidirectional)" },
      {
        type: "p",
        text: "Data শুধু এক দিকে যেতে পারে। Communication একমুখী। Efficiency low। Examples — broadcasting (radio, TV), keyboard থেকে computer, sensors থেকে controllers, fire alarms।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি one-way street। গাড়ি শুধু এক দিকে যেতে পারে, কখনো ফিরে আসতে পারে না।",
      },
      { type: "h3", title: "২. Half-Duplex Mode (Bidirectional, Alternating)" },
      {
        type: "p",
        text: "Data উভয় দিকে যেতে পারে কিন্তু একসাথে নয়। এক সময়ে শুধু এক দিক। Efficiency medium। Examples — walkie-talkies, CB radio, early Ethernet (10Base5), older wireless LANs।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি single-lane bridge যেখানে traffic light আছে। এক সময়ে শুধু এক দিকের traffic যেতে পারে।",
      },
      { type: "h3", title: "৩. Full-Duplex Mode (Bidirectional, Simultaneous)" },
      {
        type: "p",
        text: "Data উভয় দিকে একসাথে যেতে পারে। দুটি channels প্রয়োজন। Efficiency high। Examples — telephone networks, modern Ethernet (switched), cellular networks, instant messaging।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি two-lane road। গাড়ি উভয় দিকে একসাথে যেতে পারে।",
      },

      { type: "h2", id: "line-coding", title: "Line Coding Techniques" },
      {
        type: "p",
        text: "Line coding হলো digital data কে digital signals-এ convert করার প্রক্রিয়া transmission-এর জন্য। বিভিন্ন techniques bandwidth efficiency, synchronization, ও DC balance-এর মধ্যে বিভিন্ন trade-offs দেয়।",
      },
      { type: "h3", title: "Key Concepts" },
      {
        type: "list",
        items: [
          "DC Balance — DC drift prevent করা।",
          "Self-Synchronization — clock recovery।",
          "Bandwidth Efficiency — data rate maximize করা।",
          "Error Detection — transmission errors detect করা।",
          "Noise Immunity — noise effects minimize করা।",
        ],
      },
      { type: "h3", title: "Important Terms" },
      {
        type: "list",
        items: [
          "Baseline — reference হিসেবে used average voltage level।",
          "DC Component — constant voltage offset যা problems cause করতে পারে।",
          "Baud Rate — per second signal changes-এর সংখ্যা।",
          "Bit Rate — per second transmitted bits-এর সংখ্যা।",
        ],
      },
      {
        type: "multi-code",
        filename: "baud_bit_rate",
        codeSamples: {
          cpp: `#include <cmath>
#include <iostream>
using namespace std;

// Calculate bit rate from baud rate and number of signal levels.
// Bit rate = Baud rate × log2(levels)
double bit_rate(double baud, int levels) {
    return baud * log2(levels);
}

int main() {
    cout << "Baud 1000, levels 2: " << bit_rate(1000, 2) << " bps\\n";  // 1000
    cout << "Baud 1000, levels 4: " << bit_rate(1000, 4) << " bps\\n";  // 2000
    cout << "Baud 1000, levels 16: " << bit_rate(1000, 16) << " bps\\n"; // 4000
}`,
          go: `package main

import (
    "fmt"
    "math"
)

func bitRate(baud float64, levels int) float64 {
    return baud * math.Log2(float64(levels))
}

func main() {
    fmt.Println("Baud 1000, levels 2:", bitRate(1000, 2))   // 1000
    fmt.Println("Baud 1000, levels 4:", bitRate(1000, 4))   // 2000
    fmt.Println("Baud 1000, levels 16:", bitRate(1000, 16))  // 4000
}`,
          python: `import math

def bit_rate(baud, levels):
    """Calculate bit rate from baud rate and signal levels."""
    return baud * math.log2(levels)

print("Baud 1000, levels 2:", bit_rate(1000, 2))   # 1000
print("Baud 1000, levels 4:", bit_rate(1000, 4))   # 2000
print("Baud 1000, levels 16:", bit_rate(1000, 16))  # 4000`,
          java: `public class BaudBitRate {
    static double bitRate(double baud, int levels) {
        return baud * (Math.log(levels) / Math.log(2));
    }
    public static void main(String[] args) {
        System.out.println("Baud 1000, levels 2: " + bitRate(1000, 2));
        System.out.println("Baud 1000, levels 4: " + bitRate(1000, 4));
        System.out.println("Baud 1000, levels 16: " + bitRate(1000, 16));
    }
}`,
        },
      },

      { type: "h3", title: "NRZ-L (Non-Return to Zero, Level)" },
      {
        type: "p",
        text: "NRZ-L encoding-এ voltage level directly bit value represent করে। Bit 1 → positive voltage (+V), bit 0 → negative voltage (-V)। Bits-এর মধ্যে zero-তে return নেই।",
      },
      {
        type: "list",
        items: [
          "Advantages — implement করা simple, bandwidth সাশ্রয়ী, short-distance communication-এর জন্য ভালো।",
          "Disadvantages — DC component present (transformers-এর জন্য problematic), self-synchronization নেই (একই bit-এর long runs-এ clock loss), কোনো error detection নেই।",
        ],
      },
      { type: "h3", title: "NRZ-I (Non-Return to Zero, Inverted)" },
      {
        type: "p",
        text: "NRZ-I-তে signal invert হয় যখন একটি 1 encounter হয় এবং 0-এর জন্য একই থাকে। Bit 1 → signal invert করো, bit 0 → no change (previous level maintain করো)। DC component reduced, 1s-এর জন্য synchronization ভালো।",
      },
      { type: "h3", title: "Manchester Coding (IEEE 802.3)" },
      {
        type: "p",
        text: "Manchester encoding self-synchronization provide করে প্রতিটি bit period-এর মাঝে একটি transition ensure করে। Bit 1 → high-to-low transition (falling edge), bit 0 → low-to-high transition (rising edge)।",
      },
      {
        type: "list",
        items: [
          "Advantages — self-synchronizing (clock signal-এ embedded), কোনো DC component নেই, error detection capability।",
          "Disadvantages — NRZ-এর 2× bandwidth প্রয়োজন, encoding/decoding বেশি complex।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — NRZ হলো একটি simple switch (on/off)। Manchester হলো একটি clock — প্রতিটি second-এ একটি tick থাকে, যা timing বোঝাতে help করে।",
      },
      { type: "h3", title: "Bipolar AMI (Alternate Mark Inversion)" },
      {
        type: "p",
        text: "AMI তিনটি voltage levels use করে — positive, zero, ও negative। Bit 0 → 0V (zero level), bit 1 → alternating +V ও -V। কোনো DC component নেই, 1s-এর জন্য self-synchronizing, error detection (alternation rule violation)।",
      },

      { type: "h3", title: "Line Coding Comparison" },
      {
        type: "list",
        items: [
          "NRZ-L — DC component yes, sync poor, bandwidth 1×, error detection না, complexity low।",
          "NRZ-I — DC component reduced, sync moderate, bandwidth 1×, error detection না, complexity low।",
          "Manchester — DC component না, sync excellent, bandwidth 2×, error detection yes, complexity medium।",
          "Diff. Manchester — DC component না, sync excellent, bandwidth 2×, error detection yes, complexity medium।",
          "AMI — DC component না, sync good, bandwidth 1×, error detection yes, complexity medium।",
        ],
      },

      { type: "h2", id: "data-rate", title: "Data Rate Concepts" },
      { type: "h3", title: "Nyquist Theorem (Noiseless Channel)" },
      {
        type: "p",
        text: "Nyquist theorem একটি noiseless channel-এর জন্য maximum data rate define করে। Formula — C = 2 × B × log₂(L), যেখানে C = channel capacity (bps), B = bandwidth (Hz), L = signal levels-এর সংখ্যা।",
      },
      {
        type: "p",
        text: "Key insights — maximum symbol rate = 2B symbols/second। বেশি levels = বেশি bits per symbol। Trade-off — বেশি levels → noise-এ বেশি susceptible।",
      },
      {
        type: "multi-code",
        filename: "nyquist_capacity",
        codeSamples: {
          cpp: `#include <cmath>
#include <iostream>
using namespace std;

// Nyquist theorem: C = 2 * B * log2(L)
double nyquist(double B, int L) {
    return 2 * B * log2(L);
}

int main() {
    cout << "B=3000, L=4:   " << nyquist(3000, 4)   << " bps\\n";  // 12000
    cout << "B=3000, L=16:  " << nyquist(3000, 16)  << " bps\\n";  // 24000
    cout << "B=3100, L=31:  " << nyquist(3100, 31)  << " bps\\n";  // ~30690
}`,
          go: `package main

import (
    "fmt"
    "math"
)

func nyquist(B float64, L int) float64 {
    return 2 * B * math.Log2(float64(L))
}

func main() {
    fmt.Println("B=3000, L=4:  ", nyquist(3000, 4))   // 12000
    fmt.Println("B=3000, L=16: ", nyquist(3000, 16))  // 24000
    fmt.Println("B=3100, L=31: ", nyquist(3100, 31))  // ~30690
}`,
          python: `import math

def nyquist(B, L):
    """Nyquist theorem: C = 2 * B * log2(L)"""
    return 2 * B * math.log2(L)

print("B=3000, L=4:  ", nyquist(3000, 4))   # 12000
print("B=3000, L=16: ", nyquist(3000, 16))  # 24000
print("B=3100, L=31: ", nyquist(3100, 31))  # ~30690`,
          java: `public class Nyquist {
    static double nyquist(double B, int L) {
        return 2 * B * (Math.log(L) / Math.log(2));
    }
    public static void main(String[] args) {
        System.out.println("B=3000, L=4:  " + nyquist(3000, 4));
        System.out.println("B=3000, L=16: " + nyquist(3000, 16));
        System.out.println("B=3100, L=31: " + nyquist(3100, 31));
    }
}`,
        },
      },

      { type: "h3", title: "Shannon Capacity (Noisy Channel)" },
      {
        type: "p",
        text: "Shannon theorem একটি noisy channel-এর জন্য maximum data rate define করে। Formula — C = B × log₂(1 + S/N), যেখানে C = channel capacity (bps), B = bandwidth (Hz), S/N = signal-to-noise ratio (linear, dB নয়)।",
      },
      {
        type: "p",
        text: "dB থেকে linear SNR তে convert — S/N (linear) = 10^(SNR_dB / 10)। Key insights — Shannon capacity হলো theoretical maximum। Encoding যাই হোক না কেন exceed করা যাবে না। Noise fundamentally channel capacity limit করে। Higher SNR বেশি signal levels allow করে।",
      },
      {
        type: "multi-code",
        filename: "shannon_capacity",
        codeSamples: {
          cpp: `#include <cmath>
#include <iostream>
using namespace std;

// Shannon capacity: C = B * log2(1 + S/N)
double shannon(double B, double snr_linear) {
    return B * log2(1 + snr_linear);
}

// Convert SNR from dB to linear: S/N = 10^(SNR_dB / 10)
double snr_db_to_linear(double snr_db) {
    return pow(10, snr_db / 10);
}

int main() {
    double B = 3100;
    double snr_db = 30;
    double snr_lin = snr_db_to_linear(snr_db);  // 1000
    cout << "Shannon capacity: " << shannon(B, snr_lin) << " bps\\n";
    // ~30890 bps
}`,
          go: `package main

import (
    "fmt"
    "math"
)

func shannon(B, snrLinear float64) float64 {
    return B * math.Log2(1 + snrLinear)
}

func snrDbToLinear(snrDb float64) float64 {
    return math.Pow(10, snrDb/10)
}

func main() {
    B := 3100.0
    snrDb := 30.0
    snrLin := snrDbToLinear(snrDb)  // 1000
    fmt.Printf("Shannon capacity: %.0f bps\\n", shannon(B, snrLin))
    // ~30890
}`,
          python: `import math

def shannon(B, snr_linear):
    """Shannon capacity: C = B * log2(1 + S/N)"""
    return B * math.log2(1 + snr_linear)

def snr_db_to_linear(snr_db):
    """Convert SNR from dB to linear: S/N = 10^(SNR_dB / 10)"""
    return 10 ** (snr_db / 10)

B = 3100
snr_db = 30
snr_lin = snr_db_to_linear(snr_db)  # 1000
print(f"Shannon capacity: {shannon(B, snr_lin):.0f} bps")
# ~30890`,
          java: `public class Shannon {
    static double shannon(double B, double snrLinear) {
        return B * (Math.log(1 + snrLinear) / Math.log(2));
    }
    static double snrDbToLinear(double snrDb) {
        return Math.pow(10, snrDb / 10);
    }
    public static void main(String[] args) {
        double B = 3100, snrDb = 30;
        double snrLin = snrDbToLinear(snrDb);
        System.out.printf("Shannon capacity: %.0f bps%n",
            shannon(B, snrLin));
    }
}`,
        },
      },

      { type: "h3", title: "Nyquist ও Shannon-এর Relationship" },
      {
        type: "p",
        text: "Nyquist বলে আমরা কত দ্রুত symbols send করতে পারি (noise consider না করে)। Shannon বলে প্রতিটি symbol-এ কতগুলো bits reliable (noise consider করে)। দুটো combine করলে — maximum reliable data rate পাওয়া যায়। Actual rate ≤ min(Nyquist capacity, Shannon capacity)।",
      },

      { type: "h3", title: "Comprehensive Example" },
      {
        type: "p",
        text: "Problem — একটি telephone line-এ Bandwidth (B) = 3.1 kHz = 3100 Hz, SNR = 30 dB। Step 1 — SNR কে linear scale-এ convert করো — S/N = 10^(30/10) = 1000। Step 2 — Shannon Capacity calculate করো — C = 3100 × log₂(1001) ≈ 30,900 bps ≈ 30.9 kbps। Step 3 — Shannon দিয়ে maximum levels determine করো — L_max = √(1 + S/N) = √1001 ≈ 31। Step 4 — L = 31 দিয়ে Nyquist Capacity — C = 2 × 3100 × log₂(31) ≈ 30,690 bps। Step 5 — L = 4 হলে — C = 2 × 3100 × log₂(4) = 12,400 bps।",
      },
      {
        type: "p",
        text: "Conclusion — শুধু 4 levels দিয়ে channel Nyquist-limited (12.4 kbps)। Optimal levels (31) দিয়ে Shannon capacity-তে approach করা যায় (30.9 kbps)। Channel fundamentally noise দ্বারা limited (Shannon)।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Transmission media choice bandwidth requirements, distance, cost, ও environmental factors-এর উপর depend করে।",
          "Digital signals noise immunity, processing ease, ও error correction capabilities-এর জন্য analog-এর চেয়ে preferred।",
          "Transmission modes (simplex, half-duplex, full-duplex) data flow-এর direction ও simultaneity determine করে।",
          "Line coding techniques DC balance, synchronization, bandwidth efficiency, ও error detection-এর মধ্যে trade-offs balance করে।",
          "Nyquist theorem noiseless channels-এর জন্য maximum symbol rate define করে।",
          "Shannon theorem noise দ্বারা imposed fundamental capacity limit define করে।",
          "Practical data rate সবসময় ≤ min(Nyquist capacity, Shannon capacity)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Physical layer বোঝা জরুরি কারণ এটি সব communication-এর foundation। পরের chapter-এ আমরা Data Link Layer-এ যাব — যেখানে bits কে frames-এ organize করা হয় ও error handling করা হয়।",
      },
    ],
  },

  {
    id: "net-data-link",
    subject: "net",
    title: "Ch 04 — Data Link Layer",
    bangla: "ডেটা লিংক লেয়ার",
    difficulty: "Hard",
    est: "2.5 hr",
    summary:
      "Data Link Layer হলো OSI model ও TCP/IP protocol suite-এর দ্বিতীয় layer। এটি Network Layer (Layer 3) ও Physical Layer (Layer 1)-এর মাঝে বসে। এর primary responsibility হলো একটি physical link-এর উপর data frames-এর node-to-node (hop-to-hop) delivery provide করা। Physical Layer raw bits নিয়ে কাজ করে, কিন্তু Data Link Layer সেই bits গুলোকে frames-এ organize করে, addressing information যোগ করে, errors detect ও correct করে, data-এর flow control করে, এবং shared communication medium-এ access manage করে।",
    sections: [
      { type: "h2", id: "functions", title: "Data Link Layer-র Functions" },
      {
        type: "p",
        text: "Data Link Layer একটি physical link-এর উপর reliable data transfer ensure করার জন্য কয়েকটি critical function perform করে।",
      },
      { type: "h3", title: "Framing" },
      {
        type: "p",
        text: "Framing হলো Network Layer থেকে data কে frames-এ encapsulate করার প্রক্রিয়া। এটি boundaries provide করে যাতে receiver প্রতিটি frame-এর start ও end identify করতে পারে। Physical layer continuous bit stream transmit করে, কিন্তু receiver জানতে হয় কোথায় এক frame শেষ হয় এবং পরেরটা শুরু হয়।",
      },
      {
        type: "p",
        text: "Framing methods গুলো হলো — Character Count (first field-এ frame length specify করে, simple কিন্তু count-এ error হলে framing corrupt), Flag Bytes with Byte Stuffing (special FLAG byte boundaries mark করে, ESC for stuffing, reliable কিন্তু binary data-এ inefficient), Flag Bits with Bit Stuffing (special bit pattern যেমন 01111110, পাঁচটি 1s-এর পর 0 insert করে, efficient ও widely used), Physical Layer Coding Violations (invalid signal patterns delimiters হিসেবে use করে)।",
      },
      { type: "h3", title: "Error Detection ও Correction" },
      {
        type: "p",
        text: "Transmission errors noise, attenuation, ও interference-এর কারণে হয়। Data Link Layer redundancy যোগ করে এই errors detect এবং কখনো correct করে। Single-bit error-এ শুধু একটি bit change হয়। Burst error-এ একাধিক consecutive bits corrupt হয়।",
      },
      { type: "h3", title: "Flow Control" },
      {
        type: "p",
        text: "Flow control একটি fast sender-কে slow receiver-কে overwhelm করা থেকে prevent করে। এটি ensure করে যে receiver-এর buffer overflow না হয়। দুটি main technique — Stop-and-Wait (sender একটি frame পাঠিয়ে ACK-এর জন্য wait করে) ও Sliding Window (sender ACK-এর প্রয়োজন হওয়ার আগে একাধিক frames পাঠাতে পারে)।",
      },
      { type: "h3", title: "Access Control" },
      {
        type: "p",
        text: "যখন একাধিক devices একটি common communication medium share করে, Data Link Layer determine করে কে transmit করবে এবং কখন। এটি MAC (Media Access Control) sub-layer দ্বারা handle হয়।",
      },

      { type: "h2", id: "parity-check", title: "Error Detection: Parity Check" },
      {
        type: "p",
        text: "Parity হলো simplest error detection technique। একটি single parity bit যোগ করা হয় যাতে 1s-এর total সংখ্যা even বা odd হয়। Even Parity-তে 1s-এর total সংখ্যা (parity সহ) even হয়। Odd Parity-তে 1s-এর total সংখ্যা (parity সহ) odd হয়।",
      },
      {
        type: "list",
        items: [
          "Limitations — শুধু odd সংখ্যক bit errors detect করে। Even সংখ্যক errors detect করতে পারে না। Errors correct করতে পারে না।",
          "Two-Dimensional Parity — data কে matrix-এ arrange করো, প্রতিটি row ও column-এর জন্য parity যোগ করো। Single-bit errors detect ও correct করতে পারে।",
        ],
      },

      { type: "h2", id: "checksum", title: "Error Detection: Checksum" },
      {
        type: "p",
        text: "Internet Checksum IP, TCP, ও UDP-তে use হয়। এটি data কে 16-bit words-এর sequence হিসেবে treat করে, one's complement arithmetic দিয়ে sum করে, এবং sum-এর complement append করে। Algorithm — data কে 16-bit words-এ ভাগ করো, সব words one's complement addition দিয়ে sum করো, sum-এর one's complement নাও, checksum data-তে append করো।",
      },

      { type: "h2", id: "crc", title: "Error Detection: CRC (Cyclic Redundancy Check)" },
      {
        type: "p",
        text: "CRC হলো polynomial division-এর উপর based একটি powerful error detection technique। এটি Ethernet, Wi-Fi, ও storage devices-এ widely used। Data কে একটি polynomial হিসেবে treat করা হয়। একটি generator polynomial G(x) of degree r agree করা হয়। Sender data-তে r zeros append করে, G(x) দিয়ে divide করে, এবং remainder (CRC) append করে। Receiver received data কে G(x) দিয়ে divide করে; যদি remainder zero হয়, কোনো error detect হয়নি।",
      },
      {
        type: "multi-code",
        filename: "crc_calculation",
        codeSamples: {
          cpp: `#include <iostream>
using namespace std;

// CRC calculation using modulo-2 division.
// data: binary string, gen: generator polynomial (binary string)
string crc(string data, string gen) {
    int n = data.length();
    int r = gen.length() - 1;
    string frame = data + string(r, '0');
    int flen = frame.length();

    for (int i = 0; i <= flen - gen.length(); i++) {
        if (frame[i] == '1') {
            for (int j = 0; j < gen.length(); j++) {
                frame[i + j] = (frame[i + j] == gen[j]) ? '0' : '1';
            }
        }
    }
    return frame.substr(n);  // remainder = CRC
}

int main() {
    string data = "110101";
    string gen  = "1011";
    cout << "CRC: " << crc(data, gen) << '\\n';  // 011
    cout << "Transmitted: " << data << crc(data, gen) << '\\n';  // 110101011
}`,
          go: `package main

import "fmt"

func crc(data, gen string) string {
    r := len(gen) - 1
    frame := data
    for i := 0; i < r; i++ { frame += "0" }
    bytes := []byte(frame)

    for i := 0; i <= len(bytes)-len(gen); i++ {
        if bytes[i] == '1' {
            for j := 0; j < len(gen); j++ {
                if bytes[i+j] == gen[j] {
                    bytes[i+j] = '0'
                } else {
                    bytes[i+j] = '1'
                }
            }
        }
    }
    return string(bytes[len(data):])
}

func main() {
    fmt.Println("CRC:", crc("110101", "1011"))  // 011
}`,
          python: `def crc(data, gen):
    """CRC calculation using modulo-2 division."""
    r = len(gen) - 1
    frame = list(data + '0' * r)
    for i in range(len(frame) - r):
        if frame[i] == '1':
            for j in range(len(gen)):
                frame[i + j] = '0' if frame[i + j] == gen[j] else '1'
    return ''.join(frame[len(data):])

print("CRC:", crc("110101", "1011"))  # 011
print("Transmitted:", "110101" + crc("110101", "1011"))`,
          java: `public class CRC {
    static String crc(String data, String gen) {
        int r = gen.length() - 1;
        char[] frame = (data + "0".repeat(r)).toCharArray();
        for (int i = 0; i <= frame.length - gen.length(); i++) {
            if (frame[i] == '1') {
                for (int j = 0; j < gen.length(); j++) {
                    frame[i + j] = (frame[i + j] == gen.charAt(j)) ? '0' : '1';
                }
            }
        }
        return new String(frame, data.length(), r);
    }
    public static void main(String[] args) {
        System.out.println("CRC: " + crc("110101", "1011"));
    }
}`,
        },
      },

      { type: "h2", id: "hamming", title: "Error Correction: Hamming Code" },
      {
        type: "p",
        text: "Hamming codes হলো error-correcting codes যেগুলো single-bit errors detect ও correct করতে পারে। এগুলো multiple parity bits use করে যেগুলো powers of 2 positions-এ রাখা হয়। Hamming Distance (d_min) হলো bit positions-এর সংখ্যা যেখানে দুটি codewords ভিন্ন। d errors detect করতে: d_min ≥ d + 1। t errors correct করতে: d_min ≥ 2t + 1।",
      },
      { type: "h3", title: "Hamming(7,4) Code" },
      {
        type: "p",
        text: "৪টি data bits, ৩টি parity bits। Positions 1, 2, 4 হলো parity bits। Positions 3, 5, 6, 7 হলো data bits। P1 (position 1) covers positions 1, 3, 5, 7। P2 (position 2) covers positions 2, 3, 6, 7। P4 (position 4) covers positions 4, 5, 6, 7।",
      },
      {
        type: "multi-code",
        filename: "hamming_code",
        codeSamples: {
          cpp: `#include <iostream>
#include <string>
using namespace std;

// Hamming(7,4) encoder.
// Input: 4 data bits (e.g., "1011"), Output: 7-bit codeword.
string hamming_encode(string data) {
    // Positions: 1=D3, 2=D5, 3=D6, 4=D7 (1-indexed)
    // P1=1, P2=2, P4=4 are parity; data at 3,5,6,7
    char d[8] = {};
    d[3] = data[0]; d[5] = data[1]; d[6] = data[2]; d[7] = data[3];
    d[1] = ((d[3]-'0') ^ (d[5]-'0') ^ (d[7]-'0')) + '0';
    d[2] = ((d[3]-'0') ^ (d[6]-'0') ^ (d[7]-'0')) + '0';
    d[4] = ((d[5]-'0') ^ (d[6]-'0') ^ (d[7]-'0')) + '0';
    return string(d + 1, 7);
}

// Returns the position of the error (0 = no error).
int hamming_syndrome(string received) {
    char d[8] = {};
    for (int i = 1; i <= 7; i++) d[i] = received[i-1];
    int s1 = (d[1]-'0') ^ (d[3]-'0') ^ (d[5]-'0') ^ (d[7]-'0');
    int s2 = (d[2]-'0') ^ (d[3]-'0') ^ (d[6]-'0') ^ (d[7]-'0');
    int s4 = (d[4]-'0') ^ (d[5]-'0') ^ (d[6]-'0') ^ (d[7]-'0');
    return s1 * 1 + s2 * 2 + s4 * 4;
}

int main() {
    string data = "1011";
    string codeword = hamming_encode(data);
    cout << "Encoded: " << codeword << '\\n';  // 1010011
    cout << "Syndrome (no error): " << hamming_syndrome(codeword) << '\\n';
    // Flip bit 5
    string bad = codeword; bad[4] = (bad[4] == '0') ? '1' : '0';
    cout << "Error at: " << hamming_syndrome(bad) << '\\n';  // 5
}`,
          go: `package main

import "fmt"

func hammingEncode(data string) string {
    d := make([]byte, 8)
    d[3] = data[0]; d[5] = data[1]; d[6] = data[2]; d[7] = data[3]
    d[1] = byte((d[3]-'0')^(d[5]-'0')^(d[7]-'0')) + '0'
    d[2] = byte((d[3]-'0')^(d[6]-'0')^(d[7]-'0')) + '0'
    d[4] = byte((d[5]-'0')^(d[6]-'0')^(d[7]-'0')) + '0'
    return string(d[1:8])
}

func hammingSyndrome(received string) int {
    d := make([]int, 8)
    for i := 1; i <= 7; i++ { d[i] = int(received[i-1] - '0') }
    s1 := d[1] ^ d[3] ^ d[5] ^ d[7]
    s2 := d[2] ^ d[3] ^ d[6] ^ d[7]
    s4 := d[4] ^ d[5] ^ d[6] ^ d[7]
    return s1*1 + s2*2 + s4*4
}

func main() {
    cw := hammingEncode("1011")
    fmt.Println("Encoded:", cw)   // 1010011
    fmt.Println("Syndrome:", hammingSyndrome(cw))
}`,
          python: `def hamming_encode(data):
    """Hamming(7,4) encoder. Input: 4 data bits, Output: 7-bit codeword."""
    d = ['0'] * 8
    d[3], d[5], d[6], d[7] = data[0], data[1], data[2], data[3]
    d[1] = str(int(d[3]) ^ int(d[5]) ^ int(d[7]))
    d[2] = str(int(d[3]) ^ int(d[6]) ^ int(d[7]))
    d[4] = str(int(d[5]) ^ int(d[6]) ^ int(d[7]))
    return ''.join(d[1:8])

def hamming_syndrome(received):
    """Returns error position (0 = no error)."""
    d = ['0'] + list(received)  # 1-indexed
    s1 = int(d[1]) ^ int(d[3]) ^ int(d[5]) ^ int(d[7])
    s2 = int(d[2]) ^ int(d[3]) ^ int(d[6]) ^ int(d[7])
    s4 = int(d[4]) ^ int(d[5]) ^ int(d[6]) ^ int(d[7])
    return s1 * 1 + s2 * 2 + s4 * 4

cw = hamming_encode("1011")
print("Encoded:", cw)   # 1010011
print("Syndrome (no error):", hamming_syndrome(cw))
bad = cw[:4] + ('1' if cw[4] == '0' else '0') + cw[5:]
print("Error at:", hamming_syndrome(bad))  # 5`,
          java: `public class HammingCode {
    static String encode(String data) {
        char[] d = new char[8];
        d[3] = data.charAt(0); d[5] = data.charAt(1);
        d[6] = data.charAt(2); d[7] = data.charAt(3);
        d[1] = (char) (((d[3]-'0') ^ (d[5]-'0') ^ (d[7]-'0')) + '0');
        d[2] = (char) (((d[3]-'0') ^ (d[6]-'0') ^ (d[7]-'0')) + '0');
        d[4] = (char) (((d[5]-'0') ^ (d[6]-'0') ^ (d[7]-'0')) + '0');
        return new String(d, 1, 7);
    }
    static int syndrome(String received) {
        int[] d = new int[8];
        for (int i = 1; i <= 7; i++) d[i] = received.charAt(i-1) - '0';
        int s1 = d[1] ^ d[3] ^ d[5] ^ d[7];
        int s2 = d[2] ^ d[3] ^ d[6] ^ d[7];
        int s4 = d[4] ^ d[5] ^ d[6] ^ d[7];
        return s1 + s2 * 2 + s4 * 4;
    }
    public static void main(String[] args) {
        String cw = encode("1011");
        System.out.println("Encoded: " + cw);
        System.out.println("Syndrome: " + syndrome(cw));
    }
}`,
        },
      },

      { type: "h2", id: "flow-control-protocols", title: "Flow ও Error Control Protocols" },
      {
        type: "p",
        text: "Flow ও error control protocols reliable data transfer ensure করে — Acknowledgements (ACK) দিয়ে receiver successful receipt confirm করে, Timeouts দিয়ে sender ACK না পেলে retransmit করে, Sequence Numbers দিয়ে duplicate ও out-of-order frames detect করা হয়, Windows দিয়ে multiple outstanding frames allow করা হয়।",
      },
      { type: "h3", title: "Stop-and-Wait Protocol" },
      {
        type: "p",
        text: "Simplest flow control protocol। Sender একটি frame পাঠায়, তারপর ACK-এর জন্য wait করে পরেরটা পাঠানোর আগে। Efficiency — U = 1 / (1 + 2a), যেখানে a = T_prop / T_frame। Advantages — implement করা simple, low buffer requirements। Disadvantages — high bandwidth-delay product links-এ খুব inefficient, শুধু একটি frame in flight।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন courier যে একটি package দিয়ে যায়, confirmation phone call-এর জন্য wait করে, তারপর পরের package নেয়। খুব reliable কিন্তু খুব slow।",
      },
      { type: "h3", title: "Sliding Window Protocol" },
      {
        type: "p",
        text: "Sender কে individual ACKs-এর জন্য wait না করে একাধিক frames transmit করতে allow করে। Window size determine করে কতগুলো frames outstanding হতে পারে। যদি W ≥ 1 + 2a হয়, U = 1। যদি W < 1 + 2a হয়, U = W / (1 + 2a)। Advantages — bandwidth-এর efficient use, pipelining throughput improve করে। Disadvantages — বেশি complex, buffering প্রয়োজন।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন courier যে একসাথে ৫টা package নিয়ে যায়। সবগুলো deliver করে, তারপর একসাথে সবার confirmation নেয়। অনেক দ্রুত কিন্তু বেশি coordination লাগে।",
      },

      { type: "h2", id: "arq", title: "ARQ (Automatic Repeat reQuest) Protocols" },
      {
        type: "p",
        text: "ARQ flow control কে error control-এর সাথে combine করে। যখন error detect হয়, receiver retransmission request করে।",
      },
      { type: "h3", title: "Stop-and-Wait ARQ" },
      {
        type: "p",
        text: "Sender একটি frame পাঠায়, ACK-এর জন্য wait করে। Timeout হলে retransmit করে। Sequence numbers: 0 ও 1 (1 bit)। ACK number next expected frame indicate করে। Real-life thinking — registered mail where each letter is sent one at a time with delivery confirmation।",
      },
      { type: "h3", title: "Go-Back-N (GBN)" },
      {
        type: "p",
        text: "Sender N পর্যন্ত frames ACK ছাড়া পাঠাতে পারে। Window size = N। Sequence numbers: m bits, N = 2^m - 1। Cumulative ACK — ACK n মানে n-1 পর্যন্ত সব frames received। Frame lost হলে, সব subsequent frames retransmit হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন teacher যিনি assignment ১ থেকে ৫ পর্যন্ত দেন। যদি assignment ৩ হারিয়ে যায়, teacher assignment ৩, ৪, ৫ সব আবার দেন। সহজ কিন্তু কিছু redundant work।",
      },
      { type: "h3", title: "Selective Repeat (SR)" },
      {
        type: "p",
        text: "Sender N পর্যন্ত frames পাঠাতে পারে। Window size = N। Sequence numbers: m bits, N = 2^(m-1)। Receiver প্রতিটি frame individually ACK করে। শুধু lost frames retransmit হয়। Receiver out-of-order frames buffer করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন teacher যিনি শুধু হারিয়ে যাওয়া assignment ৩ আবার দেন, ৪ ও ৫ নয়। Efficient কিন্তু বেশি complex।",
      },
      { type: "h3", title: "ARQ Protocols Comparison" },
      {
        type: "list",
        items: [
          "Window Size — Stop-and-Wait: 1; Go-Back-N: 2^m - 1; Selective Repeat: 2^(m-1)।",
          "ACK Type — Stop-and-Wait: individual; Go-Back-N: cumulative; Selective Repeat: individual।",
          "Retransmission — Stop-and-Wait: শুধু lost frame; Go-Back-N: lost frame + সব subsequent; Selective Repeat: শুধু lost frame।",
          "Receiver Buffer — Stop-and-Wait: none; Go-Back-N: none; Selective Repeat: required।",
          "Efficiency — Stop-and-Wait: low; Go-Back-N: medium; Selective Repeat: high।",
          "Complexity — Stop-and-Wait: low; Go-Back-N: medium; Selective Repeat: high।",
        ],
      },

      { type: "h2", id: "mac-sublayer", title: "MAC Sub-layer" },
      {
        type: "p",
        text: "MAC (Media Access Control) sub-layer shared media-এ addressing ও access control-এর জন্য responsible।",
      },
      { type: "h3", title: "MAC Addressing" },
      {
        type: "p",
        text: "MAC address হলো একটি 48-bit (6-byte) hardware address যেটা প্রতিটি network interface card (NIC)-এ assigned থাকে। Hexadecimal notation-এ লেখা হয়: XX:XX:XX:YY:YY:YY। First 3 bytes (XX:XX:XX): OUI (Organizationally Unique Identifier), IEEE দ্বারা assigned। Last 3 bytes (YY:YY:YY): NIC-specific, manufacturer দ্বারা assigned।",
      },
      { type: "h3", title: "MAC Address Types" },
      {
        type: "list",
        items: [
          "Unicast — first byte LSB = 0, single destination (যেমন 00:1A:2B:3C:4D:5E)।",
          "Multicast — first byte LSB = 1, group of devices (যেমন 01:00:5E:00:00:01)।",
          "Broadcast — all 1s, all devices on LAN (FF:FF:FF:FF:FF:FF)।",
        ],
      },

      { type: "h2", id: "channel-access", title: "Channel Access Protocols" },
      {
        type: "p",
        text: "যখন একাধিক devices একটি common medium share করে, MAC protocols determine করে কে next transmit করবে। তিনটি category আছে — Contention-Based, Controlled Access, ও Channelization।",
      },

      { type: "h3", title: "ALOHA" },
      {
        type: "p",
        text: "ALOHA University of Hawaii-তে wireless communication-এর জন্য developed। এটি simplest contention-based protocol। Pure ALOHA-তে stations যখন তাদের data থাকে transmit করে। Collision হলে random time wait করে retransmit করে। কোনো carrier sensing নেই। Max throughput = 1/(2e) ≈ 0.184।",
      },
      {
        type: "p",
        text: "Slotted ALOHA-তে time slots-এ ভাগ করা হয়। Stations শুধু slot-এর শুরুতে transmit করে। Collision window reduce হয়। Max throughput = 1/e ≈ 0.368। Real-life thinking — Pure ALOHA হলো একটা meeting-এ যেখানে সবাই যখন খুশি কথা বলে (chaos)। Slotted ALOHA হলো একটা meeting-এ যেখানে শুধু একটি timer beep করলে কথা বলা যায় (কম chaos)।",
      },

      { type: "h3", title: "CSMA/CD (Carrier Sense Multiple Access with Collision Detection)" },
      {
        type: "p",
        text: "Wired Ethernet (IEEE 802.3)-এ used। Stations transmit করার আগে listen করে এবং transmission-এর সময় collisions detect করে। Steps — Carrier Sense (medium listen করো), যদি idle হয় transmit করো, যদি busy হয় wait করো, Collision Detection (transmit করার সময় collision-এর জন্য listen করো), collision detect হলে transmission abort করো, jam signal পাঠাও, random time wait করো (binary exponential backoff), retry করো।",
      },
      {
        type: "p",
        text: "Binary Exponential Backoff — i-th collision-এর পর, [0, 2^i - 1] থেকে random k choose করো। k × slot time wait করো। Minimum Frame Size — collision detect করার জন্য যথেষ্ট long হতে হবে। 10 Mbps Ethernet-এ 64 bytes (512 bits)। Slot time = 51.2 μs।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটা dark room-এ কয়েকজন মানুষ। প্রথমে listen করো কেউ কথা বলছে কিনা। শান্ত হলে কথা শুরু করো। যদি দুজন একসাথে শুরু করে, দুজনই থেমে যায়, একটা random সময় wait করে আবার চেষ্টা করে।",
      },

      { type: "h3", title: "CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)" },
      {
        type: "p",
        text: "Wireless LANs (IEEE 802.11)-এ used। Wireless stations transmit করার সময় easily collisions detect করতে পারে না, তাই তারা collisions avoid করে। Hidden terminal problem — A ও C একে অপরকে hear করতে পারে না, দুজনই B-তে transmit করে → B-তে collision। Exposed terminal problem — B, A-কে transmit করতে শুনে, unnecessarily defer করে।",
      },
      {
        type: "p",
        text: "Mechanisms — IFS (Inter-Frame Space): SIFS (short), DIFS (distributed), PIFS (point)। Backoff: medium idle হওয়ার পর random wait। ACK: receiver SIFS-এর পর ACK পাঠায়। RTS/CTS (optional): Request-to-Send / Clear-to-Send handshake।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটা classroom-এ hand raise করে question করা (RTS), teacher permission দেয় (CTS), তারপর কথা বলা (data), তারপর teacher thank বলে (ACK)। এতে দুজন একসাথে কথা বলবে না।",
      },

      { type: "h3", title: "CSMA/CD vs CSMA/CA" },
      {
        type: "list",
        items: [
          "Medium — CSMA/CD: wired; CSMA/CA: wireless।",
          "Collision Detection — CSMA/CD: yes; CSMA/CA: no।",
          "Collision Avoidance — CSMA/CD: no; CSMA/CA: yes (RTS/CTS, IFS)।",
          "ACK — CSMA/CD: not always; CSMA/CA: always।",
          "Standard — CSMA/CD: IEEE 802.3; CSMA/CA: IEEE 802.11।",
          "Efficiency — CSMA/CD: high; CSMA/CA: lower (overhead-এর কারণে)।",
        ],
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Framing data units delimit করার জন্য essential; bit stuffing সবচেয়ে robust method।",
          "Error detection redundancy use করে — Parity simple, Checksum software-friendly, CRC powerful, Hamming single-bit errors correct করতে পারে।",
          "Flow control buffer overflow prevent করে; Sliding Window Stop-and-Wait-এর চেয়ে efficient।",
          "ARQ protocols flow ও error control combine করে — Stop-and-Wait simple, Go-Back-N low error rates-এ efficient, Selective Repeat high error rates-এ best।",
          "MAC addressing 48-bit addresses use করে OUI ও NIC-specific parts সহ।",
          "ALOHA হলো simplest contention protocol; CSMA/CD wired Ethernet-এ; CSMA/CA wireless LANs-এ used।",
          "CSMA/CD collisions detect করে; CSMA/CA RTS/CTS ও ACKs দিয়ে collisions avoid করে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Data Link Layer বোঝা জরুরি কারণ এটি node-to-node delivery-র ভিত্তি। পরের chapter-এ আমরা Network Layer-এ যাব — যেখানে packets গুলো একাধিক networks জুড়ে route করা হয়।",
      },
    ],
  },

  {
    id: "net-network-layer",
    subject: "net",
    title: "Ch 05 — Network Layer",
    bangla: "নেটওয়ার্ক লেয়ার",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "Network layer (Layer 3) একাধিক networks জুড়ে end-to-end communication-এর জন্য responsible। এর main functions হলো — logical addressing (IP addresses assign করা), routing (source থেকে destination-এর best path determine করা), ও packet forwarding (packets কে incoming interface থেকে correct outgoing interface-এ move করা)।",
    sections: [
      { type: "h2", id: "functions", title: "Network Layer-র Functions" },
      {
        type: "p",
        text: "Network layer-র তিনটি main function আছে। Logical addressing — প্রতিটি host একটি IP address পায় (যেমন 192.168.1.10), যা source ও destination identify করতে use হয়। Routing — routers একে অপরের সাথে network topology সম্পর্কে information exchange করে এবং routing tables build করে। Forwarding — যখন একটি packet arrive করে, router তার table-এ destination IP খুঁজে বের করে এবং সেটিকে next hop-এ পাঠায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — postal system। Logical addressing হলো প্রতিটি বাড়ির address (IP address)। Routing হলো post office কীভাবে letter কোথায় পাঠাবে তার পথ ঠিক করা (routing table)। Forwarding হলো প্রতিটি sorting center-এ letter কে সঠিক বাক্সে ফেলা (incoming → outgoing interface)।",
      },

      { type: "h2", id: "ip-addressing", title: "IP Addressing" },
      { type: "h3", title: "IPv4 Address Classes" },
      {
        type: "p",
        text: "IPv4 addresses গুলো 32 bits long, সাধারণত চারটি decimal octets হিসেবে লেখা হয়। Originally addresses গুলোকে classes-এ ভাগ করা হয়েছিল। Class A (leading bits 0, first octet 1-126, mask 255.0.0.0, large networks)। Class B (leading bits 10, first octet 128-191, mask 255.255.0.0, medium networks)। Class C (leading bits 110, first octet 192-223, mask 255.255.255.0, small networks)। Class D (leading bits 1110, first octet 224-239, multicast)। Class E (leading bits 1111, first octet 240-255, experimental)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building। Class A হলো একটি বিশাল apartment complex যার অনেক floors ও কয়েকটি apartments। Class B হলো medium building। Class C হলো একটি ছোট building যার অল্প কয়েকটি apartments। Class D হলো intercom system (একজন একসাথে অনেককে call করে)। Class E হলো একটি building যা শুধু experiment-এর জন্য reserved।",
      },
      {
        type: "multi-code",
        filename: "ip_class_detect",
        codeSamples: {
          cpp: `#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// Detect IP address class from first octet.
char ip_class(const string& ip) {
    int first;
    char dot;
    istringstream iss(ip);
    iss >> first >> dot;
    if (first >= 1   && first <= 126) return 'A';
    if (first >= 128 && first <= 191) return 'B';
    if (first >= 192 && first <= 223) return 'C';
    if (first >= 224 && first <= 239) return 'D';
    return 'E';
}

int main() {
    cout << "10.0.0.1      -> Class " << ip_class("10.0.0.1")      << '\\n';   // A
    cout << "172.16.0.1    -> Class " << ip_class("172.16.0.1")    << '\\n';   // B
    cout << "192.168.1.1   -> Class " << ip_class("192.168.1.1")   << '\\n';   // C
    cout << "224.0.0.1     -> Class " << ip_class("224.0.0.1")     << '\\n';   // D
}`,
          go: `package main

import (
    "fmt"
    "strconv"
    "strings"
)

func ipClass(ip string) string {
    parts := strings.Split(ip, ".")
    first, _ := strconv.Atoi(parts[0])
    switch {
    case first >= 1   && first <= 126: return "A"
    case first >= 128 && first <= 191: return "B"
    case first >= 192 && first <= 223: return "C"
    case first >= 224 && first <= 239: return "D"
    default: return "E"
    }
}

func main() {
    fmt.Println("10.0.0.1    -> Class", ipClass("10.0.0.1"))    // A
    fmt.Println("172.16.0.1  -> Class", ipClass("172.16.0.1"))  // B
    fmt.Println("192.168.1.1 -> Class", ipClass("192.168.1.1")) // C
}`,
          python: `def ip_class(ip):
    """Detect IP address class from first octet."""
    first = int(ip.split(".")[0])
    if 1   <= first <= 126: return "A"
    if 128 <= first <= 191: return "B"
    if 192 <= first <= 223: return "C"
    if 224 <= first <= 239: return "D"
    return "E"

for ip in ["10.0.0.1", "172.16.0.1", "192.168.1.1", "224.0.0.1"]:
    print(f"{ip:15s} -> Class {ip_class(ip)}")`,
          java: `public class IPClass {
    static char ipClass(String ip) {
        int first = Integer.parseInt(ip.split("\\\\.")[0]);
        if (first >= 1   && first <= 126) return 'A';
        if (first >= 128 && first <= 191) return 'B';
        if (first >= 192 && first <= 223) return 'C';
        if (first >= 224 && first <= 239) return 'D';
        return 'E';
    }
    public static void main(String[] args) {
        System.out.println("10.0.0.1    -> Class " + ipClass("10.0.0.1"));
        System.out.println("172.16.0.1  -> Class " + ipClass("172.16.0.1"));
        System.out.println("192.168.1.1 -> Class " + ipClass("192.168.1.1"));
    }
}`,
        },
      },

      { type: "h3", title: "Subnetting" },
      {
        type: "p",
        text: "Subnetting একটি বড় network কে ছোট, manageable subnets-এ ভাগ করে। এটি host bits কে network portion-এর জন্য borrow করে। উদাহরণ — 192.168.1.0/24 (Class C, 256 addresses)। ৪টি subnets প্রয়োজন যাতে প্রতিটিতে অন্তত ৫০টি hosts থাকে। ২টি bits borrow করো → new subnet mask = /26 (255.255.255.192)। Subnets সংখ্যা = 2² = 4। Hosts per subnet = 2⁶ - 2 = 62।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি বড় office floor কে ছোট cabins-এ ভাগ করা। পুরো floor একটি /24 network। প্রতিটি cabin একটি subnet। Cabin এর walls হলো subnet bits। প্রতিটি cabin-এ কয়েকজন বসতে পারে (hosts per subnet)।",
      },
      {
        type: "multi-code",
        filename: "subnet_calculator",
        codeSamples: {
          cpp: `#include <cmath>
#include <iostream>
using namespace std;

// Calculate number of subnets and hosts per subnet.
void subnet_info(int original_prefix, int borrowed_bits) {
    int new_prefix = original_prefix + borrowed_bits;
    int num_subnets = 1 << borrowed_bits;            // 2^borrowed
    int host_bits = 32 - new_prefix;
    int hosts_per_subnet = (1 << host_bits) - 2;      // 2^host - 2
    cout << "New prefix: /" << new_prefix << '\\n';
    cout << "Subnets: " << num_subnets << '\\n';
    cout << "Hosts per subnet: " << hosts_per_subnet << '\\n';
}

int main() {
    // 192.168.1.0/24, borrow 2 bits → /26
    subnet_info(24, 2);
    // Output: /26, 4 subnets, 62 hosts each
}`,
          go: `package main

import "fmt"

func subnetInfo(originalPrefix, borrowedBits int) {
    newPrefix := originalPrefix + borrowedBits
    numSubnets := 1 << borrowedBits
    hostBits := 32 - newPrefix
    hostsPerSubnet := (1 << hostBits) - 2
    fmt.Printf("New prefix: /%d\\n", newPrefix)
    fmt.Printf("Subnets: %d\\n", numSubnets)
    fmt.Printf("Hosts per subnet: %d\\n", hostsPerSubnet)
}

func main() {
    subnetInfo(24, 2)  // /26, 4 subnets, 62 hosts each
}`,
          python: `def subnet_info(original_prefix, borrowed_bits):
    new_prefix = original_prefix + borrowed_bits
    num_subnets = 2 ** borrowed_bits
    host_bits = 32 - new_prefix
    hosts_per_subnet = 2 ** host_bits - 2
    print(f"New prefix: /{new_prefix}")
    print(f"Subnets: {num_subnets}")
    print(f"Hosts per subnet: {hosts_per_subnet}")

subnet_info(24, 2)  # /26, 4 subnets, 62 hosts each`,
          java: `public class SubnetCalc {
    static void subnetInfo(int originalPrefix, int borrowedBits) {
        int newPrefix = originalPrefix + borrowedBits;
        int numSubnets = 1 << borrowedBits;
        int hostBits = 32 - newPrefix;
        int hostsPerSubnet = (1 << hostBits) - 2;
        System.out.println("New prefix: /" + newPrefix);
        System.out.println("Subnets: " + numSubnets);
        System.out.println("Hosts per subnet: " + hostsPerSubnet);
    }
    public static void main(String[] args) {
        subnetInfo(24, 2);  // /26, 4 subnets, 62 hosts each
    }
}`,
        },
      },

      { type: "h3", title: "CIDR (Classless Inter-Domain Routing)" },
      {
        type: "p",
        text: "CIDR class boundaries remove করে। একটি IP address কে prefix length সহ লেখা হয় (যেমন /20)। এটা supernetting allow করে — একাধিক networks কে একটি route-এ aggregate করা। উদাহরণ — 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24 কে 192.168.0.0/22-তে combine করা (কারণ first 22 bits common)। এটি routing table entries reduce করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building-এ ৪টি floors। প্রতিটি floor-এ একটি doorbell list। CIDR হলো সব floors-এর doorbells কে একটি single entry তে merge করা — 'Building A' বললেই চারটো floor বোঝায়।",
      },

      { type: "h3", title: "IPv6 Basics" },
      {
        type: "p",
        text: "IPv6 128-bit addresses use করে (৮টি groups of ৪ hex digits হিসেবে লেখা হয়)। Main features — কোনো broadcast নেই (multicast ও anycast use করে), auto-configuration (SLAAC), simplified header (কোনো checksum নেই, routers-এ কোনো fragmentation নেই)। IPv6 address types — Unicast (single interface), Multicast (one-to-many), Anycast (one-to-nearest)।",
      },

      { type: "h2", id: "routing-algorithms", title: "Routing Algorithms" },
      { type: "h3", title: "Distance Vector (Bellman-Ford)" },
      {
        type: "p",
        text: "প্রতিটি router তার সম্পূর্ণ routing table neighbors-এর সাথে periodically share করে। Hop count-এর মতো metrics use করা হয়। Problem — slow convergence, count-to-infinity। উদাহরণ — তিনটি routers A-B-C। B-C link fail করে। A ভাবে সে B-এর মাধ্যমে C-তে পৌঁছাতে পারবে (cost 3), B ভাবে A-এর মাধ্যমে (cost 4) — loop যতক্ষণ না infinity (16) set করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি গ্রামে মানুষ একে অপরকে গল্প করে যে সে কোথায় যেতে পারে। প্রতিটি মানুষ তার neighbor-দের বলে কোথায় যাওয়া যায়। কিন্তু যদি একটি road বন্ধ হয়ে যায়, তারা অনেকক্ষণ না জেনে ভুল তথ্য দিতে থাকে (count-to-infinity)।",
      },

      { type: "h3", title: "Link State (Dijkstra)" },
      {
        type: "p",
        text: "প্রতিটি router সম্পূর্ণ topology learn করে এবং Dijkstra algorithm দিয়ে shortest paths compute করে। প্রতিটি router Link State Advertisements (LSAs) সব অন্য routers-এ flood করে। Advantage — fast convergence, কোনো loops নেই।",
      },
      {
        type: "p",
        text: "Real-life thinking — প্রতিজনের কাছে একটি সম্পূর্ণ city map আছে। প্রত্যেকে নিজে Dijkstra চালিয়ে best route বের করে। যদি কোনো road বন্ধ হয়ে যায়, সবাই তখনই জানে এবং নতুন route বের করে — কোনো গল্প বা confusion নেই।",
      },
      {
        type: "multi-code",
        filename: "dijkstra_routing",
        codeSamples: {
          cpp: `#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// Dijkstra's shortest path algorithm.
// graph[u] = list of (neighbor, weight).
vector<int> dijkstra(int V, vector<vector<pair<int,int>>>& graph, int src) {
    vector<int> dist(V, INT_MAX);
    vector<bool> visited(V, false);
    dist[src] = 0;
    for (int i = 0; i < V; i++) {
        int u = -1, minD = INT_MAX;
        for (int j = 0; j < V; j++)
            if (!visited[j] && dist[j] < minD) { minD = dist[j]; u = j; }
        if (u == -1) break;
        visited[u] = true;
        for (auto& [v, w] : graph[u])
            if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
    }
    return dist;
}

int main() {
    // 4 nodes: A=0, B=1, C=2, D=3
    vector<vector<pair<int,int>>> g(4);
    g[0] = {{1,2},{2,5}};   // A-B:2, A-C:5
    g[1] = {{0,2},{2,3},{3,1}};  // B-A:2, B-C:3, B-D:1
    g[2] = {{0,5},{1,3},{3,2}};  // C-A:5, C-B:3, C-D:2
    g[3] = {{1,1},{2,2}};   // D-B:1, D-C:2
    auto dist = dijkstra(4, g, 0);  // from A
    for (int i = 0; i < 4; i++)
        cout << "A -> " << (char)('A'+i) << " = " << dist[i] << '\\n';
    // A->A=0, A->B=2, A->C=5, A->D=3
}`,
          go: `package main

import "fmt"

func dijkstra(V int, graph [][][]int, src int) []int {
    dist := make([]int, V)
    visited := make([]bool, V)
    for i := range dist { dist[i] = 1 << 30 }
    dist[src] = 0
    for i := 0; i < V; i++ {
        u, minD := -1, 1<<30
        for j := 0; j < V; j++ {
            if !visited[j] && dist[j] < minD {
                minD = dist[j]; u = j
            }
        }
        if u == -1 { break }
        visited[u] = true
        for _, edge := range graph[u] {
            v, w := edge[0], edge[1]
            if dist[u]+w < dist[v] { dist[v] = dist[u] + w }
        }
    }
    return dist
}

func main() {
    // graph[u] = list of [neighbor, weight]
    graph := [][][]int{
        {{1, 2}, {2, 5}},
        {{0, 2}, {2, 3}, {3, 1}},
        {{0, 5}, {1, 3}, {3, 2}},
        {{1, 1}, {2, 2}},
    }
    dist := dijkstra(4, graph, 0)
    names := []string{"A", "B", "C", "D"}
    for i, d := range dist {
        fmt.Printf("A -> %s = %d\\n", names[i], d)
    }
}`,
          python: `def dijkstra(V, graph, src):
    """graph[u] = list of (neighbor, weight)."""
    dist = [float('inf')] * V
    visited = [False] * V
    dist[src] = 0
    for _ in range(V):
        u, min_d = -1, float('inf')
        for j in range(V):
            if not visited[j] and dist[j] < min_d:
                min_d, u = dist[j], j
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

# 4 nodes: A=0, B=1, C=2, D=3
graph = [
    [(1, 2), (2, 5)],           # A-B:2, A-C:5
    [(0, 2), (2, 3), (3, 1)],   # B-A:2, B-C:3, B-D:1
    [(0, 5), (1, 3), (3, 2)],   # C-A:5, C-B:3, C-D:2
    [(1, 1), (2, 2)],           # D-B:1, D-C:2
]
dist = dijkstra(4, graph, 0)
names = ["A", "B", "C", "D"]
for i, d in enumerate(dist):
    print(f"A -> {names[i]} = {d}")`,
          java: `import java.util.*;

public class Dijkstra {
    static int[] dijkstra(int V, List<List<int[]>> graph, int src) {
        int[] dist = new int[V];
        boolean[] visited = new boolean[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        for (int i = 0; i < V; i++) {
            int u = -1, minD = Integer.MAX_VALUE;
            for (int j = 0; j < V; j++) {
                if (!visited[j] && dist[j] < minD) { minD = dist[j]; u = j; }
            }
            if (u == -1) break;
            visited[u] = true;
            for (int[] edge : graph.get(u)) {
                int v = edge[0], w = edge[1];
                if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
            }
        }
        return dist;
    }
    public static void main(String[] args) {
        List<List<int[]>> graph = new ArrayList<>();
        graph.add(Arrays.asList(new int[]{1,2}, new int[]{2,5}));
        graph.add(Arrays.asList(new int[]{0,2}, new int[]{2,3}, new int[]{3,1}));
        graph.add(Arrays.asList(new int[]{0,5}, new int[]{1,3}, new int[]{3,2}));
        graph.add(Arrays.asList(new int[]{1,1}, new int[]{2,2}));
        int[] dist = dijkstra(4, graph, 0);
        String[] names = {"A", "B", "C", "D"};
        for (int i = 0; i < 4; i++)
            System.out.println("A -> " + names[i] + " = " + dist[i]);
    }
}`,
        },
      },

      { type: "h3", title: "Flooding" },
      {
        type: "p",
        text: "একটি router incoming packet কে সব interface-এ forward করে যেটার উপর এসেছে সেটা ছাড়া। Military, OSPF initial LSA propagation, বা robustness-এর জন্য use হয়। Control mechanisms — hop count limit, sequence numbers।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন postman যে একটি letter পায় এবং সেটিকে প্রতিটি house-এ এক এক করে দেয়। খুব reliable কিন্তু অনেক কাগজ নষ্ট হয়। যেহেতু একটা letter অনেকবার copy হয়, একটা sequence number দিয়ে আগে পাওয়া copies discard করা যায়।",
      },

      { type: "h2", id: "routing-protocols", title: "Routing Protocols" },
      { type: "h3", title: "RIP (Routing Information Protocol)" },
      {
        type: "p",
        text: "Distance-vector protocol, hop count কে metric হিসেবে use করে (max 15 hops)। প্রতি 30 second-এ updates করে। উদাহরণ — RIP route entry: 192.168.5.0/24 via 10.0.0.2, metric 2।",
      },
      { type: "h3", title: "OSPF (Open Shortest Path First)" },
      {
        type: "p",
        text: "Link-state protocol, cost (bandwidth-এর উপর based) use করে। Hierarchical design — areas গুলো একটি backbone (Area 0)-এর সাথে connected। Faster convergence, VLSM/CIDR support করে।",
      },
      { type: "h3", title: "BGP (Border Gateway Protocol)" },
      {
        type: "p",
        text: "Path-vector protocol যেটা Autonomous Systems (AS)-এর মধ্যে use হয়। Routes-এ AS_PATH attribute include করা থাকে loops prevent করতে। উদাহরণ — AS 100, 200.1.0.0/16-কে path [100] সহ advertise করে। AS 200 সেটি receive করে, নিজের AS prepend করে: [200, 100]।",
      },
      {
        type: "p",
        text: "Real-life thinking — RIP হলো neighbors একে অপরকে gossip করে (আমি X-এ যেতে পারি, 2 hops)। OSPF হলো সবার কাছে একটি full map আছে এবং প্রত্যেকে নিজে route বের করে। BGP হলো বিভিন্ন দেশের post offices একে অপরের সাথে আলোচনা করে যে কোন package কোন দেশে যাবে।",
      },

      { type: "h2", id: "additional-topics", title: "Additional Topics" },
      { type: "h3", title: "Fragmentation" },
      {
        type: "p",
        text: "যখন একটি packet একটি link-এর MTU (Maximum Transmission Unit)-এর চেয়ে বড়, router সেটিকে fragments-এ ভাগ করে। IPv4 fragments গুলো destination-এ reassemble করা হয়; IPv6 in-path fragmentation allow করে না। উদাহরণ — MTU = 1500 bytes, original packet = 4000 bytes। তিনটি fragments — Fragment 1 (offset 0, length 1500), Fragment 2 (offset 1480, length 1500), Fragment 3 (offset 2960, length 1020)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি বড় parcel কে ছোট ছোট বাক্সে ভাগ করা যাতে প্রতিটি বাক্স একটি narrow door দি�়ে যেতে পারে। Destination-এ সব বাক্স একসাথে যোগ করে আসল parcel পাওয়া যায়।",
      },
      { type: "h3", title: "NAT (Network Address Translation)" },
      {
        type: "p",
        text: "NAT একাধিক private IP addresses (যেমন 192.168.1.x) কে একটি single public IP share করতে allow করে। Common types — Source NAT (SNAT) outbound traffic-এর জন্য, Port Address Translation (PAT)। উদাহরণ — 192.168.1.10:12345 → 203.0.113.5:50001।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building যার একটি single public phone আছে। প্রতিটি apartment থেকে call করলে receptionist সেটিকে public number থেকে বের করে এবং একটি extension number assign করে। Incoming call-এ receptionist extension number দেখে সঠিক apartment-এ পাঠায়।",
      },
      { type: "h3", title: "ICMP (Internet Control Message Protocol)" },
      {
        type: "p",
        text: "ICMP error reporting ও diagnostics-এর জন্য use হয়। এটি IP-এর ভেতরে encapsulate করা থাকে। Common message types — Echo request/reply (ping), Destination unreachable (port/network unreachable), Time exceeded (traceroute-এ used), Redirect (host-কে better gateway সম্পর্কে inform)। উদাহরণ — ping 8.8.8.8 একটি ICMP Echo Request পাঠায়; Google-এর server Echo Reply দিয়ে উত্তর দেয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি delivery service-এ যদি কোনো package deliver না হয়, তাহলে একটি 'return to sender' sticker লাগানো হয় সমস্যার কারণ লেখা (ICMP Destination Unreachable)। Traceroute হলো প্রতিটি মাইলফলকে দাঁড়িয়ে জিজ্ঞেস করা 'এখানে কতক্ষণ লেগেছে?'",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Subnetting — host bits কে network-এর জন্য borrow করো (যেমন 192.168.1.0/26 → 4 subnets of 62 hosts)।",
          "CIDR — prefixes aggregate করো (যেমন 192.168.0.0/22 চারটি /24-এর জন্য)।",
          "Distance Vector — Bellman-Ford, periodic updates (RIP)।",
          "Link State — Dijkstra, full topology (OSPF)।",
          "Flooding — incoming ব্যতীত সব ports-এ পাঠাও (LSA distribution)।",
          "NAT — private ও public IPs এর মধ্যে map করো (home router একটি public IP share করে)।",
          "ICMP — error reporting ও diagnostics (ping, traceroute)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Network Layer বোঝা জরুরি কারণ এটি পুরো Internet-এর routing-এর ভিত্তি। পরের chapter-এ আমরা Transport Layer-এ যাব — যেখানে TCP ও UDP end-to-end communication handle করে।",
      },
    ],
  },

  {
    id: "net-transport",
    subject: "net",
    title: "Ch 06 — Transport Layer",
    bangla: "ট্রান্সপোর্ট লেয়ার",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "Transport Layer হলো OSI model-এর চতুর্থ layer এবং TCP/IP stack-এর core। এটি বিভিন্ন hosts-এ চলা application processes-এর মধ্যে logical communication provide করে। দুটি main protocol রয়েছে — TCP (Transmission Control Protocol) ও UDP (User Datagram Protocol)। এই chapter-এ transport layer-এর functions, TCP-র সম্পূর্ণ mechanism (handshake, flow control, congestion control), ও UDP-র characteristics বিস্তারিত আলোচনা করা হয়েছে।",
    sections: [
      { type: "h2", id: "functions", title: "Transport Layer-র Functions" },
      {
        type: "p",
        text: "Transport layer নিচের পাঁচটি main function perform করে। Process-to-Process Communication — Network layer packets গুলো hosts পর্যন্ত deliver করে, কিন্তু transport layer data কে নির্দিষ্ট processes (applications) পর্যন্ত deliver করে ports use করে। Segmentation ও Reassembly — application data কে ছোট segments-এ ভাগ করে transmission-এর জন্য এবং destination-এ পুনরায় assemble করে। Error Control — corrupted বা lost segments detect করে এবং retransmission request করে। Flow Control — fast sender কে slow receiver-কে overwhelm করা থেকে prevent করে। Congestion Control — অতিরিক্ত traffic যাতে network congestion cause না করে সেটা prevent করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি apartment building-এ একটি postman (network layer) শুধু building-এ পৌঁছায়। কিন্তু একজন receptionist (transport layer) প্রতিটি letter কে সঠিক apartment ও সঠিক person পর্যন্ত deliver করে। Postman building জানে, কিন্তু receptionist person জানে।",
      },

      { type: "h2", id: "tcp", title: "TCP — Transmission Control Protocol" },
      {
        type: "p",
        text: "TCP হলো একটি connection-oriented, reliable transport protocol যা stream-oriented service provide করে।",
      },
      { type: "h3", title: "Key Characteristics" },
      {
        type: "list",
        items: [
          "Connection-oriented — data exchange এর আগে একটি logical connection establish করতে হবে।",
          "Reliable — acknowledgements (ACKs) ও retransmissions use করে delivery guarantee করে।",
          "In-order delivery — segments গুলো সঠিক order-এ reassemble করা হয়।",
          "Full-duplex — simultaneous bidirectional data transfer।",
        ],
      },

      { type: "h3", title: "Three-Way Handshake" },
      {
        type: "p",
        text: "TCP একটি connection establish করতে three-way handshake use করে। এই process sequence numbers synchronize করে এবং parameters negotiate করে। তিনটি ধাপ — প্রথমে Client থেকে Server-এ SYN (seq=x) পাঠায়। Server SYN receive করে, buffers allocate করে, এবং Client-কে SYN+ACK (seq=y, ack=x+1) পাঠায়। Client SYN+ACK receive করে এবং Server-কে ACK (ack=y+1) পাঠায়। এর পর connection established হয় এবং উভয় পক্ষ data send করতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — দুজন মানুষের phone call। প্রথমে একজন 'hello' বলে (SYN)। অপরজন 'hello, I can hear you' বলে (SYN+ACK)। প্রথম জন 'ok, let's talk' বলে (ACK)। তারপর কথা শুরু হয়।",
      },
      {
        type: "multi-code",
        filename: "tcp_handshake_sim",
        codeSamples: {
          cpp: `#include <iostream>
using namespace std;

// Simulate TCP three-way handshake.
int main() {
    int x = 1000, y = 5000;

    cout << "=== TCP Three-Way Handshake ===\\n";
    cout << "Client -> Server: SYN (seq=" << x << ")\\n";
    cout << "Server -> Client: SYN+ACK (seq=" << y
         << ", ack=" << x+1 << ")\\n";
    cout << "Client -> Server: ACK (ack=" << y+1 << ")\\n";
    cout << "\\nConnection established!\\n";
    cout << "Client can send data starting from seq=" << x+1 << "\\n";
    cout << "Server can send data starting from seq=" << y+1 << "\\n";
    return 0;
}`,
          go: `package main

import "fmt"

func main() {
    x, y := 1000, 5000

    fmt.Println("=== TCP Three-Way Handshake ===")
    fmt.Printf("Client -> Server: SYN (seq=%d)\\n", x)
    fmt.Printf("Server -> Client: SYN+ACK (seq=%d, ack=%d)\\n", y, x+1)
    fmt.Printf("Client -> Server: ACK (ack=%d)\\n", y+1)
    fmt.Println("\\nConnection established!")
}`,
          python: `# Simulate TCP three-way handshake
x, y = 1000, 5000

print("=== TCP Three-Way Handshake ===")
print(f"Client -> Server: SYN (seq={x})")
print(f"Server -> Client: SYN+ACK (seq={y}, ack={x+1})")
print(f"Client -> Server: ACK (ack={y+1})")
print(f"\\nConnection established!")
print(f"Client can send data starting from seq={x+1}")
print(f"Server can send data starting from seq={y+1}")`,
          java: `public class TCPHandshake {
    public static void main(String[] args) {
        int x = 1000, y = 5000;
        System.out.println("=== TCP Three-Way Handshake ===");
        System.out.println("Client -> Server: SYN (seq=" + x + ")");
        System.out.println("Server -> Client: SYN+ACK (seq=" + y + ", ack=" + (x+1) + ")");
        System.out.println("Client -> Server: ACK (ack=" + (y+1) + ")");
        System.out.println("\\nConnection established!");
    }
}`,
        },
      },

      { type: "h3", title: "Reliable Communication" },
      {
        type: "p",
        text: "TCP reliability নিশ্চিত করতে তিনটি mechanism use করে — Sequence numbers (প্রতিটি byte of data কে number করে), Acknowledgments (receipt confirm করে), ও Retransmission timers (timeout-এর পর unacknowledged data resend করে)।",
      },

      { type: "h3", title: "Flow Control: Sliding Window" },
      {
        type: "p",
        text: "TCP data flow control করতে sliding window mechanism use করে। Receiver একটি rwnd (receiver window) advertise করে যা available buffer space indicate করে। Sender receiver-এর advertised window exceed করতে পারবে না। Receiver data process করে এবং ACKs পাঠানোর সাথে সাথে window সামনে slide করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি conveyor belt। Worker (sender) products রাখে, কিন্তু belt-এর উপর কতগুলো product থাকতে পারে সেটা receiver-এর একটি signal (rwnd) determine করে। Receiver প্রতিটি product process করে একটি 'go ahead' signal দেয়, যা window কে সামনে slide করে।",
      },

      { type: "h2", id: "congestion-control", title: "TCP Congestion Control" },
      {
        type: "p",
        text: "TCP network congestion manage করতে চারটি algorithm implement করে। Congestion window (cwnd) একটি sender কতটুকু data network-এ inject করতে পারবে সেটা limit করে।",
      },
      { type: "h3", title: "১. Slow Start" },
      {
        type: "p",
        text: "Initially cwnd = 1 MSS (Maximum Segment Size)। প্রতিটি ACK receive হলে cwnd double হয় (exponential growth) যতক্ষণ না একটি threshold (ssthresh) reach করে। উদাহরণ — cwnd = 1 → 2 → 4 → 8 → 16 → ssthresh এ।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি car সকালে highway-এ ঢুকছে। প্রথমে ধীরে শুরু করে (1 MSS), তারপর traffic কম থাকলে speed দ্রুত বাড়ায় (double), কিন্তু একটি limit-এ পৌঁছালে steady হয়ে যায়।",
      },
      { type: "h3", title: "২. Congestion Avoidance" },
      {
        type: "p",
        text: "যখন cwnd >= ssthresh, growth linear হয়ে যায় — cwnd += 1/cwnd per ACK। এটি ততক্ষণ চলে যতক্ষণ packet loss detect না হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — highway-এ traffic বাড়তে থাকলে ধীরে ধীরে speed বাড়ানো যায় (linear), যাতে আচমকা jam না হয়ে যায়।",
      },
      { type: "h3", title: "৩. Fast Retransmit" },
      {
        type: "p",
        text: "৩টি duplicate ACKs receive হলে, sender missing segment-কে immediately retransmit করে (timeout-এর জন্য wait না করে)। এটি packet loss দ্রুত detect ও recover করার একটি mechanism।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন delivery person যদি তিনজন customer থেকে 'আমি package পাইনি' শোনে, সে সাথে সাথে resend করে — অপেক্ষা করে না যতক্ষণ 'গত ৩০ সেকেন্ডে কেউ complaint করেনি' এমন timeout হবে।",
      },
      { type: "h3", title: "৪. Fast Recovery" },
      {
        type: "p",
        text: "Fast retransmit-এর পর, ssthresh = cwnd/2, cwnd = ssthresh + 3। প্রতিটি subsequent duplicate ACK-এ cwnd += 1। যখন একটি new ACK arrive করে, cwnd = ssthresh হয় এবং congestion avoidance-এ enter করে।",
      },

      { type: "h2", id: "udp", title: "UDP — User Datagram Protocol" },
      {
        type: "p",
        text: "UDP হলো একটি simple, connectionless transport protocol যা minimal service provide করে।",
      },
      { type: "h3", title: "Key Characteristics" },
      {
        type: "list",
        items: [
          "Connectionless — কোনো handshake নেই; প্রতিটি datagram independent।",
          "Unreliable — delivery, ordering, বা duplicate protection-এর কোনো guarantee নেই।",
          "No flow control — sender যেকোনো rate-এ transmit করতে পারে।",
          "No congestion control — network congestion-এ react করে না।",
          "Low overhead — 8-byte header (TCP-র 20-byte header-এর বিপরীতে)।",
        ],
      },
      {
        type: "multi-code",
        filename: "udp_datagram",
        codeSamples: {
          cpp: `#include <cstring>
#include <iostream>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

// Send a UDP datagram.
int main() {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    sockaddr_in dest{};
    dest.sin_family = AF_INET;
    dest.sin_port = htons(9090);
    inet_pton(AF_INET, "127.0.0.1", &dest.sin_addr);

    const char* msg = "Hello, UDP!";
    sendto(sock, msg, strlen(msg), 0,
           (sockaddr*)&dest, sizeof(dest));
    std::cout << "Sent: " << msg << '\\n';
    close(sock);
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "net"
)

func main() {
    conn, _ := net.Dial("udp", "127.0.0.1:9090")
    defer conn.Close()

    msg := []byte("Hello, UDP!")
    conn.Write(msg)
    fmt.Println("Sent:", string(msg))
}`,
          python: `import socket

# Send a UDP datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = b"Hello, UDP!"
sock.sendto(msg, ("127.0.0.1", 9090))
print("Sent:", msg.decode())
sock.close()`,
          java: `import java.net.*;

public class UDPClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket sock = new DatagramSocket();
        byte[] msg = "Hello, UDP!".getBytes();
        InetAddress addr = InetAddress.getByName("127.0.0.1");
        DatagramPacket pkt = new DatagramPacket(
            msg, msg.length, addr, 9090);
        sock.send(pkt);
        System.out.println("Sent: " + new String(msg));
        sock.close();
    }
}`,
        },
      },

      { type: "h3", title: "UDP-র Use Cases" },
      {
        type: "p",
        text: "UDP তখন preferred যখন speed ও low latency reliability-এর চেয়ে বেশি important।",
      },
      {
        type: "list",
        items: [
          "Live streaming / VoIP — dropped packets tolerable; retransmission delay cause করে।",
          "DNS queries — short request-response; retry mechanism application layer-এ।",
          "SNMP (network monitoring) — low overhead, periodic polling।",
          "DHCP — broadcast-based, কোনো connection state প্রয়োজন নেই।",
          "Online gaming — fast updates; পুরোনো data অকেজো।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — TCP হলো registered mail (tracking, confirmation, resend)। UDP হলো একটি postcard — ছুঁড়ে দাও, পৌঁছাক বা না পৌঁছাক, চিন্তা নেই। DNS-এর মতো ছোট query-তে postcard যথেষ্ট, কারণ সহজে আবার পাঠানো যায়। কিন্তু একটি file transfer-এ registered mail দরকার — প্রতিটি byte পৌঁছাতে হবে।",
      },

      { type: "h2", id: "tcp-vs-udp", title: "TCP vs UDP Comparison" },
      {
        type: "list",
        items: [
          "Connection — TCP: connection-oriented (handshake প্রয়োজন); UDP: connectionless (no handshake)।",
          "Reliability — TCP: reliable (ACKs, retransmission); UDP: unreliable (no guarantees)।",
          "Ordering — TCP: in-order delivery; UDP: unordered (no guarantee)।",
          "Flow control — TCP: yes (sliding window); UDP: না।",
          "Congestion control — TCP: yes (4 algorithms); UDP: না।",
          "Header size — TCP: 20 bytes; UDP: 8 bytes।",
          "Speed — TCP: slower (overhead); UDP: faster (minimal overhead)।",
          "Use case — TCP: file transfer, email, web; UDP: streaming, gaming, DNS।",
        ],
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: TCP বেছে নিন যখন data integrity ও order গুরুত্বপূর্ণ। UDP বেছে নিন যখন speed ও low latency critical। কিছু application দুটোই use করে — যেমন একটি video call-এ signaling TCP-তে চলে, কিন্তু প্রকৃত audio/video UDP-তে চলে।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Transport layer process-to-process communication enable করে এবং segmentation, error control, flow control, ও congestion control provide করে।",
          "TCP হলো connection-oriented ও reliable — three-way handshake, sliding window flow control, ও sophisticated congestion control (slow start, congestion avoidance, fast retransmit, fast recovery) use করে।",
          "UDP হলো connectionless, fast, ও lightweight — real-time applications ও simple request-response protocols-এর জন্য suitable।",
          "TCP বেছে নিন যখন data integrity ও order গুরুত্বপূর্ণ; UDP বেছে নিন যখন speed ও low latency critical।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Transport layer বোঝা জরুরি কারণ এটি application-এর সাথে network-এর মধ্যে bridge। পরের chapter-এ আমরা TCP-র 3-way handshake-এর আরও details-এ যাব এবং তারপর Application Layer-এ (HTTP, DNS)।",
      },
    ],
  },

  {
    id: "net-application",
    subject: "net",
    title: "Ch 07 — Application Layer",
    bangla: "অ্যাপ্লিকেশন লেয়ার",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Application Layer (OSI model-এর Layer 7) end user-এর সবচেয়ে কাছে। এটি protocols ও services provide করে যা applications-কে network-এর উপর communicate করতে enable করে। এই chapter-এ essential protocols — HTTP/HTTPS, FTP, SMTP, POP3/IMAP, DNS, DHCP — এবং client-server architecture, URL structure, cookies, ও sessions-এর core concepts cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "client-server", title: "Client-Server Architecture" },
      {
        type: "p",
        text: "Client-Server architecture হলো একটি distributed application structure যা tasks কে service providers (servers) ও service requesters (clients)-এ ভাগ করে। Client — contact initiate করে, replies-এর জন্য wait করে, user devices-এ চলে। Server — সবসময় on থাকে, requests-এর জন্য listen করে, responses provide করে, প্রায়ই অনেক clients-কে simultaneously serve করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant। Client হলো customer যে waiter-কে order দেয়। Server হলো kitchen যেটা food prepare করে। Client সবসময় প্রথমে initiate করে এবং server কখনো প্রথমে client-কে contact করে না।",
      },

      { type: "h2", id: "url", title: "URL Structure (Uniform Resource Locator)" },
      {
        type: "p",
        text: "URL হলো একটি specific string যা একটি resource identify করে এবং client-কে বলে কীভাবে সেটা access করতে হয়। উদাহরণ — https://alice:[email protected]:443/search?q=mermaid&lang=en#results।",
      },
      { type: "h3", title: "URL Components" },
      {
        type: "list",
        items: [
          "scheme — protocol (যেমন https = HTTP over TLS)।",
          "user:password — authentication (browsers-এ কদাচিৎ used)।",
          "host — domain name বা IP address (যেমন docs.example.com)।",
          "port — TCP port (HTTPS-এর জন্য default 443)।",
          "path — server-এ resource location (যেমন /search)।",
          "query — key-value parameters (dynamic content, যেমন q=mermaid&lang=en)।",
          "fragment — HTML page-এর ভেতরে section (client-side only, যেমন #results)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: Practice-এ URLs-এ credentials deprecated — security reasons-এ এড়ানো উচিত।",
      },

      { type: "h2", id: "cookies-sessions", title: "Cookies ও Sessions" },
      {
        type: "p",
        text: "HTTP হলো stateless — প্রতিটি request independent। Cookies ও sessions state যোগ করে।",
      },
      { type: "h3", title: "Cookies" },
      {
        type: "p",
        text: "Cookies হলো ছোট text files যা browser-এ store করা থাকে এবং প্রতিটি request-এ একই domain-এ automatically পাঠানো হয়। Key attributes — Expires/Max-Age (lifetime), Domain/Path (scope), Secure (শুধু HTTPS-এ send), HttpOnly (JavaScript access prevent করে, XSS mitigate)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি membership card যা প্রতিবার store-এ গেলে দেখাতে হয়। Store আপনাকে চিনে ফেলে এবং previous purchases বা loyalty points দেখায়।",
      },
      { type: "h3", title: "Sessions" },
      {
        type: "p",
        text: "Session হলো server-side storage যা একটি unique session ID-র সাথে tied (সাধারণত একটি cookie-তে stored)। Server user data (যেমন shopping cart, login state) keep করে এবং client শুধু identifier hold করে। উদাহরণ — user cart-এ items যোগ করে → session ID xyz server-এ {cart: ['laptop','mouse']} store করে। পরের request-এ Cookie: sessionId=xyz include করে → server cart retrieve করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hotel-এ আপনার একটি room key আছে (session ID)। আপনি key নিজে ধরে রাখেন, কিন্তু আপনার luggage (session data) hotel-এর locker-এ রাখা। Key দেখালে hotel staff আপনার luggage এনে দেয়।",
      },

      { type: "h2", id: "http-https", title: "HTTP / HTTPS" },
      { type: "h3", title: "HTTP (HyperText Transfer Protocol)" },
      {
        type: "p",
        text: "Port 80 (plain text)। Methods — GET, POST, PUT, DELETE, ইত্যাদি। Status codes — 200 OK, 404 Not Found, 500 Internal Server Error। একটি basic HTTP exchange-এ browser থেকে GET /index.html HTTP/1.1 with Host header যায়, server 200 OK ও HTML content ফিরে পাঠায়।",
      },
      { type: "h3", title: "HTTPS (HTTP Secure)" },
      {
        type: "p",
        text: "Port 443। Client ও server-এর মধ্যে TLS/SSL encryption যোগ করে। Eavesdropping, tampering, ও impersonation prevent করে। TLS handshake — ClientHello (supported ciphers), ServerHello + Certificate (public key), Client verify করে ও premaster secret encrypt করে (server-এর public key দিয়ে), Server Finished, তারপর উভয়ের session keys হয় যায় symmetric encryption-এর জন্য।",
      },
      {
        type: "p",
        text: "Real-life thinking — HTTP হলো একটি postcard — যে কেউ পথে পড়ে দেখতে পারে। HTTPS হলো একটি sealed envelope — শুধু প্রেষক ও প্রাপকই খুলতে পারে। Banking websites, e-commerce (Amazon, eBay) সবসময় HTTPS use করে credentials ও payment data protect করতে।",
      },
      {
        type: "multi-code",
        filename: "http_request",
        codeSamples: {
          cpp: `#include <iostream>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>

// Simple HTTP GET request (port 80).
int main() {
    struct hostent* he = gethostbyname("example.com");
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr = *((in_addr*)he->h_addr);
    connect(sock, (sockaddr*)&addr, sizeof(addr));

    std::string req = "GET / HTTP/1.1\\r\\nHost: example.com\\r\\nConnection: close\\r\\n\\r\\n";
    send(sock, req.c_str(), req.size(), 0);

    char buf[4096];
    int n = recv(sock, buf, sizeof(buf)-1, 0);
    buf[n] = '\\0';
    std::cout << buf << '\\n';
    close(sock);
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "io"
    "net/http"
)

func main() {
    resp, err := http.Get("http://example.com")
    if err != nil { panic(err) }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    fmt.Printf("Status: %d\\n", resp.StatusCode)
    fmt.Println("Body:", string(body)[:100], "...")
}`,
          python: `import urllib.request

# Simple HTTP GET request
response = urllib.request.urlopen("http://example.com")
print(f"Status: {response.status}")
body = response.read().decode()
print(f"Body: {body[:100]}...")`,
          java: `import java.net.*;
import java.io.*;

public class HttpRequest {
    public static void main(String[] args) throws Exception {
        URL url = new URL("http://example.com");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        System.out.println("Status: " + conn.getResponseCode());
        BufferedReader r = new BufferedReader(
            new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = r.readLine()) != null) {
            System.out.println(line);
            if (line.length() > 100) break;
        }
    }
}`,
        },
      },

      { type: "h2", id: "ftp", title: "FTP (File Transfer Protocol)" },
      {
        type: "p",
        text: "Ports — 20 (data) ও 21 (control)। Purpose — client ও server-এর মধ্যে files transfer করা। Authentication — username/password (বা anonymous)। দুটি mode — Active Mode (client port 21 → server port 21 control, server → client port 20 data) ও Passive Mode (client → server port 21 control, client → server high port data)।",
      },
      {
        type: "p",
        text: "Common FTP commands — USER, PASS (login), RETR filename (download), STOR filename (upload), LIST (list directory)। উদাহরণ — একজন web developer FileZilla (FTP client) দিয়ে website files কে ftp.example.com-এ upload করে।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: FTP insecure (passwords plain text-এ পাঠানো হয়)। SFTP (SSH File Transfer Protocol) বা FTPS (FTP over TLS) preferred।",
      },

      { type: "h2", id: "smtp", title: "SMTP (Simple Mail Transfer Protocol)" },
      {
        type: "p",
        text: "Ports — 25 (standard), 587 (submission), 465 (SMTPS)। Purpose — client থেকে server-এ এবং mail servers-এর মধ্যে email send করা। Direction — push protocol (client server-এ email push করে)। Email flow — User Agent (Outlook) → Mail Submission Agent (SMTP server) → Mail Transfer Agent (relay) → Mail Delivery Agent। MDA recipient-এর mailbox-এ store করে, যা POP3/IMAP দিয়ে retrieve করা যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — SMTP হলো post office-এ একটি letter drop করা। Post office (MSA) সেটি সঠিক destination post office (MTA)-এ forward করে। Destination post office (MDA) recipient-এর mailbox-এ রাখে। তারপর recipient যখন খুশি সেই mailbox থেকে letter তুলে নেয় (POP3/IMAP)।",
      },

      { type: "h2", id: "pop3-imap", title: "POP3 / IMAP (Email Retrieval)" },
      {
        type: "p",
        text: "দুটোই pull protocols — client server থেকে emails retrieve করে। POP3 (Post Office Protocol v3) — port 110/995। Emails download করে ও সাধারণত server থেকে delete করে। শুধু Inbox support করে। Offline access ভালো। উদাহরণ — legacy setups যেখানে এক computer থেকে email পড়া হয়।",
      },
      {
        type: "p",
        text: "IMAP (Internet Message Access Protocol) — port 143/993। Emails server-এ keep করে, devices জুড়ে synchronize করে। Multiple folders support করে। Gmail, Outlook.com, corporate environments-এ used (phone, laptop, webmail সব sync-এ)।",
      },
      {
        type: "p",
        text: "Real-life thinking — POP3 হলো post office থেকে letter নিয়ে বাড়িতে রাখা (server থেকে delete)। IMAP হলো post office-এ letter রেখে যাওয়া কিন্তু যখন দরকার পড়া (server-এ থাকে, সব devices sync)।",
      },

      { type: "h2", id: "dns", title: "DNS (Domain Name System)" },
      {
        type: "p",
        text: "Port — 53 (queries-এর জন্য UDP, zone transfers-এর জন্য TCP)। Purpose — human-readable domain names (যেমন google.com) কে IP addresses (যেমন 142.250.190.46)-এ translate করা। DNS resolution steps — browser local DNS resolver-কে query করে → resolver root DNS server-কে ask করে → root .com TLD server refer করে → TLD authoritative server refer করে → authoritative server IP দেয় → resolver browser-কে IP দেয়।",
      },
      {
        type: "p",
        text: "Record types — A (IPv4 address), AAAA (IPv6 address), CNAME (alias, যেমন www → @), MX (mail exchange server)। উদাহরণ — আপনি https://github.com type করলে, আপনার computer DNS-কে ask করে 'github.com কোথায়?' এবং 140.82.112.3 receive করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — DNS হলো একটি phone book। আপনি 'John Smith' নাম search করেন, phone book আপনাকে তার phone number দেয়। আপনি নাম মনে রাখেন, কিন্তু call করতে number প্রয়োজন। DNS domain নাম কে IP ঠিকানায় রূপান্তর করে।",
      },
      {
        type: "multi-code",
        filename: "dns_lookup",
        codeSamples: {
          cpp: `#include <arpa/inet.h>
#include <iostream>
#include <netdb.h>

// DNS lookup: hostname -> IP address
int main() {
    const char* hostname = "example.com";
    struct hostent* he = gethostbyname(hostname);
    if (!he) {
        std::cerr << "DNS lookup failed\\n";
        return 1;
    }
    struct in_addr** addr_list =
        (struct in_addr**)he->h_addr_list;
    for (int i = 0; addr_list[i]; i++) {
        std::cout << hostname << " -> "
                  << inet_ntoa(*addr_list[i]) << '\\n';
    }
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "net"
)

func main() {
    ips, err := net.LookupHost("example.com")
    if err != nil { fmt.Println("err:", err); return }
    for _, ip := range ips {
        fmt.Println("example.com ->", ip)
    }
}`,
          python: `import socket

# DNS lookup: hostname -> IP address
hostname = "example.com"
ip = socket.gethostbyname(hostname)
print(f"{hostname} -> {ip}")

# All IPs
all_ips = socket.getaddrinfo(hostname, None)
for info in all_ips:
    print(f"{hostname} -> {info[4][0]}")`,
          java: `import java.net.*;

public class DNSLookup {
    public static void main(String[] args) throws Exception {
        InetAddress[] addrs = InetAddress.getAllByName("example.com");
        for (InetAddress addr : addrs) {
            System.out.println("example.com -> " + addr.getHostAddress());
        }
    }
}`,
        },
      },

      { type: "h2", id: "dhcp", title: "DHCP (Dynamic Host Configuration Protocol)" },
      {
        type: "p",
        text: "Ports — 67 (server), 68 (client)। Purpose — network-এ devices-কে automatically IP addresses, subnet mask, default gateway, ও DNS servers assign করা। DORA process — Discover (client broadcast করে 'আমার IP দরকার'), Offer (server offer করে 'তুমি 192.168.1.100 use করতে পারো 24 ঘণ্টার জন্য'), Request (client accept করে), Acknowledge (server confirm করে ও DNS, gateway দেয়)।",
      },
      {
        type: "p",
        text: "Lease time — IP শুধু একটি নির্দিষ্ট সময়ের জন্য valid (যেমন 24 hours)। Client expiry-র আগে renew করে। উদাহরণ — আপনি coffee shop Wi-Fi-তে connect করলে, আপনার phone DHCP use করে 192.168.0.15 এর মতো IP address পায়, সাথে router-এর IP gateway হিসেবে ও ISP-এর DNS servers।",
      },
      {
        type: "p",
        text: "Real-life thinking — DHCP হলো একটি hotel-এ check-in করা। আপনি front desk-কে বলেন 'আমার একটি room দরকার' (DISCOVER)। Front desk বলে 'Room 215 আপনার, 2 রাতের জন্য' (OFFER)। আপনি বলেন 'আমি Room 215 নেব' (REQUEST)। Front desk বলে 'Confirmed, এখানে keycard ও breakfast time' (ACK)। Lease time শেষ হলে আপনি renew করেন।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Application Layer lower layers-এর complexity end-user applications থেকে hide করে।",
          "Client-server dominant model, কিন্তু peer-to-peer (P2P) ও exist করে (যেমন BitTorrent)।",
          "Security ক্রমশ এই layer-এ embedded হচ্ছে (HTTPS, SMTPS, IMAPS, POP3S, DNSSEC)।",
          "HTTP/HTTPS — web pages transfer, ports 80/443।",
          "FTP — file transfer, ports 20/21, কিন্তু insecure (SFTP/FTPS preferred)।",
          "SMTP — email send, ports 25/587/465।",
          "POP3/IMAP — email retrieve, POP3 downloads ও delete করে, IMAP server-এ রাখে ও sync করে।",
          "DNS — domain names কে IP-তে translate করে, port 53।",
          "DHCP — automatically IP configuration assign করে, ports 67/68, DORA process।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: এই protocols ও concepts বোঝা modern networks ও web build, use, বা troubleshoot করার জন্য essential। পরের chapter-এ আমরা TCP-র 3-way handshake-এর আরও details-এ যাব।",
      },
    ],
  },

  {
    id: "net-security",
    subject: "net",
    title: "Ch 08 — Network Security",
    bangla: "নেটওয়ার্ক সিকিউরিটি",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Network security হলো data, devices, ও communications-কে unauthorized access, misuse, বা destruction থেকে protect করার practice। এই chapter-এ security-এর fundamental goals, cryptographic building blocks, key security protocols (SSL/TLS, HTTPS), common attacks (phishing, MitM, DoS/DDoS), ও protection mechanisms (firewalls, intrusion detection systems) cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "goals", title: "Security Goals (CIA Triad + Non-repudiation)" },
      {
        type: "p",
        text: "Security objectives গুলো সাধারণত Confidentiality, Integrity, Availability — এর সাথে Authentication ও Non-repudiation যোগ করে summarize করা হয়।",
      },
      { type: "h3", title: "৫টি Security Goals" },
      {
        type: "list",
        items: [
          "Confidentiality — শুধু authorised parties data read করতে পারবে। Encryption দিয়ে achieve করা হয়। উদাহরণ — WhatsApp message encrypt করা যাতে শুধু recipient read করতে পারে।",
          "Integrity — data অপরিবর্তিত থাকবে, undetectableভাবে modify করা যাবে না। Hash functions বা digital signatures দিয়ে। উদাহরণ — checksum দিয়ে downloaded file verify করা।",
          "Availability — systems ও data যখন দরকার accessible থাকবে। Redundancy, DDoS protection দিয়ে। উদাহরণ — flash sale-এর সময় website online থাকা।",
          "Authentication — user বা device-এর identity verify করা। Passwords, certificates, biometrics দিয়ে। উদাহরণ — online banking-এ username + OTP।",
          "Non-repudiation — একটি action perform করা অস্বীকার করা যাবে না। Digital signatures, audit logs দিয়ে। উদাহরণ — digitally signed contract পাঠানোর পর sender অস্বীকার করতে পারবে না।",
        ],
      },

      { type: "h2", id: "crypto", title: "Cryptography" },
      {
        type: "p",
        text: "Cryptography হলো communication secure করার art — data কে একটি unreadable format (ciphertext)-এ transform করা এবং আবার back।",
      },
      { type: "h3", title: "Symmetric Key Encryption" },
      {
        type: "p",
        text: "Encryption ও decryption-এর জন্য একই key use হয়। Fast ও efficient bulk data-র জন্য। Problem — parties-এর মধ্যে key securely share করা। Common algorithms — AES (Advanced Encryption Standard), ChaCha20, DES (legacy)। উদাহরণ — BitLocker দিয়ে hard drive encrypt করা (AES use করে)। Wi-Fi WPA2 AES use করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — symmetric encryption হলো একটি locked box যার একটি single key আছে। আপনি ও আপনার friend-এর কাছে একই key-এর copy আছে। কিন্তু সমস্যা হলো key টা কীভাবে friend-কে দেবেন — যদি কেউ key চুরি করে, সে box খুলতে পারবে।",
      },
      { type: "h3", title: "Asymmetric Key Encryption (Public Key)" },
      {
        type: "p",
        text: "Key pair — public key (freely share করা যায়) ও private key (secret রাখা হয়)। Public key দিয়ে encrypt করা data শুধু matching private key দিয়ে decrypt করা যায়। Symmetric-এর তুলনায় অনেক slow; প্রায়ই একটি symmetric session key exchange করতে use হয়। Common algorithms — RSA, ECC (Elliptic Curve Cryptography)।",
      },
      {
        type: "p",
        text: "Real-life thinking — asymmetric encryption হলো একটি mailbox যার একটি slot (public key) সবাই দেখতে পারে। যে কেউ letter ঢুকিয়ে দিতে পারে, কিন্তু শুধু আপনার কাছে key (private key) আছে box খোলার। কেউ কখনো key ছাড়া box খুলতে পারবে না।",
      },
      {
        type: "multi-code",
        filename: "aes_encrypt",
        codeSamples: {
          cpp: `#include <iostream>
#include <openssl/evp.h>
#include <string>
#include <vector>

// AES-256-CBC encryption (simplified).
std::vector<unsigned char> aes_encrypt(
    const std::string& plaintext,
    const unsigned char* key,
    const unsigned char* iv) {

    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key, iv);

    std::vector<unsigned char> ciphertext(plaintext.size() + 16);
    int len;
    EVP_EncryptUpdate(ctx, ciphertext.data(), &len,
        (const unsigned char*)plaintext.data(), plaintext.size());
    int total = len;
    EVP_EncryptFinal_ex(ctx, ciphertext.data() + len, &len);
    total += len;
    ciphertext.resize(total);
    EVP_CIPHER_CTX_free(ctx);
    return ciphertext;
}

int main() {
    unsigned char key[32] = {0};  // 256-bit key (use random!)
    unsigned char iv[16] = {0};   // initialization vector
    auto ct = aes_encrypt("Hello, AES!", key, iv);
    std::cout << "Ciphertext length: " << ct.size() << " bytes\\n";
    return 0;
}
// Compile: g++ aes.cpp -lcrypto`,
          go: `package main

import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "fmt"
)

func encryptAES(plaintext, key []byte) []byte {
    block, _ := aes.NewCipher(key)
    ciphertext := make([]byte, aes.BlockSize+len(plaintext))
    iv := ciphertext[:aes.BlockSize]
    rand.Read(iv)
    stream := cipher.NewCFBEncrypter(block, iv)
    stream.XORKeyStream(ciphertext[aes.BlockSize:], plaintext)
    return ciphertext
}

func main() {
    key := make([]byte, 32)  // 256-bit key
    ct := encryptAES([]byte("Hello, AES!"), key)
    fmt.Printf("Ciphertext: %x\\n", ct)
}`,
          python: `from cryptography.fernet import Fernet

# Generate a key (in practice, store it securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
plaintext = b"Hello, AES!"
ciphertext = cipher.encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt
decrypted = cipher.decrypt(ciphertext)
print(f"Decrypted: {decrypted}")
# pip install cryptography`,
          java: `import javax.crypto.*;
import javax.crypto.spec.*;
import java.security.*;
import java.util.*;

public class AESEncrypt {
    public static void main(String[] args) throws Exception {
        // Generate a 256-bit AES key
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        SecretKey key = kg.generateKey();

        // Encrypt
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(iv));
        byte[] ct = cipher.doFinal("Hello, AES!".getBytes());

        System.out.println("Ciphertext: " + Base64.getEncoder().encodeToString(ct));
    }
}`,
        },
      },
      { type: "h3", title: "Hash Functions" },
      {
        type: "p",
        text: "Hash function হলো one-way function — input কে একটি fixed-length output (hash/digest)-এ রূপান্তর করে। Hash কে reverse করে original input খুঁজে পাওয়া যায় না। একই input সবসময় একই hash দেয়। Input-এ ছোট change হলে hash সম্পূর্ণ ভিন্ন হয়ে যায় (avalanche effect)। Common algorithms — SHA-256, SHA-3, MD5 (broken, not secure)।",
      },
      {
        type: "p",
        text: "Applications — Password storage (hash store করো, plaintext নয়), Integrity checking (downloaded file + SHA-256 hash verify করো), Digital signatures (message-এর hash sign করো, পুরো message নয়)। Real-life thinking — hash হলো একটি fingerprint। প্রতিটি মানুষের fingerprint unique। আপনি fingerprint থেকে মানুষটিকে recreate করতে পারবেন না, কিন্তু দুটি fingerprint compare করে বলতে পারবেন একই মানুষ কি না।",
      },
      {
        type: "multi-code",
        filename: "hash_demo",
        codeSamples: {
          cpp: `#include <iomanip>
#include <iostream>
#include <openssl/sha.h>
#include <sstream>
#include <string>

// SHA-256 hash of a string.
std::string sha256(const std::string& input) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((const unsigned char*)input.data(), input.size(), hash);
    std::ostringstream oss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        oss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    return oss.str();
}

int main() {
    std::cout << "SHA-256 of 'hello': "
              << sha256("hello") << '\\n';
    std::cout << "SHA-256 of 'Hello': "
              << sha256("Hello") << '\\n';  // completely different!
}
// Compile: g++ hash.cpp -lcrypto`,
          go: `package main

import (
    "crypto/sha256"
    "fmt"
)

func main() {
    h1 := sha256.Sum256([]byte("hello"))
    h2 := sha256.Sum256([]byte("Hello"))
    fmt.Printf("SHA-256 of 'hello': %x\\n", h1)
    fmt.Printf("SHA-256 of 'Hello': %x\\n", h2)
}`,
          python: `import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(f"SHA-256 of 'hello': {sha256('hello')}")
print(f"SHA-256 of 'Hello': {sha256('Hello')}")  # completely different!`,
          java: `import java.security.*;
import java.util.*;

public class HashDemo {
    public static void main(String[] args) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] h1 = md.digest("hello".getBytes());
        byte[] h2 = md.digest("Hello".getBytes());
        System.out.println("SHA-256 of 'hello': " + bytesToHex(h1));
        System.out.println("SHA-256 of 'Hello': " + bytesToHex(h2));
    }
    static String bytesToHex(byte[] b) {
        StringBuilder sb = new StringBuilder();
        for (byte x : b) sb.append(String.format("%02x", x));
        return sb.toString();
    }
}`,
        },
      },

      { type: "h2", id: "tls-https", title: "Security Protocols: SSL/TLS ও HTTPS" },
      { type: "h3", title: "SSL / TLS (Transport Layer Security)" },
      {
        type: "p",
        text: "SSL (Secure Sockets Layer) deprecated; TLS (Transport Layer Security) হলো modern standard। এটি Application layer (HTTP) ও Transport layer (TCP)-এর মাঝে operate করে। Confidentiality (encryption), integrity (message authentication codes), ও authentication (certificates) provide করে।",
      },
      { type: "h3", title: "TLS 1.3 Handshake" },
      {
        type: "list",
        items: [
          "১. Client → Server: ClientHello (supported ciphers, random value)।",
          "২. Server → Client: ServerHello (chosen cipher, random value) + Certificate (server-এর public key)।",
          "৩. Client → Server: Certificate verify করো, session keys generate করো, encrypted Finished পাঠাও।",
          "৪. Server → Client: Encrypted Finished।",
          "৫. এর পর সব data session keys দিয়ে encrypted।",
        ],
      },
      {
        type: "p",
        text: "Certificate হলো একটি document যা একটি domain name কে একটি public key-এর সাথে bind করে, একটি Certificate Authority (CA) দ্বারা digitally signed (যেমন Let's Encrypt, DigiCert)।",
      },
      { type: "h3", title: "HTTPS (HTTP over TLS)" },
      {
        type: "p",
        text: "Port 443। HTTP messages গুলো একটি TLS tunnel-এর ভেতরে পাঠানো হয়। Eavesdropping (কেউ আপনার search terms দেখতে পারবে না), tampering (ISP কোনো ads inject করতে পারবে না), ও impersonation (আপনি real paypal.com-এর সাথে কথা বলছেন) protect করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — HTTPS হলো একটি sealed, tamper-evident envelope। কেউ দেখতে পারবে না ভেতরে কী আছে (confidentiality), কেউ চুপচাপ সেটি পরিবর্তন করতে পারবে না (integrity), এবং আপনি জানেন কে পাঠিয়েছে (authentication)।",
      },

      { type: "h2", id: "attacks", title: "Common Attacks" },
      { type: "h3", title: "Phishing" },
      {
        type: "p",
        text: "Attacker একটি legitimate entity (bank, IT support) হিসেবে impersonate করে user-কে trick করে credentials, credit card numbers, reveal করতে বা malicious links click করতে। সাধারণত email, SMS (smishing), বা fake websites-এর মাধ্যমে deliver করা হয়। Prevention — sender address ও URL ভালোভাবে check করো, MFA use করো, browser warnings মেনে চলো, user education।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন প্রতারক যে bank-এর uniform পরে আপনার দরজায় এসে বলে 'আমি bank থেকে এসেছি, আপনার ATM card ও PIN দিন'। আপনি যদি দেন, সে আপনার টাকা চুরি করবে।",
      },
      { type: "h3", title: "Man-in-the-Middle (MitM)" },
      {
        type: "p",
        text: "Attacker secretly দুটি parties-এর মধ্যে communication intercept ও সম্ভবত alter করে, যারা ভাবে তারা directly কথা বলছে। Unencrypted Wi-Fi (evil twin access point), ARP spoofing, বা compromised routers-এ হতে পারে। Prevention — HTTPS with proper certificate validation, public Wi-Fi এড়ানো বা VPN use করা, mutual authentication।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন postman যে আপনার letters চুপচাপ খোলে, পড়ে, সম্ভবত পরিবর্তন করে, এবং আবার seal করে পাঠিয়ে দেয়। আপনি ও recipient ভাবেন direct কথা হচ্ছে, কিন্তু মাঝখানে কেউ intercept করছে।",
      },
      { type: "h3", title: "DoS / DDoS (Denial of Service)" },
      {
        type: "p",
        text: "DoS — single source একটি target-কে traffic দিয়ে flood করে, unavailable করে দেয়। DDoS — একাধিক compromised machines (botnet) coordinate করে attack করে। Types — Volumetric (bandwidth flood, UDP/ICMP floods), Protocol (SYN flood, Ping of Death), Application layer (slow HTTP requests)।",
      },
      {
        type: "p",
        text: "Real-life thinking — DoS হলো একজন মানুষ যে একটি restaurant-এর দরজায় দাঁড়িয়ে সবাইকে ঢুকতে বাধা দেয়। DDoS হলো ১০০০ জন মানুষ যারা একসাথে restaurant-এ ঢুকে পড়ে এবং কেউই কিছু order করে না — শুধু বসে আছে। Real customers ঢুকতে পারে না।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: 2016 Dyn DNS attack-এ Mirai botnet (IoT devices) ব্যবহার করে massive DDoS attack হয়েছিল — Twitter, Netflix, ও অন্যান্য sites down হয়ে গিয়েছিল। IoT devices-এর weak security এর কারণ।",
      },

      { type: "h2", id: "protection", title: "Protection Mechanisms" },
      { type: "h3", title: "Firewalls" },
      {
        type: "p",
        text: "Firewall incoming/outgoing network traffic-কে predefined rules অনুযায়ী monitor ও control করে। তিনটি প্রকার — Packet filtering (headers inspect করে, যেমন iptables, Windows Firewall), Stateful inspection (connection state track করে, modern firewalls), Application layer (deep packet inspection, HTTP/DNS বোঝে, যেমন Palo Alto, Fortinet)।",
      },
      {
        type: "p",
        text: "Example rules — Block all incoming traffic on port 23 (Telnet), Allow outgoing HTTPS (port 443), Allow SSH (port 22) only from IT department's IP range। Real-life thinking — firewall হলো একটি building-এর security guard। Guard প্রতিটি ব্যক্তিকে check করে — কে আসছে, কোথায় যাচ্ছে, এবং একটি list অনুযায়ী allow বা deny করে।",
      },
      { type: "h3", title: "Intrusion Detection Systems (IDS)" },
      {
        type: "p",
        text: "IDS passively traffic monitor করে এবং suspicious patterns (signatures) বা anomalies detect হলে alert করে। Traffic block করে না (IPS-এর বিপরীত)। দুটি detection method — Signature-based (known attack patterns match করে, fast কিন্তু zero-day detect করতে পারে না), Anomaly-based (normal behaviour learn করে ও deviations alert করে, novel attacks detect করতে পারে কিন্তু false positives)।",
      },
      {
        type: "list",
        items: [
          "NIDS (Network IDS) — একটি network segment monitor করে (যেমন switch span port)।",
          "HIDS (Host-based IDS) — একটি server-এ চলে, logs, file integrity, system calls monitor করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — IDS হলো একটি building-এর CCTV camera। Camera সব কিছু record করে এবং suspicious activity হলে alert করে, কিন্তু নিজে থামায় না। IPS হলো security guard যে সাথে সাথে action নেয়।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Confidentiality — encryption data secret রাখে (AES, TLS)।",
          "Integrity — hash functions changes detect করে (SHA-256, HMAC)।",
          "Authentication — identity prove করা (passwords, certificates, MFA)।",
          "Non-repudiation — digital signatures (RSA + SHA-256)।",
          "Symmetric encryption — উভয় পক্ষের জন্য একই key (AES-256)।",
          "Asymmetric encryption — public/private key pair (RSA, ECC)।",
          "TLS/SSL — application data encrypt করে (HTTPS port 443)।",
          "Phishing — social engineering, fake login pages (MFA, user training)।",
          "Man-in-the-middle — communication intercept করা (certificate validation, VPN)।",
          "DDoS — resources overwhelm করা (Cloudflare, rate limiting)।",
          "Firewall — rules অনুযায়ী packets filter করা (iptables, pfSense)।",
          "IDS — intrusions detect করে, alert করে (Snort, Suricata)।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Defence in depth — একাধিক layers use করো — firewall, IDS, encryption, strong authentication। কোনো single solution security guarantee করে না; people, processes, ও technology একসাথে কাজ করতে হবে।",
      },
    ],
  },

  {
    id: "net-qos",
    subject: "net",
    title: "Ch 09 — Congestion Control & QoS",
    bangla: "কনজেশন কন্ট্রোল ও কোয়ালিটি অফ সার্ভিস",
    difficulty: "Medium",
    est: "1.5 hr",
    summary:
      "Congestion তখন হয় যখন network resources-এর চাহিদা available capacity-কে exceed করে। এই chapter-এ congestion control mechanisms, traffic shaping algorithms (leaky bucket, token bucket), ও key Quality of Service (QoS) parameters (delay, jitter, bandwidth) cover করা হয়েছে।",
    sections: [
      { type: "h2", id: "causes", title: "Causes of Congestion" },
      {
        type: "p",
        text: "Congestion তখন হয় যখন network resources-এর চাহিদা available capacity-কে exceed করে। Common causes গুলো হলো:",
      },
      {
        type: "list",
        items: [
          "High traffic bursts — একাধিক sources থেকে হঠাৎ data-এর spikes।",
          "Insufficient link bandwidth — slow links bottleneck হয়ে যায়।",
          "Buffer overflow at routers — queues ভরে গেলে packets drop করা হয়।",
          "Slow receiver processing — receiver incoming data-র সাথে পাল্লা দিতে পারে না।",
          "Retransmissions — lost packets আরও traffic trigger করে, পরিস্থিতি আরও খারাপ করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি traffic jam। খুব বেশি গাড়ি একটি narrow road-এ ঢুকে পড়ে (high traffic bursts)। Road অনেক narrow (insufficient bandwidth)। Traffic signal-এ অনেক গাড়ি queue করে (buffer overflow)। কেউ slowly চলে (slow receiver)। কেউ পিছনে ফিরে আবার চেষ্টা করে (retransmissions)। সব মিলে একটা deadlock।",
      },

      { type: "h2", id: "traffic-shaping", title: "Traffic Shaping" },
      {
        type: "p",
        text: "Traffic shaping data transmission-এর rate ও burstiness control করে congestion avoid করতে। দুটি main algorithm আছে — Leaky Bucket ও Token Bucket।",
      },

      { type: "h3", title: "Leaky Bucket" },
      {
        type: "p",
        text: "Leaky Bucket algorithm input bursts নির্বিশেষে একটি constant output rate enforce করে। এটি নিচে একটি ছোট hole সহ bucket-এর মতো কাজ করে। Packets arbitrary rate-এ arrive করে, একটি bucket (queue)-তে রাখা হয়। Bucket একটি fixed rate-এ packets transmit (leak) করে। যদি bucket overflow হয়, packets discard করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bucket যার তলায় একটি ছোট গর্ত। আপনি যেভাবেই পানি ঢালুন (packets arrive), পানি গর্ত দিয়ে একটি constant rate-এ বের হবে। বেশি পানি ঢাললে bucket ভরে গিয়ে overflow হবে — বাড়তি পানি পড়ে যাবে (packets dropped)।",
      },
      {
        type: "multi-code",
        filename: "leaky_bucket",
        codeSamples: {
          cpp: `#include <iostream>
#include <queue>
using namespace std;

class LeakyBucket {
    queue<int> bucket;
    int capacity, leak_rate;
public:
    LeakyBucket(int cap, int rate) : capacity(cap), leak_rate(rate) {}

    // Try to add a packet. Returns true if accepted.
    bool add_packet(int id) {
        if ((int)bucket.size() >= capacity) return false;
        bucket.push(id);
        return true;
    }

    // Transmit 'leak_rate' packets.
    void leak() {
        for (int i = 0; i < leak_rate && !bucket.empty(); i++) {
            cout << "Transmitted packet " << bucket.front() << '\\n';
            bucket.pop();
        }
    }
};

int main() {
    LeakyBucket lb(5, 1);  // capacity=5, leak=1/sec
    // 10 packets arrive simultaneously
    for (int i = 1; i <= 10; i++) {
        if (!lb.add_packet(i))
            cout << "Dropped packet " << i << '\\n';
    }
    // Leak 1 per second for 5 seconds
    for (int t = 0; t < 5; t++) lb.leak();
}`,
          go: `package main

import "fmt"

type LeakyBucket struct {
    bucket    []int
    capacity  int
    leakRate  int
}

func NewLeakyBucket(cap, rate int) *LeakyBucket {
    return &LeakyBucket{capacity: cap, leakRate: rate}
}

func (lb *LeakyBucket) AddPacket(id int) bool {
    if len(lb.bucket) >= lb.capacity { return false }
    lb.bucket = append(lb.bucket, id)
    return true
}

func (lb *LeakyBucket) Leak() {
    for i := 0; i < lb.leakRate && len(lb.bucket) > 0; i++ {
        fmt.Printf("Transmitted packet %d\\n", lb.bucket[0])
        lb.bucket = lb.bucket[1:]
    }
}

func main() {
    lb := NewLeakyBucket(5, 1)
    for i := 1; i <= 10; i++ {
        if !lb.AddPacket(i) {
            fmt.Printf("Dropped packet %d\\n", i)
        }
    }
    for t := 0; t < 5; t++ { lb.Leak() }
}`,
          python: `from collections import deque

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.bucket = deque()
        self.capacity = capacity
        self.leak_rate = leak_rate

    def add_packet(self, pkt_id):
        if len(self.bucket) >= self.capacity:
            return False
        self.bucket.append(pkt_id)
        return True

    def leak(self):
        for _ in range(self.leak_rate):
            if not self.bucket:
                break
            print(f"Transmitted packet {self.bucket.popleft()}")

lb = LeakyBucket(5, 1)  # capacity=5, leak=1/sec
for i in range(1, 11):
    if not lb.add_packet(i):
        print(f"Dropped packet {i}")
for _ in range(5):
    lb.leak()`,
          java: `import java.util.*;

public class LeakyBucket {
    Queue<Integer> bucket = new LinkedList<>();
    int capacity, leakRate;

    LeakyBucket(int cap, int rate) { capacity = cap; leakRate = rate; }

    boolean addPacket(int id) {
        if (bucket.size() >= capacity) return false;
        bucket.add(id);
        return true;
    }

    void leak() {
        for (int i = 0; i < leakRate && !bucket.isEmpty(); i++) {
            System.out.println("Transmitted packet " + bucket.poll());
        }
    }

    public static void main(String[] args) {
        LeakyBucket lb = new LeakyBucket(5, 1);
        for (int i = 1; i <= 10; i++) {
            if (!lb.addPacket(i))
                System.out.println("Dropped packet " + i);
        }
        for (int t = 0; t < 5; t++) lb.leak();
    }
}`,
        },
      },

      { type: "h3", title: "Token Bucket" },
      {
        type: "p",
        text: "Token Bucket একটি নির্দিষ্ট limit পর্যন্ত bursts allow করে যখন average rate-ও shape করে। Tokens একটি constant rate-এ bucket-এ যোগ করা হয়। একটি packet শুধু তখনই transmit হতে পারে যখন যথেষ্ট tokens available। Bucket একটি নির্দিষ্ট সংখ্যক tokens (b) hold করে (burst size)। Tokens গুলো r tokens/sec rate-এ arrive করে। প্রতিটি packet t tokens consume করে। Bucket ভর্তি থাকলে নতুন tokens discard করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি amusement park-এর ride tokens। আপনি প্রতি মিনিটে একটি token পান (token generation rate)। আপনি সেগুলো জমা করতে পারেন সর্বোচ্চ ১০টি (bucket size)। যদি আপনি ১০টি token জমিয়ে রাখেন, আপনি একসাথে ১০টি ride করতে পারবেন (burst)। কিন্তু দীর্ঘ সময়ে আপনি প্রতি মিনিটে একটি ride পাবেন (average rate)।",
      },
      {
        type: "multi-code",
        filename: "token_bucket",
        codeSamples: {
          cpp: `#include <algorithm>
#include <iostream>
using namespace std;

class TokenBucket {
    double tokens = 0;
    int capacity, rate;
public:
    TokenBucket(int cap, int r) : capacity(cap), rate(r) {}

    // Add tokens based on time elapsed (seconds).
    void refill(double elapsed) {
        tokens = min((double)capacity, tokens + elapsed * rate);
    }

    // Try to send a packet consuming 'cost' tokens.
    bool send(int cost) {
        if (tokens >= cost) {
            tokens -= cost;
            cout << "Sent packet (cost=" << cost
                 << ", tokens left=" << tokens << ")\\n";
            return true;
        }
        cout << "Dropped (tokens=" << tokens
             << ", needed=" << cost << ")\\n";
        return false;
    }
};

int main() {
    TokenBucket tb(10, 2);  // capacity=10, rate=2/sec
    tb.refill(5);           // 5 seconds → 10 tokens
    tb.send(3);             // ok, 7 left
    tb.send(5);             // ok, 2 left
    tb.send(5);             // drop, only 2
}`,
          go: `package main

import "fmt"

type TokenBucket struct {
    tokens   float64
    capacity int
    rate     int
}

func NewTokenBucket(cap, r int) *TokenBucket {
    return &TokenBucket{capacity: cap, rate: r}
}

func (tb *TokenBucket) Refill(elapsed float64) {
    tb.tokens = float64(tb.capacity)
    if t := tb.tokens + elapsed*float64(tb.rate); t < float64(tb.capacity) {
        tb.tokens = t
    }
}

func (tb *TokenBucket) Send(cost int) bool {
    if tb.tokens >= float64(cost) {
        tb.tokens -= float64(cost)
        fmt.Printf("Sent (tokens left=%.1f)\\n", tb.tokens)
        return true
    }
    fmt.Printf("Dropped (tokens=%.1f, needed=%d)\\n", tb.tokens, cost)
    return false
}

func main() {
    tb := NewTokenBucket(10, 2)
    tb.Refill(5)
    tb.Send(3)
    tb.Send(5)
    tb.Send(5)
}`,
          python: `class TokenBucket:
    def __init__(self, capacity, rate):
        self.tokens = 0
        self.capacity = capacity
        self.rate = rate

    def refill(self, elapsed):
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)

    def send(self, cost):
        if self.tokens >= cost:
            self.tokens -= cost
            print(f"Sent (tokens left={self.tokens:.1f})")
            return True
        print(f"Dropped (tokens={self.tokens:.1f}, needed={cost})")
        return False

tb = TokenBucket(10, 2)  # capacity=10, rate=2/sec
tb.refill(5)             # 5 sec → 10 tokens
tb.send(3)               # ok, 7 left
tb.send(5)               # ok, 2 left
tb.send(5)               # drop, only 2`,
          java: `public class TokenBucket {
    double tokens = 0;
    int capacity, rate;

    TokenBucket(int cap, int r) { capacity = cap; rate = r; }

    void refill(double elapsed) {
        tokens = Math.min(capacity, tokens + elapsed * rate);
    }

    boolean send(int cost) {
        if (tokens >= cost) {
            tokens -= cost;
            System.out.printf("Sent (tokens left=%.1f)%n", tokens);
            return true;
        }
        System.out.printf("Dropped (tokens=%.1f, needed=%d)%n", tokens, cost);
        return false;
    }

    public static void main(String[] args) {
        TokenBucket tb = new TokenBucket(10, 2);
        tb.refill(5);
        tb.send(3);
        tb.send(5);
        tb.send(5);
    }
}`,
        },
      },

      { type: "h3", title: "Leaky Bucket vs Token Bucket" },
      {
        type: "list",
        items: [
          "Output rate — Leaky Bucket: strictly constant; Token Bucket: varies, up to peak burst rate।",
          "Burst handling — Leaky Bucket: কোনো bursts allow করে না; Token Bucket: bursts allow করে (bucket size পর্যন্ত)।",
          "Long-term average rate — Leaky Bucket: fixed leak rate; Token Bucket: token generation rate।",
          "Packet discard — Leaky Bucket: bucket overflow হলে; Token Bucket: packet wait করে বা drop হয়।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Leaky Bucket হলো একটি faucet যা সবসময় একটি constant rate-এ পানি দেয়, আপনি যতই পানি ঢালুন। Token Bucket হলো একটি savings account — আপনি প্রতি মাসে একটি fixed amount পান, জমা করতে পারেন, এবং একসাথে বেশি খরচ করতে পারেন (burst) — কিন্তু দীর্ঘমেয়াদে average ঠিক থাকে।",
      },

      { type: "h2", id: "qos", title: "Quality of Service (QoS)" },
      {
        type: "p",
        text: "QoS বলতে বিভিন্ন traffic types-কে বিভিন্ন priority levels provide করার ability বোঝায়, যা predictable performance ensure করে।",
      },

      { type: "h3", title: "Delay (Latency)" },
      {
        type: "p",
        text: "Delay হলো সেই সময় যেটা একটি packet source থেকে destination-এ যেতে নেয়। Components গুলো হলো — Processing delay (bit errors ও header check করার সময়), Queuing delay (output buffer-এ wait করার সময়), Transmission delay (bits কে link-এ push করার সময়), Propagation delay (signal-এর medium-এ travel করার সময়)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি letter পাঠানো। Processing delay হলো letter লেখার সময়। Queuing delay হলো post office-এ queue-এ দাঁড়ানো। Transmission delay হলো postman-এর letter নেওয়ার সময়। Propagation delay হলো letter-এর রাস্তা দিয়ে যাওয়ার সময়। উদাহরণ — online gaming-এ round-trip delay (ping) 100 ms-এর বেশি হলে noticeable; 200 ms-এর বেশি হলে game unresponsive লাগে।",
      },

      { type: "h3", title: "Jitter" },
      {
        type: "p",
        text: "Jitter হলো packet arrival times-এর variation। High jitter real-time applications (VoIP, video conferencing)-এ সমস্যা তৈরি করে কারণ packets uneven intervals-এ play out হয়। উদাহরণ — একটি VoIP call-এ 50 ms jitter থাকলে jitter buffer প্রয়োজন (যা delay যোগ করে) playback smooth করতে; নাহলে audio choppy হয়ে যায়।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি একটি restaurant-এ order করছেন। কখনো food ৫ মিনিটে আসে, কখনো ২০ মিনিটে। এই variation হলো jitter। যদি food সবসময় ১০ মিনিটে আসত (low jitter), আপনি প্রস্তুত থাকতেন। কিন্তু variation থাকলে আপনি হয়তো আগেই খেয়ে ফেলেছেন বা অনেকক্ষণ wait করছেন।",
      },

      { type: "h3", title: "Bandwidth" },
      {
        type: "p",
        text: "Bandwidth হলো একটি network path-এর maximum data rate (throughput)। সাধারণত bits per second (bps)-এ measured হয়। বিভিন্ন applications-এর বিভিন্ন bandwidth requirements আছে — Email/Web (< 1 Mbps, delay tolerant), Video streaming (3-25 Mbps, stable throughput প্রয়োজন), 4K Video call (15-30 Mbps, jitter sensitive), Large file download (100+ Mbps, শুধু speed গুরুত্বপূর্ণ)।",
      },
      {
        type: "p",
        text: "Real-life thinking — bandwidth হলো একটি highway-এর lanes সংখ্যা। একটি single-lane road-এ (low bandwidth) একসাথে অল্প গাড়ি যেতে পারে। একটি 8-lane highway-তে (high bandwidth) অনেক গাড়ি একসাথে যেতে পারে। QoS হলো কিছু lanes-কে emergency vehicles-এর জন্য reserve করা — তারা সবসময় চলতে পারে, traffic যাই হোক না কেন।",
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Congestion — resources-এর oversubscription থেকে হয়; shaping ও QoS এটি mitigate করতে help করে।",
          "Leaky bucket — constant output rate enforce করে; Token bucket — controlled bursts allow করে।",
          "QoS parameters (delay, jitter, bandwidth) — performance expectations define করে।",
          "Real-time apps — বিশেষত jitter ও delay-এ sensitive।",
          "এই mechanisms modern networks-এ implemented হয় (যেমন DiffServ, traffic policing, RED queue management) — fair ও predictable communication ensure করতে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Congestion control ও QoS বোঝা জরুরি কারণ এগুলো modern networks-এ reliable ও predictable communication ensure করে। পরের chapter-এ আমরা TCP-র 3-way handshake ও তারপর HTTP methods-এ যাব।",
      },
    ],
  }
];
