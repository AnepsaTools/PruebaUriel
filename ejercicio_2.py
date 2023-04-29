"""
Escribe una función que reciba como parámetro una lista de números enteros y devuelva el promedio de los valores en la lista.
"""
# --> Librerias
import statistics

# --> Función
def promedio_lista(lista):
    """Promediara la lista de datos recibida"""
    promedio = statistics.mean(lista)
    return promedio

# --> Ejecución de código
lista_numeros = [1,2,3,4,5,6]
print(promedio_lista(lista_numeros))