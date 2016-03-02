#!/usr/bin/env python

"""https://www.codeeval.com/open_challenges/237/
"""

import sys

def main(dfile):
    """Panacea - truth or lie
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            numVir, numAntiVir = [e.split() for e in l.rstrip().split('|')]

            print sum([int(e, 16) for e in numVir]) <= \
                  sum([int(e,  2) for e in numAntiVir])
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))