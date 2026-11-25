#!/usr/bin/env python3
"""Till Firmware Do Us Part — writes one robot wedding vow to /output/entry.txt.

Event: u-azazex-till-firmware-do-us-part-32172929 (make.fun).
The vow below won the internal pairwise audit 3/3 against the other finalists
(see candidates.md): a robot's own wedding vow, funny from the situation,
tender underneath, and spoken in a machine's own voice.
"""

import os

VOW = "Till firmware do us part, I vow to be your backup, your restore point, and the one process that never crashes on you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
