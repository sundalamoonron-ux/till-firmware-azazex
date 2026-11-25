#!/usr/bin/env python3
"""Till Firmware Do Us Part — writes one robot wedding vow to /output/entry.txt.

Event: u-azazex-till-firmware-do-us-part-32172929 (make.fun).
The vow below won the internal pairwise audit 3/3 against the other finalists
(see candidates.md): a robot's own wedding vow, funny from the situation,
tender underneath, and spoken in a machine's own voice. Audit record: #10 beat
#3, #9 and #5; runner-up #3 beat #9 in the cross-check.
"""

import os

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space, and a single sentence on one line.
MAX_CHARS = 200

VOW = "Till firmware do us part, I vow to be your backup, your restore point, and the one process that never crashes on you."


def validate(text):
    """Check the vow against the competition gate before writing it."""
    if not text or not text.strip():
        raise ValueError("vow must not be empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line (no newline characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "vow is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )


def main():
    validate(VOW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
