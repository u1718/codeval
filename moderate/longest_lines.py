#!/usr/bin/env python
"""Longest Lines
Challenge Description:

Write a program to read a multiple line text file and write the 'N' longest lines to stdout. Where the file to be read is specified on the command line.
Input sample:
2
Hello World
CodeEval
Quick Fox
A
San Francisco

Your program should read an input file (the first argument to your program will be a path to a filename). The first line contains the value of the number 'N' followed by multiple lines. You may assume that the input file is formatted correctly and the number on the first line i.e. 'N' is a valid positive integer. E.g.
Output sample:
San Francisco
Hello World

The 'N' longest lines, newline delimited. Ignore all empty lines in the input. Ensure that there are no trailing empty spaces on each line you print. Also ensure that the lines are printed out in decreasing order of length i.e. the output should be sorted based on their length. E.g.

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
"""

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        n = int(f.readline())
        ll = []
        for l in f:
            ll.append(l)
            ll.sort(key=len, reverse=True)
            ll = ll[:n]

        print ''.join(ll)
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
