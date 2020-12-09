from itertools import combinations

data = [int(x) for x in open('9-1.in').readlines()]

for i in range(25, len(data)):
    found = False
    for x,y in combinations(data[i-25:i],2):
        if data[i] == x+y:
            found = True
            break

    if not found:
        print(data[i])
        exit()
