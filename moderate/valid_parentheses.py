#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/68/

Valid parentheses

Challenge Description:

Given a string comprising just of the characters (,),{,},[,] determine if it is
well-formed or not.

Input sample:

Your program should accept as its first argument a path to a filename. Each line
in this file contains a string comprising of the characters mentioned above.
E.g.

()
([)]

Output sample:

Print out True or False if the string is well-formed. E.g.

True
False
"""

import sys

def main(dfile):
    """Valid parentheses
    @param dfile: data file path
    @type of dfile: str
    """
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            q = []
            for e in l:
                if e in '({[':
                    q.append(e)
                else:
                    if not q:
                      q = [0]
                      break
                    
                    if e == ')' and q[-1] == '(' or\
                       e == '}' and q[-1] == '{' or\
                       e == ']' and q[-1] == '[':
                      q = q[:-1]
                    else:
                      q = [0]
                      break

            if q:
                print('False')
            else:
                print('True')
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
