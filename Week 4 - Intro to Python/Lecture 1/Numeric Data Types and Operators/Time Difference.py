from datetime import datetime

starting_time = datetime.fromisoformat(input('Enter the starting time: '))
ending_time = datetime.fromisoformat(input('Enter the ending time: '))

time_difference = ending_time - starting_time
print('Time Difference: ', time_difference)
