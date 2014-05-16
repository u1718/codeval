#!/bin/env python

"""Lowest Unique Number
Challenge Description:

There is a game where each player picks a number from 1 to 9, writes it on a paper and gives to a guide. A player wins if his number is the lowest unique. We may have 10-20 players in our game.
Input sample:

Your program should accept as its first argument a path to a filename.

You're a guide and you're given a set of numbers from players for the round of game. E.g. 2 rounds of the game look this way:

3 3 9 1 6 5 8 1 5 3
9 2 9 9 1 8 8 8 2 1 1

Output sample:

Print a winner's position or 0 in case there is no winner. In the first line of input sample the lowest unique number is 6. So player 5 wins.

5
0

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            bids = l.strip().split()
            try:
                print bids.index(str([bids.count(e) for e in '123456789'].index(1) + 1)) + 1
            except ValueError:
                print 0

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))