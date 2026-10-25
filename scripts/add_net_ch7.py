#!/usr/bin/env python3
"""
Add Networking Ch 07 — Application Layer (Maximum Bangla + English terms).
Rename: TCP Ch 07 → Ch 08, HTTP Ch 08 → Ch 09.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 07 → Ch 08, HTTP Ch 08 → Ch 09
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 07 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 08 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 08 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 09 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 07 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH7 = r'''  {
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

'''

new_text = before + NEW_CH7 + after

# Verify
assert 'id: "net-application"' in new_text, "net-application missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 07 (Application Layer) added. File size: {len(new_text)} bytes")
