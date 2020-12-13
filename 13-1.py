timestamp, buses = [x.strip() for x in open('13-1.in').readlines()]
timestamp = int(timestamp)

in_service = [int(x) for x in buses.split(',') if x != 'x']

next_departure = 2*timestamp
best_line = -1

for line in in_service:
    time = 0
    while time < timestamp:
        time += line
    if time < next_departure:
        next_departure = time
        best_line = line

print((next_departure-timestamp)*best_line)
