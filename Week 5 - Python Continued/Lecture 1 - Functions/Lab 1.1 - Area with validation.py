def calculate_area(height, width):
    return round(height * width, ndigits=2)

def is_non_neg_float(a):
    try:
        a = float(a)

        if a < 0:
            return False

        return True
    except ValueError:
        return False

def get_non_neg_float(p):
    inp_val = input(p)

    while not is_non_neg_float(inp_val):
        print('This value must be a positive float! Please try again...')
        inp_val = input(p)

    return float(inp_val)


print("Please enter two numbers in order to calculate the area of a shape:")

print('')

userHeight = get_non_neg_float('Please enter the height in centimetres: ')
userWidth = get_non_neg_float('Please enter the width in centimetres: ')

print('')

print('Height:', str(userHeight), 'cm')
print('Width:', str(userWidth), 'cm')
print('')
print('Area:', str(calculate_area(userHeight, userWidth)), 'cm')