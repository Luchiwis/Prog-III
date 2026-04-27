def exp2(a, b):

    if ( b==0 ):
        print(f"({a},{b})=> 1")

        return 1
    else:
        result = exp2(a*a, b//2)
        if (b%2 == 1):
            result = a * result
        print(f"({a},{b})=>{result}")
        return result
    
# es un a recursion de tipo division T(n/b)
# a = 1 (el maximo de veces que se invoca la funcion dentro de si misma)
# b = 2 (por cuanto se reduce el problema en cada recursion)
# k = 0 (el grado del polinomio de p(n) que en este caso es una multiplicacion)

"""
en una recursion de tipo division a*T(a/b)+p(n)

si a < b^k : O(n^k)
si a = b^k : O(n^k * log(n))
si a > b^k : O(n^(logb(a)))

"""

print(exp2(2,14))