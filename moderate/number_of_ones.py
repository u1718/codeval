#!/bin/env python

# Number of Ones
# Challenge Description:

# Write a program to determine the number of 1 bits in the internal representation of a given integer.
# Input sample:

# The first argument will be a path to a filename containing an integer, one per line. E.g.

# 10
# 22
# 56

# Output sample:

# Print to stdout, the number of ones in the binary form of each number. E.g.

# 2
# 3
# 3

# Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
# Sponsored Challenge Eligibility

# In order to be eligible to push solution to the employer (PeopleNet), you must satisfy the following conditions:

#     Location: United States
#     Minimum Education: High School
#     Your email / resume will always be sent to the employer

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            n = int(l.rstrip('\n'))
            noo = 0
            while n > 0:
                noo += n & 1
                n >>= 1

            print noo

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))