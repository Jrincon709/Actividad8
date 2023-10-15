import sys

from AP8.tiendalibros.modelo.libro_existente_error import LibroExistenteError
from AP8.tiendalibros.modelo.tienda_libros import TiendaLibros
from AP8.tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from AP8.tiendalibros.modelo.libro_agotado_error import LibroAgotadoError


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras

    def retirar_libro_de_carrito_de_compras(self):
        isbn_librito = input ("Ingrese el ISBN del libro a retirar")

        self.tienda_libros.retirar_item_de_carrito(isbn_librito)
        print (f"Libro con ISBN {isbn_librito} retirado del carrito de compras.")

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        isbn_librito:str = str(input ("Ingrese el ISBN del libro que quieres agregar al carrito"))
        cantidad : int = int (input ("Ingrese la cantidad de existencias del libro que quieres agregar al carrito"))
        try:
            libro_buscado = self.tienda_libros.Catalogo.get(isbn_librito)
            if libro_buscado:
                self.tienda_libros.carrito.agregar_item(isbn_librito,cantidad)
                print (f"Libro agregado con exito")
            else:
                print (f"No se encontro el libro")


        except ValueError:

            print ("Error: Cantidad no válida. Asegúrese de ingresar valores numéricos válidos.")

        except ExistenciasInsuficientesError as e:

            print (f"Error: {e}")

        except LibroAgotadoError as e:
            print(f"Error: {e}")

        except Exception as e:
            print (f"Error inesperado: {e}")





    def adicionar_un_libro_a_catalogo(self):
        isbn_librito:str = str(input ("Ingrese el ISBN del libro que quieres agregar al catalogo"))
        titulo:str = str(input ("Ingrese el TITULO del libro que quieres agregar al catalogo"))
        try:
            precio: float = float (input ("Ingrese el Precio del libro que quieres agregar al catalogo"))
            existencias: int = int (input ("Ingrese las existencias del libro que quieres agregar al catalogo"))
            nuevo_libro = self.tienda_libros.adicionar_libro_catalogo(isbn_librito,titulo,precio,existencias)
            print (f"Libro agregado al catálogo con ISBN: {nuevo_libro.isbn}")
        except ValueError:
            print ("Error: Precio o existencias no válidos. Asegúrese de ingresar valores numéricos válidos.")
        except LibroExistenteError as e:
            print (f"Error: {e}")
        except Exception as e:
            print (f"Error inesperado: {e}")
