#!/usr/bin/python3

recs = {}

try:
    while True:
        line = input()
        line, _, num = line.rpartition(' ')
        if not line: continue
        num = int(num)
        pre = []
        for p in line.split(';'):
            for i, p2 in enumerate(pre):
                if p2 == p:
                    pre = pre[:i]
                    break
            pre.append(p)
        pre = tuple(pre)
        tot = recs.get(pre, 0)
        recs[pre] = tot + num
except EOFError:
    pass

recs = list(recs.items())
recs.sort()
for k, v in recs:
    print(';'.join(k), v)
