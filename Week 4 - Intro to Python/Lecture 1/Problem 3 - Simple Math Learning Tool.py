from random import randint

number1 = randint(1, 9)
number2 = randint(1, 9)

actualAnswer = number1 + number2
userAnswer = int(input('Please enter your answer for the following: (' + str(number1) + ' + ' + str(number2) + ' = ?) '))

if userAnswer == actualAnswer:
    print('Well done')
else:
    print('Sorry, try another time')