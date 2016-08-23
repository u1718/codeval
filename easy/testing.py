#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/225/

Testing

Challenge Description:

In many teams, there is a person who tests a project, finds bugs and errors, and
prioritizes them. Now, you have the unique opportunity to try yourself as a
tester and test a product. Here, you have two strings - the first one is
provided by developers, and the second one is mentioned in design. You have to
find and count the number of bugs, and also prioritize them for fixing using the
following statuses: 'Low', 'Medium', 'High', 'Critical' or 'Done'.

Input sample:

The first argument is a path to a file. Each line includes a test case with two
strings separated by a pipeline '|'. The first string is the one the developers
provided to you for testing, and the second one is from design.

Heelo Codevval | Hello Codeeval
hELLO cODEEVAL | Hello Codeeval
Hello Codeeval | Hello Codeeval

Output sample:

Write a program that counts the number of bugs and prioritizes them for fixing
using the following statuses:

'Low' - 2 or fewer bugs;
'Medium' - 4 or fewer bugs;
'High' - 6 or fewer bugs;
'Critical' - more than 6 bugs;
'Done' - all is done;

Low
Critical
Done

Constraints:

   1 Strings are of the same length from 5 to 40 characters.
   2 Upper and lower case matters.
   3 The number of test cases is 40.

"""

import sys

def main(dfile):
    """Testing
    @param dfile: data file path
    @type of dfile: str
    """

    state = ['Critical' for i in range(0, 40)]
    state[0] = 'Done'
    state[1] = state[2] = 'Low'
    state[3] = state[4] = 'Medium'
    
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            s1, s2 = l.split(' | ')

            n = [ e1 == e2 for e1, e2 in zip(s1, s2)]
            print(state[n.count(False)])

            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
