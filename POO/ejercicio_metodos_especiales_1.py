"""EJERCICIO 1: "Clase Libro con representaciones" """

class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor} ({self.paginas}pag.)"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas}, isbn='{self.isbn}')"

    def __eq__(self, otro) -> bool:
        """
            Compara dos libros por ISBN.

            Args:
                otro: Objeto a comparar

            Returns:
                bool: True si tienen el mismo ISBN
        """
        if not isinstance(otro,Libro):
            return NotImplemented
        return self.isbn == otro.isbn

    def __lt__(self, otro) -> bool:
        if not isinstance(otro,Libro):
            return NotImplemented
        return self.paginas < otro.paginas
