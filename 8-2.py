import copy

def test_program(data):
    run_lines = set()
    acc = 0
    idx = 0
    while True:
        if idx in run_lines:
            return()

        try:
            d = data[idx]
        except:
            print(acc)
            exit()

        run_lines.add(idx)

        if d[0] == 'acc':
            acc += d[1]
            idx += 1
        elif d[0] == 'jmp':
            idx += d[1]
        elif d[0] == 'nop':
            idx += 1

def sub_op(idx, data):
    for i in range(idx, len(data)):
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
            return (i+1, data)
        elif data[i][0] == 'jmp':
            data[i][0] = 'nop'
            return (i+1, data)

data = [[y for y in x.strip().split(' ')] for x in open('8-1.in').readlines()]
for d in data:
    d[1] = int(d[1])

replace_idx = 0
while True:
    replace_test = copy.deepcopy(data)
    replace_idx, new_data = sub_op(replace_idx, replace_test)
    test_program(new_data)
