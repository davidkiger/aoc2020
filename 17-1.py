data = [x for x in open('17-1.in').readlines()]

field_map = []
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == '#':
            field_map.append((x,y,0))

neighbor_map = []
for x in (-1,0,1):
    for y in (-1,0,1):
        for z in (-1,0,1):
            if x == y == z == 0:
                continue
            neighbor_map.append((x,y,z))

for i in range(6):
    neighbors = {}
    for pos in field_map:
        for (x,y,z) in neighbor_map:
            check = (pos[0]+x, pos[1]+y, pos[2]+z)
            try:
                neighbors[check] += 1
            except:
                neighbors[check] = 1

    new_map = []
    for pos in neighbors:
        if neighbors[pos] == 3:
            new_map.append(pos)
        elif pos in field_map and neighbors[pos] == 2:
            new_map.append(pos)

    field_map = new_map

print(len(field_map))
