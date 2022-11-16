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
  """
  Tworzenie __str__
    Dodajemy do stringa po kolei według kolejności jaka była by w tablicy dwuwymiarowej.
    Pamiętaj, że lecimy po kolumnach. temu najpierw wys a potem szer
  """
    def __str__(self):
        string = ""
        for wys in range(self.wys):
            for szer in range(self.szer):
                string = string + str(self.dane[wys +szer * self.wys]) + '\t'
            string += '\n'
        return string
"""
Tworzenie __add__
    Ustalamy sobie na początku największe wymiary bo kto mi zabroni. 
    W if sprawdzamy ew niezgodność:
        Jeżeli wymiary macierzy są nie zgodne to wykonuje się metoda wyrowna().
        
    Tworzymy nowy obiekt do zwrócenia, oczywiście wykorzystujemy nowo zyskane wielkość.
    
    Trudne się skończyło, lecimy forem i dodajemy. 
    Pamiętemy żeby zwrócić obiekt
"""
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
""""
THIS IS WHERE THE FUN BEGINS
    Słuchaj tego. Największa trudność jak dla mnie tutaj to w tym wszystkim to jest brak tablicy tablic.
    Więc pozdro 6set na rejonie. Robie sobie tablice tablic. 
    Czy to legalne? 
    Nie wiem. W konstytucji o tym nie piszą. 
    
    Macierzowanie to prosta sprawa a dużo ułatwia. 
    Deklarujemy sobie pustą tablicę i szybkim forem ją wypełniamy. 
    
    Potem trochę wolniejszym forem lecimy żeby wypełnić macierz wartościami. Oczywiście po kolumnach. Dlaczego? Nie wiem, działa po co wnikać
    
    Zwracamy sobie tą macierz do dalszego użytku.
    
    WAŻNE WIĘC SIĘ SKUP. 
    macierz to nie obiekt ani nie tablica jednowymiarowa. Czyli self.dane = macierz nic ci nie da. W sensi da. Fige z makiem. 
"""
    def macierzowanie(self):
        macierz = []
        for i in range(self.szer):
            macierz.append([int(0) for liczba in range(self.wys)])

        for szer in range(self.szer):
            for wys in range(self.wys):
                   macierz[szer][wys]=self.dane[wys+ szer * self.wys]

        return macierz
""""
Każde ing ma swoje jang. 
    Aby równowaga świata została zachowana robimy z macierzy liste.
    Jak? 
    Ano łatwo. 
    Pusta lista. 
    Pętla for po macierzy
    Dodajemy do pustej listy listy zawarte w macierzy
    ***obrazek poglądowy*** [[kolumna],[kolumna]] - for kolumna in macierz-> [lista] = [lista]+[kolumna] 
    Zwracamy liste
"""
    def listowanie(self,macierz):
        lista = []
        for kolumna in macierz:
            lista = lista + wiersz
        return lista
""""
    Wyrówanie robimy w oddzielnej metodzie bo aż dwie inne metody z niego korzystają. 
    Do tego można się chwalić, że jest się programistą15K
    
    Więc po kolei: 
      Argument przyjmuje docelowy rozmiar.
        Robimy macierz (dobrze, że mamy na to metode).
        if sprawdza czy dany rozmiar się zgadza.
            Jeżeli nie to równamy. 
                kolumny: wyrówanie kolumn w macierzy to łatwizna, dowalasz po prostu kolejną tablicę o danym rozmiarze wypełnioną zerami*
                        *autor progamu nie liczy się jako zero
                         Ile tego dodać? Ano różnicę tego co ma być z tym co jest.
                         Ktoś by powiedział "nr_kolumny - akutalna szerokość" ale ja bym mu nie wierzył to nie może być takie łatwe.
                         Na koniec pamiętamy aby przedeklarować rozmiar. Ważne fest. 
                         self.szer = nr_kolumny
                         
                wiersze: no równanie wierszy to tragedia. Sprawa trudna i skomplikowana. 
                A nie czekaj, przecież to nie jest kraizi macierz w tablicy jednowymiarowej.
                To essa lecimy po kolumnach i dodajemy na koniec każdej 0. 
                Ile zer? 
                No tyle żeby było dobrze. 
                Czyli  while len(kolumna) != nr_wiersza:
                                kolumna.append(0)
                Słownie dodajemy zera aż długość kolumny nie będzie taka jaka ma być.
                
                Możesz się zastanawiać, "Ale czemu wydłużam kolumne?"
                Spieszę z odpowiedzią.
                Dla tablicy jednowymiarowej:       Dla tablicy dwuwymiarowej:  
                dane[1,2,3,4]                      macierz[[1,2],[3,4]]
                                            1 3   
                                            2 4
                Łatwo więc zauważyć, że:
                dane[1,2,0,3,4,0]                      macierz[[1,2,0],[3,4,0]]
                                            1 3
                                            2 4
                                            0 0
               
               A jak już dodasz to przedelkaruj rozmiar. Ważna sprawa serio.
               self.wys = nr_wiersza
               
               Listowanie zwraca ci listę, wiem szok. 
               Więc można self.dane = lista
"""
    def wyrowanj(self,nr_wiersza,nr_kolumny):
        macierz = self.macierzowanie()
        if nr_kolumny>self.szer:
            for kolumna in range(nr_kolumny-self.szer):
                macierz.append([int(0) for liczba in range(self.wys)])
            self.szer = nr_kolumny
            
        if nr_wiersza > self.wys:
            for kolumna in macierz:
                while len(kolumna) != nr_wiersza:
                    kolumna.append(0)
            self.wys = nr_wiersza

        lista = self.listowanie(macierz)
        self.dane = lista
"""
A oto i ona, moja nemezis. Pomiot szatana z najgłębszych czeluści kulkańskiej. 

Jak coś ma się zjebać to pewnie tutaj 

Dlaczego? Bo ta metoda korzysta z innych, czyli jak jesteś debil i nie potrafisz dobrze zrobić wyrownaj(), macierzowanie(), listowanie() to tyle dziękuję dowidzenia. 

Generalnie nie jest ona wcale aż tak skomplikowana. Ot i prosta sprawa.
    Sprawdzamy czy wiersze i kolumny są w zakresie. 
        Jak nie są to o zgrozo używasz wyrownaj() i już są
    A jak już są to podmieniasz wartość we wcześniej zadanym miejscu i jest dobrze.
    Pamiętaj, że tablice indeksujemy od 0 czyli musisz odjąć jeden od współrzędnych bo macierz tego nie wytrzyma.
"""
    def ustal(self,nr_wiersza,nr_kolumny,wartosc):
        
        if nr_wiersza <= 0 or nr_kolumny <= 0:
            print("No chyba żarty wypad mi z tymi minusami")
            return None
        if nr_wiersza > self.wys or nr_kolumny > self.szer:
            self.wyrowanj(nr_wiersza,nr_kolumny)
            
        self.dane[(nr_wiersza-1) + (nr_kolumny-1)*self.wys] = wartosc
"""
Tu nie ma nic ciekawego. Miłego dnia. 
"""
    def pobierz(self,nr_wiersza,nr_kolumny):

        if nr_wiersza <= 0 or nr_kolumny <= 0:
            return 0
        if nr_wiersza*nr_kolumny > self.wys*self.szer:
            return 0
        return self.dane[(nr_wiersza-1) + (nr_kolumny-1)*self.wys]
"""
Jak transponować? 

Prosto. 
Robisz maciesz. Bierzesz kod z na transponowanie macierzy z neta.
Fiku miuku i masz przetransponowane. 
Robisz macierz na liste. 
Pamiętamy oczywiście, że mamy zwrócić przetransponowaną macierz, czyli koniecznie, trzeba zrobić nową instancję klasy
"""
    def transponuj(self):
        transpozycja = Mac_2d_p(self.szer,self.wys)
        macierz = self.macierzowanie()
        trans = [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]
        macierz = trans
        macierz = self.listowanie(macierz)
        transpozycja.dane = macierz
        return transpozycja
"""
Jak uproscić macierz? 
Ciężki kawałek chleba jeżeli ktoś jest głupi, naszczęscie usunąć tablice z tablicy tablic jest już łatwo.
Macieżujemy. 
Robimy sobie nową listę na indeksy do usunięcia (trochę głupie ale ja tak zrobiłem i ty to czytasz więc nwm kto jest głupszy)
Robimy zmienną na indeks bo jest potrzebna, chyba. Pomniejszamy ją o 1 i jest dobrze

For sprawdzamy, czy dane kolumny to same zera. A i odwracamy kolejność czytania, żeby najpierw zapisały się indeksy kolumn zewnętrznych
    Jeżeli tak to bosko zapisujemy indeks i go pomniejszamy.
    
    Jeżeli nie to break. Ważna sprawa bo bez tego breka usuną się wszystkie kolumny zerowe. 
    
    Właśnie dotarło do mnie, że mogłem to whilem zrobić. 
    Nie ważne, jestem zmęczony.
    
    Drugi for leci po tablicy z indeksami usunięć.
    Ale głupia ta metoda
    
    Macierz na liste i podmieniamy. 
    self.dane = lista
"""
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
"""
Jestem już całkowicie bez mocy...
    Upraszczanie jest łatwe. 
    upraszczasz kolumny
    transponujesz
    upraszczasz kolumny transpozycji
    transponujesz transpozycje
    przypisujesz wartości
   
"""
    def uprosc(self):
        self.uprosc_kolumne()
        trans = self.transponuj()
        trans.uprosc_kolumne()
        trans = trans.transponuj()
        self.dane = trans.dane
        self.szer = trans.szer
        self.wys  = trans.wys
"""
Polecam usunąć wszystko i pokolei sprawdzać co jak i CZY działa. Żadnej gwarancji nie daje. Ten kod się kompiluje. Jest niezgodny z PEP8 i ma 69 (nice) warningów.
Co prawda nic poważnego. Same, spacje których tu i tam brakuje.

Mam nadzieję, że pomogłem. 
Wszystkie pytania proszę kierować do przeglądarki Google. 

Z fartem
Bartłomiej Żmijewski
"""
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
