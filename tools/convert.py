import re
import sys

# SVG_REPL = r'''
# \\begin{figure}
#     \\centering
#     \\def\\svgwidth{\\columnwidth}
#     \\input{\1.pdf_tex}
#     \\caption{\2}
# \\end{figure}
# '''
SVG_REPL = '''
\\begin{figure}
    \\centering
    \\def\\svgwidth{\\columnwidth}
    \\input{$1.pdf_tex}
    \\caption{$2}
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
                if '^' in line:
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
        a = re.sub(r'\s*<!--[\s\S]*?-->', '', a)
        a = re.sub(r'\n\[ .*', '', a) # remove refs
        #
        a = code_sensitive(a, notInCode = lambda k: k.replace('->', '$\\rightarrow$'))
        #
        # a = re.sub(r'!\[\]\((\S*\.svg) "([^"]*)"\)', SVG_REPL, a)
        while True:
            m = re.search(r'!\[\]\((\S*\.svg) "([^"]*)"\)', a)
            if not m: break
            a = a[:m.start()] + \
                SVG_REPL \
                    .replace('$1', m.group(1).replace('_', '\\_')) \
                    .replace('$2', m.group(2)) + \
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
        a = parse_footnotes(a)
        print(a, end='')


if __name__ == '__main__':
    fname = sys.argv[1]
    main(fname=fname)
