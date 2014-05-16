#!/usr/bin/env python
#https://www.codeeval.com/open_challenges/136/
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        p = -1
        for l in f:
            try:
                np = l.index('C')
            except ValueError:
                np = l.index('_')

            if np == p or p == -1:
                t = '|'
            elif np < p:
                t = '/'
            else:
                t = '\\'

            p = np
            print l[:p] + t + l[min(p+1, 12):12]
                
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
