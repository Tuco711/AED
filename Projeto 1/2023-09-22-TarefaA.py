lista1 = [1, 2, 4]
lista2 = [1, 3, 4, 5, 6]

def insereOrdenado( a, lista):
    indice = 0

    while (a > lista[indice]):
        indice = indice+1

    lista.insert(indice, a)
    return lista

listaOrdenada = lista2.copy()

for a in lista1:
    insereOrdenado(a, listaOrdenada)
    
print(listaOrdenada)