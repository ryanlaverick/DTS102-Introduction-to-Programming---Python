number = int(input('Please enter a number to see if it is divisible by 2: '))

remainder = number % 2 # modulo function, which returns the remainder of dividing the number specified by 2

if remainder == 0: # no remainder, meaning number is divisible by 2
    print('It is divisible by 2')
else:
    print('It is not divisible by 2')