#!/bin/env python
"""https://www.codeeval.com/open_challenges/93/

Capitalize Words

Challenge Description:

Write a program which capitalizes the first letter of each word in a sentence.

Input sample:

Your program should accept as its first argument a path to a filename. Input
example is the following

Hello world
javaScript language
a letter
1st thing

Output sample:

Print capitalized words in the following way.

Hello World
JavaScript Language
A Letter
1st Thing
"""
import sys

def main(dfile):
    """Capitalize Words
    @param dfile: data file path
    @type of dfile: str
    """

    from string import maketrans
    
    intab = "qwertyuiopasdfghjklzxcvbnm"
    outtab = "QWERTYUIOPASDFGHJKLZXCVBNM"
    trantab = maketrans(intab, outtab)
    
    with open(dfile, 'r') as f:
        for l in f:
            sar = l.rstrip('\n').split()
            print ' '.join([e[0].translate(trantab) + e[1:] for e in sar])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

    
