Istotą działania programu jest fakt, że ma on stworzyć pewnego rodzaju ranking plików, które posiadają najwięcej zadeklarowanych przez użytkownika wyrazów przy jednoczesnym zawieraniu jak najmniejszej ilości zbędnych wyrazów. 
Każdy plik zawiera opisy różnych kolekcji, a program ocenia, który plik najlepiej spełnia zadane wymagania. 
Działa to poprzez przypisanie współczynnika dopasowania i liczby zbędnych elementów każdemu plikowi na podstawie porównania z wymaganymi elementami. 

Główny zamysł programu można zaprezentować w kilku krokach:
- Użytkownik podaje listę wymaganych elementów i liczbę plików oraz nazwy plików do porównania,
- Program przetwarza każdy plik, oblicza współczynnik dopasowania i liczbę zbędnych elementów, a wyniki zapisuje w liście “wyniki”,
- Dochodzi następnie do posortowania listy wyników według współczynnika dopasowania, a w przypadku tych samych wartości, według liczby zbędnych elementów,
- Dochodzi do wyświetlenia wyników do wglądu dla użytkownika.


ENG:

The essence of the program's operation lies in the fact that it is designed to create a kind of ranking of files that have the highest number of user-declared words while containing the least amount of unnecessary words. Each file contains descriptions of different collections, and the program evaluates which file best meets the specified requirements. This is done by assigning a matching coefficient and the number of unnecessary elements to each file based on a comparison with the required elements.

The main idea of the program can be presented in several steps:

The user provides a list of required elements, the number of files, and the names of files to compare.
The program processes each file, calculates the matching coefficient and the number of unnecessary elements, and records the results in a "results" list.
The program then sorts the results list based on the matching coefficient, and in case of equal values, based on the number of unnecessary elements.
Finally, the program displays the results for the user to review.

