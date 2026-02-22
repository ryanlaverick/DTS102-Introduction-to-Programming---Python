from itertools import count
from random import randint

def generate_even_list():
    num_list = []
    for x in range(0, 100):
        num_list.append(randint(0, 100))

    even_list = list(filter(lambda x: x % 2 == 0, num_list))
    print(even_list)

    return even_list

generate_even_list()

