inp = [line for line in open('2-1.in').readlines()]
pws = []

for i in inp:
    tokens = i.split()
    min_, max_ = map(int, tokens[0].split('-'))
    char = tokens[1][0]
    pw = tokens[2]

    pws.append([min_, max_, char, pw])

valid = 0
for min_, max_, c, pw in pws:
    if pw.count(c) >= min_ and pw.count(c) <= max_:
        valid += 1

print(valid)
