#!/bin/env python

import sys
 
def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n = int(l.rstrip('\n'))
            rn = ''
            for d, r in zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
                            ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']):

                while n >= d:
                    rn += r
                    n -= d

            print rn
                
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    