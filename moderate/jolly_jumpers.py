#!/usr/bin/env python3
"""https://www.codeeval.com/open_challenges/43/

Jolly Jumpers

Challenge Description:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

A sequence of n > 0 integers is called a jolly jumper if the absolute values of
the differences between successive elements take on all possible values 1
through n - 1. eg.

1 4 2 3 

is a jolly jumper, because the absolute differences are 3, 2, and 1,
respectively. The definition implies that any sequence of a single integer is a
jolly jumper. Write a program to determine whether each of a number of sequences
is a jolly jumper.

Input sample:

Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain an integer n < 3000
followed by n integers representing the sequence. The integers are space
delimited.

For example:

4 1 4 2 3
3 7 7 8
9 8 9 7 10 6 12 17 24 38

Output sample:

For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.

For example:

Jolly
Not jolly
Not jolly
"""
import sys

def main(dfile):
    """Jolly Jumpers
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            n, *sq = [int(e) for e in l.rstrip('\n').split()]
            if len(sq) == 1:
                print('Jolly')
                continue
                
            ds = sorted([abs(a - b) for a, b in zip(sq, sq[1:])],
                            reverse = True)
            if ds[-1] == 1 and all([a - b == 1  for a, b in zip(ds, ds[1:])]):
                print('Jolly')
            else:
                print('Not jolly')
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
