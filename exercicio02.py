
def select_sort(data):
    n = len(data)
    for t in range(n - 1):
        menor = data[t]
        menor_id = t
        for j in range(t + 1, n):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
        data[t], data[menor_id] = data[menor_id], data[t]


lista = [3, 2, 1, 4, 5]
select_sort(lista)
print(lista) 