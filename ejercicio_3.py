"""
Escribe una función que reciba como parámetro una cadena de caracteres y verifique si es un palíndromo. Un palíndromo es una cadena que se lee igual de atrás hacia adelante que de adelante hacia atrás. Por ejemplo, "ana" es un palíndromo, pero "hola" no lo es.
"""

# --> Funciones

def invertir_cadena(cadena):
    """Función secundaria"""

    return cadena[::-1]


def es_palindromo(texto):
    """Función primaria"""

    palabra_invertida = invertir_cadena(texto)
    # --> Verificar
    if palabra_invertida == texto:
        # --> Si es palindromo
        print(f"[+]Es palindromo la palabra: {texto}")
    else:
        print(f"[-]No es palindromo la palabra: {texto}")
        # --> Si no es palindromo

# --> Ejecución de código
es_palindromo("juan")