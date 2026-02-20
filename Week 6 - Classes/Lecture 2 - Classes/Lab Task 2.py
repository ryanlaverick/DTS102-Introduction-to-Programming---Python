from random import randint

class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.published_year = ''
        self.isbn = randint(10000000, 99999999)

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_published_year(self, published_year):
        self.published_year = published_year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_published_year(self):
        return self.published_year

    def get_isbn(self):
        return self.isbn

def print_book(book):
    print('Title:', book.get_title())
    print('Author:', book.get_author())
    print('Published Year:', book.get_published_year())
    print('ISBN:', book.get_isbn())

to_kill_a_mockingbird = Book()
to_kill_a_mockingbird.set_title('To Kill A Mockingbird')
to_kill_a_mockingbird.set_author('Harper Leech')
to_kill_a_mockingbird.set_published_year('1960')
print_book(to_kill_a_mockingbird)

print('')

iliad = Book()
iliad.set_title('Iliad')
iliad.set_author('Homer')
iliad.set_published_year('650 BCE')
print_book(iliad)

print('')

don_quixote = Book()
don_quixote.set_title('Don Quixote')
don_quixote.set_author('Miguel de Cervantes')
don_quixote.set_published_year('Part 1 - 1605, Part 2-  1615')
print_book(don_quixote)