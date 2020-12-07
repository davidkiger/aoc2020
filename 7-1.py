import re

data = [x[0:-1] for x in open('7-1.in').read().split('\n')]
data = data[0:-1]

contents_by_key = {}
containers_by_key = {}
for d in data:
    k,v = d.split(' bags contain ')
    contents_by_key[k] = list(re.sub(r'\d+ ', '', x.replace(' bags', '').replace(' bag', '')) for x in v.split(', '))

    for x in v.split(', '):
        num, color = x.replace(' bags', '').replace(' bag', '').split(' ', 1)
        if color in containers_by_key.keys():
            containers_by_key[color].append(k)
        else:
            containers_by_key[color] = [k]

possible_containers = containers_by_key['shiny gold']
len_cont = len(possible_containers)
while True:
    for container in possible_containers:
        try:
            possible_containers.extend(containers_by_key[container])
        except:
            pass
    possible_containers = list(set(possible_containers))
    if len_cont == len(possible_containers):
        break
    else:
        len_cont = len(possible_containers)

print(len_cont)
