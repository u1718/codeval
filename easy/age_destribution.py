#!/usr/bin/env python

"""https://www.codeeval.com/open_challenges/152/
Age destribution
Challenge Description:

In this challenge, we are analyzing the ages of people
to determine their status.

If the age is from 0 to 2 the child should be with parents at home,
print : 'Home'
If the age is from 3 to 4 the child should visit preschool,
print : 'Preschool'
If the age is from 5 to 11 the child should visit elementary school,
print : 'Elementary school'
From 12 to 14: 'Middle school'
From 15 to 18: 'High school'
From 19 to 22: 'College'
From 23 to 65: 'Work'
From 66 to 100: 'Retirement'
If the age of the person less than 0 or more than 100 -
it might be an alien - print: "This program is for humans"

Input sample:
0
19

Your program should accept as its first argument a path to a filename.
Each line of input contains one integer - age of the person:

Output sample:
Home
College

For each line of input print out where the person is:

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl|
php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online
editor.
"""

import sys

def main(dfile):
    """Age destribution
    @param dfile: data file path
    @type of dfile: str
    """
    status = [(None, -1, "This program is for humans"),
              (0, 2, "Home"),
              (3, 4, "Preschool"),
              (5, 11, "Elementary school"),
              (12, 14, "Middle school"),
              (15, 18, "High school"),
              (19, 22, "College"),
              (23, 65, "Work"),
              (66, 100, "Retirement")]

    with open(dfile, 'r') as dfld:
        for l in dfld:
            age = int(l.strip('\n'))
            for from_age, to_age, status_age in status:
                if age <= to_age:
                    print status_age
                    break

            else:
                print "This program is for humans"
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))