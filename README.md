# fo_project_24Z

## Skład zespołu

- Kornelia Błaszczuk (331361)
- Kinga Łukiewicz (331399)

## Temat

Dipole elektryczne w zmiennym polu elektrycznym - dipole w obecności sił lepkości.

## Założenia i cel projektu

Ukazanie ruchu dipolu w zmiennym polu elektrycznym w zależności od parametrów takich jak częstotliwość pola elektrycznego i współczynnik lepkości. Użytkownik będzie miał możliwość zmiany tych parametrów za pomocą suwaków, co umożliwi zobaczenie jak wpływają one na ruch dipola.
Podstawowym elementem symulacji jest wizualizacja zmiany kąta dipola w czasie oraz animacja jego ruchu w zmiennym polu elektrycznym. Symulacja będzie także obejmować wykres zależności kąta od czasu, umożliwiając lepszą obserwację.

#### Przy jakiej częstotliwości pola / lepkości przestaną się obracać?
Dipol przestaje się obracać, gdy jego ruch jest w pełni tłumiony przez siłę lepkości. Wzrost częstotliwości pola lub zwiększenie lepkości powoduje, że moment oporu (lepkości) staje się silniejszy niż moment obrotowy wywoływany przez pole elektryczne, co skutkuje zatrzymaniem się dipola. Dla naszej implementacji dla częstotliwości i lepkości równych 5 zmiana kąta jest mniejsza niż 0.003, czyli dla ludzkiego oka dipol przestaje się obracać.

## Technologia

Projekt jest realizowany w języku Python z wykorzystaniem bibliotek:

- matplotlib: do tworzenia wykresu oraz animacji
- scipy: do liczenia równania ruchu
- numpy: do obliczeń pomocniczych

## Sposób uruchomienia programu

Aby uruchomić program należy przygotować środowisko w Pythonie oraz pobrać powyżej wypisane biblioteki. 
Po uruchomieniu programu pojawi się okno z wykresami i animacją. Użytkownik może zmieniać wartość częstotliwości oraz współczynnika lepkości za pomocą interaktywnych suwaków znajdujących się pod wykresami. Symulacja automatycznie zaktualizuje wykresy oraz animację, ilustrując wpływ zmienianych parametrów na ruch dipola.

#### Obserwacja wyników
Na pierwszym wykresie będzie widoczna zmiana kąta w czasie, a na drugim wykresie będzie animacja przedstawiająca ruch dipola w zmiennym polu elektrycznym.
Użytkownik może obserwować, jak zmiany parametrów wpływają na ruch dipola i jego kąt wychylenia.

