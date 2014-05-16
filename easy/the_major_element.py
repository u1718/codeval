#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            nums = [0 for i in xrange(100)]
            no_nums = 0
            for s in map(int, l.split(',')):
                nums[s] += 1
                no_nums += 1

            maxnumocc = max(nums)
            if maxnumocc > no_nums / 2:
                print nums.index(maxnumocc) 
            else:
                print 'None'
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
