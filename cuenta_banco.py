# Definición de la clase Cuenta
class Cuenta:
    def __init__(self, saldo):
        # Inicialización del saldo de la cuenta
        self.saldo = saldo

    # Método para depositar fondos en la cuenta
    def depositar(self, cantidad):
        self.saldo += cantidad

    # Método para retirar fondos de la cuenta
    def retirar(self, cantidad):
        # Verificar si hay suficientes fondos para realizar la operación
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True  # La operación se realizó con éxito
        else:
            return False  # La operación no se pudo realizar debido a saldo insuficiente

# Función principal del programa
def main():
    print("Este programa simula una cuenta bancaria.")

    # Solicitar al usuario el saldo inicial de la cuenta
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = Cuenta(saldo_inicial)

    # Pedir al usuario que seleccione entre depositar, retirar o salir
    opcion = input("¿Desea depositar (D) o retirar (R) fondos? \nEn caso de no querer realizar ninguna acción pulse (x) para salir. \n>>> ").upper()
    print()
    # Loop para permitir al usuario realizar múltiples operaciones
    while opcion != "X":
        if opcion == "D":
            # Si el usuario elige depositar fondos
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
            print("Depósito exitoso. Nuevo saldo:", cuenta.saldo)
        elif opcion == "R":
            # Si el usuario elige retirar fondos
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cuenta.retirar(cantidad):
                print("Retiro exitoso. Nuevo saldo:", cuenta.saldo)
            else:
                print("No se puede retirar fondos. Saldo insuficiente.\nSu saldo sigue siendo de:", cuenta.saldo)
        print()
        # Pedir al usuario que seleccione nuevamente
        opcion = input("¿Desea depositar (D) o retirar (R) fondos? \nEn caso de no querer realizar ninguna acción pulse (x) para salir. \n>>> ").upper()
        print()

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    # Llamar a la función main si es así
    main()
