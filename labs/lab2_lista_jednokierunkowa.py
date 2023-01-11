from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self,value:Any):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):

        self.tail = None
        self.head = None

    def push(self,value: Any) -> None:

        if self.head == None and self.tail == None:
            self.head = Node(value)
            self.tail = self.head

        elif self.head == self.tail and self.tail != None:

            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            self.tail = temp
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    def append(self, value: Any) -> None:

        if self.head == None and self.tail == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def node(self,at: int) -> Node:

        licznik = 0
        curr = self.head
        while licznik != at:
            curr = curr.next
            licznik += 1

        return curr

    def insert(self,value:Any, after:Node):

        if after.next == None:
            self.append(value)
        else:
            curr = self.head
            while curr != after:
                curr = curr.next

            nexter = curr.next
            new = Node(value)
            new.next = nexter
            curr.next = new

    def pop(self):

        pierwszy_el = self.head
        self.head = self.head.next
        return pierwszy_el

    def remove_last(self):

        if self.head == self.tail:
            ostatni_element = self.tail
            self.head = None
            self.tail = None
            return ostatni_element

        ostatni_element = self.tail
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        self.tail = curr
        self.tail.next = None

        return ostatni_element

    def remove(self, after:Node):

        if after == self.tail:
            pass

        curr = self.head
        while curr.next != after:
            curr = curr.next
        curr.next = curr.next.next


    def __str__(self):
        lista = ''
        curr = self.head
        while curr != None:
            lista = lista +" "+ str(curr.value)
            if curr.next != None:
                lista = lista + " " + '->'
            curr = curr.next
            lista = lista.strip()
        return lista

    def __len__(self):
        curr = self.head
        licznik = 0
        while curr != None:
            licznik+=1
            curr = curr.next
        return licznik

class Stack:

    storage: LinkedList

    def __init__(self):
        self.storage = LinkedList()

    def push(self, value: Any) -> None:
        self.storage.push(value)

    def pop(self):
       return self.storage.pop()

    def __str__(self):
        string = self.storage.__str__()
        return string

    def __len__(self):
        return self.storage.__len__()

class Queue:

    storage: LinkedList

    def __init__(self):
        self.storage = LinkedList()

    def enqueue(self,value):
        self.storage.append(value)

    def peek(self):
        return self.storage.head.value

    def dequeue(self):
        return self.storage.pop().value

    def __len__(self):
        return self.storage.__len__()

    def __str__(self):
        kolejka = ''
        curr = self.storage.head
        while curr != None:
            kolejka = kolejka + str(curr.value)
            if curr.next is not None:
                kolejka = kolejka + ', '
            curr = curr.next
        return kolejka
# zadanie 1
def zadanie1():
    lista_jednokierunkowa = LinkedList()

    assert lista_jednokierunkowa.head == None


    lista_jednokierunkowa.push(4)
    lista_jednokierunkowa.push(3)
    lista_jednokierunkowa.push(2)
    lista_jednokierunkowa.push(1)

    lista_jednokierunkowa.append(5)

    lista_jednokierunkowa.node(0)
    assert str(lista_jednokierunkowa) == '1 -> 2 -> 3 -> 4 -> 5'

    first_element = lista_jednokierunkowa.node(at=0)
    returned_first_element = lista_jednokierunkowa.pop()

    assert first_element.value == returned_first_element.value

    last_element = lista_jednokierunkowa.node(at=3)

    returned_last_element = lista_jednokierunkowa.remove_last()

    assert last_element.value == returned_last_element.value
    assert str(lista_jednokierunkowa) == '2 -> 3 -> 4'
    second_node = lista_jednokierunkowa.node(at=1)
    lista_jednokierunkowa.remove(second_node)
    assert str(lista_jednokierunkowa) == '2 -> 4'

# koniec zadania 1

# zadanie 2
def zadanie2():
    stack = Stack()

    assert len(stack) == 0

    stack.push(3)
    stack.push(10)
    stack.push(1)

    assert len(stack) == 3

# koniec zadania 2

# zadanie 3

def zadanie3():
    queue = Queue()
    assert len(queue) == 0

    queue.enqueue('klient1')
    queue.enqueue('klient2')
    queue.enqueue('klient3')

    assert str(queue) == 'klient1, klient2, klient3'

    client_first = queue.dequeue()

    assert client_first == 'klient1'
    assert str(queue) == 'klient2, klient3'
    assert len(queue) == 2

# koniec zadania 3
