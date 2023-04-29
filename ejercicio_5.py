"""
Escribe una función que reciba como parámetros dos números enteros y devuelva el resultado de la división de estos dos números. Si el segundo número es cero, la función debe devolver un mensaje de error indicando que la división por cero no está permitida.
"""

def division_dos_numeros(a,b):
    # --> Convertir numeros a enteros
    a = int(a)
    b = int(b)
    try:
        division = a/b
        print(division)
    except ZeroDivisionError:
        print("[+]El denominador no puede ser 0")

# --> Ejecución de código
division_dos_numeros(2,0)