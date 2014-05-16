#!/usr/bin/env python
import sys

def main():
    for i in xrange(1, 13):
        row = ''
        for j in xrange(1, 13):
            row += format(i * j, '4d')

        print row
        
    return 0
            
if __name__ == '__main__':
    sys.exit(main())
