#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            sq, swop = l.rstrip('\n').split(':')
            sq = sq.split()
            for o in swop.split(','):
                lf, rt  = [int(p) for p in o.split('-')]
                sq[lf], sq[rt] = sq[rt], sq[lf]

            print ' '.join(sq)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))