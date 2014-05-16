#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            a, p1, p2 = map(int, l.split(','))
            print 'true' if a >> (p1 - 1) & 1 == a >> (p2 - 1) & 1 else 'false'
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
