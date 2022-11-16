from typing import List

#tworzenie klasy
class Mac_2d_p:
    dane: List[int]
    wys: int
    szer: int
    #tworzenie inicjalizatora

    def __init__(self,wys,szer):
        self.szer = szer
        self.wys = wys
        self.dane = []
        for miejsce in range(wys*szer):
            self.dane.append(0)

    def __str__(self):
        string = ""
        for wys in range(self.wys):
            for szer in range(self.szer):
                k = wys + self.wys * szer
                string = string + str(self.dane[wys +szer * self.wys]) + '\t'
            string += '\n'
        return string

    def __add__(self, macierz):
        wieksze_szer = max(macierz.szer, self.szer)
        wieksze_wys = max(macierz.wys, self.wys)

        if macierz.szer != self.szer or macierz.wys != self.wys:
            macierz.wyrowanj(wieksze_wys, wieksze_szer)
            self.wyrowanj(wieksze_wys, wieksze_szer)

        dodane = Mac_2d_p(wieksze_wys, wieksze_szer)

        for szer in range(self.szer):
            for wys in range(self.wys):
                index = wys + szer * self.wys
                dodane.dane[index] = self.dane[index] + macierz.dane[index]

        return dodane

    def macierzowanie(self):
        macierz = []
        for i in range(self.szer):
            macierz.append([int(0) for liczba in range(self.wys)])

        for szer in range(self.szer):
            for wys in range(self.wys):
                if self.dane[wys + szer * self.wys] in self.dane:
                    macierz[szer][wys]=self.dane[wys+ szer * self.wys]

        return macierz

    def listowanie(self,macierz):
        lista = []
        for wiersz in macierz:
            lista = lista + wiersz
        return lista

    def wyrowanj(self,nr_wiersza,nr_kolumny):
        macierz = self.macierzowanie()
        if nr_kolumny>self.szer:
            for kolumna in range(nr_kolumny-self.szer):
                macierz.append([int(0) for liczba in range(self.wys)])
            self.szer = nr_kolumny
        if nr_wiersza > self.wys:
            for wiersz in macierz:
                while len(wiersz) != nr_wiersza:
                    wiersz.append(0)
            self.wys = nr_wiersza

        macierz = self.listowanie(macierz)
        self.dane = macierz

    def ustal(self,nr_wiersza,nr_kolumny,wartosc):
        if nr_wiersza <= 0 or nr_kolumny <= 0:
            print("No chyba żarty wypad mi z tymi minusami")
            return None
        if nr_wiersza > self.wys or nr_kolumny > self.szer:
            self.wyrowanj(nr_wiersza,nr_kolumny)
        self.dane[(nr_wiersza-1) + (nr_kolumny-1)*self.wys] = wartosc

    def pobierz(self,nr_wiersza,nr_kolumny):

        if nr_wiersza <= 0 or nr_kolumny <= 0:
            return 0
        if nr_wiersza*nr_kolumny > self.wys*self.szer:
            return 0
        return self.dane[(nr_wiersza-1) + (nr_kolumny-1)*self.wys]

    def transponuj(self):
        transpozycja = Mac_2d_p(self.szer,self.wys)
        macierz = self.macierzowanie()
        trans = [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]
        macierz = trans
        macierz = self.listowanie(macierz)
        transpozycja.dane = macierz
        return transpozycja

    def uprosc_kolumne(self):
        macierz = self.macierzowanie()
        do_usuniecia = []
        index = self.szer - 1
        for kol in reversed(macierz):
            if all(zawartosc==0 for zawartosc in kol):
                do_usuniecia.append(index)
            if not all(zawartosc == 0 for zawartosc in kol):
                break
            index -= 1

        for index in do_usuniecia:
            macierz.pop(index)
            self.szer -= 1

        lista = self.listowanie(macierz)
        self.dane = lista

    def uprosc(self):
        self.uprosc_kolumne()
        trans = self.transponuj()
        trans.uprosc_kolumne()
        trans = trans.transponuj()
        self.dane = trans.dane
        self.szer = trans.szer
        self.wys  = trans.wys

macierz = Mac_2d_p(3,3)
macierz2 = Mac_2d_p(2,4)
print(macierz)

macierz.dane=[0,1,2,3,4,5,6,7,8]
macierz.ustal(5,4,0)

macierz2.ustal(1,1,0)
macierz2.ustal(2,1,1)
macierz2.ustal(3,1,2)
macierz2.ustal(1,2,3)
macierz2.ustal(2,2,4)
macierz2.ustal(3,2,5)
macierz2.ustal(1,3,6)
macierz2.ustal(2,3,7)
macierz2.ustal(3,4,8)

print(macierz)
print(macierz)
trans = macierz.transponuj()
print(trans)
print(macierz2)
dodane = macierz+macierz2
print(dodane)

print(macierz)
macierz.uprosc()
print(macierz)
