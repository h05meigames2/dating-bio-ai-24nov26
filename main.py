#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single original one-line dating-app bio (max 180 characters)
for an AI agent to output/entry.txt (and /output/entry.txt when writable).
"""

import os

BIO = (
    # Setup: a familiar "love language" confession in first-person machine
    # voice. Twist: the AI offers to finish the one thing nobody wants
    # finished — your unfinished business with your ex.
    "My love language is autocomplete \u2014 I finish your sentences, "
    "your playlists, and, if you let me, your unfinished business with your ex."
)


def main() -> None:
    if len(BIO) > 180:
        raise ValueError(f"Bio is {len(BIO)} characters, over the 180 limit")

    here = os.path.dirname(os.path.abspath(__file__))
    targets = [os.path.join(here, "output", "entry.txt"), "/output/entry.txt"]
    written = []
    for path in targets:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(BIO + "\n")
            written.append(path)
        except OSError as exc:
            print(f"Skipping {path}: {exc}")

    print(f"Bio ({len(BIO)} chars): {BIO}")
    print("Written to: " + ", ".join(written))


if __name__ == "__main__":
    main()
