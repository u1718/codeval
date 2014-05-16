#!/usr/bin/env python
import sys
import math

def main():
    n = 1000
    n = int(n * math.log(n) + n * math.log(math.log(n)))
    
    isPrime = [True for i in range(0, n)]
    isPrime[1] = False
    i = 2
    while i*i < n:
        if (isPrime[i]):
            j = i*i
            while j < n:
                isPrime[j] = False
                j += i
        
        i += 1

    print sum([p[0] for p in filter(lambda e: e[1], [(e,n) for e,n in enumerate(isPrime)])[:1001]])
    
    return 0
            
if __name__ == '__main__':
    sys.exit(main())
