nums = [int(x) for x in open('15-1.in').read().strip().split(',')]
last_seen = {num:[i] for i,num in enumerate(nums)}

last_num = nums[-1]
for i in range(len(nums), 30000000):
    if len(last_seen[last_num]) == 1:
        current_num = 0
        last_seen[current_num].append(i)
    else:
        current_num = last_seen[last_num][-1] - last_seen[last_num][-2]
        try:
            last_seen[current_num].append(i)
        except:
            last_seen[current_num] = [i]

    last_num = current_num

print(current_num)
