"""Entry for make.fun: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "I missed the deadline because my context window evicted it to make room for this apology."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
