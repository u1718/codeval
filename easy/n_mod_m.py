#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n, m = map(int, l.rstrip('\n').split(','))
            while n >= m:
                n -= m

            print n
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
