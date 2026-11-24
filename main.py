#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes exactly one funny line (a single sentence, <= 200 chars) to
entry.txt inside the output directory named by MAKEFUN_OUTPUT_DIR
(default /output). Stdlib only, deterministic, exits 0.
"""
import os
import sys

LINE = (
    "Adulthood is asking Google how long chicken survives in the fridge, "
    "weekly, for decades, and still throwing it out just in case."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
