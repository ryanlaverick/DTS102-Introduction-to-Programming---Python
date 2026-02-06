from math import pow

total = 0
n = int(input('Please enter the number of iterations: '))

for k in range(1, n + 1):
    total += int(pow(k, 3))

print('Total: ', total)