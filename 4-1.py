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

req = {
    'byr', # (Birth Year)
    'iyr', # (Issue Year)
    'eyr', # (Expiration Year)
    'hgt', # (Height)
    'hcl', # (Hair Color)
    'ecl', # (Eye Color)
    'pid', # (Passport ID)
    # 'cid', # (Country ID)
}

valid = 0
for pp in pps:
    tokens = pp.split()
    ks = set()
    vs = set()
    for t in tokens:
        k,v = t.split(':')
        ks.add(k)
        vs.add(v)

    if not (req - ks):
        valid += 1

print(valid)
