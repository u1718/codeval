#!/bin/env python3

"""https://www.codeeval.com/open_challenges/199/

String mask

Challenge Description:

You’ve got a binary code which has to be buried among words in order to
unconsciously pass the cipher.
Create a program that would cover the word with a binary mask. If, while
covering, a letter finds itself as 1, you have to change its register to the
upper one, if it’s 0, leave it as it is. Words are always in lower case and in
the same row with the binary mask.

Input sample:

The first argument is a path to a file. Each row contains a test case with a
word and a binary code separated with space, inside of it. The length of each
word is equal to the length of the binary code.

For example:

hello 11001
world 10000
cba 111

Output sample:

Print the encrypted words without binary code.

For example:

HEllO
World
CBA

Constraints:

    Words are from 1 to 20 letters long.
    The number of test cases is 40.

"""

import sys

def main(dfile):
    """String mask
    @param dfile: data file path
    @type of dfile: str
    """
    with open(dfile, 'r') as f:
        for l in f:
            word, cipher = l.strip().split()
            print(''.join([c.upper() if z == '1' else c
                               for c, z in zip(word, cipher)]))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
