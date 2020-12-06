data = [[y for y in x.strip().split('\n')] for x in open('6-1.in').read().split('\n\n')]

total = 0
for f in data:
    s = set(f[0])
    for x in f[1:]:
        s |= set(x)
    total += len(s)

print(total)
