#!/usr/bin/env python3
"""One Line to Your Younger Self entry.

Writes exactly one line of advice to your younger self to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

MAX_CHARS = 200

ENTRY_TEXT = (
    "Buy the bitcoin, skip the all-nighter, and call your grandmother "
    "back — she won't be there forever, but the deadline will."
)

if len(ENTRY_TEXT) > MAX_CHARS:
    raise SystemExit(
        f"entry is {len(ENTRY_TEXT)} chars, over the {MAX_CHARS} limit"
    )

if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
    raise SystemExit("entry must be a single line")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
