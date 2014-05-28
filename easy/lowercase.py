#!/usr/bin/env python
"""Lowercase
Challenge Description:

Given a string write a program to convert it into lowercase.
Input sample:

The first argument will be a path to a filename containing sentences, one per line. You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text

Output sample:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            print l.lower()
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
