#!/usr/bin/env python3
"""
Add Networking Ch 04 — Data Link Layer (Maximum Bangla + English terms).
Rename: TCP Ch 04 → Ch 05, HTTP Ch 05 → Ch 06.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 04 → Ch 05, HTTP Ch 05 → Ch 06
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 04 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 05 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 05 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 06 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 04 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH4 = r'''  {
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

'''

new_text = before + NEW_CH4 + after

# Verify
assert 'id: "net-data-link"' in new_text, "net-data-link missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'id: "net-physical"' in new_text, "net-physical missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 04 (Data Link Layer) added. File size: {len(new_text)} bytes")
