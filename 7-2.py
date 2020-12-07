import re

data = [x[0:-1] for x in open('7-1.in').read().split('\n')]
data = data[0:-1]

contents_by_key = {}
containers_by_key = {}
for d in data:
    k,v = d.split(' bags contain ')
    contents_by_key[k] = []
    for x in v.split(', '):
        num, color = x.replace(' bags', '').replace(' bag', '').split(' ', 1)
        contents_by_key[k].append((color, num))

    for x in v.split(', '):
        num, color = x.replace(' bags', '').replace(' bag', '').split(' ', 1)
        if color in containers_by_key.keys():
            containers_by_key[color].append(k)
        else:
            containers_by_key[color] = [k]

def get_bag_count(color, bags):
    total = 1 
    for b in bags[color]:
        if b[0] != 'other':
            total += int(b[1]) * get_bag_count(b[0], bags)

    return total

print(get_bag_count('shiny gold', contents_by_key) - 1) # spent way too long counting the gold bag itself...
