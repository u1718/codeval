#!/bin/env python

"""Working experience
    Challenge Description:

    You're building a new social platform and you want to store user's working experience. You've decided to calculate the total experience in years for each user based on the time periods entered by users. Using this approach you need to be sure that you're taking into account overlapping time periods in order to retrieve an actual working experience in years. E.g.
    Jan 2010-Dec 2010
    Jan 2010-Dec 2010
    Two jobs with 12 months of experience each, but the actual work experience is 1 year, because of overlapping time periods. The challenge is to calculate the actual working experience based on the list of time intervals.
    Input sample:
Feb 2004-Dec 2009; Sep 2004-Jul 2008
Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-Nov 2004; Apr 2014-Jan 2015
Mar 2003-Jul 2003; Nov 2003-Jan 2004; Apr 1999-Nov 1999
Apr 1992-Dec 1993; Feb 1996-Sep 1997; Jan 2002-Jun 2002; Sep 2003-Apr 2004; Feb 2010-Nov 2011
Feb 2004-May 2004; Jun 2004-Jul 2004

    Your program should accept as its first argument a path to a filename. Each line of the file contains a list of time periods separated by a semicolon with and a single whitespace. Each period is represented by begin date and end date. Each date consists of a month as an abbreviated name and a year with century as a decimal number separated by a single white space. The begin and end dates are separated by dash ("-"). E.g.
    Output sample:
5
4
1
6
0

    For each test case print out the actual work experience in a full years. E.g.

    Constraints:
    The number of line in a file is in range [20, 40]
    The dates are in range [Jan 1990, Dec 2020]
    The end date > begin date.
    Assume that the day of begin date is the firs day of given month and the day of the end date is the last day of a given month.
"""

import sys

def main(dfile):
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    def encode_time_period(period):
        start, stop = map(lambda e: e.lstrip(), period.split('-'))
        return (months.index(start[:3]) + int(start[3:]) * 12,
                months.index(stop[:3]) + int(stop[3:]) * 12)

    with open(dfile, 'r') as f:
        for l in f:
            tp = [encode_time_period(e) for e in l.rstrip().split(';')]
            tp.sort(key=lambda e: e[0])
            awe = tp[0:1]
            for i in tp[1:]:
                j = awe[-1]
                if i[0] <= j[1]:
                    awe[-1] = ((j[0], max(i[1], j[1])))
                else:
                    awe.append(i)

            print sum([e - s + 1 for s, e in awe]) / 12
            
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
    
        