#!/bin/env python3

"""https://www.codeeval.com/open_challenges/223/

Alternative reality

Challenge Description:

Have you even wondered about another life? Maybe there is an alternative reality
where different things are happening. Everything is almost the same, but still a
bit different…
You are walking in one reality, but driving the car in another. Here you like
golf, and there – basketball. In one reality you changed a $100 banknote to five
$20 banknotes, while in another – to ten $10 banknotes.
Today, your task is to count how many alternative versions of money change are
if you have 1¢, 5¢, 10¢, 25¢, and 50¢ coins.
So, if you have 11 cents that you need to change, you have four alternative ways
how to do it:

1+1+1+1+1+1+1+1+1+1+1
5+1+1+1+1+1+1
5+5+1
10+1

Input sample:

The first argument is a path to a file. Each line includes a test case with the
number of cents that you want to change.

100
4
17

Output sample:

Print the number of alternative ways to change money.

292
1
6

Constraints:

    Number of cents can be from 1 to 100.
    You have 1¢, 5¢, 10¢, 25¢, and 50¢ coins to do the change.
    The number of test cases is 30.

https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2
"""

import sys

def count_change(amount):
    return cc(amount, 4)

coins = [5, 10, 1, 50, 25] # order no any sence

def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    if amount < 0 or kinds_of_coins == -1:
        return 0

    return cc(amount, kinds_of_coins - 1) + \
      cc(amount - coins[kinds_of_coins], kinds_of_coins)

def main(dfile):
    """Alternative reality
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as f:
        for l in f:
            print(count_change(int(l.strip())))

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
