def fibonacci(n):
    if n<2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
"""
tipo de recursion: a*T(n-b) + P(n)

a = 2
b = 1
k = 0

a > 1 -> O(2^n)
"""

print(fibonacci(40))