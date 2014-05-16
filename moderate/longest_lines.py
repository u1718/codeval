#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        n = int(f.readline())
        ll = []
        for l in f:
            ll.append(l)
            ll.sort(key=len, reverse=True)
            ll = ll[:n]

        print ''.join(ll)
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
