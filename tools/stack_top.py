#!/usr/bin/python3

from collections import defaultdict

def processStack(parts):
    parts.reverse()
    return parts







def main(ifname):
    recs = defaultdict(int)
    #
    with open(ifname) as fi:
        for line in fi:
            stack, _, _n = line.rpartition(' ')
            if not stack: continue
            n  = int(_n)
            ps = processStack(stack.split(';'))
            #
            recs[tuple(ps)] += n
    #
    res = list(recs.items())
    res.sort()
    for k, v in res:
        print(';'.join(k), v)


if __name__ == '__main__':
    import sys
    ifname = sys.argv[1]
    main(ifname=ifname)
