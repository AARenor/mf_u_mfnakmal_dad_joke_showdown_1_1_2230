#!/usr/bin/env python3
"""Write one short dad joke for a make.fun bounty entry.

The joke is a single string constant below. It is written as UTF-8 bytes,
with no trailing newline, into entry.txt inside the output directory.
"""

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def output_dir() -> Path:
    """Return the directory the entry text is written to."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 characters, got {len(TEXT)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    (target / OUTPUT_FILENAME).write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
