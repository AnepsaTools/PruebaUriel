"""
Escribe una función que reciba como parámetro una lista de palabras y devuelva una nueva lista con las palabras que empiezan y terminan con la misma letra. Por ejemplo, si la lista es ["hola", "adiós", "anna", "oso"], la función debe devolver ["anna", "oso"].
"""


# --> Funciones

def palabras_inicio_fin(lista_palabras):
    """ Determinara si cada palabra empieza y termina con la misma letra"""

    # --> Lista de palabras que cumplen la condicion
    nueva_lista = []
    # --> Leer cada palabra de la lista
    for palabra in lista_palabras:
        # --> Revisar condicion de palabra
        if palabra[0] == palabra[-1]:
            nueva_lista.append(palabra)
    return nueva_lista

# --> Ejecución de código
lista = ["hola", "adiós", "anna", "oso","ala"]

print(palabras_inicio_fin(lista))