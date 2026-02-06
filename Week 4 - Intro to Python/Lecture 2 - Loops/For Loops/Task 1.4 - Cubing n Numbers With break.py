from math import pow

total = 0
n = int(input('Please enter the number of iterations: '))

for k in range(1, n + 1):
    if total + int(pow(k, 3)) > 500:
        break

    total += int(pow(k, 3))

print('Total: ', total)