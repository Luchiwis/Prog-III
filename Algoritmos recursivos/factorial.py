def factorial(n):
    if (n == 1): #caso base
        return 1
    else:
        return n * factorial(n-1)

#la funcion factorial es una recurrencia de tipo "sustracción" a*T(n-b) + p(n)
# a=1 (el maximo de veces que factorial puede autoinvocarse)
# b = 1 (por cuanto se reduce el problema en cada recursion)
# p(n) = k = 0 es el costo de las operaciones adicionales fuera de la recursion, en este caso es la multiplicación (una operacion constante) por lo que el grado del polinomio p(n) es 0

"""
en una recursion de tipo sustraccion a*T(a-b) + p(n)

si a < 1 : O( n^k )
si a = 1 : O( n^(k+1) )
si a > 1 : O( a^(n/b) )
"""

print(factorial(5))