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

def insertionSort(linked_list):
    sorted_list = None

    current = linked_list.head
    while current:
        next_node = current.next

        if not sorted_list or sorted_list.data >= current.data:
            current.next = sorted_list
            sorted_list = current
        else:
            sorted_current = sorted_list
            while sorted_current.next and sorted_current.next.data < current.data:
                sorted_current = sorted_current.next

            current.next = sorted_current.next
            sorted_current.next = current

        current = next_node

    linked_list.head = sorted_list

lista = ListaEncadeada()
lista.append(5)
lista.append(3)
lista.append(4)
lista.append(1)
lista.append(2)

lista.print_list()

insertionSort(lista)

lista.print_list()