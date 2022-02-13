#!/usr/bin/python3

import shutil

from subprocess import run, Popen, DEVNULL, PIPE

# Old way:
#  perf scrpit >perf.txt
#  grep -o '^\s\s*[0-9a-z]* ' perf.txt | grep -o '[0-9a-z]*' | sort | uniq >addrs
#  cat addrs | go tool addr2line ~/el15066/erigon/build/bin/erigon >lines
#
# with open(lines_fname) as fl:
#     with open(addrs_fname) as fa:
#         for line in fa:
#             pc        = int(line, 16)
#             path_func = fl.readline()[:-1]
#             path_line = fl.readline()[:-1]
#             assert path_func, 'File "' + lines_fname + '" is incomplete'
#             if path_func == '?': continue
#             #
#             _, _, func = path_func.rpartition('/')
#             _, _, line = path_line.rpartition('/')
#             assert pc not in pcmap, pc
#             pcmap[pc]  = func + '@' + line

#
# New way:
#  sudo perf script -i --header -I -L -F comm,pid,tid,cpu,time,period,event,ip,sym,dso >perf.txt
#

def processtLine(line):
    [com, pidtid, cpu, time, cycles, event] = line.split()
    [pid, tid] = pidtid.split('/')
    assert time[ -1] == ':', repr(line)
    [time_i, time_f] = time[:-1].split('.')
    us = int(time_i) * 1000000 + int(time_f[:6].ljust(6, '0'))
    assert event == 'cycles:', repr(line)
    return com, pid, tid, cpu, int(us), int(cycles)

def getLabels(a2l, pcmap, pc, sym, dso):
    res = pcmap.get(pc)
    if res is None:
        #
        # ask addr2line.go process
        a2l.stdin.write(pc + '\n')
        _func = a2l.stdout.readline()[:-1]
        _src  = a2l.stdout.readline()[:-1]
        assert _func, 'addr2line2.go closed unexpectedly'
        #
        if _func != '?':
            func = _func.rpartition('/')[2]
            src  =  _src.rpartition('/')[2]
            res  = func, src
        else:
            _res = sym if sym != '[unknown]' else dso[1:-1]
            res  = _res.rpartition('/')[2], pc
        #
        pcmap[pc] = res
    return res

# def main(addrs_fname, lines_fname):
def main(mydir, perf_fname, bin_fname):
    recs  = {}
    pcmap = {}
    #
    godir     = shutil.which('go').rpartition('/bin/')[0] + '/'
    a2l_fname = godir + 'src/cmd/addr2line2.go'
    #
    t = run(['diff', mydir+'addr2line2.go', a2l_fname], check=False, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
    if t.returncode != 0:
        run(['cp',   mydir+'addr2line2.go', a2l_fname], check=True,  stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
    #
    with Popen(
        [godir+'bin/go', 'run', a2l_fname, bin_fname],
        bufsize = 1, universal_newlines = True, # line buffered
        stdin   = PIPE,
        stdout  = PIPE,
    ) as a2l:
        with open(perf_fname) as _fp:
            fp = iter(_fp)
            #
            for line in fp:
                if line[0] in '\n#': continue
                com, pid, tid, cpu, us, cycles = processtLine(line)
                delta_t = 0
                us_prev = us
                break
            else:
                raise ValueError('File ' + perf_fname + ' is empty')
            #
            while fp:
                #
                _s = []
                for line in fp:
                    if line == '\n': break
                    assert line[0] == '\t', repr(line)
                    [pc, sym, dso] = line.split()
                    _s.append(getLabels(a2l, pcmap, pc, sym, dso))
                _s.append((tid, '_no_PC'))
                _s.reverse()
                s = [func for func, _ in _s]
                _, src = _s[-1]
                s.append(src)
                #
                k = tuple(s)
                n, t, c = recs.get(k, (0,0,0))
                recs[k] = n + 1, t + delta_t, c + cycles
                #
                for line in fp:
                    com, pid, tid, cpu, us, cycles = processtLine(line)
                    delta_t = us - us_prev
                    us_prev = us
                    break
                else:
                    break
        #
    res = list(recs.items())
    # res.sort(key = lambda x: -x[1][0])
    res.sort(key = lambda x: x[0])
    for s, (n,t,c) in res:
        print(';'.join(s), n)


if __name__ == '__main__':
    import sys
    # addrs_fname = sys.argv[1]
    # lines_fname = sys.argv[2]
    # main(addrs_fname=addrs_fname, lines_fname=lines_fname)
    mydir      = sys.argv[0].rpartition('/')[0] + '/'
    perf_fname = sys.argv[1]
    bin_fname  = sys.argv[2]
    main(mydir=mydir, perf_fname=perf_fname, bin_fname=bin_fname)
