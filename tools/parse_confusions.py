
import sys

import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict

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

def process_file(ifname):
    res = None
    with open(ifname) as _fi:
        fi = revable(_fi)
        #
        try:
            while fi:
                #
                for line in fi:
                    if '--- Totals ---' in line: break
                else:
                    break
                #
                missed   = int(next(fi).split()[-1])
                added    = int(next(fi).split()[-1])
                [_, a, _, b] = next(fi).split()
                count    = int(a)
                txs      = int(b)
                res = txs, count, missed, added
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
            name = name[4:]
            parts = name.split('_')
        #
        self.parts = parts

    def __repr__(self):
        return '_'.join(self.parts)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(repr(self))

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
        else:                      t = 'readahead '+p
        if t: res.append(t)
        #
        p  = self.parts[1]
        if   p == cps[1]:          t = ''
        elif p == '1':             t =  '1 thread'
        else:                      t = p+' threads'
        if t: res.append(t)
        #
        p  = self.parts[2]
        if   p == cps[2]:          t = ''
        elif p == 'p210':          t = 'sata'
        elif p == 'sx8200':        t = 'nvme'
        if t: res.append(t)
        #
        return ', '.join(res)

    def csv(self):
        res = []
        #
        p  = self.parts[0]
        res.append(p.rjust(2)) # RA
        #
        p  = self.parts[1]
        res.append(p.rjust(2)) # WT
        #
        p  = self.parts[2]
        if   p == 'p210':          t = 'sata'
        elif p == 'sx8200':        t = 'nvme'
        else:                      t = '?'
        res.append(t.ljust(4))
        #
        return ' , '.join(res)

    def csv_header(self):
        res = [
            'RA',
            'WT',
            'STOR',
        ]
        return ' , '.join(res)

    def missing(self):
        res = []
        #
        if not self.parts[0]: res.append('readahead')
        if not self.parts[1]: res.append('thread count')
        if not self.parts[2]: res.append('storage')
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
    all_res = []
    #
    for ifname in ifnames:
        print('Processing ' + repr(ifname), file=sys.stderr)
        all_res.append((
            pretty_name( ifname.split('/')[-2]),
            process_file(ifname)
        ))
    #
    all_res.sort(key = lambda k: repr(k[0]))
    #
    common_name = all_res[0][0]
    for n, _ in all_res[1:]:
        common_name &= n
    #
    fig, ax = plt.subplots(figsize=(6, 4.5))
    #
    with open(ofname, 'w') as fo:
        print(common_name.csv_header() + f' , txs, count, missed, added', file=fo)
        #
        grouped = defaultdict(list)
        #
        for name, res in all_res:
            grouped[name].append(res)
            print(name, hash(name))
        #
        print(grouped)
        #
        for name, reses in grouped.items():
            print('Processing ' + repr(name), file=sys.stderr)
            #
            txs, count, missed, added = 0, 0, 0, 0
            #
            for res in reses:
                txs_, count_, missed_, added_ = res
                txs    += txs_
                count  += count_
                missed += missed_
                added  += added_
            #
            print(name.csv() + f' , {txs:10} , {count:10} , {missed:10} , {added:10}', file=fo)
            #
            # #
            # plt.plot(x[4:], dx/dt, label=name)
    #         ax.plot(x, 1e6 * x / t, label=name.formal(common_name))
    # #
    # ax.grid()
    # ax.set(xlabel='Blocks (+10.5M)', ylabel='blocks / second', title=common_name.full_title())
    # lframe = ax.legend(loc='upper left', bbox_to_anchor=(1,1), frameon=False).get_frame()
    # # lframe.set_facecolor('1.0')
    # # lframe.set_edgecolor('1.0')
    # plt.savefig(common_name.informal_title() + '.svg', bbox_inches='tight')
    # plt.show()

if __name__ == '__main__':
    ofname  = sys.argv[1]
    ifnames = sys.argv[2:]
    assert     ofname.endswith('.csv')
    assert all(ifname.endswith('.txt') for ifname in ifnames)
    main(ofname=ofname, ifnames=ifnames)
