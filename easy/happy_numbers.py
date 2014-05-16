#!/usr/bin/env python
import sys


def sqsum(n):
    ss = 0
    while n > 0:
        m = n % 10
        n = (n - m) / 10
        ss += m * m

    return ss

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n = int(l.rstrip('\n'))
            s = set()
            while n != 1:
                sl = len(s)
                s.add(n)
                if sl == len(s):
                    n = 0
                    break
                    
                n = sqsum(n)

            print n
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
