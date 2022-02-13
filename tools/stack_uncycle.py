#!/usr/bin/python3

from collections import defaultdict

def processStack(parts, alias_map):
    res = []
    for _p in parts:
        p = alias_map.get(_p, _p)
        for i, p0 in enumerate(res):
            if p0 == p:
                res = res[:i]
                break
        res.append(p)
    return res

def main(ifname, alias_fname):
    recs = defaultdict(int)
    #
    alias_map = {}
    if alias_fname:
        with open(alias_fname) as f:
            for line in f:
                t = line.partition('#')[0].split()
                if not t: continue
                [alias, real]    = t
                alias_map[alias] = real
    #
    with open(ifname) as fi:
        for line in fi:
            stack, _, _n = line.rpartition(' ')
            if not stack: continue
            n  = int(_n)
            ps = processStack(stack.split(';'), alias_map)
            #
            recs[tuple(ps)] += n
    #
    res = list(recs.items())
    res.sort()
    for k, v in res:
        print(';'.join(k), v)


if __name__ == '__main__':
    import sys
    ifname      = sys.argv[1]
    alias_fname = sys.argv[2] if len(sys.argv) > 2 else ''
    main(ifname=ifname, alias_fname=alias_fname)
