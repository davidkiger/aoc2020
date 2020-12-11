import copy

data = [list(x.strip()) for x in open('11-1.in').readlines()]

def print_seats(seating):
    for row in seating:
        print(''.join(row))

seating = copy.deepcopy(data)
seating_count = sum([row.count('#') for row in seating])
while True:
    next_seating = copy.deepcopy(seating)
    for row in range(0, len(seating)):
        for col in range(len(seating[row])):
            adj_occ = 0

            if row > 0 and col > 0 and seating[row-1][col-1] == '#': adj_occ += 1
            if row > 0 and seating[row-1][col] == '#': adj_occ += 1
            if row > 0 and col < len(seating[row])-1 and seating[row-1][col+1] == '#': adj_occ += 1
            if col > 0 and seating[row][col-1] == '#': adj_occ += 1
            if col < len(seating[row])-1 and seating[row][col+1] == '#': adj_occ += 1
            if row < len(seating)-1 and col > 0 and seating[row+1][col-1] == '#': adj_occ += 1
            if row < len(seating)-1 and seating[row+1][col] == '#': adj_occ += 1
            if row < len(seating)-1 and col < len(seating[row])-1 and seating[row+1][col+1] == '#': adj_occ += 1

            if seating[row][col] == 'L' and adj_occ == 0:
                next_seating[row][col] = '#'
            elif seating[row][col] == '#' and adj_occ >= 4:
                next_seating[row][col] = 'L'

    next_seating_count = sum([row.count('#') for row in next_seating])

    if seating_count == next_seating_count:
        print(seating_count)
        exit()
    else:
        seating = copy.deepcopy(next_seating)
        seating_count = sum([row.count('#') for row in seating])
