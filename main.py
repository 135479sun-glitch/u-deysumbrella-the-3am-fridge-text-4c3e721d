#!/usr/bin/env python3
"""The 3AM Fridge Text - make.fun bounty entry.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt (107 characters, one line), the artifact the house
judge reads two at a time.
"""
import os

LINE = "3am. Fourth visit tonight, still nothing eaten. I'm a fridge, not a museum. Take something or let me sleep."
MAX_CHARS = 140  # the sealed gate refuses entry.txt over 140 characters

def main():
    if not 1 <= len(LINE) <= MAX_CHARS or LINE.strip() != LINE or "\n" in LINE:
        raise SystemExit(f"entry line must be one line of 1-{MAX_CHARS} chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()
