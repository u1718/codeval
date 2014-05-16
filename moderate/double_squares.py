#!/bin/env python

"""Double Squares

Challenge Description:

Credits: This challenge appeared in the Facebook Hacker Cup 2011.

A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares. For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2.
NOTE: Do NOT attempt a brute force approach. It will not work. The following constraints hold:
0 <= X <= 2147483647
1 <= N <= 100

Input sample:

Your program should accept as its first argument a path to a filename. You should first read an integer N, the number of test cases. The next N lines will contain N values of X.

5
10
25
3
0
1

Output sample:

E.g.

1
2
0
1
1

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
Sponsored Challenge Eligibility

In order to be eligible to push solution to the employer (WhiteTruffle), you must satisfy the following conditions:

    Location: United States
    Minimum Education: High School
    Your email / resume will always be sent to the employer

http://mmmf.msu.ru/lect/spivak/summa_sq.pdf, pp 35-36
"""
import sys
import math

def main(dfile):
    with open(dfile, 'r') as f:
        l = int(math.sqrt(2147483647))
        f.readline()
        m = f.readlines()

        er_sieve = [1 for i in xrange(l + 1)]
        er_sieve[0] = er_sieve[1] = 0
        i = 2
        while i*i <= l:
            if er_sieve[i]:
                j = i*i
                while j <= l:
                    er_sieve[j] = 0
                    j += i

            i += 1

        prime1 = filter(lambda e: e % 4 == 1, [i if e else 0 for i,e in enumerate(er_sieve)])
        prime3 = filter(lambda e: e % 4 == 3, [i if e else 0 for i,e in enumerate(er_sieve)])

        for n in m:
            n = int(n.rstrip('\n'))
            if n == 0 or n == 1:
                print 1
                continue
                
            pow3 = []
            nn = n
            for p in prime3:
                if p > nn:
                    break
                    
                pp = 0
                while nn % p == 0:
                    nn /= p
                    pp += 1

                if pp > 0:
                    pow3.append(pp)

            pow1 = []
            nn = n
            for p in prime1:
                if p > nn:
                    break
                    
                pp = 0
                while nn % p == 0:
                    nn /= p
                    pp += 1

                if pp > 0:
                    pow1.append(pp)

            b = reduce(lambda x, y: x * y, [j + 1 for j in pow1]) if pow1 else 1
            if any([e % 2 for e in pow3]):
                nr2 = 0
            elif any([e % 2 for e in pow1]):
                nr2 = b / 2
            else:
                nr2 = (b + 1) / 2
                
            print nr2
                
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))