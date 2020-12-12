data = [x for x in open('12-1.in').readlines()]

facing_set = ( (-1,0), (0,1), (1,0), (0,-1) )
f = 1
loc = [0,0]

for d in data:
    c = d[0]
    num = int(d[1:])

    if c == 'N':
        loc[0] -= num
    elif c == 'S':
        loc[0] += num
    elif c == 'E':
        loc[1] += num
    elif c == 'W':
        loc[1] -= num
    elif c == 'L':
        rot = (360-num)//90
        f = (f + rot) % 4
    elif c == 'R':
        rot = num//90
        f = (f + rot) % 4
    elif c == 'F':
        loc = [loc[0] + num*facing_set[f][0], loc[1] + num*facing_set[f][1]]

print(abs(loc[0]) + abs(loc[1]))
