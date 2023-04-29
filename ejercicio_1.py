"""
Escriba un programa que calcule el área de un círculo. El programa debe recibir como entrada el radio del círculo y debe imprimir el área calculada. Recuerda que el área de un círculo se calcula como A = πr^2, donde π es el número de pi (3.1416) y r es el radio del círculo.

"""

# --> Librerias
import math

# --> Entrada de datos
radio = int(input("Ingresa el radio: "))

# --> Ejecucion de operacion
valor_pi = math.pi
area_circulo = valor_pi*(radio**2)

# --> Mostrar resultado de operación
print(f"[+]El valor del area es : {area_circulo}")