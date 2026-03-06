from time import sleep
from Playlist import Playlist
from Song import Song

control_username = 'user123'
control_password = 'Givemetheykey123'
is_authenticated = False
playlists = {}

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

def display_actions():
    print_formatted([
        'Select an action to perform:',
        '    1. Add a Playlist',
        '    2. Rename a Playlist',
        '    3. Remove a Playlist',
        '    4. Add a Song to a Playlist',
        '    5. Remove a Song from a Playlist',
        '    6. Sort Playlist',
        '    7. Shuffle Songs in a Playlist',
        '    8. Exit Program',
    ])

def attempt_login():
    login_attempts = 0
    global is_authenticated

    while not is_authenticated:
        if login_attempts == 3:
            print_formatted('Could not verify account information! Suspending logins for 5 minutes...')

            sleep(300)
            login_attempts = 0

        username = str(input('Please enter your username: '))
        password = str(input('Please enter your password: '))

        if username == control_username and password == control_password:
            is_authenticated = True
            break

        login_attempts += 1
        print_formatted('Please try again!')

def add_playlist(name: str) -> bool:
    if not name:
        print_formatted('Unable to create Playlist as the name is blank!')
        return False

    target_playlist = playlists.get(name)

    if isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to create Playlist with name {name} as it already exists!')
        return False

    playlists[name] = Playlist(name)

    print_formatted([
        'Playlists:',
        map(lambda p: p.get_name(), *playlists)
    ])

    return True

def rename_playlist(old_name: str, new_name: str) -> bool:
    if not old_name:
        print_formatted('Unable to rename Playlist as the old name is blank!')
        return False

    if not new_name:
        print_formatted('Unable to rename Playlist as the new name is blank!')
        return False

    target_playlist = playlists.get(old_name)

    if not isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to rename Playlist {old_name} as it does not exist!')
        return False

    remove_playlist(old_name)
    playlists[new_name] = target_playlist

    return True

# This function will accept a string-name of a Playlist to remove, and will return:
#    True - if the Playlist was removed successfully
#    False - if the Playlist does not exist
def remove_playlist(name: str) -> bool:
    if not name:
        print_formatted('Unable to remove Playlist as the name is blank!')
        return False

    target_playlist = playlists.get(name)

    if not isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to remove Playlist {name} as it does not exist!')
        return False

    del target_playlist
    return True

def add_song_to_playlist(playlist_name: str, song_name: str, song_artist: str, song_genre: str) -> bool:
    if not playlist_name:
        print_formatted('Unable to create Playlist as the name is blank!')
        return False

    target_playlist = playlists.get(playlist_name)

    if not isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to add Song to Playlist {playlist_name} as it does not exist!')
        return False

    if not song_name:
        print_formatted('Unable to add Song to Playlist as the name is blank!')
        return False

    if not song_artist:
        print_formatted('Unable to add Song to Playlist as the artist is blank!')
        return False

    if not song_genre:
        print_formatted('Unable to add Song to Playlist as the genre is blank!')
        return False

    target_playlist.add_song(song_name, song_artist, song_genre)
    return True

def remove_song_from_playlist(playlist_name, song_name) -> bool:
    if not playlist_name:
        print_formatted('Unable to create Playlist as the name is blank!')
        return False

    target_playlist = playlists.get(playlist_name)

    if not isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to add Song to Playlist {playlist_name} as it does not exist!')
        return False

    # TODO Remove Song

    return True

def sort_playlist(playlist_name):
    return

def shuffle_playlist(playlist_name) -> bool:
    if not playlist_name:
        print_formatted('Unable to create Playlist as the name is blank!')
        return False

    target_playlist = playlists.get(playlist_name)

    if not isinstance(target_playlist, Playlist):
        print_formatted(f'Unable to add Song to Playlist {playlist_name} as it does not exist!')
        return False

    target_playlist.shuffle_songs()
    print_formatted(*target_playlist.get_songs())

    return True

def exit_program():
    print_formatted("Goodbye!")
    exit()

print_formatted([
    'Please select one of the following:',
    '    1. Login',
    '    2. Continue as Guest',
])

account_choice = input()
while not type(account_choice) is int or int(account_choice) not in (1, 2):
    print(f'Value {account_choice} is not recognised! Please try again...')
    account_choice = input()

if account_choice == 1:
    attempt_login()

continuing = True
display_actions()
while continuing:
    choice = int(input('Please enter the numeric identifier of the action you would like to perform: '))

    if choice == 1:
        while True:
            playlist_name = str(input('Please enter a name for the new Playlist: '))
            result = add_playlist(playlist_name)

            if result:
                break

    elif choice == 2:
        while True:
            old_playlist_name = str(input('Please enter the name of the Playlist you wish to rename: '))
            new_playlist_name = str(input('Please enter the new name of the Playlist: '))

            result = rename_playlist(old_playlist_name, new_playlist_name)

            if result:
                break

    elif choice == 3:
        while True:
            playlist_name = str(input('Please enter the name of the Playlist you wish to remove: '))
            result = remove_playlist(playlist_name)

            if result:
                break

    elif choice == 8:
        exit_program()