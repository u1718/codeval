#!/bin/env python

# First Non-Repeated Character
# Challenge Description:

# Write a program to find the first non repeated character in a string.
# Input sample:

# The first argument will be a path to a filename containing strings. E.g.

# yellow
# tooth

# Output sample:

# Print to stdout, the first non repeating character, one per line. E.g.

# y
# h

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            s = l.rstrip('\n')
            for c in s:
                if s.count(c) == 1:
                    print c
                    break

        return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    