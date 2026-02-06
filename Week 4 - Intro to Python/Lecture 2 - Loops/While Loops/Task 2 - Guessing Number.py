from random import randint

number = randint(1, 10)
guess = int(input('Guess the number: '))

while number != guess:
    print('Incorrect guess! Try again.')
    guess = int(input('Guess the number: '))
else:
    print('Correct!')