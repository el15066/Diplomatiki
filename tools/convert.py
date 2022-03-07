import re
import os
import sys
import requests

PRETTY = {
    'geth':            'Geth@12f0ff4/',
    'erigon':          'Erigon-modified/',
    'original_erigon': 'Erigon@b1fef26/',
    'erigon_lib':      'Erigon-lib@143cd51/',
}

REPOS = {
    'geth':            'https://raw.githubusercontent.com/el15066/go-ethereum/from_2021_08_12/',
    'erigon':          'https://raw.githubusercontent.com/el15066/erigon/inline_uv/',
    'original_erigon': 'https://raw.githubusercontent.com/el15066/erigon/b1fef26767f2635da6816f0dc07acd3f3fa1e935/',
    'erigon_lib':      'https://raw.githubusercontent.com/ledgerwatch/erigon-lib/143cd510bd602fa4999bf79de55ae240eeaa181b/',
}

# SVG_REPL = r'''
# \\begin{figure}
#     \\centering
#     \\def\\svgwidth{\\columnwidth}
#     \\input{\1.pdf_tex}
#     \\caption{\2}
# \\end{figure}
# '''
# SVG_REPL = '''
# \\begin{figure}
#     \\centering
#     \\def\\svgwidth{\\columnwidth}
#     \\input{$1.pdf_tex}
#     \\caption{$2}
# \\end{figure}
# '''
SVG_REPL = '''
\\begin{figure}[!htbp]
  \\centering
  \\includesvg[inkscapelatex=false,width=$2]{../main/$1}
  \\caption{$3}
\\end{figure}
'''

def parse_footnotes(raw):
    _lines = raw.split('\n')
    lines  = []
    notes  = {}
    for line in _lines:
        try:
            if line and line[0] == '^':
                num, _, content = line[1:].partition(' ')
                notes[int(num)] = content
            else:
                lines.append(line)
        except:
            print(line, file=sys.stderr)
            raise
    #
    for i in range(len(lines)):
        try:
            line = lines[i]
            res  = ''
            while line:
                if ' ^' in line:
                    a,  _, bc = line.partition(' ^')
                    bsc       = re.split(r'([^0-9])', bc, maxsplit=1)
                    if len(bsc) == 1: bsc.extend(['', ''])
                    [b, s, c] = bsc
                    content   = notes[int(b)]
                    # content   = notes.get(int(b), 'NOT FOUND')
                    res      += a + '^[' + content + ']' + s
                    line      = c
                else:
                    res += line
                    break
            lines[i] = res
        except:
            print(line, notes, file=sys.stderr)
            raise
    #
    return '\n'.join(lines)

def not_in_code(a):
    a = a.replace('->', '$\\rightarrow$')
    #
    lines = a.split('\n')
    #
    for i in range(len(lines)):
        try:
            line = lines[i]
            if line and line[0] == '[':
                repo, _, src_lns = line[1:].partition('] ')
                src,  _, _lns    =  src_lns.partition(':')
                #
                fname = 'convert_cache/' + repo + '_' + src.replace('/', '_')
                if not os.access(fname, os.F_OK):
                    resp = requests.get(REPOS[repo] + src)
                    resp.raise_for_status()
                    with open(fname, 'x') as fo:
                        fo.write(resp.text)
                #
                with open(fname) as fo:
                    fls = fo.readlines()
                #
                lns, _, _ = _lns.partition(' ')
                #
                res = []
                for ln in lns.split(','):
                    if ln:
                        _l0, _t, _l1 = ln.partition('-')
                        l0 = int(_l0)
                        if _t == '-': l1 = int(_l1)
                        else:         l1 = l0
                        if res:
                            res.append('...\n')
                        res.extend(
                            l if len(l) <= 90 else l[:87] + '...\n'
                            for l in fls[l0-1:l1]
                        )
                #
                # lines[i] = '```go\n' + ''.join(res) + '```\n' # + '*(απόσπασμα από `' + PRETTY[repo] + src + '`)*\n'
                lines[i] = '''{\\vskip 2mm\\color{hrulecolor}\\hrule}
```go
''' + ''.join(res) + '''```
{\\color{hrulecolor}\\hrule\\vskip 1mm}
{\\tiny\\hfill `''' + PRETTY[repo] + src + lns + '''`}
'''
                # lines[i] = '```go\n' + PRETTY[repo] + src + ':' + lns + '\n```\n'
        except:
            print(line, file=sys.stderr)
            raise
    #
    return '\n'.join(lines)


def code_sensitive(raw, *, notInCode=None, inCode=None):
    ps = raw.split('`')
    assert len(ps) % 2 == 1, 'Odd number of backticks (`)'
    r = []
    for not_code, code in zip(ps[0::2], ps[1::2]):
        r.append(not_code if notInCode is None else notInCode(not_code))
        r.append(    code if    inCode is None else    inCode(    code))
    r.append(notInCode(ps[-1]))
    return '`'.join(r)

def main(fname):
    with open(fname) as fi:
        a = fi.read()
        a = a.replace('%', '\\%')
        a = re.sub(r'\s*<!--[\s\S]*?-->', '', a)
        a = re.sub(r'\n\[ .*', '', a) # remove refs
        #
        a = parse_footnotes(a) # global
        a = a.replace('\\^', '^')
        a = code_sensitive(a, notInCode=not_in_code)
        #
        # a = re.sub(r'!\[\]\((\S*\.svg) "([^"]*)"\)', SVG_REPL, a)
        while True:
            m = re.search(r'!\[\]\((\S*\.svg) "([^"]*)"\)', a)
            if not m: break
            c = m.group(2)
            if c[:6] == 'width=': width, _, c = c[6:].partition(', ')
            else:                 width       = '\\textwidth'
            #
            a = a[:m.start()] + \
                SVG_REPL \
                    .replace('$1', m.group(1).replace('_', '\\_')) \
                    .replace('$2', width) \
                    .replace('$3', c) + \
                a[m.end():]
            #
        #
        a = re.sub(r'\n(\[.*)',  r'\n```\n\1\n```', a) # code
        # #
        # repls = []
        # i = 0
        # while True:
        #     #
        #     # m = re.search(r'([^ ])\n```', a)
        #     i  = a.find('```', i)
        #     if i < 0: break
        #     i0 = i
        #     i += 3
        #     i  = a.find('```', i)
        #     if i < 0: raise ValueError('Unpaired ```: ' + repr(a[i0-100:i0+100]))
        #     i1 = i
        #     i += 3
        #     #

        # ps = a.split('```')
        # assert len(ps) % 2 == 1
        # a = ''.join([
        #     x[:-1] + '  \n```' + y + '```  '
        #     for x, y in zip(ps[0::2], ps[1::2])
        # ]) + ps[-1]

        # ps = a.split('```')
        # assert len(ps) % 2 == 1
        # a = ''.join([
        #     x[:-1] + '  \n\\markdownRendererCodeSpan{' + y + '}  '
        #     for x, y in zip(ps[0::2], ps[1::2])
        # ]) + ps[-1]

        # ps = a.split('```')
        # assert len(ps) % 2 == 1
        # a = ''.join([
        #     x[:-1] + '  \n\\markdownRendererCodeSpan{\\begin{verbatim}' + y + '\\end{verbatim}}  '
        #     for x, y in zip(ps[0::2], ps[1::2])
        # ]) + ps[-1]

        # ps = a.split('```')
        # assert len(ps) % 2 == 1
        # a = ''.join([
        #     x[:-1] + '  \n\\begin{verbatim}' + y + '\\end{verbatim}  '
        #     for x, y in zip(ps[0::2], ps[1::2])
        # ]) + ps[-1]

        # a = re.sub(, r'\1  \n\\begin{verbatim}```', a) # break line before ```
        # a = re.sub(r'([^ ])\n```', r'\1  \n\\end{verbatim}```', a) # break line after  ```
        # a = a.replace('```\n',      '```\\end{verbatim}  \n')        # break line after  ```
        #
        print(a, end='')


if __name__ == '__main__':
    fname = sys.argv[1]
    main(fname=fname)
