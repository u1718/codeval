#!/bin/env python

"""Pass Triangle

Challenge Description:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5

5 + 9 + 6 + 7 = 27

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

5
9 6
4 6 8
0 7 1 5

You make also check full input file which will be used for your code evaluation.

Output sample:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be

27

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
Sponsored Challenge Eligibility

In order to be eligible to push solution to the employer (Yodle), you must satisfy the following conditions:

    Location: United States
    Minimum Education: High School
    Your email / resume will always be sent to the employer
"""

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        triangle = [map(int, l.rstrip('\n').split()) for l in f.readlines()]

        s = triangle[-1]
        for r in reversed(triangle[:-1]):
            ss = []
            for i in xrange(len(r)):
                ss.append(max(r[i] + s[i], r[i] + s[i + 1]))

            s = ss

        print s[0]
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
