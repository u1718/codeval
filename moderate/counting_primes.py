#!/bin/env python

"""Counting Primes
Challenge Description:

Given two integers N and M, count the number of prime numbers between N and M (both inclusive)
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

2,10
20,30

Output sample:

Print out the number of primes between N and M (both inclusive)

4
2

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            sp, fp = map(int, l.rstrip('\n').split(','))
            er_sieve = [1 for i in xrange(fp + 1)]
            er_sieve[0] = er_sieve[1] = 0
            i = 2
            while i*i <= fp:
                if er_sieve[i]:
                    j = i*i
                    while j <= fp:
                        er_sieve[j] = 0
                        j += i

                i += 1

            print sum(er_sieve[sp:])
                
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))