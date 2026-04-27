def quickSort(vector:list)->list:
    if len(vector) <= 1:
        return vector

    pivot = vector[-1]
    a = 0
    b = -1
    while a < len(vector):
        if vector[a]>pivot:
            pass
        else:
            b+=1
            if (vector[a]<=vector[b]):
                vector[a], vector[b] = vector[b], vector[a] #swap
        a+=1
    pos_pivot = b
    return quickSort(vector[:pos_pivot]) + [pivot] + quickSort(vector[pos_pivot+1:])

"""

caso promedio (el pivot siempre queda en el medio):
a*T(n/b) + P(n)
a = 2
b = 2
k = 1

O(nlog(n))

peor caso (el pivot siempre queda en un extremo):
a*T(n-b) + P(n)
a = 1
b = 1
k=1

O(n^2)
"""

print(quickSort([1,6,5,3,9,7,55,4,3]))