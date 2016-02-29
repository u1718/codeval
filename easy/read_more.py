#!/usr/bin/env python
"""https://www.codeeval.com/open_challenges/167/
Read More

Challenge Description:

You are given a text. Write a program which outputs its lines according
to the following rules:

    1) If line length is <= 55 characters, print it without any changes.
    2) If the line length is > 55 characters, change it as follows.
        1) Trim the line to 40 characters.
        2) If there are spaces ' ' in the resulting string, trim it once again
           to the last space (the space should be trimmed too).
        3) Add a string '... <Read More>'' to the end of the resulting string
           and print it.

Input sample:

The first argument is a file. The file contains a text
For example:
Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face -
but he wouldn't look.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Tom's mouth watered for the apple, but he stuck to his work..

Output sample:

Print to stdout the text lines with their length limited according to the
rules described above.
For example:
Tom exhibited.
Amy Lawrence was proud and glad, and... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but... <Read More>

Constraints:

    1) The maximum length of a line in the input file is 300 characters.
    2) There cannot be more than one consequent space character in the
       input data.
"""

import sys

def main(dfile):
    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.rstrip()
            if len(l) > 55:
                try:
                    ep = l[:40].rindex(' ')
                    print l[:ep].rstrip() + '... <Read More>'

                except ValueError:
                    print l[:40] + '... <Read More>'
                    
            else:
                print l
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))