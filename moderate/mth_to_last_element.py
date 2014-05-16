#!/bin/env python

# Mth to last element
# Challenge Description:

# Write a program to determine the Mth to last element of a list.
# Input sample:

# The first argument will be a path to a filename containing a series of space delimited characters followed by an integer representing a index into the list (1 based), one per line. E.g.

# a b c d 4
# e f g h 2

# Output sample:

# Print to stdout, the Mth element from the end of the list, one per line. If the index is larger than the list size, ignore that input. E.g.

# a
# g

# Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
# Sponsored Challenge Eligibility

# In order to be eligible to push solution to the employer (HireVue), you must satisfy the following conditions:

#     Location: United States
#     Minimum Education: High School
#     Your email / resume will always be sent to the employer

import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            d = l.rstrip('\n').split()
            if int(d[-1]) < len(d):
                print ' '.join(d[len(d) - int(d[-1]) - 1])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    