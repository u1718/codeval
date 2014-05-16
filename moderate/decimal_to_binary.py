#!/bin/env python

# Decimal To Binary
# Challenge Description:

# Given a decimal (base 10) number, print out its binary representation.
# Input sample:

# Your program should accept as its first argument a path to a filename containing whole decimal numbers greater or equal to 0, one per line.
# Ignore all empty lines. E.g.

# 2
# 10
# 67

# Output sample:

# Print the binary representation, one per line. E.g.

# 10
# 1010
# 1000011

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            print '{0:b}'.format(int(l.rstrip('\n')))


    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))