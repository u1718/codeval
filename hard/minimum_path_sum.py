#!/bin/env python

"""Minimum Path Sum
Challenge Description:

You are given an n*n matrix of integers. You can move only right and down. Calculate the minimal path sum from the top left to the bottom right
Input sample:

Your program should accept as its first argument a path to a filename. The first line will have the value of n(the size of the square matrix). This will be followed by n rows of the matrix. (Integers in these rows will be comma delimited). After the n rows, the pattern repeats. E.g.

2
4,6
2,8
3
1,2,3
4,5,6
7,8,9
Output sample:

Print out the minimum path sum for each matrix. E.g.

14
21
"""
    
import sys

def ps(msum, m, s, i, j, n):
    if i == n:
        if j == n:
            msum.append(s + m[i][j])
            return

        else:
            ps(msum, m, s + m[i][j], i, j + 1, n)
    
    elif j == n:
        ps(msum, m, s + m[i][j], i + 1, j, n)
    
    else:
        ps(msum, m, s + m[i][j], i, j + 1, n)
        ps(msum, m, s + m[i][j], i + 1, j, n)
    

    
def main(dfile):
    with open(dfile, 'r') as f:
        l = f.readline()
        while l:
            n = int(l.strip('\n'))
            m = []
            for i in range(n):
                m.append(map(int, f.readline().strip('\n').split(',')))

            msum = []
            ps(msum, m, 0, 0, 0, n - 1)
            print min(msum)
            l = f.readline()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    