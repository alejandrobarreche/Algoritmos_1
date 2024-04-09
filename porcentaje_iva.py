# Importar la clase Enum desde el módulo enum
from enum import Enum

# Definir una enumeración para los tipos de producto y sus impuestos
class TipoProducto(Enum):
    PrimeraNecesidad = 1.04
    TasaReducida = 1.1
    General = 1.21
    Especial = 1  # Asumiremos que 'Especial' se maneja de manera diferente

# Definir una clase para representar el precio de un producto
class Precio:
    # Método de inicialización de la clase
    def __init__(self, producto, precio, tipo_impuesto):
        # Guardar los datos del producto
        self.producto = producto
        self.precio = float(precio)  # Convertir el precio a un flotante
        # Asignar el tipo de impuesto basado en el número especificado
        if tipo_impuesto == 1:
            self.impuesto = TipoProducto.PrimeraNecesidad.value
        elif tipo_impuesto == 2:
            self.impuesto = TipoProducto.TasaReducida.value
        elif tipo_impuesto == 3:
            self.impuesto = TipoProducto.General.value
        elif tipo_impuesto == 4:
            self.impuesto = TipoProducto.Especial.value
        else:
            # Lanzar una excepción si el tipo de impuesto no es válido
            raise ValueError("ERROR. Valor no válido para el impuesto")
        
    # Método para obtener el valor del impuesto
    def get_impuesto(self):
        # En el caso de un producto especial, se solicita al usuario el nuevo valor del impuesto
        if self.impuesto == TipoProducto.Especial.value:
            impuesto_nuevo = float(input(f"Cual es el impuesto especial asociado al producto: {self.producto} \n >>> Introduzca el porcentaje que aumenta (un 21% debería ponerlo como 21): "))
            self.impuesto = 1 + impuesto_nuevo / 100
        return self.impuesto
    
    # Método para calcular el precio final del producto
    def calcular_precio_final(self):
        precio_final = self.precio * self.get_impuesto()
        return precio_final
    

# Función principal del programa
def main():
    # Mensajes de introducción
    print("En este programa vamos a poder calcular el precio de un objeto tras aplicarle los correspondientes impuestos.")
    print("Para ello empezaremos mostrando los distintos tipos de objetos para tener claro que corresponde con cada uno")
    print("1º. Productos con una tasa general: Electrodomésticos, ropa, calzado, material de bricolaje, entradas de conciertos, ...")
    print("2º. Productos de tasa reducida: Alimentos en general, transporte personas, viviendas, entrada de museos, galerías de arte, ...")
    print("3º. Productos de primera necesidad: hortalizas, leche, pan, fruta, ...")
    print("4º. Ciertos productos con tasas especiales: Tabaco, hidrocarburos, bebidas alcohólicas, ...")
    
    # Solicitar al usuario información sobre el producto
    producto = input("Dime el producto: ")
    precio = input("Dime el precio sin impuestos: ")
    impuesto = int(input("Dime el tipo de impuesto (Primera necesidad : 1 / Tasa reducida : 2 / General : 3 / Especial : 4): "))

    try:
        # Crear un objeto Precio con la información proporcionada por el usuario
        producto_precio = Precio(producto, precio, impuesto)
        # Calcular y mostrar el precio final del producto
        print(f"El precio final de {producto.lower()} es: {round(producto_precio.calcular_precio_final(), 2)}")
    except ValueError as e:
        # Manejar excepción en caso de que el tipo de impuesto ingresado no sea válido
        print(e)

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()
