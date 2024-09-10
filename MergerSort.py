

def Mesclar(esquerda, direita):
    
    lista_vazia = list()

    while (len(esquerda) != 0 and len(direita) != 0):
        if esquerda[0] <= direita[0]:
            lista_vazia.append(esquerda[0])
            esquerda.pop(0)
        else:
             lista_vazia.append(direita[0])
             direita.pop(0)
        
    while (len(esquerda) != 0):
        lista_vazia.append(esquerda[0])
        esquerda.pop(0)
    
    while(len(direita) != 0):
         lista_vazia.append(direita[0])
         direita.pop(0)
         
    return lista_vazia
         

def MergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    esquerda = lista[:meio] 
    direita = lista[meio:] 
    
    lista_ordenada_esquerda = MergeSort(esquerda)
    lista_ordenada_direita = MergeSort(direita)
    
    return Mesclar(lista_ordenada_esquerda, lista_ordenada_direita)

lista = [2, 8, 4, 5, 3, 7, 6]
lista = MergeSort(lista)
print(lista)
