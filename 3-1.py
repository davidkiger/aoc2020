inp = [line.strip() for line in open('3-1.in').readlines()]

l = len(inp[0])
idx = 0

trees = 0
for i in inp:
    if i[idx] == '#':
        trees += 1

    idx = (idx + 3) % l

print(trees)
