def exp(a,n):
    if n<=2:
        return a*a
    
    else:
        return a*a * exp(a,n//2)

"""
tipo a*T(n/b)+P(n)

a= 1
b=2
k=0

- si a < b^k : O(n^k)
- si a = b^k : O(n^k * log(n))
- si a > b^k : O(n^logb(a))


 ->> O(log(n))
"""

print(exp(2,16))