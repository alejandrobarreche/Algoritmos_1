class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True
        else:
            return False

def main():
    print("Este programa simula una cuenta bancaria.")

    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = Cuenta(saldo_inicial)

    
    opcion = input("¿Desea depositar (D) o retirar (R) fondos? \nEn caso de no querer realizar ninguna acción pulse (x) para salir. \n>>> ").upper()
    print()
    while opcion != "X":
        if opcion == "D":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
            print("Depósito exitoso. Nuevo saldo:", cuenta.saldo,end="\n")
        elif opcion == "R":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cuenta.retirar(cantidad):
                print("Retiro exitoso. Nuevo saldo:", cuenta.saldo,end="\n")
            else:
                print("No se puede retirar fondos. Saldo insuficiente.\nSu saldo sigue siendo de:", cuenta.saldo,end="\n")
        print()
        opcion = input("¿Desea depositar (D) o retirar (R) fondos? \nEn caso de no querer realizar ninguna acción pulse (x) para salir. \n>>> ").upper()
        print()
if __name__ == "__main__":
    main()

