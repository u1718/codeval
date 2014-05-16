#!/bin/env python

"""Word Search
Challenge Description:

Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input sample:
ASADB
ABCCED
ABCF

The board to be used may be hard coded as:

[
[ABCE],
[SFCS],
[ADEE]
]

Your program should accept as its first argument a path to a filename. Each line in this file contains a word. E.g.

Output sample:
False
True
False

Print out True if the word exists in the board, False otherwise. E.g.

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys

def main(dfile):
    board = ["      ",
             " ABCE ",
             " SFCS ",
             " ADEE ",
             "      "]

    def find_next_letter(board, x, y, word, k):
        if k == len(word):
            return True
            
        brd = board[:]
        for i, j in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if brd[i][j] == word[k]:
                brd[i] = brd[i][:j] + ' ' + brd[i][j + 1:]
                return find_next_letter(brd, i, j, word, k + 1)

        return False
                    
    
    with open(dfile, 'r') as f:
        for l in f:
            word = l.strip()
            brd = board[:]
            for i in [1,2,3]:
                for j in [1,2,3,4]:
                    if brd[i][j] == word[0]:
                        brd[i] = brd[i][:j] + ' ' + brd[i][j + 1:]
                        if find_next_letter(brd, i, j, word, 1):
                            break

                else:
                    continue

                print True
                break

            else:
                print False
                    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
