# Definición de la clase CalculadoraNomina para calcular el importe de las horas extra
class CalculadoraNomina:
    def __init__(self, salario_bruto, horas_extra):
        # Inicialización de los atributos de la clase
        self.salario_bruto = salario_bruto
        self.horas_extra = horas_extra

    # Método para calcular el importe de las horas extra
    def calcular_horas_extra(self):
        # Calcular el salario por hora normal
        salario_hora_normal = self.salario_bruto / (35 * 4)  # Suponiendo una jornada laboral de 35 horas a la semana durante 4 semanas
        
        # Calcular las horas extra básicas y avanzadas
        horas_extra_basicas = min(self.horas_extra, 8)  # Hasta 8 horas extra se consideran básicas
        horas_extra_avanzadas = max(self.horas_extra - 8, 0)  # Horas extra adicionales se consideran avanzadas

        # Calcular el importe total de las horas extra
        # Tarifa por hora aumentada en un 125 % para las horas entre la 36ª y la 43ª
        salario_extra_36_43_horas = salario_hora_normal * 1.25 * horas_extra_basicas
        # Tarifa por hora aumentada en un 150 % para las horas a partir de la 44ª
        salario_extra_44_mas_horas = salario_hora_normal * 1.5 * horas_extra_avanzadas

        salario_total_horas_extra = salario_extra_36_43_horas + salario_extra_44_mas_horas
        return salario_total_horas_extra

# Función principal del programa
def main():
    # Mensaje de introducción
    print("Este programa calcula el importe de las horas extra que hay que pagar.")

    # Solicitar al usuario el salario bruto mensual y las horas extra trabajadas
    salario_bruto = float(input("Ingrese el salario bruto mensual: "))
    horas_extra = int(input("Ingrese la cantidad de horas extra trabajadas en el mes: "))

    # Crear un objeto CalculadoraNomina con los datos proporcionados por el usuario
    calculadora_nomina = CalculadoraNomina(salario_bruto, horas_extra)
    # Calcular y mostrar el importe total de las horas extra
    total_horas_extra = calculadora_nomina.calcular_horas_extra()
    print("El importe total de las horas extra a pagar es:", round(total_horas_extra, 2))

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()
