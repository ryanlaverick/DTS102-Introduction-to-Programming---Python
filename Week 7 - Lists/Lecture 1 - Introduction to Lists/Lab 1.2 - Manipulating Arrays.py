def get_first_and_last_item(array):
    new_array = [array[0], array[-1]]
    new_array.sort()

    return new_array

color_list = ['Red', 'Green', 'White', 'Black']
print(get_first_and_last_item(color_list))