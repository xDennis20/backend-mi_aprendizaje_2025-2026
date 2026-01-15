from ejercicio_metodos_especiales_1 import Libro

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []
        self._isbn_indice = {}

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
        self._isbn_indice[libro.isbn] = libro

    def __len__(self) -> int:
        return len(self.libros)

    def __getitem__(self, index: int) -> Libro:
        """Index: es el indice que el usuario coloca
        y busca dentro de la lista self.libros"""
        return self.libros[index]

    def __contains__(self, libro: Libro) -> bool:
        """Libro es la variable que va contener de valor un objeto libro que el usuario haya creado
        Con esto podemos retornamos la expresion con in"""
        return libro.isbn in self._isbn_indice

    def __str__(self) -> str:
        return f"Biblioteca {self.nombre}: {len(self.libros)} libros"

biblioteca = Biblioteca("Biblioteca Central")
libro1 = Libro("1984", "Orwell", 328, "123")
libro2 = Libro("El Hobbit", "Tolkien", 310, "456")

# Test 1: Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Test 2: __len__
print(len(biblioteca))  # 2

# Test 3: __getitem__
print(biblioteca[0].titulo)  # "1984"
print(biblioteca[1].titulo)  # "El Hobbit"

# Test 4: Iteración (funciona si __getitem__ existe)
for libro in biblioteca:
    print(libro.titulo)

# Test 5: __contains__
print(libro1 in biblioteca)  # True
libro3 = Libro("Otro", "Autor", 100, "789")
print(libro3 in biblioteca)  # False

# Test 6: __str__
print(biblioteca)  # "Biblioteca Central: 2 libros"
