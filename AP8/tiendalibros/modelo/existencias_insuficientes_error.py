from AP8.tiendalibros.modelo.libro import Libro
from AP8.tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):

    def __init__(self, libro: Libro,cantidad:int):
        super ().__init__ (libro)
        self.cantidad_a_comprar:int = cantidad




    def __str__(self):
        return (f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} "
                f"no tiene suficientes existencias para realizar la comprar: "
                f"cantidad a comprar: {self.cantidad_a_comprar}")
