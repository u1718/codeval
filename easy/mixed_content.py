#!/usr/bin/env python
"""https://www.codeeval.com/open_challenges/115/

Mixed Content

Challenge Description:

You have a string of words and digits divided by comma. Write a program which
separates words with digits. You shouldn't change the order elements.

Input sample:

Your program should accept as its first argument a path to a filename.
 Input example is the following

8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
24,13,14,43,41

Output sample:

melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
24,13,14,43,41

As you cas see you need to output the same input string if it has words only or
digits only.
"""
import sys

def main(dfile):
    """Mixed Content
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as f:
        for l in f:
            ws, ds = [], []
            wd = l.rstrip('\n').split(',')
            for e in wd:
                try:
                    int(e, 10)
                except ValueError:
                    ws.append(e)
                else:
                    ds.append(e)

            print ','.join(ws) + ('|' if ws and ds else '') + ','.join(ds)
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
