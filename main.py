#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it, and to leave it braver -- steadier, unhurried,
ready to move.

The text is a single fixed string. No randomness, no time, no network,
no input: two runs write byte-identical output.
"""

import os

ENTRY = (
    "The wheel slows, and the potter's hands stay where they are. "
    "Wet clay turns beneath them, rising a little with each pass. "
    "The clay does not hurry. It only rises. "
    "When the wheel stops, the bowl stands on its own, steady, "
    "ready to be filled."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts Unicode code points: 1 to 280, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} code points"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
