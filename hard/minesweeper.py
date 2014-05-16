#!/usr/bin/env python

"""Minesweeper
Challenge Description:

You will be given an M*N matrix. Each item in this matrix is either a '*' or a '.'. A '*' indicates a mine whereas a '.' does not. The objective of the challenge is to output a M*N matrix where each element contains a number (except the positions which actually contain a mine which will remain as '*') which indicates the number of mines adjacent to it. Notice that each position has at most 8 adjacent positions e.g. left, top left, top, top right, right, ...
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains M,N, a semicolon and the M*N matrix in row major form. E.g.

3,5;**.........*...
4,4;*........*......

Output sample:

Print out the new M*N matrix (in row major form) with each position(except the ones with the mines) indicating how many adjacent mines are there. E.g.

**100332001*100
*10022101*101110

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            mn, fld = l.rstrip('\n').split(';')
            m, n = map(int, mn.split(','))
            fld = [' ' * (n + 2)] + \
                  [' ' + fld[i * n : i * n + n] + ' ' for i in range(m)] +\
                  [' ' * (n + 2)]
            mine_map = []
            for i in xrange(1, m + 1):
                row = ''
                for j in xrange(1, n + 1):
                    if fld[i][j] == '*':
                        row += '*'
                    else:
                        row += str(sum([1 if fld[x][y] == '*' else 0
                                        for x in [i - 1, i, i + 1]
                                        for y in [j - 1, j, j + 1]]))

                mine_map.append(row)

            print ''.join(mine_map)
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
