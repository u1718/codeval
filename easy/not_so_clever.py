#!/bin/env python3

"""https://www.codeeval.com/open_challenges/232/

Not so clever

Challenge Description:

Imagine that you have to arrange items in a certain order: pencils from black
to white in a color palette, photographs by the date taken, banknotes from the
highest to the lowest, etc. To do this, you definitely don’t need to use the
Stupid sort algorithm.

After each action, you need to come back to the beginning and start all over
again. Not so clever, is it? But, you need to know about this algorithm, that’s
why it is used in this challenge.

Input sample:

The first argument is a path to a file. Each line includes a test case which
contains numbers that you need to sort using the Stupid sort algorithm. There is
also a number of iterations for an algorithm to carry out. The numbers
themselves and the number of iterations are separated by a pipeline '|'.

4 3 2 1 | 1
5 4 3 2 1 | 2

Output sample:

Print sorted numbers after they pass the required number of iterations. One
iteration of this sort is a pass to the moment of making changes. Once changing
the order of the digits, passing starts from the very beginning. Hence, this is
another iteration.

3 4 2 1
4 3 5 2 1

Constraints:

    The number of iterations can be from 1 to 8.
    One iteration of this sort is a pass to the moment of making changes.
    The number of test cases is 40.

"""

import sys

def main(dfile):
    """Not so clever
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            l, it = l.strip().split(' | ')
            l = [int(e) for e in l.split()]
            it = int(it)
            for i in range(it):
                for j in range(len(l) - 1):
                    if l[j] > l[j + 1]:
                        l[j], l[j + 1] = l[j + 1], l[j]
                        break

            print(' '.join([str(e) for e in l]))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
