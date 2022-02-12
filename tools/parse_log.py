
import os
import sys

from datetime import datetime

class revable:

    def __init__(self, iterable):
        self._it    = iter(iterable)
        self._cache = None
        self._reved = False
        self._prime()

    def _prime(self):
        try:
            next(self)
            self.rev()
        except StopIteration:
            pass

    def __iter__(self):
        return self

    def __bool__(self):
        return self._cache is not None

    def __next__(self):
        if self._reved:
            self._reved = False
            return self._cache
        else:
            try:
                a = next(self._it)
            except StopIteration:
                self._cache = None
                raise
            self._cache = a
            return a

    def latest(self):
        return self._cache

    def rev(self):
        self._reved = True

#   1-   0          11554          71182         822488

# def skip_until(peakable_it, f):
#     while True:
#         a = peakable_it.peek(None)
#         if a is None: return False
#         if f(a):      return True
#         next(peakable_it)

def unquote(text):
    text   = text.replace(r'\"', r'\q')
    ps     = text.split('"')
    assert len(ps) % 2 == 1, text
    plain  = ps[0::2]
    quoted = ps[1::2]
    res = []
    for p, q in zip(plain, quoted):
        res.append(p)
        res.append(q.replace(' ', r'_'))
    res.append(ps[-1])
    return ''.join(res).replace(r'\q', r'\"')

def extract_timestamp_ms(line):
    line = line.replace('[INFO]', '')
    td   = line.partition('[')[2].partition(']')[0]
    t    = datetime.strptime('2022-'+td+'000+0000', '%Y-%m-%d|%H:%M:%S.%f%z').timestamp()
    # print('extract_timestamp_ms', line, t)
    return round(t * 1000)

def process_build_info_line(line, data):
    assert 'params' not in data
    params   = {}
    data['params'] = params
    a, _, b  = line.partition('Build info')
    t        = extract_timestamp_ms(a)
    data['t_start'] = t
    for p in unquote(b).split():
        k, _, v   = p.partition('=')
        params[k] = v
    assert len(params) == 3

def process_start_line(line, data):
    params   = data['params']
    assert len(params) == 3
    a, _, b  = line.partition('Blocks execution')
    t        = extract_timestamp_ms(a)
    assert 0 <= t - data['t_start'] <= 5000
    data['t0'] = t
    for p in unquote(b).split():
        k, _, v   = p.partition('=')
        params[k] = int(v)
    assert len(params) == 5

def process_globals_line(line, data):
    params   = data['params']
    assert len(params) == 5
    a, _, b  = line.partition('Globals')
    t        = extract_timestamp_ms(a)
    assert 0 <= t - data['t0'] <= 1
    for p in unquote(b).split():
        k, _, v = p.partition('=')
        params[k] = v

def process_execute_blocks_line(line):
    res = {}
    a, _, b  = line.partition('Executed blocks')
    t        = extract_timestamp_ms(a)
    res['t'] = t
    for p in unquote(b).split():
        k, _, v = p.partition('=')
        res[k] = v
    return res

def main(ifname, ofname):
    #
    res = []
    #
    with open(ifname) as _fi:
        fi = revable(_fi)
        #
        try:
            while fi:
                #
                for line in fi:
                    if 'bin/erigon --' in line: break
                else:
                    break
                #
                assert line == fi.latest()
                a, _, b = line.partition('$ ')
                cmd = b if b else a
                #
                # for line in fi:
                #     if 'route@cf0:' in line: break
                # else:
                #     break
                # fi.rev()
                #
                # cmd = ''
                # for line in fi:
                #     if 'route@cf0:' not in line: break
                #     cmd = line
                # else:
                #     break
                # fi.rev()
                #
                rows       = []
                data       = { 'rows': rows, 'cmd': cmd[:-1] }
                res.append(data)
                row        = {}
                row_values = {}
                for line in fi:
                    if line[  :2] == '^C': line = line[2:]
                    if line[-1: ] == '\n': line = line[:-1]
                    if   'bin/erigon --'    in line: break
                    elif 'Got interrupt'    in line: break
                    elif 'Build info'       in line: process_build_info_line(line, data)
                    elif 'Blocks execution' in line: process_start_line(line, data)
                    elif 'Globals'          in line: process_globals_line(line, data)
                    elif 'Executed blocks'  in line:
                        row        = process_execute_blocks_line(line)
                        row_values = {}
                        row['vs']  = row_values
                        rows.append(row)
                        #
                    elif '[02-' in line:
                        if row_values or 'number' in row:
                            row        = {}
                            row_values = {}
                            row['vs']  = row_values
                            rows.append(row)
                        row['t'] = extract_timestamp_ms(line)
                        #
                    elif len(line) == 54 and line[4] == '-':
                        if line[:4] == '__TO':
                            if row_values or 'number' in row:
                                row        = {}
                                row_values = {}
                                row['vs']  = row_values
                                rows.append(row)
                        else:
                            [b, a, avg, cnt, tot] = [int(x) for x in line.replace('-', ' ').split()]
                            row_values[b] = a, avg, cnt, tot
                else:
                    break
                fi.rev()
                #
                assert line in fi.latest()
                if 'Got interrupt' in line:
                    data['t1'] = extract_timestamp_ms(line)
                #
        except:
            print(fi.latest(), file=sys.stderr)
            raise
    #
    for i, data in enumerate(res):
        print('### Run', i)
        print('  t0', data.get('t0'), 't1', data.get('t1'), 'params', data.get('params'), 'rows', len(data.get('rows', [])))
        # for j, row in enumerate(data.get('rows', [])):
        #     print(' ', j)
        #     for k, v in row.items(): print('    ', k, ':', v)
        print()
    #
    with open(ofname, 'w') as fo:
        for i, data in enumerate(res):
            prefix = f'Run {i:2} '
            t0 = data['t0']
            t1 = data.get('t1')
            if t1: print(f'{prefix}total,{(t1-t0)/1000:.2f}', file=fo)
            else:  print(f'{prefix}total,-1',                 file=fo)
            #
            line_t = prefix + 'time,0'
            for j, row in enumerate(data.get('rows', [])):
                t = row.get('t')
                if t: line_t += f',{(t-t0)/1000:.2f}'
                else: line_t +=  ',-1'
            print(line_t, file=fo)
            #
            for tick in [1, 4]:
                line_c = prefix + f'count   {tick}-{tick-1},0'
                line_d = prefix + f'delta_t {tick}-{tick-1},0'
                for j, row in enumerate(data.get('rows', [])):
                    a, avg, cnt, tot = row.get('vs', {}).get(tick, (-1,-1,-1,-1))
                    line_c += f',{cnt}'
                    line_d += f',{tot/1000:.2f}'
                print(line_c, file=fo)
                print(line_d, file=fo)
    #
    print('RUN |   TOTAL  | Time 4-3 |  # 4-3 | Time 1-0 |  # 1-0 | Overhead')
    for i, data in enumerate(res):
        t0   = data['t0']
        t1   = data.get('t1', t0 - 1)
        row  = data.get('rows', [{}])[-1]
        line = f'{i:3} | {(t1-t0)/1000:8.2f}'
        ovh  = (t1 - t0) * 1000
        for tick in [4, 1]:
            a, avg, cnt, tot = row.get('vs', {}).get(tick, (-1,-1,-1,-1))
            line += f' | {tot/1e6:8.2f} | {cnt:6d}'
            ovh  -= tot
        line += f' | {ovh/1e6:4.2f}'
        print(line)











if __name__ == '__main__':
    ifname = sys.argv[1]
    ofname = sys.argv[2]
    assert ifname != ofname
    main(ifname=ifname, ofname=ofname)
