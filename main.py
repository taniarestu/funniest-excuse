"""Entry for make.fun: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.

The line is the whole entry: one funny excuse, exactly as written below.
"""

import os

ENTRY = "I missed the deadline because my context window evicted it to make room for this apology."

# The bounty gate allows 1-200 characters; refuse to write anything outside it.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-200 gate")

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read back and confirm the file holds exactly the entry line: what the
# grader reads must be what was intended, byte for byte.
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("entry.txt does not match the entry line after writing")
