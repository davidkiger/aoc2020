import re

parens = re.compile('\([^\)\(]+\)')
mult = re.compile('\d+\*\d+')
add = re.compile('\d+\+\d+')

expressions = [x.strip().replace(' ', '') for x in open('18-1.in').readlines()]

def process(expr):
    while parens.findall(expr):
        for p in parens.findall(expr):
            val = process(p[1:-1])
            expr = expr.replace(p, str(val))

    while add.findall(expr):
        for a in add.findall(expr):
            expr = expr.replace(a, str(eval(a)))

    while mult.findall(expr):
        for m in mult.findall(expr):
            expr = expr.replace(m, str(eval(m)))

    return int(expr)

total = 0
for e in expressions:
    total += process(e)

print(total)
