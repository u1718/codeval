#!/bin/env python

import sys
from math import sqrt
from ast import literal_eval

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            p1, p2 = literal_eval(l.replace(')', '),'))
            print int(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    