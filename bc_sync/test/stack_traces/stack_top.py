#!/usr/bin/python3

recs = {}

try:
    while True:
        line = input()
        line, _, num = line.rpartition(' ')
        if not line: continue
        num = int(num)
        ps  = line.split(';')
        ps.reverse()
        ps  = tuple(ps)
        tot = recs.get(ps, 0)
        recs[ps] = tot + num
except EOFError:
    pass

recs = list(recs.items())
recs.sort()
for k, v in recs:
    print(';'.join(k), v)
