#!/usr/bin/env python
import unittest
import sys

def npairs(numbers, x):
    np = []
    for i, a in enumerate(numbers):
        for b in numbers[i+1:]:
            if a + b == x:
                np.append((a,b))
            #elif a + b > x:
            #    break
    return np

class TestNpairsFunction(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
    def test1(self):
        self.assertEqual(npairs([1,2,3,4,6], 5),
                         [(1,4), (2,3)])
    def test2(self):
        self.assertEqual(npairs([2,4,5,6,9,11,15], 20),
                         [(5,15), (9,11)])
    def test3(self):
        self.assertEqual(npairs([1,2,3,4], 50),
                         [])

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            numbers, x = l.split(';')
            np = npairs([int(n) for n in numbers.split(',')],
                        int(x))
            if np:
                print ';'.join(['{},{}'.format(a, b) for a,b in np])
            else:
                print "NULL"

    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
