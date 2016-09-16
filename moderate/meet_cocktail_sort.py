#!/bin/env python3

"""https://www.codeeval.com/open_challenges/231/

Meet Cocktail sort

Challenge Description:

Quite often we need to arrange items in a certain order: numbers in an ascending
or descending order, words – in an alphabetical order, people – according to
their height, and so on. There are many different sorting algorithms. Some of
them are quick, while others seem to suit in a particular case only.
In this challenge, your task is to use a cocktail sort.

Input sample:

The first argument is a path to a file. Each line includes a test case with
numbers that you need to order using cocktail sort. There is also a number of
iterations for an algorithm to carry out. The numbers themselves and the number
of iterations are separated by a pipeline '|'.

5 4 9 10 7 3 2 1 6 | 1
9 8 7 6 5 4 3 2 1 | 3

Output sample:

Print sorted numbers after they pass the required number of iterations. One
iteration of a cocktail sort is a pass through the list of numbers in both
directions: from the beginning to the end and from the end to the beginning.

1 4 5 9 7 3 2 6 10
1 2 3 6 5 4 7 8 9

Constraints:

   1 The number of iterations can be from 1 to 30.
   2 One iteration of a cocktail sort is a pass through the list of numbers in
     both directions: from the beginning to the end and from the end to the
     beginning.
   3 The number of test cases is 40.

"""

import sys

def main(dfile):
    """Meet Cocktail sort
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
                    if l[-j - 1] < l[-j -2]:
                        l[-j - 1], l[-j -2] = l[-j -2], l[-j - 1]
                    if l[j] > l[j + 1]:
                        l[j], l[j + 1] = l[j + 1], l[j]

            print(' '.join([str(e) for e in l]))
                        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
