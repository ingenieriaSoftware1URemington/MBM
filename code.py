books = []  # list book
users = []
loans = []


def agregar_libro(titulo, autor, isbn):
    book = {"titulo": titulo, "autor": autor, "isbn": isbn, "disponible": True}
    books.append(book)
    return f"Libro '{titulo}' agregado con exito"


# Search Book
def prestar_libro(isbn, id_user):
    for book in books:
        if book["isbn"] == isbn:
            if book["disponible"]:
                book["disponible"] = False
                loans.append(
                    {"isbn": isbn, "id_usuario": id_user, "fecha": "2024-01-01"}
                )
                return "Libro Prestado con exito"
            else:
                return "Libro no disponible"
    return "Libro no encontrado"


agregar_libro("1984", "Orwell", "123")
print(prestar_libro("123", 1))
