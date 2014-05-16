#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n = int(l.rstrip('n'))
            print 0 if n % 2 else 1 

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))