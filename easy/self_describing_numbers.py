#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            s = l.rstrip('\n')
            print 1 if all(str(s.count(str(d))) == c for d, c in enumerate(s)) else 0
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
