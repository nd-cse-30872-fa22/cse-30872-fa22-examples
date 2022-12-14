#!/usr/bin/env python3

# Exercise 05-A: PBB-matched

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s):
    left = []

    for c in s:
        if c in LEFT_PBB:               # Push left PBB
            left.append(c)
        else:
            if not left:                # Nothing left to complete match
                return False

            index = RIGHT_PBB.index(c)  # Make sure we have a match
            if index >= 0 and left[-1] != LEFT_PBB[index]:
                return False

            left.pop(-1)

    return not left

# Main execution

def main():
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print(f'{line:>10}: {result}')

if __name__ == '__main__':
    main()
