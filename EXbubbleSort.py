lista = [2, 7, 1, 9, 8]

def bubble_Sort(lista):
    n = len(lista)

    Temporario = 0
    for j in range(len(lista)):
        for i in range(0, n - 1):
            if lista[i] > lista[j]:
                Temporario = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = Temporario
    return lista     
        
bubble_Sort(lista)
print(lista)