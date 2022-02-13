#!/usr/bin/python3

# NOTE: input stacks must not contain cycles, or else will double count

from collections import defaultdict

shared = defaultdict(int)
own    = defaultdict(int)

def processStack(parts, count):
    global shared, own
    #
    for p in parts: shared[p] += count
    #
    assert p == parts[-1]
    own[p] += count

def main(ifname, sort_by):
    #
    with open(ifname) as fi:
        for line in fi:
            stack, _, _n = line.rpartition(' ')
            if not stack: continue
            ps = stack.split(';')
            n  = int(_n)
            processStack(ps, n)
    #
    global shared, own
    #
    total = sum(own.values())
    #
    res = [
        (k, s, own[k])
        for k, s in shared.items()
    ]
    res.sort(key = lambda x: x[sort_by], reverse = sort_by != 0)
    #
    label_k = 'Name'
    label_s = 'Shared'
    label_o = 'Own'
    #
    l_max_k = max(    max(len(k) for k, _, _ in res),   len(label_k))
    l_max_s = max(len(str(max(s  for _, s, _ in res))), len(label_s))
    l_max_o = max(len(str(max(o  for _, _, o in res))), len(label_o))
    #
    print(label_k.ljust(l_max_k) + ' | ' + label_s.center(l_max_s) +  ' | '  +  '  %  '  +  ' | ' + label_o.center(l_max_o) +  ' | '  +  '  %'         )
    print(        '-' * l_max_k  + '-|-' +          '-' * l_max_s  +  '-|-'  +  '-----'  +  '-|-' +          '-' * l_max_o  +  '-|-'  +  '-----'       )
    for k, s, o in res:
        print(  k.ljust(l_max_k) + ' | ' +   str(s).rjust(l_max_s) + f' | { 100*s/total:5.1f} | ' +   str(o).rjust(l_max_o) + f' | { 100*o/total:5.1f}')

if __name__ == '__main__':
    import sys
    ifname  = sys.argv[1]
    t       = sys.argv[2].lower()
    sort_by = 0
    if   t == 'name':   sort_by = 0
    elif t == 'shared': sort_by = 1
    elif t == 'own':    sort_by = 2
    else:               raise ValueError('Unknown arguement: ' + t)
    main(ifname=ifname, sort_by=sort_by)
