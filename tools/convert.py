import re

SVG_REPL = r'''
\\begin{figure}
    \\centering
    \\def\\svgwidth{\\columnwidth}
    \\input{\1.pdf_tex}
    \\caption{\2}
\\end{figure}
'''

def parse_footnotes(raw):
    _lines = raw.split('\n')
    lines  = []
    notes  = {}
    for line in _lines:
        if line and line[0] == '^':
            num, _, content = line[1:].partition(' ')
            notes[num]      = content
            assert len(num) > 0, line
        else:
            lines.append(line)
    #
    for i in range(len(lines)):
        line = lines[i]
        res  = ''
        while line:
            if '^' in line:
                a, _, bc = line.partition(' ^')
                b, s,  c =   bc.partition(' ')
                content  = notes.get(b, 'NOT FOUND')
                res     += a + '^[' + content + ']' + s
                line     = c
            else:
                res += line
                break
        lines[i] = res
    #
    return '\n'.join(lines)

def main(fname):
    with open(fname) as fi:
        a = fi.read()
        a = parse_footnotes(a)
        a = re.sub(r'\n\[ .*\n', '', a) # remove refs
        a = re.sub(r'<!--[\s\S]*?-->\n*', '', a)
        a = re.sub(r'!\[\]\((\S*\.svg) "([^"]*)"\)', SVG_REPL, a)
        print(a, end='')


if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    main(fname=fname)
