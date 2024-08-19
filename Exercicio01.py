def insertionSort(data):
    n = len(data)

    for contj in range(1, n):
        tmp = data[contj]
        i  = contj - 1

        while i >= 0 and tmp < data[i]:
            data[i + 1] = data[i]
            i -= 1

        data[i + 1] = tmp

data = [3, 2, 1, 4, 5]
insertionSort(data)
print(data)