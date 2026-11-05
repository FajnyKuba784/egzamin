import random

class TablicaLiczba:
    """Klasa realizująca operacja na tablicy liczb całkowitych."""
    def __init__(self,rozmiar:int):
        # *****************
        # nazwa: __init__
        # opis: Konstruktor klasy, inicjalizuje rozmiar tablicy i wypełnią ją losowymi liczbami od 1 do 1000
        # parametry: rozmiar - liczba całkowita
        # zwraca: brak
        # autor: 12345678910
        # *****************
        if rozmiar <=20:
            rozmiar = 25
        self.__liczba_elementow = rozmiar
        self.__tablica = [random.randint(1,1000) for _ in range(rozmiar)]
    def wyswietl_elementy(self) -> None :
        for i in range(self.__liczba_elementow):
            print(f"{i}: {self.__tablica[i]}")
    def wyszukaj(self,szukana_wartosc: int) -> int:
        for i in range(self.__liczba_elementow):
            if self.__tablica[i] == szukana_wartosc:
                return i
        return -1
    def wyswietl_nieparzyste(self) -> int:
        licznik = 0
        print("Liczby nieparzyste w tablicy")
        for liczba in self.__tablica:
            if liczba % 2 != 0:
                print(liczba, end=" ")
                licznik += 1
        print()
        return licznik
    def oblicz_srednia(self) -> float:
        if self.__liczba_elementow == 0:
            return 0.0
        return sum(self.__tablica)/ self.__liczba_elementow
if __name__ == "__main__":
    
    moja_tablica = TablicaLiczba(25)
    
    print("--- 1. Wyświetlanie wszystkich elementów tablicy ---")
    moja_tablica.wyswietl_elementy()

    print("\n--- 2. Wyszukiwanie wartości ---")
    szukana = 500
    indeks = moja_tablica.wyszukaj(szukana)
    if indeks != -1:
        print(f"Znaleziono wartość {szukana} pod indeksem: {indeks}")

    print("\n--- 3. Wyświetlanie liczb nieparzystych ---")
    ile_nieparzystych = moja_tablica.wyswietl_nieparzyste()
    print(f"Liczba elementów nieparzystych: {ile_nieparzystych}")

    print("\n--- 4. Średnia arytmetyczna ---")
    srednia = moja_tablica.oblicz_srednia()
    print(f"Średnia arytmetyczna elementów w tablicy wynosi: {srednia:.2f}")
    
