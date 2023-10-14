from AP8.tiendalibros.modelo.libro import Libro
from AP8.tiendalibros.modelo.item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.listaitemcompra: list = []


    # Defina el metodo agregar_item
    def agregar_item(self,librito:Libro, cantidad:int):
        item_a_agregar:ItemCompra = ItemCompra(librito, cantidad)
        self.listaitemcompra.append( item_a_agregar)
        return item_a_agregar


    def calcular_total(self):
        total = 0
        for i in self.listaitemcompra:
            total += i.calcular_subtotal()
        return total

    def quitar_item(self, isbn: str):
        self.listaitemcompra = [ librito for librito in self.listaitemcompra if  librito.libro.isbn != isbn ]

