#!/usr/bin/env python3
"""Simple test bot that plays sequentially through all grid squares."""

import sys

def main():
    if len(sys.argv) < 2:
        print("0")
        return

    # The bot receives the current shot grid as a comma-separated string
    # 0 = unknown, -1 = miss, 1 = hit, 2 = sunk
    shot_grid = sys.argv[1].split(',')

    # Find the first unknown square and shoot it
    for i, square in enumerate(shot_grid):
        if square == '0':
            print(i)
            return

    # If all squares are known, just return 0 (shouldn't happen in a valid game)
    print("0")

if __name__ == "__main__":
    main()
