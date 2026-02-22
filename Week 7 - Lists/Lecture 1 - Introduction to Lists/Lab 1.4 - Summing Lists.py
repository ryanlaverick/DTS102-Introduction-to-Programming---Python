x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]

def get_element(idx):
    x_element = x[idx]
    y_element = y[idx]
    z_element = z[idx]

    summed_element = x_element + y_element + z_element

    return summed_element

target_number = int(input('Please enter the target number: '))
index = int(input('Please enter the index: '))

summed_element = get_element(index)
if target_number == summed_element:
    print('The target number is equal to its sum')
else:
    print('The target number is not equal to its sum')

