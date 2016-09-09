#!/bin/env python3

"""https://www.codeeval.com/open_challenges/217/

One zero, two zeros...

Challenge Description:

Our agent uncovered a global criminal money-laundering network that used
offshore companies to defraud international organizations of total
$1,000,000,000! The agent changes his location each hour, but he manages to send
us the code that we need to decipher.
Deciphering code includes many stages, and you are taking part in one of them.
Therefore, your task is the following: you have two numbers – the first one is
the number of zeros in a binary code and the second one shows the range from 1
to this number, where you have to find these zeros.
For example, for the given numbers 2 and 4, you convert all numbers from 1 to 4
inclusive into the binary system. As a result, you get 1, 10, 11, and 100. As
the first given number is 2, this means that we are looking for numbers with two
zeros, so only 100 suits us. Hence, the result will be 1: there is only one
number with two zeros.

Input sample:

The first argument is a path to a file. Each line includes a test case with two
numbers: the first one is the number of zeros in a binary code that we need to
find and the second one is the range from 1 to this number where you have to
find these zeros.

For example:

1 8
2 4

Output sample:

Print the total number of numerals that contain the needed amount of zeros in a
binary system.

For example:

3
1

Constraints:

   1 Range can be from 5 to 1000.
   2 Number of zeros does not exceed the length of binary code number.
   3 The number of test cases is 40.
"""

import sys

def main(dfile):
    """One zero, two zeros...
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            nz, nn = [int(n) for n in l.strip().split()]
            print([nz == '{:b}'.format(i).count('0')
                       for i in range(1, nn + 1)].count(True))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
