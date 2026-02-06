def show_msg(message, num):
    for n in range(0, num):
        print(message)

'show_msg("Welcome to Python", 5) -- Works'
'show_msg("Computer Science", 15) -- Works'
'show_msg(4, "Computer Science") -- Throws error (arguments are flipped, which is attempting to use a string-value in the `range()` function'

'Works as intended as the arguments are passed in by name, not by order. This means we specify which parameter is bound to which argument, preventing the failure above.'
show_msg(num=4, message="Computer Science")

