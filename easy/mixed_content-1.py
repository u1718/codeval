#!/usr/bin/env python
import sys

def main(dfile):
    with open(dfile, 'r') as f:
        for l in f:
            ws, ds = [], []
            wd = l.rstrip('\n').split(',')
            for e in wd:
                if all([c.isdigit() for c in e]):
                    ds.append(e)
                else:
                    ws.append(e)

            print ','.join(ws) + ('|' if ws else '') + ','.join(ds)
            
    return 0
            
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
