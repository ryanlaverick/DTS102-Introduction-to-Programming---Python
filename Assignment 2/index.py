
# Displays formatted messages to the user
def print_formatted(message: list|str):
    print('\n' * 20)

    print('**************************************************')

    if isinstance(message, str):
        print(message)

    if isinstance(message, list):
        # Utilises the "spread" operator, which streams all items within a tuple/list/dictionary to display list-items nicely to the user
        print(*message, sep='\n')

    print('**************************************************')

