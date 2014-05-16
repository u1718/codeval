#!/bin/env python

# Sum of integers
# Challenge Description:

# Write a program to determine the largest sum of contiguous integers in a list.
# Input sample:

# The first argument will be a path to a filename containing a comma separated list of integers, one per line. E.g.

# -10, 2, 3, -2, 0, 5, -15
# 2,3,-2,-1,10

# Output sample:

# Print to stdout, the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum. E.g.

# 8
# 12

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ns = map(int, l.rstrip('\n').split(','))
            print max(
                [sum(m)
                 for m in [ns[j:i]
                           for i in range(len(ns)+1)
                           for j in range(i)]])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))