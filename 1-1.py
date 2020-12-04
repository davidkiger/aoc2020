from itertools import combinations

nums = [int(x) for x in open('1-1.in').readlines()]

for x,y in combinations(nums,2):
    if x + y == 2020:
        print (x*y)
        break
