from time import sleep

control_username = 'user123'
control_password = 'Givemetheykey123'
is_authenticated = False

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

def attempt_login():
    login_attempts = 0
    global is_authenticated

    while not is_authenticated:
        if login_attempts == 3:
            print_formatted('Could not verify account information! Suspending logins for 5 minutes...')

            sleep(5) # TODO Change this to 5 minutes
            login_attempts = 0

        username = str(input('Please enter your username: '))
        password = str(input('Please enter your password: '))

        if username == control_username and password == control_password:
            is_authenticated = True
            break

        login_attempts += 1
        print_formatted('Please try again!')

print_formatted([
    'Please select one of the following:',
    '    1. Login',
    '    2. Continue as Guest',
])

account_choice = int(input())
while account_choice not in (1, 2):
    account_choice = int(input())

if account_choice == 1:
    attempt_login()