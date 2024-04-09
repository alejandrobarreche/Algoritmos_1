class Triangulo:
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.lado * self.altura

def main():
    print("Este programa calcula el área de un triángulo cuando se conoce la medida de un lado y la altura relativa a ese lado.")

    lado = float(input("Ingrese la medida del lado del triángulo: "))
    altura = float(input("Ingrese la altura relativa al lado dado: "))

    triangulo = Triangulo(lado, altura)
    area = triangulo.calcular_area()
    print("El área del triángulo es:", area)

if __name__ == "__main__":
    main()
