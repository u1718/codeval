#!/usr/bin/env python
import unittest

def fzbz(a, b, n):
    bids = ''
    for i in range(1, n + 1):
        if i % a == 0:
            if i % b == 0:
                bids += 'FB '
            else:
                bids += 'F '
        elif i % b == 0:
            bids += 'B '
        else:
            bids += str(i) + ' '
    
    return bids[:-1]

class TestFzBzFunction(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
    def test0(self):
        self.assertEqual(fzbz(3, 5, 10),
                         "1 2 F 4 B F 7 8 F B")
    def test1(self):
        self.assertEqual(fzbz(2, 7, 15),
                         "1 F 3 F 5 F B F 9 F 11 F 13 FB 15")

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            a, b, n = l.split()
            print fzbz(int(a), int(b), int(n))
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1]))
