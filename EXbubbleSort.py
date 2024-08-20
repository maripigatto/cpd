listaAleatorios = [2, 7, 1, 9, 8]
listaOrdenada = [1, 2, 3, 4, 5]
listaRepetida = [1, 2, 3, 3, 4]
listaReversa = [5, 4, 3, 2, 1]

def linha():
    s = 32 * '#'
    print(s)

def bubble_Sort(lista):
    n = len(lista)
    Temporario = 0

    for j in range(len(lista)):
        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]:
                Temporario = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = Temporario
    return lista     
        
bubble_Sort(listaAleatorios)
print("Lista Aleatoria:",listaAleatorios)
linha()
bubble_Sort(listaOrdenada)
print("lista Ordenada:",listaOrdenada)
linha()
bubble_Sort(listaRepetida)
print("lista Repetida:",listaRepetida)
linha()
bubble_Sort(listaReversa)
print("lista Reversa:", listaReversa)