def mergeSort(vector: list) -> list:
    if len(vector) <= 1:
        return vector
    
    mid = len(vector) // 2
    primer_mitad = mergeSort(vector[:mid])
    segunda_mitad = mergeSort(vector[mid:])
    
    # Merge correcto
    resultado = []
    i = 0
    j = 0
    #recorrido paralelo de ambos vectores
    while i < len(primer_mitad) and j < len(segunda_mitad):
        if primer_mitad[i] <= segunda_mitad[j]:
            resultado.append(primer_mitad[i])
            i += 1
        else:
            resultado.append(segunda_mitad[j])
            j += 1
    print(resultado,primer_mitad[i:], segunda_mitad[j:])
    resultado = resultado + primer_mitad[i:] + segunda_mitad[j:] #sumamos el array con las sobras
    return resultado

"""
es una recursion de tipo a*T(a/b) + P(n)

a = 2
b = 2
k = 1

a = b^k -> n^k*log(n) -> n*log(n)

"""

print(mergeSort([4,7,0,9,0,5,4,2]))
