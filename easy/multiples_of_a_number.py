#!/bin/env python
"""https://www.codeeval.com/open_challenges/18/

Multiples of a Number

Challenge Description:

Given numbers x and n, where n is a power of 2, print out the smallest multiple
of n which is greater than or equal to x. Do not use division or modulo operator.

Input sample:

The first argument will be a path to a filename containing a comma separated
list of two integers, one list per line. E.g.

13,8
17,16

Output sample:

Print to stdout, the smallest multiple of n which is greater than or equal to x,
one per line. E.g.

16
32
"""

import sys

def main(dfile):
    """Multiples of a Number
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as f:
        for l in f:
            x, n = [int(n) for n in l.rstrip('\n').split(',')]
            i = 1
            while n * i < x:
                i += 1

            print n * i

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
