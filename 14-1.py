inst = [x.strip() for x in open('14-1.in').readlines()]

def apply_mask(num, mask):
    for i in range(0, len(mask)):
        num = int(num)
        p = 35-i
        if mask[i] == '0':
            num = num & ~(1<<p)
        elif mask[i] == '1':
            num = num | (1<<p)
    return num

memory = {}
mask = ''
for i in inst:
    op, val = i.split(' = ')
    if op == 'mask':
        mask = list(val)
    else:
        index = int(op[4:-1])
        memory[index] = apply_mask(val, mask)

print(sum(memory.values()))
