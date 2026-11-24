#!/usr/bin/env python3
"""Explain one everyday thing (a toaster) to a 10-year-old in two lines.

Line 1: a vivid analogy-based sentence.
Line 2: why the analogy works - what it maps and what it leaves out.
"""
import os

ENTRY = (
    "A toaster is a sunbed for bread: the slice lies flat under glowing red wires, tanning on both sides until it pops up golden brown.\n"
    "The analogy works because it maps the lying flat, the heat, and the slow browning, but it leaves out the timer, the spring that pops the bread up, and that bread never asked to sunbathe.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
