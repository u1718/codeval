#!/bin/env python

"""Sequence Transformation

Challenge Description:

There are two sequences. The first sequence consists of digits "0" and "1", the second one consists of letters "A" and "B". The challenge is to determine whether it's possible to transform a given binary sequence into a string sequence using the following rules:
1. "0" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.)
2. "1" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.) or to non empty sequence of letters "B" ("B", "BB", "BBB" etc) e.g.

Input sample:
1010 AAAAABBBBAAAA
00 AAAAAA
01001110 AAAABAAABBBBBBAAAAAAA
1100110 BBAABABBA

Your program should accept as its first argument a path to a filename. Each line in this file contains a binary sequence and a sequence of letters "A" and "B" separated by a single whitespace. E.g.

Output sample:
Yes
Yes
Yes
No

For each test case print out "Yes" if the transformation is possible, otherwise print "No". E.g.

Constraints:

The length of a binary sequence is in range [1, 150]
The length of a string sequence is in range [1, 1000]
The number of test cases is <= 50

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys
import re
import itertools

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            bs, ls = l.split()
            for p1 in itertools.product('AB', repeat=bs.count('1')):
                i = 0
                p = r''
                for d in bs:
                    if d == '0':
                        p += 'A+'
                    else:
                        p += p1[i] + '+'
                        i += 1

                if re.match(p + '$', ls):
                    print 'Yes'
                    break

            else:
                print 'No'

    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

