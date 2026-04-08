from collections import OrderedDict
from copy import copy, deepcopy
from random import shuffle
from time import sleep

control_username = 'user123'
control_password = 'Givemetheykey123'
playlists = {}


class Song:
    name = ''
    artist = ''
    genre = ''

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre


class Playlist:
    name = ''
    songs = {}

    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or {}

    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def set_name(self, name):
        self.name = name

    def add_song(self, name: str, artist: str, genre: str) -> bool:
        if name in self.songs:
            return False

        self.songs[name] = Song(name, artist, genre)
        return True

    def remove_song(self, name: str) -> bool:
        if name not in self.songs:
            return False

        self.songs.pop(name)
        return True

    def sort(self) -> Playlist:
        songs_to_sort = deepcopy(self.songs)
        songs_to_sort = sorted(songs_to_sort.items(), key=lambda item: item[0])

        return Playlist(self.name, dict(songs_to_sort))

    def shuffle(self) -> Playlist:
        songs_to_shuffle = deepcopy(self.songs)
        songs_to_shuffle = list(songs_to_shuffle.items())
        shuffle(songs_to_shuffle)

        return Playlist(self.name, dict(songs_to_shuffle))


def pretty_print(message: list | str) -> None:
    print(' ')
    print('**************************************************')

    if isinstance(message, str):
        print(message)

    if isinstance(message, list):
        # Utilises Python's "spread" operator, which streams all items within a tuple/list/dictionary to display list-items nicely to the user
        print(*message, sep='\n')

    print('**************************************************')


def format_playlist(playlist: Playlist) -> list:
    formatted_playlist = list()

    formatted_playlist.append(' ')
    formatted_playlist.append(playlist.get_name())

    for song in playlist.get_songs().values():
        formatted_playlist.append(
            '    • ' + song.get_name() + ' - ' + song.get_artist() + ' (' + song.get_genre() + ')')

    return formatted_playlist


def display_playlists() -> None:
    message = list(['Playlists:'])

    for playlist in playlists.values():
        if type(playlist) is not Playlist:
            continue

        for item in format_playlist(playlist):
            message.append(item)

    pretty_print(message)


def add_playlist(name: str, songs=None) -> bool:
    if name in playlists:
        return False

    playlists[name] = Playlist(name, songs)
    return True


def rename_playlist(old_name: str, new_name: str) -> bool:
    if old_name not in playlists:
        return False

    if new_name in playlists:
        return False

    playlist: Playlist = playlists[old_name]
    playlists.pop(old_name)

    playlist.set_name(new_name)
    playlists[new_name] = playlist

    return True


def remove_playlist(name: str) -> bool:
    if name not in playlists:
        return False

    playlists.pop(name)
    return True


def add_song(playlist_name: str, song_name: str, song_artist: str, song_genre: str) -> bool:
    if playlist_name not in playlists:
        return False

    playlist: Playlist = playlists[playlist_name]

    return playlist.add_song(song_name, song_artist, song_genre)


def remove_song(playlist_name: str, song_name: str) -> bool:
    if playlist_name not in playlists:
        return False

    playlist: Playlist = playlists[playlist_name]

    return playlist.remove_song(song_name)


def sort_playlist(name: str) -> list | bool:
    if name not in playlists:
        return False

    playlist: Playlist = playlists[name]
    return format_playlist(playlist.sort())


def shuffle_playlist(name: str) -> list | bool:
    if name not in playlists:
        return False

    playlist: Playlist = playlists[name]
    return format_playlist(playlist.shuffle())


# Sets up default playlists
add_playlist('70s', {
    'Rocketman': Song('Rocketman', 'Elton John', 'Soft Rock'),
    'Bohemian Rhapsody': Song('Bohemian Rhapsody', 'Queen', 'Hard Rock'),
    'Dancing Queen': Song('Dancing Queen', 'ABBA', 'R&B'),
    'Dreams': Song('Dreams', 'Fleetwood Mac', 'Indie'),
    'Highway to Hell': Song('Highway to Hell', 'AC/DC', 'Rock'),
})

add_playlist('80s', {
    'Another One Bites the Dust': Song('Another One Bites the Dust', 'Queen', 'Disco'),
    'Back in Black': Song('Back in Black', 'AC/DC', 'Rock'),
    'Everybody Wants to Rule the World': Song('Everybody Wants to Rule the World', 'Tears for Fears', 'Synth-pop'),
    'Love Will Tear Us Apart': Song('Love Will Tear Us Apart', 'Joy Division', 'Post-Punk')
})

add_playlist('2000s', {
    'Mr. Brightside': Song('Mr. Brightside', 'The Killers', 'Rock'),
    'Poker Face': Song('Poker Face', 'Lady Gaga', 'R&B'),
    'The Scientist': Song('The Scientist', 'Coldplay', 'Rock'),
    'Dance, Dance': Song('Dance, Dance', 'Fall Out Boy', 'Pop-Punk'),
    'Umbrella': Song('Umbrella', 'Rihanna', 'R&B'),
    'Lose Yourself': Song('Lost Yourself', 'Eminem', 'Hip-Hop'),
    'Crazy in Love': Song('Crazy in Love', 'Beyoncé', 'R&B')
})

pretty_print('Please log in to the system!')

login_attempts = 0
is_authenticated = False

while not is_authenticated:
    if login_attempts == 3:
        pretty_print('Could not verify login information! Please try again in 5 minutes...')

        sleep(300)
        login_attempts = 0

    username = str(input('Please enter your username: '))
    password = str(input('Please enter your password: '))

    if username == control_username and password == control_password:
        is_authenticated = True
        print('Logged in successfully!')
        break

    login_attempts += 1
    pretty_print('Please try again!')

def attempt_add_song() -> bool:
    playlist_name = str(input('Please enter the name of the Playlist to add a Song to: '))
    while not playlist_name:
        pretty_print('Unable to add a Song to this Playlist as the name is blank! Please try again...')
        playlist_name = str(input('Please enter the name of the Playlist to add a Song to: '))

    song_name = str(input('Please enter the name of the Song to add: '))
    while not song_name:
        pretty_print('Unable to add this Song as the name is blank! Please try again...')
        song_name = str(input('Please enter the name of the Song to add: '))

    song_artist = str(input('Please enter the artist of the Song to add: '))
    while not song_artist:
        pretty_print('Unable to add this Song as the artist is blank! Please try again...')
        song_artist = str(input('Please enter the artist of the Song to add: '))

    song_genre = str(input('Please enter the genre of the Song to add: '))
    while not song_genre:
        pretty_print('Unable to add this Song as the genre is blank! Please try again...')
        song_genre = str(input('Please enter the genre of the Song to add: '))

    return add_song(playlist_name, song_name, song_artist, song_genre)

def attempt_remove_song() -> bool:
    playlist_name = str(input('Please enter the name of the Playlist to remove a Song from: '))
    while not playlist_name:
        pretty_print('Unable to add a Song to this Playlist as the name is blank! Please try again...')
        playlist_name = str(input('Please enter the name of the Playlist to remove a Song from: '))

    song_name = str(input('Please enter the name of the Song to remove: '))
    while not song_name:
        pretty_print('Unable to add this Song as the name is blank! Please try again...')
        song_name = str(input('Please enter the name of the Song to remove: '))

    return remove_song(playlist_name, song_name)

continuing = True
while continuing:
    pretty_print([
        'Select an action to perform:',
        '    - [0] Display Playlists',
        '    - [1] Add a Playlist',
        '    - [2] Rename a Playlist',
        '    - [3] Remove a Playlist',
        '    - [4] Add a Song to a Playlist',
        '    - [5] Remove a Song from a Playlist',
        '    - [6] Sort Playlist',
        '    - [7] Shuffle Songs in a Playlist',
        '    - [8] Exit Program',
    ])

    # TODO Add non-int/non-accepted action handling
    action = input('Enter the action you would like to perform (example 1): ')

    while not action.isnumeric():
        pretty_print(f'Unable to perform action "{action}". Please provide a number between 0 and 8!"')
        action = input('Enter the action you would like to perform (example 1): ')

    action = int(action)
    while action not in range(0, 8):
        pretty_print(f'Unable to perform action "{action}". Please provide a number between 0 and 8!"')
        action = input('Enter the action you would like to perform (example 1): ')

    if action == 0:
        display_playlists()
        sleep(2)

    if action == 1:
        name = str(input('Please enter a name for the new Playlist: '))

        while not name:
            pretty_print('Unable to add a new Playlist as the name is blank! Please try again...')
            name = str(input('Please enter a name for the new Playlist: '))

        result = add_playlist(name)

        while not result:
            pretty_print('A Playlist already exists with this name! Please try again...')
            name = str(input('Please enter a name for the new Playlist: '))
            result = add_playlist(name)

        pretty_print('Successfully created new Playlist!')
        sleep(2)

    if action == 2:
        old_name = str(input('Please enter the name of the Playlist to rename: '))

        while not old_name:
            pretty_print('Unable to rename this Playlist as the name is blank! Please try again...')
            old_name = str(input('Please enter the name of the Playlist to rename: '))

        while old_name not in playlists:
            pretty_print(f'Unable to rename Playlist {old_name} as it does not exist! Please try again...')
            old_name = str(input('Please enter the name of the Playlist to rename: '))

        new_name = str(input('Please enter the new name of this Playlist: '))

        while not new_name:
            pretty_print('Unable to rename this Playlist as the name is blank! Please try again...')
            new_name = str(input('Please enter the new name of this Playlist: '))

        while new_name in playlists:
            pretty_print(f'Unable to rename Playlist to {new_name} as it already exists! Please try again...')
            new_name = str(input('Please enter the new name of this Playlist: '))

        result = rename_playlist(old_name, new_name)

        while not result:
            pretty_print('Unable to rename Playlist! Please try again...')
            old_name = str(input('Please enter the name of the Playlist to rename: '))
            new_name = str(input('Please enter the new name of this Playlist: '))

            result = rename_playlist(old_name, new_name)

        pretty_print(f'Successfully renamed Playlist from {old_name} to {new_name}!')
        sleep(2)

    if action == 3:
        name = str(input('Please enter the name of a Playlist to remove: '))

        while not name:
            pretty_print('Unable to remove this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to remove: '))

        result = remove_playlist(name)

        while not result:
            pretty_print(f'Unable to remove the Playlist "{name}" as it does not exist! Please try again...')
            name = str(input('Please enter the name of a Playlist to remove: '))
            result = remove_playlist(name)

        pretty_print('Successfully removed Playlist!')
        sleep(2)

    if action == 4:
        result = attempt_add_song()

        while not result:
            pretty_print('Unable to add Song! Please try again...')
            result = attempt_add_song()

        pretty_print('Successfully added Song to Playlist!')
        sleep(2)

    if action == 5:
        result = attempt_remove_song()

        while not result:
            pretty_print('Unable to remove Song! Please try again...')
            result = attempt_remove_song()

        pretty_print('Successfully removed Song from Playlist!')
        sleep(2)

    if action == 6:
        name = str(input('Please enter the name of a Playlist to sort: '))

        while not name:
            pretty_print('Unable to sort this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to sort: '))

        result = sort_playlist(name)

        while not result:
            pretty_print(f'Unable to sort the Playlist "{name}" as it does not exist! Please try again...')
            name = str(input('Please enter the name of a Playlist to sort: '))
            result = sort_playlist(name)

        pretty_print(result)
        sleep(2)

    if action == 7:
        name = str(input('Please enter the name of a Playlist to shuffle: '))

        while not name:
            pretty_print('Unable to shuffle this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to shuffle: '))

        result = shuffle_playlist(name)

        while not result:
            pretty_print(f'Unable to shuffle the Playlist "{name}" as it does not exist! Please try again...')
            name = str(input('Please enter the name of a Playlist to shuffle: '))
            result = shuffle_playlist(name)

        pretty_print(result)
        sleep(2)

    if action == 8:
        pretty_print('Goodbye!')

        continuing = False
