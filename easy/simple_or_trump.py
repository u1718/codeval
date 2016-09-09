#!/bin/env python3

"""https://www.codeeval.com/open_challenges/235/

Simple or trump

Challenge Description:

First playing cards were invented in Eastern Asia and then spread all over the
world taking different forms and appearance. In India, playing cards were round,
and they were called Ganjifa. In medieval Japan, there was a popular Uta-garuta
game, in which shell mussels were used instead of playing cards.
In our game, we use playing cards that are more familiar nowadays. The rules are
also simple: an ace beats a deuce (2) unless it is a trump deuce.

Input sample:

The first argument is a path to a file. Each line includes a test case which
contains two playing cards and a trump suit. Cards and a trump suite are
separated by a pipeline (|). The card deck includes thirteen ranks (from a deuce
to an ace) of each of the four suits: clubs (♣), diamonds (♦), hearts (♥), and
spades (♠). There are no Jokers.

AD 2H | H
KD KH | C
JH 10S | C

Output sample:

Your task is to print a card that wins. If there is no trump card, then the
higher card wins. If the cards are equal, then print both cards.

2H
KD KH
JH

Constraints:

   1 The card deck includes ranks from a deuce (2) to an ace, no Jokers.
   2 If the cards are equal, then print both cards.
   3 The number of test cases is 40.
"""

import sys

def main(dfile):
    """Simple or trump
    @param dfile: data file path
    @type of dfile: str
    """
    rank = dict()
    rank['A'] = 14
    rank['K'] = 13
    rank['Q'] = 12
    rank['J'] = 11
    rank['10'] = 10
    rank['9'] = 9
    rank['8'] = 8
    rank['7'] = 7
    rank['6'] = 6
    rank['5'] = 5
    rank['4'] = 4
    rank['3'] = 3
    rank['2'] = 2
    
    with open(dfile, 'r') as f:
        for l in f:
            cards, trump = l.rstrip('\n').split(' | ')
            lh, rh = cards.split()

            if lh[-1] == trump and rh[-1] != trump:
                print(lh)
            elif lh[-1] != trump and rh[-1] == trump:
                print(rh)
            elif rank[lh[0:-1]] > rank[rh[0:-1]]:
                print(lh)
            elif rank[lh[0:-1]] < rank[rh[0:-1]]:
                print(rh)
            else: #rank[lh[0:-1]] == rank[rh[0:-1]]:
                print(lh, rh)
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
