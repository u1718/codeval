#!/usr/bin/env python3

"""https://www.codeeval.com/open_challenges/186/

Max Range Sum

Challenge Description:

Bob is developing a new strategy to get rich in the stock market. He wishes
to invest his portfolio for 1 or more days, then sell it at the right time to
maximize his earnings. Bob has painstakingly tracked how much his portfolio
would have gained or lost for each of the last N days. Now he has hired you to
figure out what would have been the largest total gain his portfolio could have
achieved.

For example:

Bob kept track of the last 10 days in the stock market. On each day, the
gains/losses are as follows:

7 -3 -10 4 2 8 -2 4 -5 -2

If Bob entered the stock market on day 4 and exited on day 8 (5 days in total),
 his gains would have been

16 (4 + 2 + 8 + -2 + 4)

Input sample:
5;7 -3 -10 4 2 8 -2 4 -5 -2
6;-4 3 -10 5 3 -7 -3 7 -6 3
3;-7 0 -45 34 -24 7

The input contains N, the number of days (0 < N < 10000), followed by N
(separated by symbol ";") integers D (-10000 < D < 10000) indicating the gain or
loss on that day.

For example:
Output sample:
16
0
17

Print out the maximum possible gain over the period. If no gain is possible,
print 0.

For example:
Constraints:

  1. Gain or loss on that day is (-100 < D < 100).
  2. Number of days (0 < N < 100).
  3. Number of test cases is 20.
"""

import sys

def main(dfile):
    """Max Range Sum
    @param dfile: data file path
    @type of dfile: str
    """

    with open(dfile, 'r') as dfld:
        for l in dfld:
            l = l.strip('\n')
            ndays, gains = l.split(';')
            ndays = int(ndays)
            gains = [int(n) for n in  gains.split()]

            print(max(0, max([sum(a) for a in
                              [gains[i : i + ndays] for i in
                               range(0, len(gains) - ndays + 1)]])))

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
