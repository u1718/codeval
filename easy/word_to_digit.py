#!/bin/env python

import sys

def main(dfile):
    dw = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    with open(dfile, 'r') as f:
        for l in f:
            ws = l.rstrip('\n').split(';')
            ds = ''
            for e in ws:
                ds += dw[e]

            print ds

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    