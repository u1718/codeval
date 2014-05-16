#!/bin/env python

"""Distinct Subsequences

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
    
import sys

class Error(Exception):
    pass

def main(dfile):
    import itertools
    
    with open(dfile, 'r') as f:
        for l in f:
            string, pattern = l.strip('\n').split(',')
            fp = [] #set()
            for ssi  in xrange(len(pattern), len(string) + 1):
                for cmb in itertools.combinations(range(len(string)), ssi):
                    sslice = ''.join([e for _,e in filter(lambda (i,e): i in cmb, enumerate(string))])
                    try:
                        i = -1
                        while True:
                            try:
                                i = sslice.index(pattern[0], i + 1)

                            except ValueError:
                                raise Error('no pattern found')
                                
                            if sslice == pattern:
                                fp.append(cmb[i:len(pattern)])

                    except Error:
                        continue


            print len(set(fp))
                        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
                