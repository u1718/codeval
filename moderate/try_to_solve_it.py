#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/226/

Try to solve it

Challenge Description:

The history of cryptography has about four thousand years. It dates back to the
days of the Ancient Rome and continues up till our times. Over the years, a
countless number of methods and encryption algorithms have emerged. However, as
hackers say, there is nothing impossible to hack or decipher. Try your hand at
decoding the code below and see how quickly you will get it right!
So, you have to determine the encryption algorithm of the message below and
print the decoded word. If you find the task too difficult, get a hint at the
bottom of the page.

Input sample:

The first argument is a path to a file. Each row includes a test case with an
encoded word.

mke
mh
lhsby
pm

Output sample:

You have to print the decoded word.

try
to
solve
it

Constraints:

   1 The word can include from 2 to 40 symbols.
   2 All letters are lowercase.
   3 If you need a hint, select the text at the bottom of the page.
   4 The number of test cases is 40.

Hint (select text below):
a | b | c | d | e | f | g | h | i | j | k | l | m
u | v | w | x | y | z | n | o | p | q | r | s | t 

"""

import sys

def main(dfile):
    """Try to solve it
    @param dfile: data file path
    @type of dfile: str
    """

    trans_table = str.maketrans('abcdefghijklmuvwxyznopqrst',
                                'uvwxyznopqrstabcdefghijklm', '\n')
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            print(l.translate(trans_table))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
