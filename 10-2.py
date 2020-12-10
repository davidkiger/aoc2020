data = [int(x) for x in open('10-1.in').readlines()]

data.sort()
data.insert(0,0)
data.append(max(data)+3)

path_counts = [0 for x in data]
path_counts[0] = 1
for i in range(1, len(data)):
    path_len = 0
    for j in range(max(0, i-3), i):
        if data[i] - data[j] <= 3:
            path_len += path_counts[j]

        path_counts[i] = path_len

print(path_counts[-1])
