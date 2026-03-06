from copy import copy
from typing import Type
from random import shuffle
from Song import Song

import Song

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = {}

    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def add_song(self, name: str, artist: str, genre: str):
        self.songs[name] = Song(name, artist, genre)

    def shuffle_songs(self):
        songs = copy(self.songs)
        shuffle(list(songs))

        return songs