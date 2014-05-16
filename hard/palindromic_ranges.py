#!/bin/env python

"""Palindromic Ranges
Challenge Description:

A positive integer is a palindrome if its decimal representation (without leading zeros) is a palindromic string (a string that reads the same forwards and backwards). For example, the numbers 5, 77, 363, 4884, 11111, 12121 and 349943 are palindromes.

A range of integers is interesting if it contains an even number of palindromes. The range [L, R], with L <= R, is defined as the sequence of integers from L to R (inclusive): (L, L+1, L+2, ..., R-1, R). L and R are the range's first and last numbers.

The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. Your job is to determine how many interesting subranges of [L,R] there are.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain two positive integers, L and R (in that order), separated by a space. eg.

1 2
1 7
87 88

Output sample:

For each line of input, print out the number of interesting subranges of [L,R] eg.

1
12
1

For the curious: In the third example, the subranges are: [87](0 palindromes), [87,88](1 palindrome),[88](1 palindrome). Hence the number of interesting palindromic ranges is 1

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys

def main(dfile):
    
    def ispal(i):
        si = i
        ri = 0
        while i:
            ri += i % 10
            ri *= 10
            i //= 10

        return ri / 10 == si

    with open(dfile, 'r') as f:
        for l in f:
            lf, rt = map(int, l.rstrip().split())
            n = 0
            for i in range(lf, rt + 1):
                for j in range(i, rt + 1):
                    subrange = range(i, j + 1)
                    if len(filter(ispal, subrange)) % 2 == 0:
                        n += 1
            
            print n

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    