inp = [line.strip() for line in open('3-1.in').readlines()]

l = len(inp[0])
idx = 0

trees = []
for steps in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
    these_trees = 0
    idx = 0
    for i in range(0, len(inp), steps[0]):
        if inp[i][idx] == '#':
            these_trees += 1

        idx = (idx + steps[1]) % l

    trees.append(these_trees)

total = 1
for t in trees:
    total = total * t

print(total)
