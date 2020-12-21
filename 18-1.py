import re

parens = re.compile('\([^\)\(]+\)')
ev = re.compile('^\d+[\*\+]\d+')

expressions = [x.strip().replace(' ', '') for x in open('18-1.in').readlines()]

def process(expr):
    while parens.findall(expr):
        for p in parens.findall(expr):
            val = process(p[1:-1])
            expr = expr.replace(p, str(val))

    while ev.findall(expr):
        for e in ev.findall(expr):
            expr = expr.replace(e, str(eval(e)), 1)

    return eval(expr)

total = 0
for e in expressions:
    total += process(e)

print(total)
