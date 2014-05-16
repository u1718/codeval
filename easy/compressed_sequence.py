#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            m = ''
            nn = 0
            s = ''
            for n in (l + ' .').split():
                if n == m:
                    nn += 1
                else:
                    s += '{} {} '.format(nn, m) if m else ''
                    m = n
                    nn = 1

            print s
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
