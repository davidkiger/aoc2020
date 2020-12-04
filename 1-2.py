from itertools import combinations

nums = [int(x) for x in open('1-1.in').readlines()]

for x,y,z in combinations(nums,3):
    if x + y +z == 2020:
        print (x*y*z)
        break
