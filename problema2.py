"""
Problema 2. Frecuencia de palabras en un texto.

Escribe una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuántas veces
aparecen las distintas palabras de la lista en el fichero de texto.
Haz un pequeño programa que la ponga a prueba.

Requisitos:
1. Eliminar signos de puntuación y convertir todo a minúsculas.
2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
"""

def frecuencia_palabras(lista_palabras,ruta):
    diccionario = {}
    # 1. Leer el archivo y pasar todo el texto a minúsculas
    with open(ruta,"r", encoding="utf-8" ) as archivo:
        texto = archivo.read().lower()
    
    # 2. Eliminar signos de puntuación sustituyéndolos por espacios
    for signo in ",.:;!¡¿?":
        texto = texto.replace(signo," ")

    # 3. Dividir el texto en una lista de palabras
    palabra_texto = texto.split()

    # 4. Recorrer las palabras ordenadas y guardar su frecuencia en el diccionario
    for palabra in sorted(lista_palabras):
        diccionario[palabra] =palabra_texto.count(palabra.lower())

    return diccionario


# Comprobación del resultado
resultado =frecuencia_palabras(["Gato","casa","perro", "elefante", "tigre"],"texto.txt")
print(resultado)



    