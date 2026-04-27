def esPalindromo(palabra:str):
    if len(palabra) == 1: return True
    elif len(palabra) == 2: return palabra[0] == palabra[1]
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return esPalindromo(palabra[1:-1])


print(esPalindromo("neuquen"))
"""
tipo de recursion a*T(n-b) + P(n)
a = 1
b = 2
k = 0

a = 1 -> O(n)
"""