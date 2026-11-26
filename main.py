#!/usr/bin/env python3
"""The 3AM Commit Message — writes one funny commit line to /output/entry.txt.

The entry imagines the commit message typed at 3am by a developer who has
just fixed a bug they do not understand: the fix works, nothing was (knowingly)
changed, and the only safe move is to merge before the code changes its mind.

Python standard library only. Entry rules: a single line, 1-139 characters.
"""

import os

ENTRY = "fix: it works now. no, i don't know why. yes, i changed nothing. merge it before it changes its mind"

MAX_LENGTH = 139


def validate(text: str) -> None:
    """Raise SystemExit unless text is a valid single-line entry."""
    if not 1 <= len(text) <= MAX_LENGTH:
        raise SystemExit(f"entry length {len(text)} outside 1-{MAX_LENGTH}")
    if text.strip() == "":
        raise SystemExit("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader reads the file as a different user; default umask may not
    # grant read access, so make it readable explicitly.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
