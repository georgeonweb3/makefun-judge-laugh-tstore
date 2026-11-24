#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line, at most 200 characters.

Writes the tournament-winning line to /output/entry.txt.
"""
import os

LINE = "The hospice nurse told Dad he had two weeks. He spent the first one teaching me his Wi-Fi password, and the second one changing it."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    # Tournament winner (blind pairwise, 5-0): hospice/Wi-Fi password reversal.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
