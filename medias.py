# Definición de la clase Media para calcular diferentes tipos de medias
class Media():
    def __init__(self, num1, num2, num3, tipo_media, coeficiente1=1, coeficiente2=1, coeficiente3=1):
        # Inicialización de los atributos de la clase
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.tipo_media = tipo_media
        self.coeficiente1 = coeficiente1
        self.coeficiente2 = coeficiente2
        self.coeficiente3 = coeficiente3

    # Método para calcular la media según el tipo especificado
    def calcular_media(self):
        if self.tipo_media == 1:
            # Si es media aritmética
            media = (self.coeficiente1 * self.num1 + self.coeficiente2 * self.num2 + self.coeficiente3 * self.num3) / 3
        elif self.tipo_media == 2:
            # Si es media ponderada
            suma_coeficientes = self.coeficiente1 + self.coeficiente2 + self.coeficiente3
            media = (self.coeficiente1 * self.num1 + self.coeficiente2 * self.num2 + self.coeficiente3 * self.num3) / suma_coeficientes
        return media

# Función principal del programa
def main():
    # Mensajes de introducción
    print("Este programa calcula diferentes tipos de medias.")
    print("Puede calcular tanto la media aritmética como la ponderada.")
    print("Por favor, proporcione los detalles requeridos.")

    # Solicitar al usuario los números y el tipo de media
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    tipo_media = int(input("Seleccione el tipo de media (1 para aritmética, 2 para ponderada): "))

    # Solicitar al usuario los coeficientes si la media es ponderada
    if tipo_media == 2:
        coeficiente1 = float(input("Ingrese el coeficiente para el primer número: "))
        coeficiente2 = float(input("Ingrese el coeficiente para el segundo número: "))
        coeficiente3 = float(input("Ingrese el coeficiente para el tercer número: "))
    else:
        # Si no es media ponderada, los coeficientes por defecto son 1
        coeficiente1, coeficiente2, coeficiente3 = 1, 1, 1

    try:
        # Crear un objeto Media con los datos proporcionados por el usuario
        media_obj = Media(num1, num2, num3, tipo_media, coeficiente1, coeficiente2, coeficiente3)
        # Calcular y mostrar el resultado de la media
        print("El resultado de la media es:", media_obj.calcular_media())
    except ValueError as e:
        # Manejar excepciones en caso de errores
        print("Error:", e)

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()
