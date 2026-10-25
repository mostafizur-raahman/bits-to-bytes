#!/usr/bin/env python3
"""Diagnose escape sequences in content.ts"""
from pathlib import Path

text = Path("/home/z/my-project/src/lib/content.ts").read_text()

# The problematic pattern in the source file is the 4-char string: ' \ n '
# i.e. single-quote, backslash, lowercase n, single-quote
needle = "'" + "\\" + "n" + "'"  # '\n' as 4 chars
count = text.count(needle)
print(f"Found {count} occurrences of literal 4-char pattern '\\n' in source file")

# Show first occurrence with context
idx = text.find(needle)
if idx != -1:
    print("\nFirst occurrence (with 80 chars of context):")
    snippet = text[max(0, idx-80):idx+30]
    print(repr(snippet))

# Also count escaped \\n (which is correct)
correct = "'" + "\\\\" + "n" + "'"  # '\\n' as 5 chars
ccount = text.count(correct)
print(f"\nFound {ccount} occurrences of correctly-escaped pattern '\\\\n' in source file")
