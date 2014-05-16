#!/bin/env python

"""Reverse and Add

Challenge Description:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure. E.g.

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)

In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10,000. Assume each test case will always have an answer and that it is computable with less than 100 iterations (additions).

Output sample:

For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character). E.g.

4 9339

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
Sponsored Challenge Eligibility

In order to be eligible to push solution to the employer (DeveloperAuction), you must satisfy the following conditions:

    Location: United States
    Minimum Education: High School
    Your email / resume will always be sent to the employer
"""

import sys

def main(dfile):
    def rv(n):
        nr = 0
        while n > 0:
            nr = nr * 10 + n % 10
            n //= 10

        return nr
        
    with open(dfile, 'r') as f:
        for l in f:
            n = int(l.rstrip('\n'))
            i = 0
            nr = rv(n)
            while n != nr:
                n += nr
                i += 1
                nr = rv(n)
            
            print i, n
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
