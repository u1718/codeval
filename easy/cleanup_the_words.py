#!/bin/env python3

"""https://www.codeeval.com/open_challenges/205/

Clean up the words

Challenge Description:

You have a list of words. Letters of these words are mixed with extra symbols,
so it is hard to define the beginning and end of each word. Write a program that
will clean up the words from extra numbers and symbols.

Input sample:

The first argument is a path to a file. Each line includes a test case with a
list of words: letters are both lowercase and uppercase, and are mixed with
extra symbols.

For example:

(--9Hello----World...--)
Can 0$9 ---you~
13What213are;11you-123+138doing7

Output sample:

Print the cleaned up words separated by spaces in lowercase letters.

For example:

hello world
can you
what are you doing

Constraints:

   1 Print the words separated by spaces in lowercase letters.
   2 The length of a test case together with extra symbols can be in a range from
      10 to 100 symbols.
   3 The number of test cases is 40.
"""

import sys
import re

def main(dfile):
    """Clean up the words
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        p = re.compile(r'([a-z]+)', re.I)
        for l in f:
            m = [w.lower() for w in re.findall(p, l)]
            print(' '.join(m))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
