inst = [x.strip() for x in open('14-1.in').readlines()]

def branch(num, indeces):
    nums = []
    p = 35-indeces[0]
    if len(indeces) == 1:
        nums.append(num & ~(1<<p))
        nums.append(num | (1<<p))
        return nums
    else:
        nums.extend( branch(num & ~(1<<p), indeces[1:]) )
        nums.extend( branch(num | (1<<p), indeces[1:]) )
        return nums

def apply_mask(num, mask):
    xbits = []
    for i in range(0, len(mask)):
        num = int(num)
        p = 35-i
        if mask[i] == '1':
            num = num | (1<<p)
        elif mask[i] == 'X':
            xbits.append(i)

    nums = set(branch(num, xbits))

    return nums

memory = {}
mask = ''
for i in inst:
    op, val = i.split(' = ')
    if op == 'mask':
        mask = list(val)
    else:
        index = int(op[4:-1])
        index = apply_mask(index, mask)
        for z in index:
            memory[z] = int(val)

print(sum(memory.values()))
