from math import pow

total = 0

for k in range(1, 51):
    total += int(pow(k, 3))

print('Total: ', total)