import copy

data = [list(x.strip()) for x in open('11-1.in').readlines()]

def print_seats(seating):
    for row in seating:
        print(''.join(row))

def scan(row, col, seating):
    adj_occ = 0
    
    rc = row-1; cc = col-1; check = '.'
    while check == '.' and rc >= 0 and cc >= 0:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc -= 1; cc -= 1

    rc = row-1; cc = col; check = '.'
    while check == '.' and rc >= 0:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc -= 1

    rc = row-1; cc = col+1; check = '.'
    while check == '.' and rc >= 0 and cc <= len(seating[row])-1:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc -= 1; cc += 1

    rc = row; cc = col-1; check = '.'
    while check == '.' and cc >= 0:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        cc -= 1

    rc = row; cc = col+1; check = '.'
    while check == '.' and cc <= len(seating[row])-1:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        cc += 1

    rc = row+1; cc = col-1; check = '.'
    while check == '.' and rc <= len(seating)-1 and cc >= 0:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc += 1; cc -= 1

    rc = row+1; cc = col; check = '.'
    while check == '.' and rc <= len(seating)-1:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc += 1

    rc = row+1; cc = col+1; check = '.'
    while check == '.' and rc <= len(seating)-1 and cc <= len(seating[row])-1:
        check = seating[rc][cc]
        if check == '#': adj_occ += 1
        rc += 1; cc += 1

    return adj_occ

seating = copy.deepcopy(data)
seating_count = sum([row.count('#') for row in seating])
while True:
    next_seating = copy.deepcopy(seating)
    for row in range(0, len(seating)):
        for col in range(len(seating[row])):
            adj_occ = scan(row, col, seating)

            if seating[row][col] == 'L' and adj_occ == 0:
                next_seating[row][col] = '#'
            elif seating[row][col] == '#' and adj_occ >= 5:
                next_seating[row][col] = 'L'

    next_seating_count = sum([row.count('#') for row in next_seating])

    if seating_count == next_seating_count:
        print(seating_count)
        exit()
    else:
        seating = copy.deepcopy(next_seating)
        seating_count = sum([row.count('#') for row in seating])
