#!/bin/env python

"""Sequence Transformation

Challenge Description:

There are two sequences. The first sequence consists of digits "0" and "1", the
second one consists of letters "A" and "B". The challenge is to determine
whether it's possible to transform a given binary sequence into a string
sequence using the following rules:
1. "0" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.)
2. "1" can be transformed into non empty sequence of letters "A" ("A", "AA", "AAA" etc.)
   or to non empty sequence of letters "B" ("B", "BB", "BBB" etc) e.g.

Input sample:

1010 AAAAABBBBAAAA
00 AAAAAA
01001110 AAAABAAABBBBBBAAAAAAA
1100110 BBAABABBA

Your program should accept as its first argument a path to a filename. Each line
in this file contains a binary sequence and a sequence of letters "A" and "B"
separated by a single whitespace. E.g.

Output sample:

Yes
Yes
Yes
No

For each test case print out "Yes" if the transformation is possible,
otherwise print "No". E.g.

Constraints:

The length of a binary sequence is in range [1, 150]
The length of a string sequence is in range [1, 1000]
The number of test cases is <= 50

"""

import sys
import re
import itertools

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            bs, ls = l.split()
            cc = bs[0]
            ccc = 1
            p = r''
            for c in bs[1:] + '2':
                if cc == c:
                    ccc += 1
                else:
                    if cc == '0':
                        p += r'A{'+str(ccc)+',}'
                    else:
                        p += r'(?:A{' + str(ccc) + ',}|B{' + str(ccc) + ',})'
                        
                    cc = c
                    ccc = 1

            print l, bs, p
                    
            if re.match(p + '$', ls):
                print 'Yes'

            else:
                print 'No'

    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

