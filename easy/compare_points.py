#!/bin/env python3

"""https://www.codeeval.com/open_challenges/192/

Compare Points

Challenge Description:

Bob's hiking club is lost in the mountains on the way to a scenic overlook.
Fortunately, Bob has a GPS device, so that he can see the coordinates where the
group is currently at. The GPS gives the current X/Y coordinates as O, P, and
the scenic overlook is located at Q, R. Bob now just needs to tell the group
which way to go so they can get to the overlook in time for s'mores.

Input sample:

The input is a file with each line representing a test case. Each test case
consists of four integers O, P, Q, R on a line, separated by spaces.

0 0 1 5
12 13 12 13
0 1 0 5

Output sample:

For each test case print a line containing one of the following:
N, NE, E, SE, S, SW, W, NW, here if the coordinates Q, R are (respectively)
north, northeast, east, southeast, south, southwest, west, northwest, or already
at ("here") the coordinates O, P. Note that N, S, E and W mean directly North,
South, East or West respectively, i.e. X or Y coordinates of two points are
exactly the same. In all other cases your output should be one of the NW, NE,
SW, SE or here.

NE
here
N

Constraints:

   1 All coordinates -10000 < |O,P,Q,R| < 10000
   2 Number of test cases is 40

"""

import sys

def main(dfile):
    """Compare Points
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            o, p, q, r = [int(n) for n in l.strip().split()]
            x, y = q - o, r - p
            if x == 0:
                if y == 0:
                    print('here')
                elif y > 0:
                    print('N')
                else:
                    print('S')
            elif y == 0:
                if x > 0:
                    print('E')
                else:
                    print('W')
            elif x > 0:
                if y > 0:
                    print('NE')
                else:
                    print('SE')
            else:
                if y > 0:
                    print('NW')
                else:
                    print('SW')
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
