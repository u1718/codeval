#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            p = l[0]
            for c in l[1:].rstrip('\n'):
                if c == p[0]:
                    break

                p += c
            
            print len(p)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    