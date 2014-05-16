#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            sar = l.rstrip('\n').split()
            print ' '.join([e.capitalize() for e in sar])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

    