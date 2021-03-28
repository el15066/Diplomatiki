from datetime import datetime

ts     = []
blocks = []

try:
    while True:
        line = input()
        p    = line.split(' ')
        t    = datetime.strptime(p[1][7:-1], '%H:%M:%S.%f').timestamp()
        b    = int(p[14].partition('=')[2])
        ts.append(t)
        blocks.append(b)
except EOFError:
    pass

print('Time, Block')
t0 = ts[0]
for t, b in zip(ts, blocks):
    print(f'{round(t - t0):4}, {b:7}')

