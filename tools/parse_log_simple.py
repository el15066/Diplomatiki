
import os
import sys

from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

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

def extract_timestamp_us(line):
    line = line.replace('[INFO]', '')
    td   = line.partition('[')[2].partition(']')[0]
    t    = datetime.strptime('2022-'+td+'000+0000', '%Y-%m-%d|%H:%M:%S.%f%z').timestamp()
    # print('extract_timestamp_us', line, t)
    return round(t * 1e6)

def process_build_info_line(line, data):
    assert 'params' not in data
    params   = {}
    data['params'] = params
    a, _, b  = line.partition('Build info')
    t        = extract_timestamp_us(a)
    data['t_start'] = t
    for p in unquote(b).split():
        k, _, v   = p.partition('=')
        params[k] = v
    assert len(params) == 3

def process_start_line(line, data):
    params   = data['params']
    assert len(params) == 3
    a, _, b  = line.partition('Blocks execution')
    t        = extract_timestamp_us(a)
    assert 0 <= t - data['t_start'] <= 5000000
    data['t0'] = t
    for p in unquote(b).split():
        k, _, v   = p.partition('=')
        params[k] = int(v)
    assert len(params) == 5

def process_globals_line(line, data):
    params   = data['params']
    assert len(params) == 5
    a, _, b  = line.partition('Globals')
    t        = extract_timestamp_us(a)
    assert 0 <= t - data['t0'] <= 1000
    for p in unquote(b).split():
        k, _, v = p.partition('=')
        params[k] = v

def process_execute_blocks_line(line):
    res = {}
    a, _, b  = line.partition('Executed blocks')
    t        = extract_timestamp_us(a)
    res['t'] = t
    for p in unquote(b).split():
        k, _, v = p.partition('=')
        res[k] = v
    return res

def process_file(ifname):
    res = []
    with open(ifname) as _fi:
        fi = revable(_fi)
        #
        try:
            while fi:
                #
                for line in fi:
                    if 'bin/erigon --' in line: break
                    if 'Build info'    in line: break
                else:
                    break
                #
                rows       = []
                data       = { 'rows': rows }
                res.append(data)
                row        = {}
                row_values = {}
                #
                assert line == fi.latest()
                if 'bin/erigon --' in line:
                    a, _, b = line.partition('$ ')
                    cmd = b if b else a
                    data['cmd'] = cmd[:-1]
                else:
                    fi.rev()
                #
                for line in fi:
                    if 'bin/erigon --' in line: raise ValueError('Expected "Build info" after cmd: ' + data.get('cmd'))
                    if 'Build info'    in line:
                        process_build_info_line(line, data)
                        break
                else:
                    break
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
                for line in fi:
                    if line[  :2] == '^C': line = line[2:]
                    if line[-1: ] == '\n': line = line[:-1]
                    if   'bin/erigon --'    in line: break
                    elif 'Got interrupt'    in line: break
                    elif 'Build info'       in line: break
                    elif 'Blocks execution' in line: process_start_line(line, data)
                    elif 'Globals'          in line: process_globals_line(line, data)
                    elif 'Executed blocks'  in line:
                        row        = process_execute_blocks_line(line)
                        row_values = {}
                        row['vs']  = row_values
                        rows.append(row)
                        #
                    # elif '[02-' in line:
                    #     if row_values:
                    #         row        = {}
                    #         row_values = {}
                    #         row['vs']  = row_values
                    #         rows.append(row)
                    #     row['t'] = extract_timestamp_us(line)
                        #
                    elif len(line) == 54 and line[4] == '-':
                        if line[:4] == '__TO':
                            if row_values:
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
                    data['t1'] = extract_timestamp_us(line)
                #
        except:
            print('At line ' + repr(fi.latest()), file=sys.stderr)
            raise
    return res

class pretty_name:

    def __init__(self, name=None, parts=None):
        if parts is None:
            assert name is not None
            assert name[:4] == 'run_'
            name = name[4:] \
                .replace('false_false_false_false', 'plain') \
                .replace('true_false_false_false',  'block') \
                .replace('true_true_false_false',     'acc') \
                .replace('true_true_true_false',     'code') \
                .replace('true_true_true_true',      'full')
            parts = name.split('_')
        #
        self.parts = parts

    def __repr__(self):
        return '_'.join(self.parts)

    def __and__(self, other):
        res = []
        for p1, p2 in zip(self.parts, other.parts):
            res.append(p1 if p1 == p2 else '')
        return pretty_name(parts=res)

    def formal(self, common=None):
        res = []
        cps = common.parts if common else [''] * 6
        #
        p  = self.parts[0]
        if   p == cps[0]:          t = ''
        elif p == 'plain':         t = 'No prefetch'
        elif p == 'block':         t = 'Prefetch blocks'
        elif p == 'acc':           t = 'Prefetch accounts'
        elif p == 'code':          t = 'Prefetch code'
        elif p == 'full':          t = 'Full prefetch'
        else:                      t = ''
        if t: res.append(t)
        #
        if self.parts[0] != 'plain':
            p  = self.parts[1]
            if   p == cps[1]:          t = ''
            else:                      t = 'readahead '+p
            if t: res.append(t)
        #
        if self.parts[0] not in ('plain', 'block'):
            p  = self.parts[2]
            if   p == cps[2]:          t = ''
            elif p == '1':             t =  '1 thread'
            else:                      t = p+' threads'
            if t: res.append(t)
        #
        p  = self.parts[3]
        if   p == cps[3]:          t = ''
        elif p == '2800':          t = '2.8 GHz'
        elif p == '3800':          t = '3.8 GHz'
        if t: res.append(t)
        #
        p  = self.parts[4]
        if   p == cps[4]:          t = ''
        else:                      t = p+' GiB'
        if t: res.append(t)
        #
        p  = self.parts[5]
        if   p == cps[5]:          t = ''
        elif p == 'p210':          t = 'sata'
        elif p == 'sx8200':        t = 'nvme'
        if t: res.append(t)
        #
        return ', '.join(res)

    def csv(self):
        res = []
        #
        p  = self.parts[0]
        if   p == 'plain':         t = '1:plain'
        elif p == 'block':         t = '2:block'
        elif p == 'acc':           t = '3:acc'
        elif p == 'code':          t = '4:code'
        elif p == 'full':          t = '5:full'
        else:                      t = '?'
        res.append(t.ljust(7))
        #
        p  = self.parts[1]
        res.append(p.rjust(2)) # RA
        #
        p  = self.parts[2]
        res.append(p.rjust(2)) # WT
        #
        p  = self.parts[3]
        res.append(f'{int(p)/1000:3.1f}') # freq
        #
        p  = self.parts[4]
        res.append(p.rjust(3)) # ram
        #
        p  = self.parts[5]
        if   p == 'p210':          t = 'sata'
        elif p == 'sx8200':        t = 'nvme'
        else:                      t = '?'
        res.append(t.ljust(4))
        #
        return ' , '.join(res)

    def csv_header(self):
        res = [
            'P level',
            'RA',
            'WT',
            'GHz',
            'GiB',
            'STOR',
        ]
        return ' , '.join(res)

    def missing(self):
        res = []
        #
        if not self.parts[0]: res.append('prefetch type')
        if not self.parts[1]: res.append('readahead')
        if not self.parts[2]: res.append('thread count')
        if not self.parts[3]: res.append('CPU freq.')
        if not self.parts[4]: res.append('avail. RAM')
        if not self.parts[5]: res.append('storage')
        #
        return ', '.join(res[:-1]) + (' and ' + res[-1] if len(res) > 1 else '')

    def full_title(self):
        t1 = self.formal()
        t2 = self.missing()
        return t1 + (' | vary ' + t2 if t2 else '')

    def informal_title(self):
        return '_'.join(p if p else 'any' for p in self.parts)


def main(ofname, ifnames):
    #
    names   = []
    all_res = []
    #
    for ifname in ifnames:
        print('Processing ' + repr(ifname), file=sys.stderr)
        names.append(pretty_name(ifname.split('/')[-2]))
        all_res.append(process_file(ifname))
    #
    common_name = names[0]
    for n in names[1:]:
        common_name &= n
    #
    fig, ax = plt.subplots(figsize=(6, 4.5))
    #
    with open(ofname, 'w') as fo:
        print(common_name.csv_header() + f' , 1-0 % , mDB % , B/sec', file=fo)
        #
        for name, res in zip(names, all_res):
            print('Processing ' + repr(name), file=sys.stderr)
            assert len(res) == 1
            data = res[0]
            t0   = data['t0']
            t1   = data['t1']
            #
            x  = [0]
            y1 = [0]
            y4 = [0]
            #
            for j, row in enumerate(data['rows']):
                vs = row.get('vs', {})
                _, _, cnt1, tot1 = vs.get(1, (-1,-1,-1,-1))
                _, _, cnt4, tot4 = vs.get(4, (-1,-1,-1,-1))
                assert cnt1 == cnt4, cnt1
                if 't' in row:
                    t = row['t'] - t0
                    assert abs(tot1 + tot4 - t) < 500000, (cnt1, tot1+tot4, t)
                x.append(cnt1)
                y1.append(tot1)
                y4.append(tot4)
            #
            _, _, cnt71, tot71 = vs.get(71, (-1,-1,-1,-1))
            # print(f'{str(name):50} , blocks  ' + ''.join(f', {i:10}' for i in x ), file=fo)
            # print(f'{str(name):50} , read    ' + ''.join(f', {i:10}' for i in y1), file=fo)
            # print(f'{str(name):50} , execute ' + ''.join(f', {i:10}' for i in y4), file=fo)
            #
            x  = np.array(x)
            y1 = np.array(y1)
            y4 = np.array(y4)
            t  = y1 + y4 + 1
            #
            print(name.csv() + f' , {100*y1[-1]/t[-1]:5.2f} , {100*tot71/t[-1]:5.2f} , {1e6*x[-1]/t[-1]:5.1f}', file=fo)
            #
            # dx = x[4:] - x[:-4]
            # dt = t[4:] - t[:-4]
            # #
            # plt.plot(x[4:], dx/dt, label=name)
            ax.plot(x, 1e6 * x / t, label=name.formal(common_name))
    #
    ax.grid()
    ax.set(xlabel='Blocks (+10.5M)', ylabel='blocks / second', title=common_name.full_title())
    lframe = ax.legend(loc='upper left', bbox_to_anchor=(1,1), frameon=False).get_frame()
    # lframe.set_facecolor('1.0')
    # lframe.set_edgecolor('1.0')
    plt.savefig(common_name.informal_title() + '.svg', bbox_inches='tight')
    # plt.show()

if __name__ == '__main__':
    ofname  = sys.argv[1]
    ifnames = sys.argv[2:]
    assert     ofname.endswith('.csv')
    assert all(ifname.endswith('.txt') for ifname in ifnames)
    main(ofname=ofname, ifnames=ifnames)
