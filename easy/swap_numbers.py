#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/196/

Swap Numbers
Challenge Description:

Write a program that, given a sentence where each word has a single digit
positive integer as a prefix and suffix, swaps the numbers while retaining the
word in between. Words in the sentence are delimited from each other by a space.

Input sample:

The first argument is a path to a file. Each line of the input file contains one
test case represented by a sentence. Each word in the sentence begins and ends
with a single digit positive integer i.e. 0 through 9. Assume all characters
are ASCII.

4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
5Nobody5 7expects3 5the4 6Spanish4 9inquisition0

Output sample:

For each test case, print to standard output the sentence obtained by swapping
the numbers surrounding each word, one per line.

0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5
5Nobody5 3expects7 4the5 4Spanish6 0inquisition9

Constraints:

  1 The suffix and the prefix of each word may be equal.
  2 Sentences are form 1 to 17 words long.
  3 The number of test cases is 40.
"""

import sys

def main(dfile):
    """Swap Numbers
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            print(' '.join([w[-1] + w[1:-1] + w[0] for w in l.split()]))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
