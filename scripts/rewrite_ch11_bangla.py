#!/usr/bin/env python3
"""
Rewrite Ch 11 (Virtualization & Cloud) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch11_marker_start = "// ---- Ch 11 - Virtualization & Cloud ----"
ch12_marker_start = "// ---- Ch 12 - Distributed OS ----"

start_idx = text.find(ch11_marker_start)
assert start_idx != -1, "Ch 11 marker not found"
end_idx = text.find(ch12_marker_start, start_idx)
assert end_idx != -1, "Ch 12 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH11 = r'''// ---- Ch 11 - Virtualization & Cloud ----
  {
    id: "os-virt",
    subject: "os",
    title: "Ch 11 — Virtualization & Cloud",
    bangla: "ভার্চুয়ালাইজেশন ও ক্লাউড",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Virtualization software-কে underlying hardware থেকে decouple করে, যাতে একাধিক operating systems একটি single physical machine-এ চলতে পারে। Cloud computing virtualization-এর উপর built হয়ে computing resources-কে on-demand services হিসেবে deliver করে। এই chapter-এ hypervisors, containers, cloud models, ও তাদের trade-offs ব্যাখ্যা করা হয়েছে।",
    sections: [
      { type: "h2", id: "vm-hypervisors", title: "Virtual Machine Concepts: Hypervisors" },
      {
        type: "p",
        text: "Virtual machine (VM) হলো একটি physical computer-এর software implementation যেটা একটি operating system ও applications run করে। Hypervisor (বা virtual machine monitor, VMM) হলো সেই software layer যেটা VMs create ও manage করে।",
      },
      { type: "h3", title: "Type 1 Hypervisor (Bare-Metal)" },
      {
        type: "p",
        text: "সরাসরি physical hardware-এ চালে কোনো host OS ছাড়া। Hardware resources-এ direct access আছে। Examples — VMware ESXi, Microsoft Hyper-V, KVM (Linux kernel-based), Xen। Pros — high performance, low overhead, better security। Cons — সব devices-এর জন্য hardware drivers প্রয়োজন; বেশি complex management।",
      },
      { type: "h3", title: "Type 2 Hypervisor (Hosted)" },
      {
        type: "p",
        text: "একটি host operating system-এর উপরে application হিসেবে চালে। Host OS physical hardware manage করে। Examples — Oracle VirtualBox, VMware Workstation, QEMU (KVM acceleration ছাড়া)। Pros — install করা সহজ, development ও testing-এর জন্য ভালো। Cons — বেশি overhead (calls host OS দিয়ে যায়), lower performance।",
      },
      {
        type: "p",
        text: "Real-life thinking — Type 1 হলো একটি high-rise apartment building যেখানে property manager on-site থাকেন (hypervisor directly elevators, electricity control করে)। Type 2 হলো একটি rental agency যেটা একটি বড় office building-এর ভেতরে চলে — আপনি একটি room rent করেন, কিন্তু building-এর নিজস্ব facilities manager (host OS) infrastructure control করে।",
      },

      { type: "h2", id: "virt-vs-emulation", title: "Virtualization vs Emulation" },
      {
        type: "p",
        text: "Virtualization-এ guest ও host-এর একই instruction set architecture (ISA) থাকা জরুরি — তাহলে guest instructions directly CPU-তে run হয়। Emulation যেকোনো architecture-এর software run করতে পারে প্রতিটি instruction interpret বা translate করে।",
      },
      { type: "h3", title: "Virtualization vs Emulation — Comparison" },
      {
        type: "list",
        items: [
          "Guest instructions — Virtualization: directly CPU-তে run করে (যদি same architecture হয়); Emulation: software-এ simulate করা হয়।",
          "Performance — Virtualization: near-native (hardware support সহ); Emulation: খুব slow (10-100× slowdown)।",
          "Guest OS modification — Virtualization: প্রয়োজন নেই (full virtualization) বা minimal (para-virtualization); Emulation: কিছু প্রয়োজন নেই।",
          "Use case — Virtualization: x86 Windows-এ x86 Linux run করা; Emulation: x86-এ ARM software run করা, retro-gaming।",
        ],
      },
      {
        type: "p",
        text: "Example — QEMU একটি ARM CPU কে x86 host-এ emulate করতে পারে (emulation)। QEMU + KVM একটি x86 guest কে x86 host-এ virtualize করতে পারে (virtualization)। Real-life thinking — Virtualization হলো একটি movie theatre যেখানে films তাদের native format-এ দেখানো হয় (digital projector digital files play করে)। Emulation হলো একজন translator যে একটি French script কে English-এ aloud পড়ে — প্রতিটি word process হয়।",
      },

      { type: "h2", id: "para-vs-hw-assisted", title: "Para-Virtualization ও Hardware-Assisted Virtualization" },
      { type: "h3", title: "Para-Virtualization" },
      {
        type: "p",
        text: "Guest OS-কে modify করা হয় যাতে সে hypervisor সম্পর্কে aware হয়। Privileged instructions trap করার বদলে (যেটা emulate করা slow), guest explicit hypercalls hypervisor-এ করে। Pros — high performance (trapping overhead reduce করে)। Cons — guest OS modify করা প্রয়োজন (Windows-এর জন্য possible না)। Example — Xen-এর early approach (paravirtualized Linux, NetBSD)।",
      },
      { type: "h3", title: "Hardware-Assisted Virtualization" },
      {
        type: "p",
        text: "Modern CPUs (Intel VT-x, AMD-V) virtualization-এর জন্য hardware support যোগ করে — নতুন CPU modes (VMX root for hypervisor, VMX non-root for guest)। Extended Page Tables (EPT) / Nested Page Tables (NPT) — hardware-assisted virtual memory translation (shadow page table overhead reduce করে)। VMCS (Virtual Machine Control Structure) — guest state, exit reasons store করে।",
      },
      {
        type: "list",
        items: [
          "Benefits — Full virtualization guest modification ছাড়া। Near-native performance। Simpler hypervisor implementation।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Para-virtualization হলো একজন foreign tourist যে কয়েকটি local customs learn করে (modified OS) যাতে airport security দ্রুত pass করতে পারে। Hardware-assisted হলো immigration-এ একটি express lane যেটাতে automated passport scanners (CPU support) আছে — সবাই special training ছাড়া use করতে পারে।",
      },

      { type: "h2", id: "containers-vs-vms", title: "Containers vs Virtual Machines" },
      {
        type: "p",
        text: "Containers (যেমন Docker, LXC, Podman) OS level-এ virtualize করে, hardware level-এ না। তারা host kernel share করে কিন্তু processes কে namespaces-এ isolate করে।",
      },
      { type: "h3", title: "Containers vs VMs — Comparison" },
      {
        type: "list",
        items: [
          "Isolation — VM: strong (separate kernels); Container: moderate (shared kernel, namespaced)।",
          "Startup time — VM: seconds থেকে minutes (OS boot); Container: milliseconds (শুধু process start)।",
          "Disk footprint — VM: GBs (full OS + apps); Container: MBs (app + dependencies)।",
          "Performance overhead — VM: small (Type 1) বা moderate (Type 2); Container: very low (near-native)।",
          "Kernel — VM: প্রতিটি VM-এর নিজস্ব kernel; Container: সব containers host kernel share করে।",
          "Guest OS — VM: যেকোনো OS (Linux, Windows, BSD); Container: host kernel-এর সাথে match করতে হবে।",
        ],
      },
      { type: "h3", title: "Container primitives (Linux)" },
      {
        type: "list",
        items: [
          "Namespaces — views isolate করে (PID, network, mount, UTS, IPC, user)।",
          "Cgroups (control groups) — resource usage limit করে (CPU, memory, disk I/O)।",
          "Union filesystems (OverlayFS, AUFS) — efficient, layered images।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Virtual machines হলো detached houses — প্রতিটির নিজস্ব plumbing, electricity, foundation। খুব isolated কিন্তু expensive ও build করতে slow। Containers হলো একই building-এর apartments — central heating, water, elevator (host kernel) share করে, কিন্তু আলাদা doors (namespaces) ও rent control (cgroups) আছে।",
      },
      {
        type: "multi-code",
        filename: "pid_namespace",
        codeSamples: {
          cpp: `#include <iostream>
#include <sched.h>
#include <sys/wait.h>
#include <unistd.h>

// Run a child in a NEW PID namespace (Linux only, needs CAP_SYS_ADMIN).
// The child becomes PID 1 inside its own namespace.
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        // Child: try to enter a new PID + mount namespace
        if (unshare(CLONE_NEWPID | CLONE_NEWNS) == -1) {
            perror("unshare failed");
            _exit(1);
        }
        // After unshare, re-exec ourselves — now PID 1 in new ns
        execl("/bin/echo", "echo", "I am isolated", nullptr);
        _exit(1);
    } else {
        int status;
        waitpid(pid, &status, 0);
        std::cout << "child status=" << status << '\\n';
    }
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "os/exec"
    "syscall"
)

func main() {
    cmd := exec.Command("/bin/echo", "I am isolated")
    // Ask kernel for a new PID + mount namespace for this child
    cmd.SysProcAttr = &syscall.SysProcAttr{
        Cloneflags: syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
    }
    out, err := cmd.Output()
    if err != nil {
        fmt.Println("err:", err)
        return
    }
    fmt.Println(string(out))
}`,
          python: `import subprocess

# Linux only — child gets its own PID + mount namespace.
# Requires root or CAP_SYS_ADMIN.
proc = subprocess.Popen(
    ["/bin/echo", "I am isolated"],
    stdout=subprocess.PIPE,
    start_new_session=True,  # new session, but not a full namespace
)
out, _ = proc.communicate()
print(out.decode(), end="")`,
          java: `// Java standard library doesn't expose namespace flags.
// Real containers are launched via the Docker / containerd API.
import java.io.*;

public class PidNamespace {
    public static void main(String[] args) throws Exception {
        ProcessBuilder pb = new ProcessBuilder(
            "docker", "run", "--rm", "--pid=host",
            "alpine:3", "echo", "I am isolated");
        pb.inheritIO();
        Process p = pb.start();
        System.out.println("exit=" + p.waitFor());
    }
}`,
        },
      },

      { type: "h2", id: "cloud-models", title: "Cloud Computing Models" },
      {
        type: "p",
        text: "Cloud computing internet-এর মাধ্যমে computing resources deliver করে pay-per-use basis-এ। তিনটি main service model আছে।",
      },
      { type: "h3", title: "IaaS (Infrastructure as a Service)" },
      {
        type: "p",
        text: "Virtual machines, storage, networks, ও অন্যান্য fundamental computing resources provide করে। আপনি OS, applications, ও middleware control করেন। Examples — AWS EC2, Google Compute Engine, Microsoft Azure VMs। Customer responsibility — OS patches, security, application data।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি plot of land rent করা — আপনি যা খুশি build করেন।",
      },
      { type: "h3", title: "PaaS (Platform as a Service)" },
      {
        type: "p",
        text: "একটি platform provide করে যেখানে আপনি applications deploy করেন underlying infrastructure (OS, runtime, middleware, databases) manage না করে। Examples — AWS Elastic Beanstalk, Google App Engine, Heroku। Customer responsibility — application code ও data।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি fully equipped kitchen rent করা — আপনি শুধু ingredients আনেন এবং cook করেন।",
      },
      { type: "h3", title: "SaaS (Software as a Service)" },
      {
        type: "p",
        text: "Internet-এর মাধ্যমে ready-to-use applications provide করে। কোনো installation নেই, infrastructure বা platform manage করা নেই। Examples — Google Workspace (Gmail, Docs), Salesforce, Microsoft 365। Customer responsibility — শুধু user data ও configuration।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restaurant-এ খাওয়া — আপনি শুধু order করেন এবং consume করেন।",
      },
      { type: "h3", title: "Deployment models" },
      {
        type: "list",
        items: [
          "Public cloud — internet-এর উপর shared infrastructure।",
          "Private cloud — একটি organization-এর জন্য dedicated infrastructure।",
          "Hybrid cloud — public ও private clouds combined।",
          "Multi-cloud — একাধিক public cloud providers use করা।",
        ],
      },

      { type: "h2", id: "challenges", title: "Challenges: Isolation, Performance, Security" },
      { type: "h3", title: "Isolation" },
      {
        type: "p",
        text: "VMs strong isolation provide করে (separate kernels)। তবে side-channel attacks (যেমন Spectre, Meltdown) একই physical host-এর VMs-এর মধ্যে information leak করতে পারে।",
      },
      {
        type: "p",
        text: "Containers host kernel share করে। একটি kernel bug বা container escape অন্য containers-কে compromise করতে পারে। Mitigations — seccomp, SELinux, AppArmor, user namespaces, gVisor (sandboxed container runtime)। Real-life thinking — Apartment walls (containers) এর sound isolation separate houses (VMs) এর চেয়ে কম। একটি apartment-এ loud party প্রতিবেশীদের বিরক্ত করে।",
      },
      {
        type: "multi-code",
        filename: "cgroup_limit",
        codeSamples: {
          cpp: `#include <iostream>
#include <fstream>

// Set a memory limit (1 MB) on the current process via cgroups v2.
// Needs root or delegation. Path may vary by distro.
int main() {
    const std::string path =
        "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max";
    std::ofstream f(path);
    if (!f) {
        std::cerr << "Cannot open " << path << '\\n';
        return 1;
    }
    f << "1048576";   // 1 MB limit
    std::cout << "Memory limit set to 1 MB\\n";
    return 0;
}`,
          go: `package main

import "os"

// Set a memory limit (1 MB) on the current process via cgroups v2.
func main() {
    path := "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max"
    err := os.WriteFile(path, []byte("1048576"), 0644)
    if err != nil {
        println("err:", err.Error())
        return
    }
    println("Memory limit set to 1 MB")
}`,
          python: `# Set a memory limit (1 MB) on the current process via cgroups v2.
# Needs root or delegation. Path may vary by distro.
path = "/sys/fs/cgroup/user.slice/user-1000.slice/memory.max"
try:
    with open(path, "w") as f:
        f.write("1048576")   # 1 MB limit
    print("Memory limit set to 1 MB")
except PermissionError as e:
    print("err:", e)`,
          java: `import java.nio.file.*;

// Set a memory limit (1 MB) on the current process via cgroups v2.
public class CgroupLimit {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("/sys/fs/cgroup/user.slice/user-1000.slice/memory.max");
        Files.writeString(p, "1048576");
        System.out.println("Memory limit set to 1 MB");
    }
}`,
        },
      },
      { type: "h3", title: "Performance" },
      {
        type: "list",
        items: [
          "CPU (native) — VMs: ~0-5% (hardware assist সহ); Containers: ~0-1%।",
          "Memory — VMs: fixed per VM (static); Containers: dynamic, copy-on-write।",
          "I/O (disk, network) — VMs: higher (double-buffering); Containers: near-native।",
          "Boot time — VMs: long (OS boot); Containers: instant (process start)।",
        ],
      },
      {
        type: "p",
        text: "Considerations — VMs: mixed-trust workloads, legacy apps, different OSes-এর জন্য ভালো। Containers: microservices, CI/CD, high density-র জন্য ভালো।",
      },
      { type: "h3", title: "Security" },
      {
        type: "p",
        text: "Shared risks (VMs ও containers উভয়ের জন্য) — hypervisor বা kernel vulnerabilities। Misconfigured networking (exposed ports)। Insecure images বা base OS।",
      },
      {
        type: "list",
        items: [
          "VM-specific — hypervisor attacks (VM escape), resource exhaustion (fork bombs অন্যদের affect করে)।",
          "Container-specific — container থেকে host-এ privilege escalation, environment variables-এর মাধ্যমে secret leakage, image supply chain attacks (malicious layers)।",
        ],
      },
      { type: "h3", title: "Best practices" },
      {
        type: "list",
        items: [
          "Hypervisor/host kernel patched রাখো।",
          "Minimal base images use করো (Alpine, Distroless)।",
          "Containers কে non-root হিসেবে run করো, read-only root filesystems সহ।",
          "Secure secrets management use করো (HashiCorp Vault, Kubernetes secrets)।",
          "Micro-segmentation-এর জন্য network policies।",
        ],
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Hypervisor Type 1 — bare-metal, সরাসরি hardware-এ চালে (ESXi, KVM, Hyper-V)।",
          "Hypervisor Type 2 — host OS-এ app হিসেবে চালে (VirtualBox, Workstation)।",
          "Virtualization vs emulation — Virtualization: same ISA, near-native; Emulation: different ISA, slow।",
          "Para-virtualization — guest hypercalls use করতে modify করা; বেশি efficient (Xen)।",
          "Hardware-assisted virt — CPU extensions (VT-x, AMD-V) hypervisors simplify করে এবং performance improve করে।",
          "Containers — OS-level virtualization, host kernel share করে, lightweight (Docker, LXC)।",
          "VMs vs containers — VMs: strong isolation, slower; containers: fast, dense, shared kernel risk।",
          "Cloud IaaS — Infrastructure – VMs, storage, networks (AWS EC2)।",
          "Cloud PaaS — Platform – OS manage না করে apps deploy করা (Heroku, App Engine)।",
          "Cloud SaaS — Software – ready-to-use apps (Gmail, Office 365)।",
          "Challenges — Isolation (side-channel, container escape), performance trade-offs, security hardening।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Virtualization ও cloud computing software build ও deploy করার পদ্ধতিকে transform করেছে। এই concepts বোঝা traditional OS knowledge-কে modern DevOps practices-এর সাথে bridge করে।",
      },
    ],
  },

'''

new_text = before + NEW_CH11 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 11 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
