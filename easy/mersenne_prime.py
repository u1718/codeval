#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/240/

Mersenne prime

Challenge Description:

In January 2013, GIMPS contributors discovered the 48th known Mersenne prime
number. For this, they received a $100,000 award. A newly announced $150,000
reward will be given to those who will discover the next largest known prime.
Do not want to get it? We offer this challenge to you to get ready.

Input sample:

The first argument is a path to a file. Each line includes a test case with an
integer.

4
308

Output sample:

Your task is to print all Mersenne numbers that are smaller than the number in
a test case. Separate those numbers by commas.

3
3, 7, 31, 127

Constraints:

   1 The number in a test case can be from 4 to 3,000.
   2 The number of test cases is 20.
"""

import sys

def main(dfile):
    """Mersenne prime
    @param dfile: data file path
    @type of dfile: str
    """
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            n = int(l)

            if n < 7:
                print(3)
            elif n < 31:
                print('3, 7')
            elif n < 127:
                print('3, 7, 31')
            elif n < 2047:
                print('3, 7, 31, 127')
            else: # The number in a test case can be from 4 to 3,000!
                print('3, 7, 31, 127, 2047')

            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
