#!/bin/env python

import sys

"""
    Distinct Subsequences
    Challenge Description:

    A subsequence of a given sequence S consists of S with zero or more elements deleted. Formally, a sequence Z = z1z2..zk is a subsequence of X = x1x2...xm, if there exists a strictly increasing sequence of indicies of X such that for all j=1,2,...k we have Xij = Zj. E.g. Z=bcdb is a subsequence of X=abcbdab with corresponding index sequence <2,3,5,7>
    Input sample:

    Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated strings. The first is the sequence X and the second is the subsequence Z. E.g.

    babgbag,bag
    rabbbit,rabbit

    Output sample:

    Print out the number of distinct occurrences of Z in X as a subsequence E.g.

    5
    3

"""
    
def search(s, p):
    count = 0
    if len(p) == 1:
        count = s.count(p)

    else:
        for i in range(len(s)):
            if(s[i] == p[0]):
                count += search(s[i + 1 :],p[1 :])
                
    return count

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            string, pattern = l.strip('\n').split(',')
            print search(string, pattern)
                        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
                