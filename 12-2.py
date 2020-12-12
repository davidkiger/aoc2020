import math

data = [x for x in open('12-1.in').readlines()]

def rotate(x, y, angle):
    new_x = x*math.cos(angle) - y*math.sin(angle)
    new_y = y*math.cos(angle) + x*math.sin(angle)
    return [int(round(new_x)), int(round(new_y))]

loc = [0,0]
waypoint = [-1,10]

for d in data:
    c = d[0]
    num = int(d[1:])

    if c == 'N':
        waypoint[0] -= num
    elif c == 'S':
        waypoint[0] += num
    elif c == 'E':
        waypoint[1] += num
    elif c == 'W':
        waypoint[1] -= num

    elif c == 'L':
        waypoint = rotate(waypoint[0], waypoint[1], math.radians(num))
    elif c == 'R':
        waypoint = rotate(waypoint[0], waypoint[1], math.radians(-num))

    elif c == 'F':
        loc = [loc[0] + num*waypoint[0], loc[1] + num*waypoint[1]]

print(abs(loc[0]) + abs(loc[1]))
