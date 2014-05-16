#!/usr/bin/env python
import sys

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)

    
def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            print fib(int(l[:-1]))
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
