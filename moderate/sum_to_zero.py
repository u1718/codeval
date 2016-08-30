#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/81/

Sum to Zero

Challenge Description:

You are given an array of integers. Count the numbers of ways in which the sum
of 4 elements in this array results in zero.

Input sample:

Your program should accept as its first argument a path to a filename. Each line
in this file consist of comma separated positive and negative integers. E.g.

2,3,1,0,-4,-1
0,-1,3,-2

Output sample:

Print out the count of the different number of ways that 4 elements sum to zero.
E.g.

2
1
"""

import sys

def main(dfile):
    """Sum To Zero
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            matrix = [int(n) for n in l.split(',')]

            print([sum(e) for e in choose_iter(matrix,4)].count(0))
            
    return 0

def choose_iter(elements, length):
    """
    http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n/2837693#2837693
    """
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1 : len(elements)], length-1):
                yield (elements[i],) + next
                
def combinations(iterable, r):
    """
    https://docs.python.org/dev/library/itertools.html
    combinations('ABCD', 2) --> AB AC AD BC BD CD
    combinations(range(4), 3) --> 012 013 023 123
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    print(indices)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        print(indices)
        yield tuple(pool[i] for i in indices)
        
def combinations1(list, _):
    """
    Generate all combinations of the elements of list taken 4 at a time.
    """

    import itertools
    
    return itertools.combinations(list, 4)

def combinations2(list, _):
    """
    Generate all combinations of the elements of list taken 4 at a time.
    """

    for i in range(0, len(list) - 3):
        for j in range(i + 1, len(list) - 2):
            for k in range(j + 1, len(list) - 1):
                for z in range(k + 1, len(list)):
                    yield [list[e] for e in [i, j, k, z]]

    return None

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
