#!/bin/env python

import sys
import re

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            bs, ls = l.split()
            p = r''
            for d in bs:
                if d == '0':
                    p += r'A+'
                else:
                    p += r'(?:A+|B+)'

            print p
            m = re.match(p + r'$', ls)
            print 'Yes' if m else 'No'
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

