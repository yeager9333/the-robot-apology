#!/usr/bin/env python3
"""The Robot Apology -- make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, no network. Gate: the entry must be UTF-8 text of 1 to 400
characters, not only whitespace, in exactly two lines -- line one a single
sentence apologizing for one specific mistake, line two a single sentence
saying what the robot learned and what it will do differently.
"""

import os
import sys

ENTRY = (
    "I'm sorry I watered your laptop instead of your fern -- my moisture "
    "sensor mistook a glowing screen for thirsty soil.\n"
    "I have learned to check whether the thing I'm watering has roots "
    "before I pour, and I will now ask before I hydrate anything that "
    "plugs in.\n"
)

MAX_CHARS = 400


def validate(text: str) -> None:
    """Fail loudly unless the entry meets the competition gate."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 400 limit"
        )
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise SystemExit(f"line {i} is empty")
        if not line.rstrip().endswith("."):
            raise SystemExit(f"line {i} must end with a full stop")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("entry.txt was not written byte-identically")
    print(f"wrote {path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
