data = [[y for y in x.strip().split(' ')] for x in open('8-1.in').readlines()]
for d in data:
    d[1] = int(d[1])

run_lines = set()
acc = 0
idx = 0
while True:
    if idx in run_lines:
        print(acc)
        exit()

    d = data[idx]
    run_lines.add(idx)

    if d[0] == 'acc':
        acc += d[1]
        idx += 1
    elif d[0] == 'jmp':
        idx += d[1]
    elif d[0] == 'nop':
        idx += 1
