#!/bin/env python

"""Email Validation

Challenge Description:

You are given several strings that may/may not be valid emails. You should write a regular expression that determines if the email id is a valid email id or not. You may assume all characters are from the english language.

Input sample:

Your program should accept as its first argument a filename. This file will contain several text strings, one per line. Ignore all empty lines. E.g.

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com

Output sample:

Print out 'true' (all lowercase) if the string is a valid email. Else print out 'false' (all lowercase). E.g.

true
false
false
true

Submit your solution in a file (some file name).(py2| c| cpp| java| rb| pl| php| tcl| clj| js| scala| cs| m| py3| hs| go| bash| lua) or use the online editor.
Sponsored Challenge Eligibility

In order to be eligible to push solution to the employer (ModCloth), you must satisfy the following conditions:

    Location: United States
    Minimum Education: High School
    Your email / resume will always be sent to the employer
"""
import sys
import re

email = re.compile('^[a-z0-9.-]+@[a-z0-9-]+(\.[a-z0-9-]+)+$', re.IGNORECASE)

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            print 'true' if email.match(l) else 'false'

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))