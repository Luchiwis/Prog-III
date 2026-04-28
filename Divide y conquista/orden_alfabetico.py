def orden_alfabetico(vector: list) -> bool:
    if len(vector) == 1:
        return True
    
    primera_mitad = vector[:len(vector)//2]
    segunda_mitad = vector[len(vector)//2:]
    
    return orden_alfabetico(primera_mitad) < orden_alfabetico(segunda_mitad) 


print(orden_alfabetico(["a","b","c","f","d","k"]))