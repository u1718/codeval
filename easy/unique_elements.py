#!/usr/bin/env python
"""https://www.codeeval.com/open_challenges/29/

Unique Elements

Challenge Description:

You are given a sorted list of numbers with duplicates. Print out the sorted
list with duplicates removed.

Input sample:

File containing a list of sorted integers, comma delimited, one per line. E.g.

1,1,1,2,2,3,3,4,4
2,3,4,5,5

Output sample:

Print out the sorted list with duplicates removed, one per line.
E.g.

1,2,3,4
2,3,4,5
"""
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        """Unique Elements
        @param dfile: data file path
        @type of dfile: str
        """


        for l in f:
            print ','.join(sorted(list(set(l.rstrip('\n').split(','))), key=int))
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
