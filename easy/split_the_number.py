#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            num, pat = l.split()
            exp = ''
            st = 1
            for c in pat:
                if c.isalpha():
                    n = num[ord(c) - ord('a')]
                    if st and int(n) or not st:
                        exp += n
                        st = 0
                        
                else:
                    if st:
                        exp += '0'
                        
                    st = 1
                    exp += c

            if st:
                exp += '0'
                
            print eval(exp)
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
