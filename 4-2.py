import re

h = re.compile('^#([0-9a-f]{6})$')
p = re.compile('^([0-9]){9}$')

inp = [line.strip() for line in open('4-1.in').readlines()]

pps = []
this_pp = ''
for i in inp:
    if i:
        this_pp = this_pp + ' ' + i
    else:
        if this_pp:
            pps.append(this_pp)
        this_pp = ''
pps.append(this_pp) # Fuck this line.

req = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

valid = 0
for pp in pps:
    tokens = pp.split()
    ks = set()
    vs = set()
    for t in tokens:
        k,v = t.split(':')
        if k == 'byr' and not (1919 < int(v) < 2003):
            continue
        if k == 'iyr' and not (2009 < int(v) < 2021):
            continue
        if k == 'eyr' and not (2019 < int(v) < 2031):
            continue
        if k == 'hgt':
            n = v[:-2]
            u = v[-2:]
            if u == 'cm' and not (149 < int(n) < 194):
                continue
            if u == 'in' and not (58 < int(n) < 77):
                continue
            if u != 'cm' and u != 'in': # ... and this line.
                continue
        if k == 'hcl' and not h.match(v):
            continue
        if k == 'ecl' and v not in ('amb','blu','brn','gry','grn','hzl','oth'):
            continue
        if k == 'pid' and not p.match(v):
            continue

        ks.add(k)
        vs.add(v)


    if not (req - ks):
        valid += 1

print(valid)
