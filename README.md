# EJERCICIOS DE INTRODUCCIÓN A LA ALGORITMIA
## Realizado por Alejandro Barreche


# Algoritmo para Calcular el Precio Final de un Producto

1. **Definición de Tipos de Producto**: Se establecen categorías de productos con diferentes tasas de impuesto a través de una enumeración (`Enum`).

2. **Solicitud de Datos al Usuario**:
   - Se solicita el nombre del producto
   - Se solicita el precio base sin impuestos del producto.
   - Se solicita al usuario que elija el tipo de impuesto aplicable, ofreciendo 4 opciones.

3. **Instanciación de la Clase `Precio`**:
   - Se crea un objeto de la clase `Precio`, pasándole el nombre del producto, el precio base, y el tipo de impuesto seleccionado.

4. **Cálculo del Impuesto**:
   - Dentro de la clase `Precio`, se determina el porcentaje de impuesto basado en la selección del usuario.
   - Si el producto tiene un tipo de impuesto especial, se solicita al usuario introducir el porcentaje específico de este impuesto.

5. **Cálculo del Precio Final**:
   - Se calcula el precio final del producto aplicando el porcentaje de impuesto al precio base.


# Algoritmo para Calcular Intereses Generados

1. **Solicitud de Datos al Usuario**:
   - Se solicita al usuario que ingrese el capital inicial invertido.
   - Se solicita al usuario que seleccione el tipo de interés, ofreciendo las opciones de interés simple (1) o compuesto (2).
   - Se solicita al usuario que ingrese la tasa de interés en porcentaje.
   - Se solicita al usuario que ingrese el tiempo de la inversión en meses.

2. **Instanciación de la Clase `Interes`**:
   - Se crea una instancia de la clase `Interes`, pasando como parámetros los valores ingresados: capital, tipo de interés, tasa de interés, y tiempo.

3. **Cálculo de Intereses**:
   - Dentro de la clase `Interes`, se ejecuta el método `calcular_intereses_generados` para determinar los intereses generados.
   - Se emplea una estructura condicional para aplicar la fórmula correspondiente al tipo de interés seleccionado: simple o compuesto.
     - **Interés Simple**: Se calcula multiplicando el capital por la tasa de interés por el tiempo (en meses), dividido por 12.
     - **Interés Compuesto**: Se calcula como el capital por uno más la tasa de interés elevado al tiempo (en meses), menos el capital inicial.


# Algoritmo para Calcular el Área de un Triángulo

1. **Solicitud de Datos al Usuario**:
   - Se pide al usuario que ingrese la medida del lado del triángulo.
   - Se solicita al usuario que ingrese la altura relativa a ese lado.

2. **Instanciación de la Clase `Triangulo`**:
   - Con los datos proporcionados por el usuario, se crea una instancia de la clase `Triangulo`, pasando como parámetros la medida del lado y la altura.

3. **Cálculo del Área**:
   - Se llama al método `calcular_area` de la instancia de `Triangulo` para calcular el área.
   - Este método calcula el área multiplicando la base (lado) por la altura y dividiendo el resultado entre 2.

# Algoritmo para Calcular Medias

1. **Solicitud de Datos al Usuario**:
   - Se solicita al usuario que ingrese tres números, uno por uno.
   - Se solicita al usuario que elija el tipo de media que desea calcular: aritmética (1) o ponderada (2).

2. **Condición para Coeficientes**:
   - Si el usuario elige calcular la media ponderada (2), se le pide que ingrese los coeficientes para cada uno de los tres números.
   - Si el usuario elige la media aritmética, se asume que los coeficientes son todos iguales a 1.

3. **Instanciación de la Clase `Media`**:
   - Se crea una instancia de la clase `Media`, pasando como parámetros los tres números, el tipo de media seleccionado, y los coeficientes (si aplica).

4. **Cálculo de la Media**:
   - Dentro de la instancia de `Media`, se ejecuta el método `calcular_media` para determinar la media según el tipo seleccionado.
   - Para la media aritmética, se calcula sumando los productos de cada número por su coeficiente y dividiendo el total entre 3.
   - Para la media ponderada, se calcula de forma similar, pero el divisor es la suma de los coeficientes.


# Algoritmo para Calcular el Importe de Horas Extra

1. **Solicitud de Datos al Usuario**:
   - Se pide al usuario que ingrese su salario bruto mensual.
   - Se solicita al usuario que indique el número de horas extra trabajadas en el mes.

2. **Instanciación de la Clase `CalculadoraNomina`**:
   - Se crea una instancia de `CalculadoraNomina` utilizando el salario bruto y las horas extra proporcionadas por el usuario.

3. **Cálculo de las Horas Extra**:
   - Dentro de la clase, se calcula el salario por hora normal dividiendo el salario bruto mensual entre el total de horas regulares trabajadas en el mes (asumiendo una semana de 35 horas).
   - Se determina el número de horas extra básicas (hasta 8 horas extra) y avanzadas (más de 8 horas extra).
   - Se calcula el importe a pagar por las horas extra básicas aplicando un aumento del 125% sobre el salario por hora.
   - Para las horas extra avanzadas, se aplica un aumento del 150% sobre el salario por hora.
   - Se suma el importe de ambos rangos de horas extra para obtener el salario total por horas extra.


# Algoritmo para Simular una Cuenta Bancaria

1. **Solicitud del Saldo Inicial**:
   - Se solicita al usuario ingresar el saldo inicial de la cuenta.

2. **Creación de la Cuenta**:
   - Con el saldo inicial proporcionado, se crea una instancia de la clase `Cuenta`.

3. **Bucle de Operaciones**:
   - Se presenta al usuario la opción de depositar (D), retirar (R) fondos, o salir del programa (X).
   - Si el usuario elige depositar:
     - Se pide ingresar la cantidad a depositar.
     - Se realiza el depósito y se muestra el nuevo saldo.
   - Si el usuario elige retirar:
     - Se solicita ingresar la cantidad a retirar.
     - Si hay saldo suficiente, se realiza el retiro y se muestra el nuevo saldo.
     - Si no hay saldo suficiente, se informa al usuario y se muestra el saldo actual.
   - El bucle continúa hasta que el usuario decide salir (X).




