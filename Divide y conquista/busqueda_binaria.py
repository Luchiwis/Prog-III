def busqueda_binaria(numeros:list, encontrar:int) -> int:
    mitad = len(numeros) // 2
    numero_medio = numeros[mitad]
    if mitad == 0 and numero_medio != encontrar:
        return False
    elif numero_medio == encontrar:
        return True
    elif numero_medio > encontrar:
        return busqueda_binaria(numeros[:mitad], encontrar)
    elif numero_medio < encontrar:
        return busqueda_binaria(numeros[mitad:], encontrar)
    
"""
a = 1
b = 2
k = 0

b^k = 1 -> n^k*log(n) -> O(log(n))
"""

print(busqueda_binaria([1,2,6,8,20,21,40,43,44,54,65],41))