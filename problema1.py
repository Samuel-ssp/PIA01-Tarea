# Crea una función que reciba una lista de enteros por parámetro y devuelva otra lista, de acuerdo a las siguientes acciones:
# 1. Eliminar los números negativos de la lista.
# 2. Eliminar los valores que están repetidos, quedándonos con uno de ellos.
# 3. Ordenar los números resultantes de menor a mayor.

def ordenar(lista):
    positivos = []
    
    for numero in lista:
        # 1. Eliminar los números negativos ( mayores o iguales a cero)
        if numero >= 0:
            # 2. Eliminar duplicados (solo añadir si aún no está en la lista resultante)
            if numero not in positivos:     
                positivos.append(numero)

    # 3. Ordenar los números  de menor a mayor
    positivos.sort()
    
    return positivos


# Comprobación del resultado
print(ordenar([4, -1, 2, 4, 3, -5, 2]))  # Salida [2,3,4]
