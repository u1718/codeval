#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            set1, set2 = [e.split(',') for e in l.rstrip('\n').split(';')]
            #print ','.join(list(set(set1) & set(set2)))
            print ','.join(filter(lambda e: e in set2, set1))
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
