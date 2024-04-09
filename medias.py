class Media():
    def __init__(self, num1, num2, num3, tipo_media, coeficiente1=1, coeficiente2=1, coeficiente3=1):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.tipo_media = tipo_media
        self.coeficiente1 = coeficiente1
        self.coeficiente2 = coeficiente2
        self.coeficiente3 = coeficiente3

    def calcular_media(self):
        if self.tipo_media == 1:
            media = (self.coeficiente1 * self.num1 + self.coeficiente2 * self.num2 + self.coeficiente3 * self.num3) / 3
        elif self.tipo_media == 2:
            media = (self.coeficiente1 * self.num1 + self.coeficiente2 * self.num2 + self.coeficiente3 * self.num3) / (
                        self.coeficiente1 + self.coeficiente2 + self.coeficiente3)
        return media


def main():
    print("Este programa calcula diferentes tipos de medias.")
    print("Puede calcular tanto la media aritmética como la ponderada.")
    print("Por favor, proporcione los detalles requeridos.")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    tipo_media = int(input("Seleccione el tipo de media (1 para aritmética, 2 para ponderada): "))

    if tipo_media == 2:
        coeficiente1 = float(input("Ingrese el coeficiente para el primer número: "))
        coeficiente2 = float(input("Ingrese el coeficiente para el segundo número: "))
        coeficiente3 = float(input("Ingrese el coeficiente para el tercer número: "))
    else:
        coeficiente1, coeficiente2, coeficiente3 = 1, 1, 1

    try:
        media_obj = Media(num1, num2, num3, tipo_media, coeficiente1, coeficiente2, coeficiente3)
        print("El resultado de la media es:", media_obj.calcular_media())
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()


