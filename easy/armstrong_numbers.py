#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n = l.rstrip('\n')
            p = len(n)
            n = int(n)
            m = n
            sp = 0
            while m > 0:
                sp += pow(m % 10, p)
                m //= 10
                
            print sp == n
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
