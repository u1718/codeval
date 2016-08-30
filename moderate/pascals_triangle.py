#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/66/

Pascals Triangle

Challenge Description:

A Pascals triangle row is constructed by looking at the previous row and adding
the numbers to its left and right to arrive at the new value. If either the
number to its left/right is not present, substitute a zero in it's place. More
details can be found here: Pascal's triangle. E.g. a Pascal's triangle upto a
depth of 6 can be shown as:

            1
          1   1
        1   2   1
       1  3   3   1
     1  4   6   4   1
    1  5  10  10  5   1

Input sample:

Your program should accept as its first argument a path to a filename. Each line
in this file contains a positive integer which indicates the depth of the
triangle (1 based). E.g.

6

Output sample:

Print out the resulting pascal triangle upto the requested depth in row major
form. E.g.

1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1

"""

import sys

def main(dfile):
    """Pascals Triangle
    @param dfile: data file path
    @type of dfile: str
    """
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            depth = int(l)
            pt = [1]
            prev_row = [1]
            while depth > 1:
                cons_row = [1]
                i = len(prev_row) - 1
                while i > 0:
                    cons_row.append(prev_row[i] + prev_row[i - 1])
                    i -= 1
                    
                cons_row.append(1)
                prev_row = cons_row
                pt.extend(cons_row)
#                pt += cons_row
                depth -= 1

            print(' '.join([str(n) for n in pt]))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
