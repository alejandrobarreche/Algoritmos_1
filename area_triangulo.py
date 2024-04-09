# Definición de la clase Triangulo
class Triangulo:
    def __init__(self, lado, altura):
        # Inicialización de los atributos lado y altura del triángulo
        self.lado = lado
        self.altura = altura

    # Método para calcular el área del triángulo
    def calcular_area(self):
        # Fórmula del área del triángulo: 0.5 * base * altura
        return 0.5 * self.lado * self.altura

# Función principal del programa
def main():
    print("Este programa calcula el área de un triángulo cuando se conoce la medida de un lado y la altura relativa a ese lado.")

    # Solicitar al usuario la medida del lado y la altura relativa al lado dado
    lado = float(input("Ingrese la medida del lado del triángulo: "))
    altura = float(input("Ingrese la altura relativa al lado dado: "))

    # Crear un objeto Triangulo con los datos proporcionados por el usuario
    triangulo = Triangulo(lado, altura)
    # Calcular y mostrar el área del triángulo
    area = triangulo.calcular_area()
    print("El área del triángulo es:", area, "unidades cuadradas.")

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()

