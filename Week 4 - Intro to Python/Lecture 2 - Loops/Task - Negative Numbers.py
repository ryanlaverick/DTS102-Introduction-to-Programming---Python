should_continue = True

while should_continue:
    provided_number = int(input('Please enter a negative number: '))

    if provided_number < 0:
        print('Congratulations! This number is negative \n')
        continue

    should_continue = False
else:
    print('This number is not negative!')