from operator import concat


def text_spacer(string_one, string_two, repetitions):
    if type(repetitions) is not int or repetitions <= 0:
        print("Please enter a positive integer")
        return

    for i in range(repetitions):
        string_one = concat(" ", string_one)
        string_two = concat(" ", string_two)

    print(string_one)
    print(string_two)

text_spacer("Today's programming is fun", "I add spaces to text", 5)