#!/bin/env python
"""https://www.codeeval.com/open_challenges/91/

Simple Sorting

Challenge Description:

Write a program which sorts numbers.

Input sample:

Your program should accept as its first argument a path to a filename. Input
example is the following

70.920 -38.797 14.354 99.323 90.374 7.581
-37.507 -3.263 40.079 27.999 65.213 -55.552

Output sample:

Print sorted numbers in the following way. Please note, that you need to print
the numbers till the 3rd digit after the dot including trailing zeros.

-38.797 7.581 14.354 70.920 90.374 99.323
-55.552 -37.507 -3.263 27.999 40.079 65.213
"""
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ar = [float(e) for e in  l.rstrip('\n').split()]
            print ' '.join(['{:.3f}'.format(e) for e in  sorted(ar)])
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
