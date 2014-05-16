#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            s = [ c if c.isdigit() else str(ord(c) - 97)   for c  in filter(lambda c: c.isdigit() or c in 'abcdefghij', l)]
            print ''.join(s) if s else 'NONE'
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
