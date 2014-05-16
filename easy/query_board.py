#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        m = [[0 for i in range(256)] for j in range(256)]
        for l in f:
            op = l.rstrip('\n').split()
            if op[0] == 'SetCol':
                i = int(op[1])
                v = int(op[2])
                for j in range(256):
                    m[i][j] = v
            elif op[0] == 'SetRow':
                j = int(op[1])
                v = int(op[2])
                for i in range(256):
                    m[i][j] = v
            elif op[0] == 'QueryCol':
                print sum(m[int(op[1])])
            elif op[0] == 'QueryRow':
                print sum([m[i][int(op[1])] for i in range(256)])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))