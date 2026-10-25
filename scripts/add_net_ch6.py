#!/usr/bin/env python3
"""
Add Networking Ch 06 — Transport Layer (Maximum Bangla + English terms).
Rename: TCP Ch 06 → Ch 07, HTTP Ch 07 → Ch 08.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 06 → Ch 07, HTTP Ch 07 → Ch 08
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 06 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 07 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 07 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 08 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 06 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH6 = r'''  {
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

'''

new_text = before + NEW_CH6 + after

# Verify
assert 'id: "net-transport"' in new_text, "net-transport missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 06 (Transport Layer) added. File size: {len(new_text)} bytes")
