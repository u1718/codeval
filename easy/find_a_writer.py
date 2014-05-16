#!/bin/env python

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            if l == '\n':
                continue
                
            s, k = l.strip('\n').split('|')
            key = [int(e) for e in k.split()]
            wn = ''
            for i in key:
                wn += s[i - 1]

            print wn
                
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))