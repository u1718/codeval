#!/usr/bin/env python

"""https://www.codeeval.com/open_challenges/147/
Lettercase Percentage Ratio
Challenge Description:

Your goal is to find the percentage ratio of lowercase and uppercase letters in
line below.

Input sample:
thisTHIS
AAbbCCDDEE
N
UkJ

Your program should accept as its first argument a path to a filename.
Each line of input contains a string with uppercase and lowercase letters E.g.:

Output sample:
lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67

For each line from input, print the percentage ratio of uppercase and lowercase
letters rounded to the second digit after the dot. E.g.:

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl|
php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua)
or use the online editor.
"""

import sys

def main(dfile):
    """Lettercase Percentage Ratio
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            line = l.strip('\n')
            ratio_of_uppercase_letters = round(reduce(lambda s, c: s + int(c.isupper()), line, 0) * 100.0 / len(line), 2)
            print "lowercase: {} uppercase: {}".format(100 - ratio_of_uppercase_letters, ratio_of_uppercase_letters)
    
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))