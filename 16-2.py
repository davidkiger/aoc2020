import re

r, mt, ot = [x for x in open('16-1.in').read().split('\n\n')]

# Get all the rules straight
rules = {}
for rule in r.split('\n'):
    name, vals = rule.split(': ')
    rules[name] = []
    ranges = vals.split(' or ')
    for ra in ranges:
        rules[name].append([int(x) for x in ra.split('-')])

# Dump all the valid nums for each rule into a set (and a complete set)
valid_nums = set()
valid_by_field = {}
for r in rules.keys():
    valid_by_field[r] = set()
    for ra in rules[r]:
        for i in range(ra[0], ra[1]+1):
            valid_nums.add(i)
            valid_by_field[r].add(i)

# My ticket is basic...
my_ticket = mt.strip().split('\n')
my_ticket = [int(x) for x in my_ticket[-1].split(',')]

# ... and valid
valid_tickets = [my_ticket]

# Get rid of any invalid tickets
other_tickets = ot.strip().split('\n')
other_tickets = other_tickets[1:]
for ot in other_tickets:
    valid = True
    test_nums = [int(x) for x in ot.split(',')]
    for t in test_nums:
        if t not in valid_nums:
            valid = False

    if valid:
        valid_tickets.append(test_nums)

# Check each ticket, column by column, for each field, to see if it could be a fit
possible_fits = {}
for k in valid_by_field.keys():
    for i in range(0, len(my_ticket)):
        can_fit = True
        for t in range(0, len(valid_tickets)):
            if valid_tickets[t][i] not in valid_by_field[k]:
                can_fit = False

        if can_fit:
            if i in possible_fits.keys():
                possible_fits[i].append(k)
            else:
                possible_fits[i] = [k]

# Once we've got all the possible fits, repeatedly iterate through removing each one that's locked down.
options = sum([len(possible_fits[x]) for x in possible_fits.keys()])
prev_options = -1
while prev_options != options:
    keys = possible_fits.keys()
    for k in keys:
        if len(possible_fits[k]) == 1:
            for x in keys:
                if x != k:
                    try:
                        possible_fits[x].remove(possible_fits[k][0])
                    except:
                        pass

    prev_options = options
    options = sum([len(possible_fits[x]) for x in possible_fits.keys()])

# Once we've got that locked down, multiply the ones that start with 'departure'
mult = 1
for k in possible_fits.keys():
    if possible_fits[k][0].startswith('departure'):
        mult *= my_ticket[k]

print(mult)
