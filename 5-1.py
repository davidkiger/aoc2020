import math

def bin_split(seat, a, z):
    w = (z-a)/2
    if seat[0] == 'F' or seat[0] == 'L':
        ret = (a, math.floor(z-w))
    elif seat[0] == 'B' or seat[0] == 'R':
        ret = (math.ceil(a+w), z)

    if ret[0] == ret[1]:
        return ret[0]
    else:
        return bin_split(seat[1:], ret[0], ret[1])

inp = [line.strip() for line in open('5-1.in').readlines()]

max_row = 127
max_col = 7

highest_seat = 0
for seat in inp:
    row = bin_split(seat[:7], 0, max_row)
    col = bin_split(seat[-3:], 0, max_col)
    check = row*8 + col
    if check > highest_seat:
        highest_seat = check

print(highest_seat)
