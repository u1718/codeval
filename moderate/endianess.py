#!/bin/env python

# Endianness
# Challenge Description:

# Write a program to print out the endianness of the system.
# Input sample:

# None
# Output sample:

# Print to stdout, the endianness, wheather it is LittleEndian or BigEndian.
# e.g.

# BigEndian

import sys


if __name__ == '__main__':
    print 'BigEndian' if sys.byteorder == 'big' else 'LittleEndian'
    sys.exit(0)
    