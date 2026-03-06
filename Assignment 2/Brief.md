# Task 1: System Specification (60%)

You are required to design, implement and test a small console-based music playlist sorter in Python which performs the
description given below.

The software should enable users to login with unique username and password to authenticate them prior to giving them
access to the software features. Authenticated users should be able to create a playlist in addition to the following two
operations: rename and remove playlist. Also, authenticated users should also be able to add music by inputting songs
name, name of the singer and music type (genre) to a playlist. Further, authenticated users should be able to remove or
modify music name, singer, and genre for certain playlists of their choice. The software should have a feature to allow users
to sort playlists and songs in each playlist by name in ascending. Finally, authenticated users should be able to shuffle stored
songs in each playlist.

The software should initially create a data structure (list, tuple, or dictionary) to store at least three playlists with each
containing a minimum of four songs.

The system should have the following specific features:
1. User authentication: (5%)
    1. Ask the user to input their user credentials (username and password).
    2. The username is checked to see if it matches “user123” and password matches “Givemetheykey123”.
    3. If the user provide valid user credentials then the system should show the options a basic command line
(console) based interface
    4. Otherwise, the system should request users to enter valid credential gain. The system should limit users to
three failed login attempts and lock them for five minutes on repeated failed attempts. Note the locking
feature can be by means of displaying a message only. - Use Python sleep function here to suspend program
   
#

2. System features: (30%) 
    The system should display numbered options for users to perform the following tasks:
   1. Option 1. Add a playlist
   2. Option 2. Rename a playlist
   3. Option 3. Remove a playlist
   4. Option 4. Add song to a playlist
   5. Option 6. Remove song from playlist
   6. Option 7. Sort playlist
   7. Option 9. Shuffle songs from a playlist
   8. Option 10. Exit programme
   
#

3. Create a function (or more), for each of the option in the user interface For example, for option 1, create a function
names add_play_list(playlist_name) to take the name of a playlist and store it to the data structure, or for option 2 create a function named rename_playlist(old_name, new_name) to replace the name of the old playlist with a new
name, and so on. (9%)

#

4. Throughout the programme, you should make use of OOP principles (e.g., classes, methods, etc.), conditional
statements, iterative statements, and data structures. (6%)

#

5. Throughout your programme, you should include comments to describe your functions, their parameters, returned
values, the type of computation, or operation, they perform, and any complexities that require clarifications. (5%)

#

6. Your program should suitably handle user errors (e.g., incorrect input for username, such as empty name for
playlist, etc.). (5%)