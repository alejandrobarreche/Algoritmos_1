class Interes():
    def __init__(self, capital, tipo_interes, interes, tiempo):
        self.capital = capital
        self.tipo_interes = tipo_interes
        self.interes = interes / 100
        self.tiempo = tiempo

    def calcular_intereses_generados(self):
        if self.tipo_interes == 1:
            interes_generado = self.capital * self.interes * (self.tiempo / 12)
        elif self.tipo_interes == 2:
            interes_generado = (self.capital * ((1 + self.interes) ** (self.tiempo / 12))) - self.capital
        return round(interes_generado, 2)

def main():
    print("Este programa calcula los intereses generados por un capital invertido.")
    print("Puede calcular intereses tanto para un esquema de interés simple como compuesto.")
    print("Por favor, proporcione los detalles requeridos.")

    capital = float(input("Ingrese el capital inicial: "))
    tipo_interes = int(input("Seleccione el tipo de interés (Simple : 1 / Compuesto : 2): "))
    interes = float(input("Ingrese la tasa de interés (en porcentaje): "))
    tiempo = float(input("Ingrese el tiempo en meses: "))

    try:
        interes_obj = Interes(capital, tipo_interes, interes, tiempo)
        print("Los intereses generados son:", interes_obj.calcular_intereses_generados())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
