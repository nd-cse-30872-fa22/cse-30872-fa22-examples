#!/usr/bin/env python3

# https://leetcode.com/problems/longest-palindrome/

''' 409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.
'''

import collections
import sys

# Functions

def longest_palindrome(s):
    ''' Returns the length of the longest palindrome that can be built with
    letters in s.

    >>> longest_palindrome('abccccdd')
    7

    >>> longest_palindrome('a')
    1

    >>> longest_palindrome('aaabbbccc')
    7
    '''
    counts = collections.Counter(s)
    pairs  = sum(count // 2 * 2 for count in counts.values())           # Grab pairs
    center = 1 if any(count % 2 for count in counts.values()) else 0    # Grab center
    return pairs + center

# Main Execution

def main():
    ''' Print the longest palindrome for each line from stdin. '''
    for line in sys.stdin:
        print(longest_palindrome(line.strip()))

if __name__ == '__main__':
    main()
