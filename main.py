#!/usr/bin/env python3
"""The 3AM Fridge Text - make.fun bounty entry.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt (107 characters, one line), the artifact the house
judge reads two at a time.
"""
import os

LINE = "3am. Fourth visit tonight, still nothing eaten. I'm a fridge, not a museum. Take something or let me sleep."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()
