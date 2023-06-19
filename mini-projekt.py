import random

def losowanie_liczb():
    try:
        nick = input("Podaj swój nick: ")
        ilosc_losowan = int(input("Podaj ilość losowań: "))
        maks_zakres = int(input("Podaj maksymalny zakres losowania: "))
        liczby_typowane = []
        trafione_liczby = []

        for _ in range(ilosc_losowan):
            liczba_typowana = int(input("Podaj typowaną liczbę: "))
            if liczba_typowana < 1 or liczba_typowana > maks_zakres:
                raise ValueError("Podana liczba jest spoza zakresu losowania.")
            liczby_typowane.append(liczba_typowana)

        for _ in range(ilosc_losowan):
            liczba_wylosowana = random.randint(1, maks_zakres)
            if liczba_wylosowana in liczby_typowane:
                trafione_liczby.append(liczba_wylosowana)

        print("Ilość trafień:", len(trafione_liczby))
        print("Trafione liczby:", trafione_liczby)

        zapisz_parametry(nick, ilosc_losowan, maks_zakres, liczby_typowane, trafione_liczby)

    except ValueError as e:
        print("Błąd:", e)

def zapisz_parametry(nick, ilosc_losowan, maks_zakres, liczby_typowane, trafione_liczby):
    try:
        nazwa_pliku = nick + ".txt"
        with open(nazwa_pliku, 'w') as plik:
            plik.write("Nick: " + nick + "\n")
            plik.write("Ilość losowań: " + str(ilosc_losowan) + "\n")
            plik.write("Maksymalny zakres losowania: " + str(maks_zakres) + "\n")
            plik.write("Typowane liczby: " + str(liczby_typowane) + "\n")
            plik.write("Trafione liczby: " + str(trafione_liczby) + "\n")
        print("Parametry gry zostały zapisane do pliku", nazwa_pliku)
    except Exception as e:
        print("Błąd podczas zapisu do pliku:", e)

losowanie_liczb()
