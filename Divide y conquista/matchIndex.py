def matchIndex(vector:list, desde, hasta)->int:
    if hasta-desde == 1:
        return vector[desde] == desde

    indice_medio = ((hasta-desde) // 2) + desde
    if vector[indice_medio] == indice_medio:
        return indice_medio
    elif vector[indice_medio] < indice_medio: #seguir por la mitad derecha
        return matchIndex(vector, indice_medio, hasta)
    elif vector[indice_medio] > indice_medio: #seguir por la mitad izquierda
        return matchIndex(vector, desde, indice_medio)
    

        
print(matchIndex([-6,-3,-1,0,0,2,5,7,10],0, 8))