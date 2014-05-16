#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            sq = map(int, l.split())
            if len(sq) == 1:
                print 'Jolly'
                break
                
            ds = set([abs(a - b) for a, b in zip(sq, sq[1:])])
            if len(ds) == len(sq) - 1:
                print 'Jolly'
            else:
                print 'Not jolly'

            continue
            
            js = [1 for i in range(len(sq))]
            js[0] = 0 
            try:
                for a, b in zip(sq, sq[1:]):
                    js[abs(a-b)] = js[abs(a-b)] - 1 / js[abs(a-b)]

            except ZeroDivisionError:
                print 'Not jolly'
            else:
                print 'Jolly'
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
