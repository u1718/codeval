#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ws, dc = [e.split() for e in l.rstrip('\n').split(';')]
            wd = ['' for i in range(len(ws))]

            for i, j in enumerate([int(e) - 1 for e in dc]):
                wd[j] = ws[i]

            j = 0
            for i,e in enumerate(wd):
                if e:
                    continue
                else:
                    wd[i] = ws[len(dc) + j]
                    j += 1

            print ' '.join(wd)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    