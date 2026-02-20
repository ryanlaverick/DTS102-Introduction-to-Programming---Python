"""
Task 1
Write the definition of a class called ContestResult containing:
• A variable winner of type String, initialized to the empty String.
• A variable second_place of type String, initialized to the empty String.
• A variable third_place of type String, initialized to the empty String.
• A method called set_winner that has one parameter, whose value it assigns to
the instance variable winner.
• A method called set_second_place that has one parameter, whose value it
assigns to the instance variable second_place.
• A method called set_third_place that has one parameter, whose value it assigns
to the instance variable third_place.
• A method called get_winner that has no parameters and that returns the value
of the instance variable winner.
• A method called get_second_place that has no parameters and that returns the
value of the instance variable second_place.
• A method called get_third_place that has no parameters and that returns the
value of the instance variable third_place.
• Create an instance from ContestResult that makes call to:
o The set methods of the class by passing appropriate values to them
o The get methods of the class and prints out the results received from
them
"""

class ContestResult:
    def __init__(self):
        self.winner = ''
        self.second_place = ''
        self.third_place = ''

    def set_winner(self, winner):
        self.winner = winner

    def set_second_place(self, second_place):
        self.second_place = second_place

    def set_third_place(self, third_place):
        self.third_place = third_place

    def get_winner(self):
        return self.winner

    def get_second_place(self):
        return self.second_place

    def get_third_place(self):
        return self.third_place

contest_result = ContestResult()
contest_result.set_winner('John')
contest_result.set_second_place('Darcy')
contest_result.set_third_place('Wayne')

print('Winner', contest_result.get_winner())
print('Second Place', contest_result.get_second_place())
print('Third Place', contest_result.get_third_place())