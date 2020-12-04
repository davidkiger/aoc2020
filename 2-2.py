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
    x = min_-1
    y = max_-1
    try:
        if pw[x] == c or pw[y] == c:
            if pw[x] != pw[y]:
                valid += 1
    except:
        pass

print(valid)
