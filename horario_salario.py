class CalculadoraNomina:
    def __init__(self, salario_bruto, horas_extra):
        self.salario_bruto = salario_bruto
        self.horas_extra = horas_extra

    def calcular_horas_extra(self):
        salario_hora_normal = self.salario_bruto / (35 * 4)  # Salario por hora normal
        horas_extra_basicas = min(self.horas_extra, 8)  # Horas extra entre la 36ª y la 43ª
        horas_extra_avanzadas = max(self.horas_extra - 8, 0)  # Horas extra a partir de la 44ª

        # Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª
        salario_extra_36_43_horas = salario_hora_normal * 1.25 * horas_extra_basicas
        # Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª
        salario_extra_44_mas_horas = salario_hora_normal * 1.5 * horas_extra_avanzadas

        salario_total_horas_extra = salario_extra_36_43_horas + salario_extra_44_mas_horas
        return salario_total_horas_extra

def main():
    print("Este programa calcula el importe de las horas extra que hay que pagar.")

    salario_bruto = float(input("Ingrese el salario bruto mensual: "))
    horas_extra = int(input("Ingrese la cantidad de horas extra trabajadas en el mes: "))

    calculadora_nomina = CalculadoraNomina(salario_bruto, horas_extra)
    total_horas_extra = calculadora_nomina.calcular_horas_extra()

    print("El importe total de las horas extra a pagar es:", round(total_horas_extra,2))

if __name__ == "__main__":
    main()
