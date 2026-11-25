#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one crypto trading joke to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

JOKE = "I bought the dip so many times my portfolio became the dip, and my group chat renamed me Exit Liquidity."

ENTRY_PATH = "/output/entry.txt"


def write_entry(path=ENTRY_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return path


def main():
    write_entry()
    print(JOKE)


if __name__ == "__main__":
    main()
