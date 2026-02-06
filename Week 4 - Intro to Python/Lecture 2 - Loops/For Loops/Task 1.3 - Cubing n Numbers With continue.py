from math import pow

total = 0
n = int(input('Please enter the number of iterations: '))

for k in range(1, n + 1):
    if k % 10 == 0: # skip 10, 20, 30 etc
        continue

    total += int(pow(k, 3))

print('Total: ', total)