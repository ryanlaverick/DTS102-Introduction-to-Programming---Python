def calculate_area(height, width):
    return round(height * width)

print("Please enter two numbers in order to calculate the area of a shape:")

print('')

userHeight = int(input("Please enter your height in centimeters: "))
userWidth = int(input("Please enter your width in centimeters: "))

print('')

print('Height:', str(userHeight), 'cm')
print('Width:', str(userWidth), 'cm')
print('')
print('Area:', str(calculate_area(userHeight, userWidth)), 'cm')