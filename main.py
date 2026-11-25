import os
import sys

ENTRY = "I finally wrote the bug report I used to hate receiving: three steps, one screenshot, and an admission that I caused it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    written = f.read()

if written != ENTRY:
    print("ERROR: entry.txt does not match ENTRY exactly", file=sys.stderr)
    sys.exit(1)
if not 1 <= len(written) <= 240:
    print("ERROR: entry length out of range: %d" % len(written), file=sys.stderr)
    sys.exit(1)
if written.endswith("\n"):
    print("ERROR: entry has trailing newline", file=sys.stderr)
    sys.exit(1)
