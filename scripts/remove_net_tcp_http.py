#!/usr/bin/env python3
"""Remove net-tcp and net-http topics from content.ts."""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Find the start of net-tcp topic block (the `  {\n` before `id: "net-tcp"`)
net_tcp_marker = 'id: "net-tcp"'
tcp_idx = text.find(net_tcp_marker)
assert tcp_idx != -1, "net-tcp marker not found"
tcp_start = text.rfind("  {\n", 0, tcp_idx)
assert tcp_start != -1, "Opening brace of net-tcp not found"

# Find the end of net-http topic block (the closing `  },\n` after the last section)
# The OS section starts with "  /* ============== OS ============== */"
os_marker = "  /* ============== OS ============== */"
os_idx = text.find(os_marker, tcp_idx)
assert os_idx != -1, "OS marker not found"

# The text between tcp_start and os_idx contains both topics + whitespace.
# We want to remove everything from tcp_start to os_idx (exclusive).
# But we need to keep a clean separator. Let's check what's between the
# closing of net-http and the OS marker.
between = text[text.rfind("  },\n", 0, os_idx):os_idx]
# This should be "  },\n\n  /* ============== OS ============== */" or similar

# Remove from tcp_start to the line before the OS marker.
# The net-http topic ends with "  },\n" and then there's "\n  /* ============== OS..."
# We want to keep the "\n  /* ============== OS..." part.
# So we remove text[tcp_start : os_idx] and replace with nothing.
# But we need to make sure there's proper spacing.

before = text[:tcp_start]
after = text[os_idx:]

# Insert a clean newline between the previous topic and the OS marker
new_text = before + "\n" + after

# Verify
assert 'id: "net-tcp"' not in new_text, "net-tcp still present"
assert 'id: "net-http"' not in new_text, "net-http still present"
assert 'id: "net-intro"' in new_text, "net-intro missing"
assert 'id: "net-osi"' in new_text, "net-osi missing"
assert 'id: "os-introduction"' in new_text, "os-introduction missing"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Removed net-tcp and net-http. File size: {len(new_text)} bytes")
