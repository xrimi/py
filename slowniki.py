import uuid

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"Dodano książkę: {self.title} autora {self.author} z roku {self.year} (ID: {self.id})"

class Dictionary:
    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.name} ({self.language}) [id: {self.id}]"

class Library:
    def __init__(self):
        self.books = []
        self.dictionaries = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def add_dictionary(self, dictionary):
        self.dictionaries.append(dictionary)

    def remove_dictionary(self, dictionary_id):
        for dictionary in self.dictionaries:
            if dictionary.id == dictionary_id:
                self.dictionaries.remove(dictionary)
                return True
        return False

    def search_dictionary(self, dictionary_id):
        for dictionary in self.dictionaries:
            if dictionary.id == dictionary_id:
                return dictionary
        return None

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.dictionaries)} dictionaries"

library = Library()

while True:
    print("i - informacje")
    print("e - edytuj dane")
    print("d - dodaj ksiazke")
    print("u - usun ksiazke")
    dzialanie = input()
    if dzialanie == "i":
        for book in library.books:
            print(book)
    elif dzialanie == "e":
        id = input("Podaj id książki: ")
        book = library.search_book(id)
        if book is not None:
            field = input("Podaj pole do edycji: ")
            value = input("Podaj nową wartość: ")
            setattr(book, field, value)
            print(f"{field} zmienione na {value}")
        else:
            print("Nie ma takiej książki")
    elif dzialanie == "d":
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora książki: ")
        year = input("Podaj rok wydania książki: ")
        book = Book(title, author, year)
        library.add_book(book)
        print(book)
    elif dzialanie == "u":
        id = input("Podaj id książki: ")
        if library.remove_book(id):
            print("Książka usunięta")
        else:
            print("Nie ma takiej książki")
    else:
        print("Nieznane polecenie")
