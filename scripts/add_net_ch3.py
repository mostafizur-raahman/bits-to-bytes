#!/usr/bin/env python3
"""
Add Networking Ch 03 — Physical Layer (Maximum Bangla + English terms).
Also rename existing Ch 03 (TCP) → Ch 04, and Ch 04 (HTTP) → Ch 05.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename existing chapters first (Ch 03 → Ch 04, Ch 04 → Ch 05)
# We rename TCP first, then HTTP, since HTTP rename doesn't affect TCP.
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 03 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 04 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 04 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 05 — HTTP Methods & Status",'
)

# Step 2: Find net-tcp marker (which is now Ch 04), insert net-physical before it
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"

# Walk back to find the opening `  {` of net-tcp topic
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH3 = r'''  {
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

'''

new_text = before + NEW_CH3 + after

# Verify
assert 'id: "net-physical"' in new_text, "net-physical missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'id: "net-intro"' in new_text, "net-intro missing"
assert 'id: "net-osi"' in new_text, "net-osi missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 03 (Physical Layer) added. File size: {len(new_text)} bytes")
