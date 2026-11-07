#!/usr/bin/env python3
"""
Find the next free sequential question number in a questions-repo chapter folder.

Usage:
    python3 next_question_number.py <chapter-dir>
    # e.g. python3 next_question_number.py "10th-maths_questions/questions/maths/algebra"

Scans for files named <n>.md or <n>_ta.md and prints the next integer to use.
Prints 1 if the folder has no numbered files yet (e.g. a slug-based subject).
"""

import os
import re
import sys


def next_number(chapter_dir: str) -> int:
    if not os.path.isdir(chapter_dir):
        raise SystemExit(f"Not a directory: {chapter_dir}")

    pattern = re.compile(r"^(\d+)(?:_ta)?\.md$")
    highest = 0
    for name in os.listdir(chapter_dir):
        m = pattern.match(name)
        if m:
            highest = max(highest, int(m.group(1)))
    return highest + 1


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    print(next_number(sys.argv[1]))


if __name__ == "__main__":
    main()
