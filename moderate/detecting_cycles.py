#!/bin/env python
# http://en.wikipedia.org/wiki/Cycle_detection

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            seq = l.rstrip('\n').split()

            print ' '.join(seq[len(seq) - seq[-2::-1].index(seq[-1]) -1 : ])

        return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    