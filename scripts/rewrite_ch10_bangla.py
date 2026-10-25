#!/usr/bin/env python3
"""
Rewrite Ch 10 (Protection & Security) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch10_marker_start = "// ---- Ch 10 - Protection & Security ----"
ch11_marker_start = "// ---- Ch 11 - Virtualization & Cloud ----"

start_idx = text.find(ch10_marker_start)
assert start_idx != -1, "Ch 10 marker not found"
end_idx = text.find(ch11_marker_start, start_idx)
assert end_idx != -1, "Ch 11 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH10 = r'''// ---- Ch 10 - Protection & Security ----
  {
    id: "os-security",
    subject: "os",
    title: "Ch 10 — Protection & Security",
    bangla: "সুরক্ষা ও নিরাপত্তা",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Security ও protection যেকোনো operating system-এ fundamental। এই chapter-এ security-এর goals, authentication methods, access control models, protection mechanisms, common attacks, ও encryption techniques cover করা হয়েছে যেগুলো data ও resources safeguard করে।",
    sections: [
      { type: "h2", id: "cia", title: "Security Goals: Confidentiality, Integrity, Availability" },
      {
        type: "p",
        text: "CIA triad information security-এর core objectives define করে। তিনটি goal একসাথে থাকা জরুরি — একটি দুর্বল হলে পুরো system দুর্বল হয়ে যায়।",
      },
      { type: "h3", title: "CIA Triad" },
      {
        type: "list",
        items: [
          "Confidentiality — unauthorised access prevent করা information-এ। Failure example: hacker password file steal করে।",
          "Integrity — ensure করা যে data tamper বা permission ছাড়া modify করা হবে না। Failure example: malware system binaries alter করে।",
          "Availability — ensure করা যে systems ও data দরকার হলে accessible। Failure example: Denial-of-service (DoS) attack website-কে unreachable করে দেয়।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি bank vault। Confidentiality — শুধু authorised staff ভেতর দেখতে পারে। Integrity — stored money alter করা যায় না (counterfeiting prevented)। Availability — vault business hours-এ accessible।",
      },

      { type: "h2", id: "authentication", title: "Authentication" },
      {
        type: "p",
        text: "Authentication একটি user বা process-এর identity verify করে। তিনটি common factor আছে — something you know, something you have, ও something you are।",
      },
      { type: "h3", title: "১. Something you know (passwords, PINs)" },
      {
        type: "p",
        text: "Most common, কিন্তু guessing, theft, phishing-এ vulnerable। Password storage-এ modern OSes plaintext-এর বদলে hashed passwords store করে (bcrypt, SHA-256 with salt সহ)। Salt হলো একটি random value যেটা প্রতিটি password-এ যোগ করা হয় hashing-এর আগে rainbow table attacks prevent করতে।",
      },
      {
        type: "multi-code",
        filename: "password_hashing",
        codeSamples: {
          cpp: `#include <iostream>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <string>
#include <vector>

// Generate a random salt, then hash password+salt with SHA-256.
std::vector<unsigned char> hash_password(
    const std::string& pw, std::vector<unsigned char>& salt) {
    salt.resize(16);
    RAND_bytes(salt.data(), 16);

    EVP_MD_CTX* ctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(ctx, EVP_sha256(), nullptr);
    EVP_DigestUpdate(ctx, pw.data(), pw.size());
    EVP_DigestUpdate(ctx, salt.data(), salt.size());

    std::vector<unsigned char> hash(EVP_MAX_MD_SIZE);
    unsigned int len;
    EVP_DigestFinal_ex(ctx, hash.data(), &len);
    hash.resize(len);
    EVP_MD_CTX_free(ctx);
    return hash;
}

int main() {
    std::vector<unsigned char> salt;
    auto hash = hash_password("hunter2", salt);
    std::cout << "Hash length: " << hash.size() << " bytes\\n";
    return 0;
}
// Compile: g++ password.cpp -lcrypto`,
          go: `package main

import (
    "crypto/rand"
    "crypto/sha256"
    "fmt"
)

// Generate a random salt, then hash password+salt with SHA-256.
func hashPassword(pw string) (hash, salt []byte) {
    salt = make([]byte, 16)
    rand.Read(salt)
    h := sha256.New()
    h.Write([]byte(pw))
    h.Write(salt)
    hash = h.Sum(nil)
    return
}

func main() {
    hash, salt := hashPassword("hunter2")
    fmt.Printf("Hash: %x\\nSalt: %x\\n", hash, salt)
}`,
          python: `import hashlib
import os

# Generate a random salt, then hash password+salt with SHA-256.
def hash_password(pw):
    salt = os.urandom(16)
    h = hashlib.sha256()
    h.update(pw.encode())
    h.update(salt)
    return h.digest(), salt

pw_hash, salt = hash_password("hunter2")
print(f"Hash: {pw_hash.hex()}")
print(f"Salt: {salt.hex()}")`,
          java: `import java.security.*;
import java.util.*;

public class PasswordHashing {
    public static void main(String[] args) throws Exception {
        // Generate a random salt
        byte[] salt = new byte[16];
        SecureRandom.getInstanceStrong().nextBytes(salt);

        // Hash password + salt with SHA-256
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update("hunter2".getBytes());
        md.update(salt);
        byte[] hash = md.digest();

        System.out.println("Hash: " + Base64.getEncoder().encodeToString(hash));
        System.out.println("Salt: " + Base64.getEncoder().encodeToString(salt));
    }
}`,
        },
      },
      { type: "h3", title: "২. Something you have (smart card, security token, phone)" },
      {
        type: "p",
        text: "একটি second factor যোগ করে; সাধারণত password-এর সাথে combine করা হয় (two-factor authentication – 2FA)। Hardware tokens — YubiKey, RSA SecurID। Software tokens — TOTP (Google Authenticator) – time-based one-time password।",
      },
      { type: "h3", title: "৩. Something you are (biometrics)" },
      {
        type: "p",
        text: "Fingerprint, iris scan, face recognition, voice। Pros — hard to forge, convenient। Cons — compromised হলে change করা যায় না; false positives/negatives হতে পারে।",
      },
      { type: "h3", title: "Multi-factor Authentication (MFA)" },
      {
        type: "p",
        text: "দুটি বা ততোধিক factors combine করে। যেমন password (knowledge) + SMS code (possession)। Security greatly increase করে। Real-life thinking — একটি secure building-এ প্রবেশ করা। Password = door-এ keycode। Security token = keycard। Biometric = fingerprint scanner। MFA = keycard + PIN।",
      },

      { type: "h2", id: "access-control", title: "Access Control" },
      {
        type: "p",
        text: "Authenticate হওয়ার পর, OS decide করতে হবে একটি user কোন resources access করতে পারবে এবং কোন operations allowed। তিনটি classic model আছে।",
      },
      { type: "h3", title: "DAC (Discretionary Access Control)" },
      {
        type: "p",
        text: "একটি resource-এর owner decide করে কে access করতে পারবে। General-purpose OSes-এ common (Unix permissions, Windows ACLs)। Unix permissions — read, write, execute for owner, group, others। Problem — users accidentally excessive permissions grant করতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — আপনি একটি house own করছেন; আপনি friends কে keys দেন যেমন চান।",
      },
      { type: "h3", title: "MAC (Mandatory Access Control)" },
      {
        type: "p",
        text: "System (OS) একটি global policy enforce করে যা users override করতে পারে না। High-security environments-এ use হয় (military, SELinux, AppArmor)। Labels — প্রতিটি resource ও user-এর একটি security label আছে (যেমন 'Top Secret', 'Secret', 'Unclassified')। Rules — একজন user একটি resource access করতে পারবে শুধু যদি তার clearance resource-এর label-কে dominate করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — Military document classification — একজন 'Secret' clearance holder 'Top Secret' documents read করতে পারবে না, তার ইচ্ছা যাই হোক না কেন।",
      },
      { type: "h3", title: "RBAC (Role-Based Access Control)" },
      {
        type: "p",
        text: "Permissions roles-এ assign করা হয়, এবং users roles-এ assign করা হয়। Roles job functions reflect করে (যেমন 'Doctor', 'Nurse', 'Accountant')। Advantage — administration simplify করে; per-user এর বদলে role permissions change করুন। Examples — database systems, enterprise applications, Windows groups।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hospital — doctors-এর prescription rights আছে; nurses-এর patient care rights আছে; receptionists শুধু appointments schedule করতে পারে। Users roles-এ assign করা হয়।",
      },

      { type: "h2", id: "matrix", title: "Protection Mechanisms: Capabilities ও Access Matrix" },
      {
        type: "p",
        text: "OS-এর internal structures প্রয়োজন access control enforce করতে।",
      },
      { type: "h3", title: "Access Matrix" },
      {
        type: "p",
        text: "একটি conceptual table যেখানে rows subjects (users, processes) represent করে এবং columns objects (files, devices) represent করে। প্রতিটি cell allowed operations (read, write, execute, delete) ধারণ করে।",
      },
      {
        type: "p",
        text: "Implementation — Access Control Lists (ACLs): প্রতিটি object-এর সাথে একটি list attach করো (matrix-এর column)। Windows NTFS, POSIX ACLs। Capabilities: প্রতিটি subject-এর সাথে একটি list attach করো (matrix-এর row)। প্রতিটি capability একটি unforgeable token যেটা একটি নির্দিষ্ট object-এ নির্দিষ্ট rights সহ access grant করে।",
      },
      {
        type: "multi-code",
        filename: "acl_capability",
        codeSamples: {
          cpp: `#include <iostream>
#include <unordered_map>
#include <string>

enum class Perm { NONE = 0, READ = 1, WRITE = 2, EXEC = 4 };

inline Perm operator|(Perm a, Perm b) {
    return static_cast<Perm>(static_cast<int>(a) | static_cast<int>(b));
}
inline bool has(Perm s, Perm p) {
    return (static_cast<int>(s) & static_cast<int>(p)) != 0;
}

// ACL: file -> user -> permission
std::unordered_map<std::string,
    std::unordered_map<std::string, Perm>> acl = {
    {"secret.txt", { {"alice", Perm::READ | Perm::WRITE},
                      {"bob",   Perm::READ} }},
};

bool check_acl(const std::string& file,
               const std::string& user, Perm need) {
    auto it = acl.find(file);
    if (it == acl.end()) return false;
    auto& fileAcl = it->second;
    auto u = fileAcl.find(user);
    if (u == fileAcl.end()) return false;
    return has(u->second, need);
}

int main() {
    std::cout << "alice read:  " << check_acl("secret.txt", "alice", Perm::READ)  << '\\n';
    std::cout << "alice write: " << check_acl("secret.txt", "alice", Perm::WRITE) << '\\n';
    std::cout << "alice exec:  " << check_acl("secret.txt", "alice", Perm::EXEC)  << '\\n';
    std::cout << "bob write:   " << check_acl("secret.txt", "bob",   Perm::WRITE) << '\\n';
}`,
          go: `package main

import "fmt"

type Perm int

const (
    Read Perm = 1 << iota
    Write
    Exec
)

func (p Perm) Has(bit Perm) bool { return p&bit != 0 }

// ACL: file -> user -> permission
var acl = map[string]map[string]Perm{
    "secret.txt": {
        "alice": Read | Write,
        "bob":   Read,
    },
}

func checkACL(file, user string, need Perm) bool {
    fileAcl, ok := acl[file]
    if !ok { return false }
    p, ok := fileAcl[user]
    return ok && p.Has(need)
}

func main() {
    fmt.Println("alice read: ", checkACL("secret.txt", "alice", Read))
    fmt.Println("alice write:", checkACL("secret.txt", "alice", Write))
    fmt.Println("alice exec: ", checkACL("secret.txt", "alice", Exec))
    fmt.Println("bob write:  ", checkACL("secret.txt", "bob",   Write))
}`,
          python: `from enum import Flag, auto

class Perm(Flag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    EXEC = auto()

# ACL: file -> user -> permission
acl = {
    "secret.txt": {
        "alice": Perm.READ | Perm.WRITE,
        "bob":   Perm.READ,
    },
}

def check_acl(file, user, need):
    file_acl = acl.get(file, {})
    p = file_acl.get(user)
    if p is None:
        return False
    return bool(p & need)

print("alice read: ", check_acl("secret.txt", "alice", Perm.READ))
print("alice write:", check_acl("secret.txt", "alice", Perm.WRITE))
print("alice exec: ", check_acl("secret.txt", "alice", Perm.EXEC))
print("bob write:  ", check_acl("secret.txt", "bob",   Perm.WRITE))`,
          java: `import java.util.*;

public class ACL {
    enum Perm { NONE, READ, WRITE, EXEC }
    static class PermSet {
        final Set<Perm> perms;
        PermSet(Perm... ps) {
            perms = EnumSet.noneOf(Perm.class);
            for (Perm p : ps) if (p != Perm.NONE) perms.add(p);
        }
        boolean has(Perm p) { return perms.contains(p); }
    }

    // ACL: file -> user -> permission set
    static Map<String, Map<String, PermSet>> acl = Map.of(
        "secret.txt", Map.of(
            "alice", new PermSet(Perm.READ, Perm.WRITE),
            "bob",   new PermSet(Perm.READ)
        )
    );

    static boolean checkACL(String file, String user, Perm need) {
        Map<String, PermSet> fileAcl = acl.get(file);
        if (fileAcl == null) return false;
        PermSet p = fileAcl.get(user);
        return p != null && p.has(need);
    }

    public static void main(String[] args) {
        System.out.println("alice read:  " + checkACL("secret.txt", "alice", Perm.READ));
        System.out.println("alice write: " + checkACL("secret.txt", "alice", Perm.WRITE));
        System.out.println("alice exec:  " + checkACL("secret.txt", "alice", Perm.EXEC));
        System.out.println("bob write:   " + checkACL("secret.txt", "bob",   Perm.WRITE));
    }
}`,
        },
      },
      { type: "h3", title: "Capability" },
      {
        type: "p",
        text: "Capability হলো একটি ticket যেটা একটি process-কে permission দেয় একটি object-এ নির্দিষ্ট operations perform করার জন্য। প্রায়ই একটি protected, kernel-managed reference হিসেবে implement করা হয়। Advantage — easy to delegate; fine-grained। Disadvantage — capabilities revoke করা complex হতে পারে। Examples — early research OS (Hydra, KeyKOS), কিছু microkernels (seL4)।",
      },
      {
        type: "p",
        text: "Real-life thinking — ACL হলো একটি club-এ bouncer-এর list — প্রতিটি club-এর নিজস্ব allowed guests list। Capability হলো একটি wristband — আপনি এটি show করেন প্রবেশ করতে; বিভিন্ন colors বিভিন্ন access দেয়।",
      },

      { type: "h2", id: "least-privilege", title: "Principle of Least Privilege" },
      {
        type: "p",
        text: "Principle of least privilege বলে যে একটি process (বা user)-কে শুধু ততটুকু privilege grant করা উচিত যতটুকু তার task perform করার জন্য প্রয়োজন, এবং শুধু ততটুকু সময়ের জন্য যতটুকু দরকার।",
      },
      {
        type: "p",
        text: "Benefit — bugs বা attacks থেকে damage limit করে। Examples — Unix setuid programs initial setup-এর পর privileges drop করে। Web browsers tabs-কে sandboxes-এ চালায় limited file access সহ। Linux capabilities: root privileges-কে ছোট pieces-এ ভাগ করে (CAP_NET_ADMIN, CAP_SYS_ADMIN)।",
      },
      {
        type: "p",
        text: "Real-life thinking — একজন hotel valet — তারা আপনার car park করতে পারে কিন্তু আপনার room safe খুলতে পারবে না।",
      },

      { type: "h2", id: "malware", title: "Malicious Software (Malware)" },
      {
        type: "p",
        text: "Malware হলো এমন software যেটা harm বা infiltrate করার জন্য design করা। বিভিন্ন প্রকার আছে।",
      },
      {
        type: "list",
        items: [
          "Virus — legitimate programs-এ attach হয়; user action প্রয়োজন (infected program run করা)। File infection-এ propagate হয়। Payload: corruption, theft, backdoor।",
          "Worm — networks-এ user action ছাড়া self-replicate করে। Network exploits, emails-এ propagate হয়। Payload: resource exhaustion, backdoor।",
          "Trojan — legitimate software হিসেবে disguised; self-replicate করে না। Social engineering-এ propagate হয়। Payload: data theft, ransomware।",
          "Rootkit — OS থেকে তার presence (files, processes, network connections) hide করে। Initial compromise-এর পর install হয়। Payload: stealth, persistent backdoor।",
          "Ransomware — user files encrypt করে এবং payment demand করে। Trojan, worm, exploit-এ propagate হয়। Payload: file encryption।",
          "Spyware — secretly user information collect করে। Freeware-এর সাথে bundled হয়। Payload: keylogging, browsing data।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Virus হলো একটি contagious disease touch দ্বারা spread হয়। Worm হলো একটি airborne pathogen যেটা ventilation systems-এর মাধ্যমে নিজে ছড়ায়। Trojan হলো একটি delivery box 'gift' label করা যেটার ভেতরে bomb। Rootkit হলো একজন spy যে security camera footage delete করতে পারে যাতে আপনি জানতেই না সে ছিল।",
      },

      { type: "h2", id: "buffer-overflow", title: "Buffer Overflow Attacks ও Defenses" },
      {
        type: "p",
        text: "Buffer overflow তখন হয় যখন একটি program allocated buffer bounds-এর বাইরে data write করে, adjacent memory overwrite করে। Attackers এটিকে exploit করে malicious code inject করতে বা execution flow change করতে।",
      },
      { type: "h3", title: "Classic stack overflow" },
      {
        type: "code",
        lang: "c",
        text: `void vulnerable(char *str) {
    char buffer[64];
    strcpy(buffer, str);   // no bounds check
}`,
      },
      {
        type: "p",
        text: "str যদি 64 bytes-এর বেশি হয়, সেটা stack-এ return address overwrite করে। একজন attacker এমন input craft করে যেটা attacker code (shellcode) place করে এবং return address-কে সেটি point করতে set করে।",
      },
      { type: "h3", title: "Defenses" },
      {
        type: "list",
        items: [
          "Non-executable stack (NX bit) — stack memory কে non-executable mark করো। Shellcode execution prevent করে। Bypass হয় return-to-libc বা ROP দিয়ে।",
          "Address Space Layout Randomization (ASLR) — stack, heap, libraries-এর base addresses randomise করো। Attacker return address location জানতে পারবে না। Effective; 32-bit-এ brute-force possible।",
          "Stack canaries — return address-এর আগে একটি secret value (canary) place করো। Overflow এটি overwrite করলে program abort হয়। Very effective; GCC দ্বারা use হয় (-fstack-protector)।",
          "Bounds checking — compile-time বা runtime checks (যেমন Rust, Safe C extensions)। Most thorough, কিন্তু performance cost।",
          "Control Flow Integrity (CFI) — program jumps-কে একটি precomputed set of valid targets-এ restrict করো। Emerging standard (যেমন Intel CET)।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি hotel keycard system। Buffers হলো mail slots-এর মতো — যদি আপনি একটি লম্বা package shove করেন, এটা room door push করে open করতে পারে। Defenses হলো slot-কে খুব narrow করা (little canary) বা key যে door open করে সেটা randomise করা (ASLR)।",
      },
      {
        type: "callout",
        calloutTone: "warn",
        text: "Warning: একটি single defense পর্যাপ্ত না। Modern systems defense-in-depth use করে — NX + ASLR + stack canaries একসাথে। তবুও ROP (Return-Oriented Programming) এর মতো advanced attacks থেকে যায়।",
      },

      { type: "h2", id: "encryption", title: "Encryption Basics for OS Security" },
      {
        type: "p",
        text: "Encryption data transform করে unauthorised reading prevent করতে। Modern OSes encryption use করে data at rest (disk) ও in transit (network) protect করতে।",
      },
      { type: "h3", title: "Symmetric Encryption" },
      {
        type: "p",
        text: "একই key encrypt ও decrypt করে। Algorithms — AES (Advanced Encryption Standard), ChaCha20। Use — full-disk encryption (FDE), file encryption, network session encryption (TLS)। একই key দুই পক্ষ share করে, তাই key distribution একটি সমস্যা।",
      },
      { type: "h3", title: "Asymmetric Encryption (Public Key)" },
      {
        type: "p",
        text: "দুটি keys — public key (encrypt করে), private key (decrypt করে)। Public থেকে private derive করা infeasible। Algorithms — RSA, ECC (Elliptic Curve Cryptography)। Use — key exchange, digital signatures, authentication।",
      },
      { type: "h3", title: "Full-Disk Encryption (FDE)" },
      {
        type: "p",
        text: "Entire storage device encrypt করে (boot block ছাড়া)। OS on-the-fly decrypt করে একটি key দিয়ে যেটা passphrase, TPM (Trusted Platform Module), বা USB token থেকে derive হয়।",
      },
      {
        type: "list",
        items: [
          "Examples — Windows BitLocker, macOS FileVault, Linux LUKS (dm-crypt)।",
          "Threat model — device-এর physical theft থেকে protect করে; compromised running system থেকে protect করে না।",
        ],
      },
      { type: "h3", title: "How LUKS works (simplified)" },
      {
        type: "list",
        items: [
          "১. User passphrase enter করে।",
          "২. Passphrase LUKS header-এ stored master key-কে decrypt করে।",
          "৩. Master key disk blocks-কে on-the-fly decrypt করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি safe (encrypted disk) যার combination lock (passphrase) আছে। একজন thief safe steal করলেও combination ছাড়া ভেতরের documents read করতে পারবে না।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Security goals — Confidentiality, Integrity, Availability (CIA triad)।",
          "Authentication — something you know (password), have (token), are (biometric); MFA factors combine করে।",
          "Access control — DAC (owner decide করে), MAC (system decide করে), RBAC (roles)।",
          "Protection mechanisms — Access matrix; ACLs (per object) বা capabilities (per subject) হিসেবে implement করা।",
          "Least privilege — minimal rights minimal time-এর জন্য grant করো damage limit করতে।",
          "Malware types — viruses (attach), worms (self-spread), trojans (disguised), rootkits (hide), ransomware (encrypt)।",
          "Buffer overflow defenses — NX bit, ASLR, stack canaries, bounds checking, CFI।",
          "Encryption for OS — Full-disk encryption (BitLocker, FileVault, LUKS) physical theft থেকে protect করে।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Security একটি product না, একটি continuous process। OS-level mechanisms বোঝা trustworthy systems build ও maintain করার প্রথম ধাপ।",
      },
    ],
  },

'''

new_text = before + NEW_CH10 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 10 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
