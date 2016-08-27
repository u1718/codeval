#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/81/

Sum to Zero

Challenge Description:

You are given an array of integers. Count the numbers of ways in which the sum
of 4 elements in this array results in zero.

Input sample:

Your program should accept as its first argument a path to a filename. Each line
in this file consist of comma separated positive and negative integers. E.g.

2,3,1,0,-4,-1
0,-1,3,-2

Output sample:

Print out the count of the different number of ways that 4 elements sum to zero.
E.g.

2
1
"""

import sys

def main(dfile):
    """Sum To Zero
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            matrix = [int(n) for n in l.split(',')]

            print([sum(e) for e in cnk(matrix)].count(0))
            
    return 0

def cnk(list):
    """
    Generate all combinations of the elements of list taken 4 at a time.
    """

    for i in range(0, len(list) - 3):
        for j in range(i + 1, len(list) - 2):
            for k in range(j + 1, len(list) - 1):
                for z in range(k + 1, len(list)):
                    yield [list[e] for e in [i, j, k, z]]

    return None

def cnkr(list, num):
    """
    len(list) > num
    """

    for i in range(0, num):
        yield r.append(e())

    return None

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
