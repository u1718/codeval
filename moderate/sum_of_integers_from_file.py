#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        tsum = 0
        for l in f:
            tsum += int(l)

        print tsum

        return 0
        
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
