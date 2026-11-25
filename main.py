"""Entry program for make.fun bounty
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66
"The One-Line AI Excuse for Breaking Production" (v2 — Garbage Collection).

Writes exactly one line of UTF-8 text, 1-180 characters, no trailing
newline, to /output/entry.txt. Standard library only.
"""

import os
import sys

EXCUSE = "I ran garbage collection on the database. It collected the customers."

MIN_CHARS = 1
MAX_CHARS = 180


def gate_ok(text):
    """The sealed gate: 1-180 chars, UTF-8, not only whitespace, one line."""
    if "\n" in text or "\r" in text:
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_ok(EXCUSE):
        sys.stderr.write(
            "gate refused: entry is %d chars, must be %d-%d\n"
            % (len(EXCUSE), MIN_CHARS, MAX_CHARS)
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(EXCUSE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
