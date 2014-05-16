#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ab = [s.strip() for s in l.split(',')]
            if len(ab) == 2 and ab[1] == ab[0][ -len(ab[1]) :]:
                print 1
            else:
                print 0
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
