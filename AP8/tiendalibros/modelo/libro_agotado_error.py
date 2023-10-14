from AP8.tiendalibros.modelo.libro_error import LibroError

from AP8.tiendalibros.modelo.libro import Libro


class LibroAgotadoError(LibroError):
    def __init__(self,libro:Libro):
        super().__init__(libro)


    def __str__(self):
        return f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} esta agotado"
