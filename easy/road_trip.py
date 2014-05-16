#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            dist = [int(e[e.index(',') + 1 : ]) for e in l.split(';')[:-1]]
            dist.sort()
            print ','.join([format(a - b, 'd') for a, b in zip(dist, [0] + dist)])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

