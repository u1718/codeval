#!/usr/bin/env python
import sys

def main():
    n = 1000
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

    print filter(lambda e: e[1] and e[0] // 100 == e[0] % 10, [(e,n) for e,n in enumerate(isPrime)])[-1][0]
    
    return 0
            
if __name__ == '__main__':
    sys.exit(main())
