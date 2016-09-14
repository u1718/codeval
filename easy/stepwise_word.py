#!/bin/env python3

"""https://www.codeeval.com/open_challenges/202/

Stepwise word

Challenge Description:

Print the longest word in a stepwise manner.

Input sample:

The first argument is a path to a file. Each line contains a test case with a
list of words that have different or the same length.

For example:

cat dog hello
stop football play
music is my life

Output sample:

Find the longest word in each line and print it in one line in a stepwise
manner. Separate each new step with a space. If there are several words of the
same length and they are the longest, then print the first word from the list.

h *e **l ***l ****o
f *o **o ***t ****b *****a ******l *******l
m *u **s ***i ****c

Constraints:

   1 The word length is from 1 to 10 characters.
   2 The number of words in a line is from 5 to 15.
   3 If there are several words of the same length and they are the longest,
     then print the first word from the list.
   4 The number of test cases is 40.

"""

import sys

def main(dfile):
    """Stepwise word
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            ws = l.strip().split()
            imax = max(range(len(ws)), key=lambda e: len(ws.__getitem__(e)))
            print(' '.join(['*'*z + c for c, z in zip(ws[imax],
                                                      range(len(ws[imax])))]))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
