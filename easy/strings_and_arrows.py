#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/203/

Strings and arrows

Challenge Description:

You have a string composed of the following symbols: '>', '<', and '-'. Your
task is to find, count, and print to the output a number of arrows in the
string. An arrow is a set of the following symbols: '>>-->' or '<--<<'.
Note that one character may belong to two arrows at the same time. Such example
is shown in the line #1.

Input sample:

The first argument is a path to a file. Each line includes a test case with a
string of different length from 10 to 250 characters. The string consists of
'>', '<', and '-' symbols.

For example:

<--<<--<<
<<>>--><--<<--<<>>>--><
<-->>

Output sample:

Print the total number of found arrows for each test case.

For example:

2
4
0

Constraints:

   1 An arrow is a set of the following symbols: '>>-->' or '<--<<'.
   2 One symbol may belong to two arrows at the same time.
   3 The number of test cases is 40.
"""

import sys

def main(dfile):
    """Strings and arrows
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            nra = 0
            nla = 0
            state = 'Start'
            for e in l:
                if e == '>':
                    if state == '>':
                        state = '>>'
                    elif state == '>>':
                        state = '>>'
                    elif state == '>>--':
                        nra += 1
                        state = '>'
                    else:
                        state = '>'

                elif e == '<':
                    if state == '<':
                        state = '<'
                    elif state == '<--':
                        state = '<--<'
                    elif state == '<--<':
                        nla += 1
                        state = '<'
                    else:
                        state = '<'

                elif e == '-':
                    if state == '>>':
                        state = '>>-'
                    elif state == '>>-':
                        state = '>>--'
                    elif state == '<':
                        state = '<-'
                    elif state == '<-':
                        state = '<--'
                    elif state == '<--<':
                        state = '<-'
                    else:
                        state = 'Start'

            print(nra + nla)

            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
