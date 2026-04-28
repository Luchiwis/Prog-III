pico = [1,2,5,7,10,23,4,2,1,0]


def encontrarPico(vector:list) -> int:
    inicio = 0
    fin = len(vector) - 1

    while (inicio < fin):
        medio = (inicio + fin) // 2

        if vector[medio] < vector[medio+1]:
            # seguimos en la parte creciente
            inicio = medio + 1
        else:
            #nos fuimos a la parte decreciente
            fin = medio
    
    return inicio


"""
problema de tipo a*T(a/b) + P(n)

a=1
b=2
k=0

a = b^k -> O(n^k*log(n)) -> O(log(n))

para a*T(n/b)+ P(n)
- si a < b^k : O(n^k)
- si a = b^k : O(n^k * log(n))
- si a > b^k : O(n^logb(a))
"""

print(encontrarPico(pico))