#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            wa = l.rstrip('\n'). split()
            print wa[-2]

    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))