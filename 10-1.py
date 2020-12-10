data = [int(x) for x in open('10-1.in').readlines()]

data.sort()
data.insert(0,0)
data.append(max(data)+3)

ones = 0
threes = 0
prev = data[0]
for d in data[1:]:
    if d == prev+1:
        ones += 1
    elif d == prev+3:
        threes += 1
    prev = d

print(ones * threes)
