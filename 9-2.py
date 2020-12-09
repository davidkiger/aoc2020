data = [int(x) for x in open('9-1.in').readlines()]

target = 23278925
for i in range(0, len(data)):
    test_val = 0
    vals = list()
    for j in range(i, len(data)):
        test_val += data[j]
        vals.append(data[j])
        if test_val == target:
            print(min(vals) + max(vals))
            exit()

        elif test_val > target:
            break
