import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers , value: int) -> Tuple[bool, int]:
    poczatek_przedzialu = 0
    koniec_przedzialu = len(numbers) - 1

    while poczatek_przedzialu <= koniec_przedzialu:
        middle = (poczatek_przedzialu+koniec_przedzialu)/2

        if numbers[int(middle)] == value:
            middle = int(middle)
            zwrot = (True,middle)
            return zwrot

        elif numbers[int(middle)] < value:
            poczatek_przedzialu+=1

        elif numbers[int(middle)] > value:
            poczatek_przedzialu-=1

    return False, -1  # wartosc nie zostala znaleziona


ints = [1, 5, 6, 7, 10, 26, 29, 40]

result = binary_search(ints, 40)
print(result)


def sortowanie_bombelkowe(lista,porzadek):

    if porzadek == '>':
        for i in range(len(lista) - 1):
            for j in range(len(lista) - 1 - i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    elif porzadek == '<':
        for i in range(len(lista) - 1):
            for j in range(len(lista) - 1 - i):
                print(i,j)
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)

def selection_sort(lista):
    print(lista)
    n_o_el = len(lista)
    for i in range(n_o_el - 1):
        imin = i

        for j in range(i,n_o_el - 1):
            if lista[j+1] < lista[imin]:
                imin = j+1

        if i != imin:
            temp = lista[i]
            lista[i] = lista[imin]
            lista[imin] = temp
        print(lista,i)

    print(lista)


def insert_sort(lista):

    for i in range(1,len(lista)):
        elem = lista[i]
        j = i
        while j > 0 and lista[j-1] > elem:
            lista[j] = lista[j-1]
            j-=1
        lista[j] = elem
    print(lista)

lista = [6, 3, 9, 0, 4]
insert_sort(lista)