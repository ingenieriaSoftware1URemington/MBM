class Book:
    # Constructor
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    # Prestar
    def lend(self):
        if self.available:
            self.available = False
            return f"'{self.title}' prestado"
        return f"'{self.title}' no disponible"

    # Regresar Libro
    def return_book(self):
        self.available = True
        return f"'{self.title}' devuelto"


class User:
    # Constructor
    def __init__(self, name, id_user):
        self.name = name
        self.id = id_user
        self.borroweb_book = []

    # Pedir
    def borrow(self, book):
        if book.lend():
            self.borroweb_book.append(book)
            return f"{self.name} tiene '{book.title}'"
        return "No se pudo prestar"


class Library:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    # Agregar un libro
    def add_book(self, libro):
        self.books.append(libro)

    # Registrar usuario
    def register_user(self, user):
        self.users.append(user)

library = Library("Central")
book1 = Book("1984", "Orwell", "123")
user1 = User("Ana", 1)

library.add_book(book1)
library.register_user(user1)

print(user1.borrow(book1))