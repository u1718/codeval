#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/220/

Trick or Treat

Challenge Description:

Everyone knows what Halloween is and how children love it. Children in costumes
travel from house to house asking for treats with a phrase "Trick or treat".
After that, they divide the treats equally among all. This year, they collected
tons of candies, and need your help to share everything equally.
You know that children receive different number of candies depending on their
costume: vampire gets 3 candies from one house, zombie – 4 candies, and witch –
5 candies.
That is, three children in three different costumes get 3+4+5=12 candies from
one house.

Input sample:

The first argument is a path to a file. Each line includes a test case with
number of vampires, zombies, witches, and houses that they visited.

For example:

Vampires: 1, Zombies: 1, Witches: 1, Houses: 1
Vampires: 3, Zombies: 2, Witches: 1, Houses: 10

Output sample:

You need to print number of candies that each child will get. If the number is
not integer, round it to the lower: for example, if the resulting number is
13.666, round it to 13.

For example:

4
36

Constraints:

   1 Number of vampires, zombies, witches, and houses can be from 0 to 100.
   2 If the final number of candies is not integer, round it to the lower.
   3 The number of test cases is 40.
"""

import sys

def main(dfile):
    """Trick or Treat
    @param dfile: data file path
    @type of dfile: str
    """

    import re
    p = re.compile(r'^Vampires: (\d+), '
                       'Zombies: (\d+), '
                       'Witches: (\d+), '
                       'Houses: (\d+)$',
                       re.ASCII)
    
    with open(dfile, 'r') as dfld:
        for l in dfld:
            m = p.match(l)
            a = [int(i) for i in  m.groups()]
            print(int((a[0] * 3 + a[1] * 4 + a[2] * 5) * a[3] / sum(a[:3])))
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
