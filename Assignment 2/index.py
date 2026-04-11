from copy import deepcopy
from random import shuffle
from time import sleep

"""
Defines control variables for re-use across the Program
"""
control_username = 'user123'
control_password = 'Givemetheykey123'
playlists = {}

"""
Defines the basic Song class
"""
class Song:
    """
    Define basic attributes for a Song - name, artist & genre
    """
    name: str = ''
    artist: str = ''
    genre: str = ''


    def __init__(self, name: str, artist: str, genre: str):
        """
        Defines class constructor - the parameters name, artist, and genre define the information that must be passed
        in when the class is instantiated

        :param name: the name of the Song
        :param artist: the Artist who performs the Song
        :param genre: the genre of the Song
        """
        self.name = name
        self.artist = artist
        self.genre = genre


    def get_name(self) -> str:
        """
        Declares a getter method to retrieve the Song name from the class object, avoiding accidentally
        manipulating the value of the attribute by accessing it directly

        :return: the name of the Song
        :rtype str
        """
        return self.name


    def get_artist(self) -> str:
        """
        Declares a getter method to retrieve the artist who performs the Song from the class object, avoiding accidentally
        manipulating the value of the attribute by accessing it directly

        :return: the Artist who performs the Song
        :rtype str
        """
        return self.artist


    def get_genre(self) -> str:
        """
        Declares a getter method to retrieve the genre of the Song from the class object, avoiding accidentally
        manipulating the value of the attribute by accessing it directly

        :return: the genre of the Song
        :rtype str
        """
        return self.genre


class Playlist:
    """
    Defines a Playlist class for tracking information about a Playlist (its name, and the songs it contains)
    """
    name: str = ''
    songs: dict = {}


    def __init__(self, name: str, songs: dict=None):
        """
        Defines class constructor - the parameters name and songs define the information that can be passed in
        Name must be provided but songs do not have to be. Passing this information in allows for default
        data to be seeded easily without having to repeatedly call `playlist.add_song()`

        :param name: the name of the Playlist
        :param songs: Songs to add to the Playlist by default
        """

        self.name = name

        """ If no Songs are passed in via the constructor then "songs" is defaulted to a blank dictionary """
        self.songs = songs or {}


    def get_name(self) -> str:
        """
        Declares a getter method to retrieve the Playlist name from the class object, avoiding accidentally
        manipulating the value of the attribute by accessing it directly

        :return: the name of the Playlist
        :rtype str
        """
        return self.name

    def get_songs(self) -> dict:
        """
        Declares a getter method to retrieve the Songs in the Playlist from the class object, avoiding accidentally
        manipulating the value of the attribute by accessing it directly

        :return: the list of Songs on the Playlist
        :rtype dict
        """
        return self.songs

    def set_name(self, name: str) -> None:
        """
        Declares setter method for updating the name of a Playlist

        :param name: the new name of the Playlist
        """
        self.name = name


    def add_song(self, name: str, artist: str, genre: str) -> bool:
        """
        Declares a method for adding a Song to a Playlist

        :param name: the name of the Song
        :param artist: the name of the Artist who performs the Song
        :param genre: the genre of the Song

        :return: if the action is successful
        :rtype bool
        """

        """ 
        Performs a check to ensure that the Song name is not already in use. If it is, FALSE is returned and
        a message is displayed to the user 
        """
        if name in self.songs:
            pretty_print(f'Unable to add Song {name} to Playlist {self.get_name()} as it already exists!')
            return False

        """ Adds a Song to the dictionary using the Song name as the key, which can be used to look up the entry later on """
        self.songs[name] = Song(name, artist, genre)
        return True


    def remove_song(self, name: str) -> bool:
        """
        Declares a method for removing a Song from a Playlist

        :param name: the name of the Song to remove from a Playlist

        :return: if the action is successful
        :rtype bool
        """

        """ Performs a check to ensure that the Song name is a valid entry in the dictionary. If it is not, FALSE is returned """
        if name not in self.songs:
            pretty_print(f'Unable to remove Song {name} from Playlist {self.get_name()} as it does not exist!')
            return False

        """ Removes the Song from the dictionary using its corresponding key """
        self.songs.pop(name)
        return True


    def sort(self) -> Playlist:
        """
        Declares a method for sorting a Playlists Songs alphabetically by name. The underlying dictionary of
        Songs in the original Playlist is not modified and the ordering remains the same - a new Playlist
        instance is instead returned

        :return: a new Playlist with the Songs sorted by name alphabetically
        :rtype Playlist
        """

        """
        Assigns a copy of the underlying dictionary of Songs to a local variable which is in the scope of the method
        This ensures the underlying dictionary is not affected, and outside the sort the ordering
        remains the same
        """
        songs_to_sort = deepcopy(self.songs)

        """
        Leverages the built-in "sorted" Python function in order to sort the dictionary - the "key" parameter is used
        by this function to determine how the list should be sorted - in this instance using the name of the song
        """
        songs_to_sort = sorted(songs_to_sort.items(), key=lambda item: item[0])

        return Playlist(self.name, dict(songs_to_sort))


    def shuffle(self) -> Playlist:
        """
        Declares a method for shuffling a Playlists Songs. The underlying dictionary of Songs in the original Playlist
        is not modified - a new Playlist instance is instead returned

        :return: a new Playlist with the Songs shuffled
        :rtype Playlist
        """

        """
        Assigns a copy of the underlying dictionary of Songs to a local variable which is in the scope of the method
        This ensures the underlying dictionary is not affected, as outside the shuffle the ordering
        remains the same
        """
        songs_to_shuffle = deepcopy(self.songs)

        """
        Converts the dictionary of Songs within the Playlist to a List which can be handled by the "shuffle" method
        imported from the built-in Python library, random
        """
        songs_to_shuffle = list(songs_to_shuffle.items())
        shuffle(songs_to_shuffle)

        return Playlist(self.name, dict(songs_to_shuffle))


def pretty_print(message: list | str) -> None:
    """
    Declares a helper method for displaying information/feedback to the user of the program
    This method can accept either an individual string, or a list of strings to display complex/multi-line messages

    :param message: the message to display to the user
    """

    print(' ')
    print('**************************************************')

    if isinstance(message, str):
        print(message)

    if isinstance(message, list):
        """ Utilises Python's "spread" operator, which streams all items within a tuple/list/dictionary to display list-items nicely to the user """
        print(*message, sep='\n')

    print('**************************************************')


def format_playlist(playlist: Playlist) -> list:
    """
    Declares a method for converting a Playlist object into a message that can be sent to the user

    :param playlist: the Playlist to be formatted

    :return: a list of information to show the user
    :rtype list
    """

    formatted_playlist = list()

    formatted_playlist.append(' ')
    formatted_playlist.append(playlist.get_name())

    """ Loops through each Song in the Playlist and adds an entry to the "formatted_playlist" list for sending to the user """
    for song in playlist.get_songs().values():
        formatted_playlist.append(
            '    • ' + song.get_name() + ' - ' + song.get_artist() + ' (' + song.get_genre() + ')')

    return formatted_playlist


def display_playlists() -> None:
    """
    Declares a method that will send a message to the user with all existing Playlists and their Songs
    """

    """ Defines a "message" variable that is bound to a list of lines of text to send to the user """
    message = list(['Playlists:'])

    """ Loops through each Playlist currently registered to perform an action on them one at a time """
    for playlist in playlists.values():
        """ Type safety check to ensure that we do not pass an illegal parameter of the wrong type to a method that expects a Playlist object """
        if type(playlist) is not Playlist:
            continue

        """" Calls the method defined above which formats a Playlist, and iterates over each line to add to a larger message object """
        for item in format_playlist(playlist):
            message.append(item)

    pretty_print(message)


def add_playlist(name: str, songs=None) -> bool:
    """
    Defines a method that will attempt to create a Playlist based on the information passed in to it
    This method returns TRUE if the action was successful, and FALSE if not. If the
    Playlist name has already been used then a message is displayed to the user

    :param name: the name of the new Playlist to create

    :return: if the action is successful
    :rtype bool
    """

    """ Performs a check to ensure that the Playlist name is not blank. If it is, FALSE is returned and a message is displayed to the user """
    if not name:
        pretty_print('Unable to add a new Playlist as the name is blank! Please try again...')
        return False

    """ Performs a check to ensure that the Playlist name is already in use. If it is, FALSE is returned and a message is displayed to the user """
    if name in playlists:
        pretty_print(f'Unable to add Playlist {name} as it already exists!')
        return False

    """ Adds a new Playlist with the name specified to the dictionary, using the Playlist name as the key for future lookup """
    playlists[name] = Playlist(name, songs)
    return True


def rename_playlist(old_name: str, new_name: str) -> bool:
    """
    Defines a method that will attempt to rename a Playlist, using the existing and new name provided by the user
    If the Playlist is renamed successfully, TRUE is returned. FALSE is returned if not, with feedback
    to the user

    :param old_name: the current name of the Playlist to rename
    :param new_name: the new name of the Playlist

    :return: if the action is successful
    :rtype bool
    """

    """ Performs a check to ensure that the old name provided by the user matches an existing Playlist. If not, FALSE is returned """
    if old_name not in playlists:
        pretty_print(f'Unable to rename Playlist {old_name} as it does not exist!')
        return False

    """" Performs a check to ensure that the new name of the Playlist is not already in use. If it is, FALSE is returned """
    if new_name in playlists:
        pretty_print(f'Unable to rename Playlist to {old_name} to {new_name} as it already exists!')
        return False

    """ Removes the existing Playlist from the dictionary by looking up the entry using the old name """
    playlist: Playlist = playlists[old_name]
    playlists.pop(old_name)

    """ Adds the Playlist back to the dictionary using the new name as its key, whilst updating the internal name of the Playlist using the setter """
    playlist.set_name(new_name)
    playlists[new_name] = playlist

    return True


def remove_playlist(name: str) -> bool:
    """
    Defines a method that will attempt to remove a Playlist from the dictionary, which expects the name of the Playlist
    to be passed as a parameter
    If the action is successful, TRUE is returned. FALSE is returned if not, with feedback

    :param name: the name of the Playlist being returned

    :return: if the action is successful
    :rtype bool
    """

    """ Performs a check to ensure that a Playlist exists within the dictionary with the provided name. If not, FALSE is returned """
    if name not in playlists:
        pretty_print(f'Unable to remove Playlist {name} as it does not exist!')
        return False

    """ Removes the Playlist from the dictionary using the name to look up the correct entry """
    playlists.pop(name)
    return True


def add_song(playlist_name: str, song_name: str, song_artist: str, song_genre: str) -> bool:
    """
    Defines a method that will attempt to add a Song to a Playlist within the dictionary, which expects various information
    regarding the Playlist the Song should be added to, and general information about the song itself
    If the action is successful, TRUE is returned. FALSE is returned if not, with feedback

    :param playlist_name: the name of the Playlist to add the Song to
    :param song_name: the name of the Song to add
    :param song_artist: the name of the artist who performs the Song
    :param song_genre: the genre of the Song

    :return if the action is successful
    :rtype bool
    """

    """ Performs a check to ensure the Playlist exists within the dictionary with the provided name. If not, FALSE is returned """
    if playlist_name not in playlists:
        pretty_print(f'Unable to add Song {song_name} to Playlist {playlist_name} as the Playlist does not exist!')
        return False

    """ Locates the Playlist instance which needs to have the Song added to it from the dictionary, using the Playlist name to perform the lookup """
    playlist: Playlist = playlists[playlist_name]
    return playlist.add_song(song_name, song_artist, song_genre)


def remove_song(playlist_name: str, song_name: str) -> bool:
    """
    Defines a method which will attempt to remove a Song from a Playlist within the dictionary, based on the Playlist name
    and Song name provided to the method
    If the action is successful, TRUE is returned. FALSE is returned if not, with feedback

    :param playlist_name: the name of the Playlist to remove the Song from
    :param song_name: the name of the Song to remove

    :return: if the action is successful
    :rtype bool
    """

    """ Performs a check to ensure the Playlist exists within the dictionary with the provided name. If not, FALSE is returned """
    if playlist_name not in playlists:
        pretty_print(f'Unable to remove Song {song_name} from Playlist {playlist_name} as the Playlist does not exist!')
        return False

    """ Locates the Playlist instance which needs to have the Song removed from it from the dictionary, using the Playlist name to perform the lookup """
    playlist: Playlist = playlists[playlist_name]
    return playlist.remove_song(song_name)


def sort_playlist(name: str) -> list[str] | bool:
    """
    Defines a method which will attempt to sort a Playlists Songs alphabetically by name, based on the Playlist name
    provided to the method

    :param name: the name of the Playlist to sort

    :return: False if the action is not successful, a list of messages if it is successful
    :rtype list[str] | bool
    """

    """ Performs a check to ensure the Playlist exists within the dictionary with the provided name. If not, FALSE is returned """
    if name not in playlists:
        pretty_print(f'Unable to sort Playlist {name} as the Playlist does not exist!')
        return False

    """ Locates the Playlist instance which needs to be sorted from the dictionary, using the Playlist name to perform the lookup """
    playlist: Playlist = playlists[name]
    return format_playlist(playlist.sort())


def shuffle_playlist(name: str) -> list[str] | bool:
    """
    Defines a method which will attempt to shuffle a Playlists Songs randomly, based on the Playlist name provided to the method
    If the action is successful, a list of messages to send to the user is returned. If it is not successful, False is returned

    :param name: the name of the Playlist to shuffle

    :return: False if the action is not successful, a list of messages if it is successful
    :rtype list[str] | bool
    """

    """ Performs a check to ensure the Playlist exists within the dictionary with the provided name. If not, FALSE is returned """
    if name not in playlists:
        pretty_print(f'Unable to shuffle Playlist {name} as it does not exist!')
        return False

    """ Locates the Playlist instance which needs to be shuffled from the dictionary, using the Playlist name to perform the lookup """
    playlist: Playlist = playlists[name]
    return format_playlist(playlist.shuffle())


""" Seeds default Playlists with Songs """
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

""" Defines control variables for attempting to log in to the system """
login_attempts = 0
is_authenticated = False

""" Continually re-attempt the login process until the user has successfully logged in """
while not is_authenticated:

    """ Used to determine if the cooldown timer for unsuccessful logins needs to be enforced """
    if login_attempts == 3:
        pretty_print('Could not verify login information! Please try again in 5 minutes...')

        """ 
        When enforcing the cooldown the CLI is slept for 5 minutes, and the number of failed logins is reset back to 0
        This means that if the user fails to log in three times after the cooldown has expired, then the cooldown
        is enforced again
        """
        sleep(300)
        login_attempts = 0

    username = str(input('Please enter your username: '))
    password = str(input('Please enter your password: '))

    if username == control_username and password == control_password:
        is_authenticated = True
        print('Logged in successfully!')

        """ This breaks out of the while loop early as the user has successfully logged in to the system """
        break

    login_attempts += 1
    pretty_print('Login failed... please try again!')


def attempt_add_song() -> bool:
    """
    Declares a method which will attempt to add a Song to a Playlist, interacting with the user via the CLI to ask them
    for information regarding which Playlist needs to be used, and information around the Song that should be added

    This method has been created with the purpose of being wrapped in a `while` loop to continually perform the action
    until a successful response is encountered, without having to repeat the code for pulling and checking the input

    :return: if the Song has been successfully added to the Playlist
    :rtype bool
    """

    """ Prompts the user to input the name of the Playlist they are wanting to modify and assigns this value to the "playlist_name" variable """
    playlist_name = str(input('Please enter the name of the Playlist to add a Song to: '))

    """ Using a `while` loop here will continually re-trigger the code inside of the block until `playlist_name` has a value - this ensures the user cannot provide invalid data """
    while not playlist_name:
        pretty_print('Unable to add a Song to this Playlist as the name is blank! Please try again...')

        """ Replay the question continually until a satisfactory value is encountered """
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


    """ When acceptable values have been provided for Playlist name, Song name, Song artist, and Song genre, then attempt to add the Song to the Playlist """
    return add_song(playlist_name, song_name, song_artist, song_genre)


def attempt_remove_song() -> bool:
    """
    Declares a method which will attempt to remove a Song from a Playlist, interacting with the user via the CLI to ask them
    for information regarding which Playlist needs to be used, and which Song should be removed

    This method has been created with the purpose of being wrapped in a `while` loop to continually perform the action
    until a successful response is encountered, without having to repeat the code for pulling and checking the input

    :return: if the Song has been successfully removed from the Playlist
    :rtype bool
    """

    """ Prompts the user to input the name of the Playlist they are wanting to modify and assigns this value to the "playlist_name" variable """
    playlist_name = str(input('Please enter the name of the Playlist to remove a Song from: '))

    """ Using a `while` loop here will continually re-trigger the code inside of the block until `playlist_name` has a value - this ensures the user cannot provide invalid data """
    while not playlist_name:
        pretty_print('Unable to remove Song from this Playlist as the Playlist name is blank! Please try again...')

        """ Replay the question continually until a satisfactory value is encountered """
        playlist_name = str(input('Please enter the name of the Playlist to remove a Song from: '))

    song_name = str(input('Please enter the name of the Song to remove: '))
    while not song_name:
        pretty_print('Unable to remove Song from this Playlist as the Song name is blank! Please try again...')

        """ Replay the question continually until a satisfactory value is encountered """
        song_name = str(input('Please enter the name of the Song to remove: '))

    """ When acceptable values have been provided for Playlist name, and Song name, then attempt to remove the Song from the Playlist """
    return remove_song(playlist_name, song_name)


""" 
Defines a `while` loop that will simulate the program "running" until it is explicitly told to stop. This is an 
easy way of mimicking how an actual application would run
"""
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

    """ Prompts the user to select an action/option to perform and assign it to an "action" variable """
    action = input('Enter the action you would like to perform (example 1): ')

    """ 
    Ensures that the action provided is a number, if it is a character, word, phrase, or other symbol an error message is displayed to the user
    This check is performed within a `while` loop to ensure that the user can't force an unexpected value through,
    as if the action is not numeric it will continually error and re-prompt the user for their decision
    """
    while not action.isnumeric():
        pretty_print(f'Unable to perform action "{action}". Please provide a number between 0 and 8!"')
        action = input('Enter the action you would like to perform (example 1): ')

    """ 
    Casts the user input to an integer now it is confirmed to be numeric, then checks if it is within an acceptable range (0 to 8)
    If it is not, then the user is continually re-prompted to enter their decision until they pick a "valid" option
    This ensures the application cannot get into an errored state where the user is attempting to perform
    an action that doesn't exist
    """
    action = int(action)
    while action not in range(0, 9):
        pretty_print(f'Unable to perform action "{action}". Please provide a number between 0 and 8!"')
        action = int(input('Enter the action you would like to perform (example 1): '))

    """ Checks if the value contained within the `action` variable is 0, if it is, then execute the following code block """
    if action == 0:
        display_playlists()
        sleep(2)

    """ Checks if the value contained within the `action` variable is 1, if it is, then execute the following code block """
    if action == 1:
        name = str(input('Please enter a name for the new Playlist: '))

        """ Continually re-prompt the user if the provided Playlist name is blank. This would cause the action to fail as the Playlist name would be blank """
        while not name:
            pretty_print('Unable to add a new Playlist as the name is blank! Please try again...')
            name = str(input('Please enter a name for the new Playlist: '))

        result = add_playlist(name)

        """
        A `while` loop is used here to continually re-trigger the `add_playlist` method until the action is successful.
        This method will return False if a number of clauses are failed to be met (blank inputs, a Playlist that does not exist etc)

        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False, if it is successful the success message is displayed to the user
        """
        while not result:
            name = str(input('Please enter a name for the new Playlist: '))

            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = add_playlist(name)

        """ Displays a success message to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print('Successfully created new Playlist!')
        sleep(2)

    """ Checks if the value contained within the `action` variable is 2, if it is, then execute the following code block """
    if action == 2:
        old_name = str(input('Please enter the name of the Playlist to rename: '))

        """ Continually re-prompt the user if the provided Playlist name is blank. This would cause the action to fail as the Playlist would not exist """
        while not old_name:
            pretty_print('Unable to rename this Playlist as the name is blank! Please try again...')
            old_name = str(input('Please enter the name of the Playlist to rename: '))

        new_name = str(input('Please enter the new name of this Playlist: '))

        while not new_name:
            pretty_print('Unable to rename this Playlist as the name is blank! Please try again...')
            new_name = str(input('Please enter the new name of this Playlist: '))

        result = rename_playlist(old_name, new_name)

        """
        A `while` loop is used here to continually re-trigger the `rename_playlist` method until the action is successful.
        This method will return False if a number of clauses are failed to be met (blank inputs, a Playlist that does not exist etc)

        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False, if it is successful the success message is displayed to the user
        """
        while not result:
            old_name = str(input('Please enter the name of the Playlist to rename: '))
            new_name = str(input('Please enter the new name of this Playlist: '))

            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = rename_playlist(old_name, new_name)

        """ Displays a success message to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print(f'Successfully renamed Playlist from {old_name} to {new_name}!')
        sleep(2)

    """ Checks if the value contained within the `action` variable is 3, if it is, then execute the following code block """
    if action == 3:
        name = str(input('Please enter the name of a Playlist to remove: '))

        """ Continually re-prompt the user if the provided Playlist name is blank. This would cause the action to fail as the Playlist would not exist """
        while not name:
            pretty_print('Unable to remove this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to remove: '))

        result = remove_playlist(name)

        """
        A `while` loop is used here to continually re-trigger the `remove_playlist` method until the action is successful.
        This method will return False if a number of clauses are failed to be met (blank inputs, a Playlist that does not exist etc)

        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False, if it is successful the success message is displayed to the user
        """
        while not result:
            name = str(input('Please enter the name of a Playlist to remove: '))

            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = remove_playlist(name)

        pretty_print('Successfully removed Playlist!')
        sleep(2)

    """ Checks if the value contained within the `action` variable is 4, if it is, then execute the following code block """
    if action == 4:
        result = attempt_add_song()

        """
        A `while` loop is used here to continually re-trigger the `attempt_add_song` method until the action is successful.
        This method will return False if a number of clauses are failed to be met (blank inputs, a Playlist that does not exist etc)

        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False, if it is successful the success message is displayed to the user
        """
        while not result:
            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = attempt_add_song()

        """ Displays a success message to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print('Successfully added Song to Playlist!')
        sleep(2)

    """ Checks if the value contained within the `action` variable is 5, if it is, then execute the following code block """
    if action == 5:
        result = attempt_remove_song()

        """
        A `while` loop is used here to continually re-trigger the `attempt_remove_song` method until the action is successful.
        This method will return False if a number of clauses are failed to be met (blank inputs, a Playlist that does not exist etc)
        
        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False, if it is successful the success message is displayed to the user
        """
        while not result:
            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = attempt_remove_song()

        """ Displays a success message to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print('Successfully removed Song from Playlist!')
        sleep(2)

    """ Checks if the value contained within the `action` variable is 6, if it is, then execute the following code block """
    if action == 6:
        name = str(input('Please enter the name of a Playlist to sort: '))

        """ Continually re-prompt the user if the provided Playlist name is blank. This would cause the action to fail as the Playlist would not exist """
        while not name:
            pretty_print('Unable to sort this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to sort: '))

        """ Attempts to perform the sort action using the Playlist name provided """
        result = sort_playlist(name)

        """
        Using a while loop here will continually re-prompt the user for the name of the Playlist until the action is successful. 
        The method called will only return False if the action could not be completed successfully, typically due to the Playlist provided
        not existing

        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False
        """
        while not result:
            name = str(input('Please enter the name of a Playlist to sort: '))

            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = sort_playlist(name)

        """ Displays the result of the action (which is a list of sorted Songs) to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print(result)
        sleep(2)

    """ Checks if the value contained within the `action` variable is 7, if it is, then execute the following code block """
    if action == 7:
        name = str(input('Please enter the name of a Playlist to shuffle: '))

        """ Continually re-prompt the user if the provided Playlist name is blank. This would cause the action to fail as the Playlist would not exist """
        while not name:
            pretty_print('Unable to shuffle this Playlist as the name is blank! Please try again...')
            name = str(input('Please enter the name of a Playlist to shuffle: '))

        """ Attempts to perform the shuffle action using the Playlist name provided """
        result = shuffle_playlist(name)

        """
        Using a while loop here will continually re-prompt the user for the name of the Playlist until the action is successful. 
        The method called will only return False if the action could not be completed successfully, typically due to the Playlist provided
        not existing
        
        Using `not result` as the clause will only cause the code within the block to be executed if the method called
        returns False
        """
        while not result:
            name = str(input('Please enter the name of a Playlist to shuffle: '))

            """ Re-attempt the action and re-assign the value returned to the `result` variable """
            result = shuffle_playlist(name)

        """ Displays the result of the action (which is a list of shuffled Songs) to the user, then adds a delay before the action menu is re-displayed to give them chance to read the message """
        pretty_print(result)
        sleep(2)

    """ Checks if the value contained within the `action` variable is 8, if it is, then execute the following code block """
    if action == 8:
        pretty_print('Goodbye!')

        """ Causes the wrapping `while` loop clause to evaluate to false, which then exits the application """
        continuing = False
