#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            l = l.rstrip('\n').lower()
            chfr = [l.count(c) for c in 'qwertyuiopasdfghjklzxcvbnm']
            print sum([f * i for f,i in zip(sorted(chfr, reverse=True), range(26,0,-1))])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
