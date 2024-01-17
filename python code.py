def oblicz_wspolczynnik_dopasowania(wymagane_elementy, kolekcja):
    dopasowanie = sum(element in kolekcja for element in wymagane_elementy)
    return dopasowanie

def licz_zbedne_elementy(wymagane_elementy, kolekcja):
    zbedne_elementy = [element for element in kolekcja if element not in wymagane_elementy]
    return len(zbedne_elementy)

def glowna():
    wymagane_elementy = input("Podaj wymagane elementy oddzielone spacją: ").split()

    try:
        liczba_plikow = int(input("Podaj liczbę plików do porównania: "))
    except ValueError:
        print("Nieprawidłowa liczba plików.")
        return

    nazwy_plikow = []

    for i in range(liczba_plikow):
        nazwa_pliku = input(f"Podaj nazwę pliku {i + 1} z opisami kolekcji: ")
        if not nazwa_pliku.endswith(".txt"):
            nazwa_pliku += ".txt"
        nazwy_plikow.append(nazwa_pliku)

    wyniki = []

    for nazwa_pliku in nazwy_plikow:
        try:
            with open(nazwa_pliku, 'r') as plik:
                opisy_kolekcji = [line.strip() for line in plik]

            dopasowanie = oblicz_wspolczynnik_dopasowania(wymagane_elementy, opisy_kolekcji)
            zbedne_elementy = licz_zbedne_elementy(wymagane_elementy, opisy_kolekcji)
            wyniki.append((nazwa_pliku, dopasowanie, zbedne_elementy))

        except FileNotFoundError:
            print(f"Plik '{nazwa_pliku}' nie istnieje.")
        except Exception as e:
            print(f"Wystąpił błąd podczas przetwarzania pliku '{nazwa_pliku}': {e}")

    posortowane_wyniki = sorted(wyniki, key=lambda x: (x[1], -x[2]), reverse=True)

    if any(wynik[1] > 0 for wynik in posortowane_wyniki):
        print("\nNajlepsze dopasowanie plików do zadeklarowanych wymagań w postaci wyrazów:")
        for nazwa_pliku, dopasowanie, zbedne_elementy in posortowane_wyniki:
            print(f"{nazwa_pliku}:\nDopasowanie elementów: {dopasowanie}\nLiczba zbędnych elementów: {zbedne_elementy}\n")
    else:
        print("Brak dopasowań.")

if __name__ == "__main__":
    glowna()

