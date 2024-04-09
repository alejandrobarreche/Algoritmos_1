# Definición de la clase Interes para calcular los intereses generados
class Interes():
    def __init__(self, capital, tipo_interes, interes, tiempo):
        # Inicialización de los atributos de la clase
        self.capital = capital
        self.tipo_interes = tipo_interes
        self.interes = interes / 100  # Convertir el porcentaje a decimal
        self.tiempo = tiempo

    # Método para calcular los intereses generados según el tipo de interés especificado
    def calcular_intereses_generados(self):
        if self.tipo_interes == 1:
            # Si es interés simple
            interes_generado = self.capital * self.interes * (self.tiempo / 12)
        elif self.tipo_interes == 2:
            # Si es interés compuesto
            interes_generado = (self.capital * ((1 + self.interes) ** (self.tiempo / 12))) - self.capital
        return round(interes_generado, 2)

# Función principal del programa
def main():
    # Mensajes de introducción
    print("Este programa calcula los intereses generados por un capital invertido.")
    print("Puede calcular intereses tanto para un esquema de interés simple como compuesto.")
    print("Por favor, proporcione los detalles requeridos.")

    # Solicitar al usuario los detalles de la inversión
    capital = float(input("Ingrese el capital inicial: "))
    tipo_interes = int(input("Seleccione el tipo de interés (Simple : 1 / Compuesto : 2): "))
    interes = float(input("Ingrese la tasa de interés (en porcentaje): "))
    tiempo = float(input("Ingrese el tiempo en meses: "))

    try:
        # Crear un objeto Interes con los datos proporcionados por el usuario
        interes_obj = Interes(capital, tipo_interes, interes, tiempo)
        # Calcular y mostrar los intereses generados
        print("Los intereses generados son:", interes_obj.calcular_intereses_generados())
    except ValueError as e:
        # Manejar excepciones en caso de errores
        print("Error:", e)

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()
