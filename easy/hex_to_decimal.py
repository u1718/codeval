#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            print format(int(l[:-1], 16), 'd')
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
