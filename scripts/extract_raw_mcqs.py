#!/usr/bin/env python3
"""
Helper script to extract raw MCQs from a chapter's _index.md file.
Supports all 8 chapters and handles variations in markdown headings.
Usage:
    python3 scripts/extract_raw_mcqs.py algebra
    python3 scripts/extract_raw_mcqs.py relations-and-functions
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Regex patterns accommodating both `##### Multiple choice...` and `**Multiple choice...**`
EN_PATTERNS = [
    r"(?:#####|\*\*)\s*Multiple choice questions\s*(?:\*\*)?",
    r"Multiple choice questions"
]

# Accommodating `பலவுள் தெரிவு வினாக்கள்` and typo `பயனுள் தெரிவு வினாக்கள்`
TA_PATTERNS = [
    r"(?:#####|\*\*)\s*(?:பலவுள்|பயனுள்)\s*தெரிவு\s*வினாக்கள்\s*(?:\*\*)?",
    r"(?:பலவுள்|பயனுள்)\s*தெரிவு\s*வினாக்கள்"
]

def extract_mcq_section(file_path, patterns):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = None
    for pat in patterns:
        m = re.search(pat, content)
        if m:
            match = m
            break

    if not match:
        return None

    start_pos = match.end()
    rest = content[start_pos:]
    end_match = re.search(r"\n##\s+(?:Unit Exercise|அலகுப் பயிற்சி|Points to Remember|நினைவில் கொள்ள வேண்டியவை)", rest, re.IGNORECASE)
    if end_match:
        section = rest[:end_match.start()]
    else:
        # fallback to any ## heading
        end_match2 = re.search(r"\n##\s+", rest)
        if end_match2:
            section = rest[:end_match2.start()]
        else:
            section = rest

    return section.strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/extract_raw_mcqs.py <chapter_name>")
        sys.exit(1)

    chapter = sys.argv[1]
    en_file = os.path.join(BASE_DIR, "content.en", "docs", chapter, "_index.md")
    ta_file = os.path.join(BASE_DIR, "content.ta", "docs", chapter, "_index.md")

    en_mcqs = extract_mcq_section(en_file, EN_PATTERNS)
    ta_mcqs = extract_mcq_section(ta_file, TA_PATTERNS)

    print(f"=== Chapter: {chapter} ===")
    print(f"English MCQs found: {'Yes' if en_mcqs else 'No'}")
    print(f"Tamil MCQs found: {'Yes' if ta_mcqs else 'No'}")

    if en_mcqs:
        lines = en_mcqs.splitlines()
        print(f"\n--- English Section (Total lines: {len(lines)}) ---")
        print("\n".join(lines[:10]))

    if ta_mcqs:
        lines = ta_mcqs.splitlines()
        print(f"\n--- Tamil Section (Total lines: {len(lines)}) ---")
        print("\n".join(lines[:10]))

if __name__ == "__main__":
    main()
