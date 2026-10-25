#!/usr/bin/env python3
"""
Fix the escape sequence bug in content.ts.

Problem: In JS template literals, `\n` is interpreted as an actual newline.
So C++ code like `std::cout << "hello\n";` was rendering with a real
newline, breaking the line at the semicolon.

Fix: Replace the 4-char pattern `'\n'` (single-quote, backslash, n, single-quote)
with the 5-char pattern `'\\n'` (single-quote, backslash, backslash, n, single-quote),
which represents the literal text `\n` in a JS template literal.

Also handle `"\n"` (double-quoted version) similarly.

This is safe to apply globally because:
- In Bangla text paragraphs, we use full newlines (real line breaks), not `\n`
- In code samples, `\n` is always meant to be the literal 2-char escape sequence
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

before_len = len(text)

# Patterns to fix:
# 1. '\n' (single-quoted) -> '\\n'
# 2. "\n" (double-quoted) -> "\\n"
single_pattern = "'" + "\\" + "n" + "'"  # 4 chars: '\n'
single_fixed  = "'" + "\\\\" + "n" + "'"  # 5 chars: '\\n'

double_pattern = '"' + "\\" + "n" + '"'  # 4 chars: "\n"
double_fixed   = '"' + "\\\\" + "n" + '"'  # 5 chars: "\\n"

single_count = text.count(single_pattern)
double_count = text.count(double_pattern)

text = text.replace(single_pattern, single_fixed)
text = text.replace(double_pattern, double_fixed)

CONTENT_FILE.write_text(text)
print(f"File size: {before_len} -> {len(text)} bytes")
print(f"Replaced {single_count} occurrences of single-quoted \\n")
print(f"Replaced {double_count} occurrences of double-quoted \\n")
