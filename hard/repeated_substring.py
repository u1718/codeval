#!/bin/env python

"""Repeated Substring
Challenge Description:

You are to find the longest repeated substring in a given text. Repeated substrings may not overlap. If more than one substring is repeated with the same length, print the first one you find.(starting from the beginning of the text).
NOTE: The substrings can't be all spaces.
Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. Each line contains a test string. E.g.

banana
am so uniqe

Output sample:

For each set of input produce a single line of output which is the longest repeated substring. If there is none, print out the string NONE. E.g.

an
NONE

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
Sponsored Challenge Eligibility

In order to be eligible to push solution to the employer (Email Cherry), you must satisfy the following conditions:

    Location: United States
    Minimum Education: High School
    Your email / resume will always be sent to the employer
"""

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            s = l.rstrip('\n')
            

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))