#!/usr/bin/env python

import sys
import os

def main(fname):
    print os.path.getsize(fname)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
