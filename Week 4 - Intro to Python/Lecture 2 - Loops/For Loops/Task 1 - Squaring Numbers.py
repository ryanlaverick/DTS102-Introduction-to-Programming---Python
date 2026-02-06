from math import pow

total = 0

for k in range(1, 51):
    total += int(pow(k, 2))

print('Total: ', total)