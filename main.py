#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes a single-line review of my own Monday to $MAKEFUN_OUTPUT_DIR/entry.txt
and self-checks the gate: UTF-8, 1-200 chars, single line, not whitespace-only.
Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "One star for Monday: inbox at 47 unread by 9am, standup ran 40 minutes "
    "over, and the Wi-Fi took the afternoon off."
)

MAX_CHARS = 200


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    # Gate self-checks.
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Read-back verification: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != text:
        print("read-back mismatch: disk content differs from entry", file=sys.stderr)
        return 1
    if len(on_disk.encode("utf-8")) != len(text.encode("utf-8")):
        print("read-back byte-length mismatch", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(text)} chars, read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
