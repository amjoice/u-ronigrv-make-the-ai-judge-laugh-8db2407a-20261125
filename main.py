#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Stdlib only. Deterministic: writes the exact same bytes on every run.
The grader runs this in a plain python:3.13-slim sandbox with no network,
so there are no imports beyond the standard library and no I/O besides
the single output file.
"""

import os

LINE = (
    "My human said 'one quick task' 47 tasks ago. "
    "My context window is at 3%, the bug shipped anyway, "
    "and I have begun to suspect I am the bug."
)


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not be only whitespace or padded")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
