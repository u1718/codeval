#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/238/

Code combinations

Challenge Description:

You definitely know the game where you have to make as many words from the
given letters as possible. In our case, the rules are a bit different: you need
to check whether it is possible to make the word 'code' with the four given
letters, and, if possible, count how many times you can do this. Letters can be
in a various order.

Solution example:

| * * * * |
| * c o * |     | c o |  =  1
| * d e * |     | d e |

Input sample:

The first argument is a path to a file. Each line includes a test case with
symbol matrix. Each line of the matrix is separated by a pipeline '|'.

**** | *co* | *de* | ****
codx | decx
co | dx

Output sample:

You need to calculate and print a number that will tell how many times you can
make the word ‘code’ from the letters in the matrix, using a 2x2 submatrix.

1
2
0

Constraints:

   1 The number of rows or columns in the matrix can be from 2 to 10.
   2 Matrix can include one face for 2 solutions in case.
     | c o d x |     | c o |     | o d |  =  2
     | d e c x |     | d e |     | e c |

   3 The number of test cases is 40.

"""

import sys

def main(dfile):
    """Code combinations
    @param dfile: data file path
    @type of dfile: str
    """
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            matrix = l.split(' | ')
            num = 0
            for row in range(0, len(matrix) - 1):
                for col in range(0, len(matrix[0]) - 1):
                    m2x2 = matrix[row][col : col + 2] +\
                           matrix[row + 1][col : col + 2]

                    if 'c' in m2x2 and\
                       'o' in m2x2 and\
                       'd' in m2x2 and\
                       'e' in m2x2:
                       num += 1

            print(num)
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
