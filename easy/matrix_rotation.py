#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/178/
#  Matrix Rotation

import sys
import math

def main(dfile):
    """Matrix Rotation
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            v = l.rstrip().split(' ')
            d = int(math.sqrt(len(v)))
            
            m = []
            for i in xrange(d):
                m.append([])
                for j in xrange(d):
                    m[i].append(v[d * i + j])

            r = []
            for i in xrange(d):
                r.append([])
                for j in xrange(d):
                    r[i].append(m[d - 1 - j][i])

            print ' '.join([' '.join(e) for e in r]);

    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
