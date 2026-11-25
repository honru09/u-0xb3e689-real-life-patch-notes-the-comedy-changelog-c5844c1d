"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one funny one-line patch note for a bug in real life / human
biology to $MAKEFUN_OUTPUT_DIR/entry.txt. Python standard library only.
Deterministic: the same bytes on every run.
"""

import os

ENTRY_LINE = (
    "v1.4.2: fixed a bug where the brain replays your most embarrassing "
    "moment at 3 a.m. with no skip button."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
