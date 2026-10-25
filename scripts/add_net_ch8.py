#!/usr/bin/env python3
"""
Add Networking Ch 08 — Network Security (Maximum Bangla + English terms).
Rename: TCP Ch 08 → Ch 09, HTTP Ch 09 → Ch 10.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Step 1: Rename TCP Ch 08 → Ch 09, HTTP Ch 09 → Ch 10
text = text.replace(
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 08 — TCP 3-Way Handshake",',
    'id: "net-tcp",\n    subject: "net",\n    title: "Ch 09 — TCP 3-Way Handshake",'
)
text = text.replace(
    'id: "net-http",\n    subject: "net",\n    title: "Ch 09 — HTTP Methods & Status",',
    'id: "net-http",\n    subject: "net",\n    title: "Ch 10 — HTTP Methods & Status",'
)

# Step 2: Insert new Ch 08 before net-tcp
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

before = text[:tcp_start]
after = text[tcp_start:]

NEW_CH8 = r'''  {
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

'''

new_text = before + NEW_CH8 + after

# Verify
assert 'id: "net-security"' in new_text, "net-security missing"
assert 'id: "net-tcp"' in new_text, "net-tcp missing"
assert 'id: "net-http"' in new_text, "net-http missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Networking Ch 08 (Network Security) added. File size: {len(new_text)} bytes")
