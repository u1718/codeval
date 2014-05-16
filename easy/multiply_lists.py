#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ls1, ls2 = [[int(j) for j in i.split()] for i in l.rstrip('\n').split('|')]
            print ' '.join([str(i * j) for i, j in zip(ls1, ls2)])

    return

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    