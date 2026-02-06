from random import randint

number = randint(1, 100)

for i in range(10**100):
    guess = int(input('Guess the number: '))

    if guess == number:
        print('Correct!')
        break

    if guess < number:
        print('Too low')
        continue

    if guess > number:
        print('Too high')
        continue
