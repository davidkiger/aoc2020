import re

r, ticket, other_tickets = [x for x in open('16-1.in').read().split('\n\n')]

rules = {}
for rule in r.split('\n'):
    name, vals = rule.split(': ')
    rules[name] = []
    ranges = vals.split(' or ')
    for ra in ranges:
        rules[name].append([int(x) for x in ra.split('-')])

_, other_tickets = other_tickets.strip().split('\n', 1)
other_nums = [int(x) for x in re.split('\n|,', other_tickets)]

valid_nums = set()
for r in rules.keys():
    for ra in rules[r]:
        for i in range(ra[0], ra[1]+1):
            valid_nums.add(i)

invalid = 0
for i in other_nums:
    if i not in valid_nums:
        invalid += i

print(invalid)
