from math import pow

total = 0
k = 1

while k <= 50:
    total += pow(k, 2)

    k += 1

print('Total: ', total)