from AP8.tiendalibros.modelo.libro import Libro
from AP8.tiendalibros.modelo.carro_compra import CarroCompras
from AP8.tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from AP8.tiendalibros.modelo.libro_existente_error import LibroExistenteError
from AP8.tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    Catalogo:dict[Libro] ={}


    def __init__ (self):
        self.carrito = CarroCompras()



    @staticmethod
    def adicionar_libro_catalogo(isbn:str, titulo:str, precio:float, existencias:int):

        if isbn in TiendaLibros.Catalogo:
            libro_existente = TiendaLibros.Catalogo[isbn]
            raise LibroExistenteError(libro_existente)
        else:
            librito = Libro (isbn, titulo, precio, existencias)
            TiendaLibros.Catalogo[isbn]=librito
            return librito


    def agregar_libro_a_carrito(self,libro:Libro,cantidades_a_comprar:int):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)

        elif cantidades_a_comprar > libro.existencias:
            raise ExistenciasInsuficientesError(libro)

        else:
            self.carrito.append(libro)







    # Defina metodo retirar_item_de_carrito
