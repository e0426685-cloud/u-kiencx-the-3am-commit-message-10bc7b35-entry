#!/usr/bin/env python3
"""The 3AM Commit Message — writes one funny commit line to /output/entry.txt.

Python standard library only.
"""

import os

ENTRY = "fix: it works now. no, i don't know why. yes, i changed nothing. merge it before it changes its mind"


def main() -> None:
    if not 1 <= len(ENTRY) <= 139:
        raise SystemExit(f"entry length {len(ENTRY)} outside 1-139")
    if ENTRY.strip() == "":
        raise SystemExit("entry is only whitespace")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
