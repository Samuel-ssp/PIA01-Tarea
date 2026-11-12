"""
Problema 3. Trabajo con conjuntos
Escribe una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
CALCULARLOS)
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos). 

"""

def conjuntos(lita1,lista2):
    # 1. Convertir ambas listas en conjuntos (set)
    conjunto1 = set(lita1)
    conjunto2 = set(lista2)

    # 2. Calcular la intersección (elementos comunes en ambos conjuntos)
    interseccion = conjunto1.intersection(conjunto2)

    # 3. Calcular la unión (todos los elementos sin duplicados)
    total = conjunto1.union(conjunto2)

    # 4. Calcular la diferencia simétrica (elementos en uno u otro, pero no en ambos)
    diferencia = conjunto1.symmetric_difference(conjunto2)

    # 5. Guardar los resultados en un diccionario y devolverlo
    informacion = {"1. Interseccion":interseccion, "2. Union":total, "3. Diferencia simétrica":diferencia}
    return informacion


# Comprobación del resultado
print(conjuntos([3,4,5,6], [4,5,6,7,8,9]))