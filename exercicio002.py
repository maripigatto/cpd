class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def selectionSort(linked_list):
    if not linked_list.head:
        return

    start = linked_list.head
    while start:
        min_node = start
        current = start.next

        while current:
            if current.data < min_node.data:
                min_node = current
            current = current.next

        start.data, min_node.data = min_node.data, start.data
        
        start = start.next

lista = ListaEncadeada()
lista.append(5)
lista.append(3)
lista.append(4)
lista.append(1)
lista.append(2)

lista.print_list()

selectionSort(lista)

lista.print_list()