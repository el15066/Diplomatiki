import sys
import numpy             as np
import matplotlib.pyplot as plt

from collections import Counter

# blkparse -f '%5T.%9t, %5p, %3d, %S, %n\n' stage5_4aa | grep -F ',   R,' > stage5_4aa.csv

FILENAME = sys.argv[1]
with open(FILENAME) as f:
    cols = [[] for _ in range(5)]
    for line in f:
        parts = line[:-1].split(',')
        if len(parts) != 5: print(repr(line))
        else:
            for i in range(5):
                part = parts[i]
                try:
                    v = int(part)
                except ValueError:
                    try:
                        v = float(part)
                    except ValueError:
                        v = part.strip()
                cols[i].append(v)
    print(len(cols), len(cols[0]))

t0s  = np.array(cols[0])
pids = np.array(cols[1])
rws  = np.array(cols[2])
offs = np.array(cols[3]) // 8
szs  = np.array(cols[4]) // 8

c = Counter(pids)
print('Most common (PID, count)', c.most_common(10))

# c2 = {}
# for pid, sz in zip(pids, szs):
#     c2[pid] = c2.get(pid, 0) + sz

# def getCommon(c2):
#     res = [(v, k) for k, v in c2.items()]
#     res.sort()
#     res.reverse()
#     return [(k, v) for v, k in res]

# c2l = getCommon(c2)
# print(c2l[:10])

nt0s  = []
noffs = []
for t0, off, sz in zip(t0s, offs, szs):
    for i in range(sz):
        nt0s.append(t0)
        noffs.append(off + i)

nt0s  = np.array(nt0s)
noffs = np.array(noffs)

plt.scatter(nt0s, noffs); plt.scatter(t0s, offs); plt.grid(); plt.show()
#plt.scatter(t0s, szs); plt.grid(); plt.show()
