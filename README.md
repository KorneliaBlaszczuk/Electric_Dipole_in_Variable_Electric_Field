# fo_project_24Z
## ENG

## Team Members
- Kornelia Błaszczuk
- Kinga Łukiewicz

## Topic
Electric Dipoles in a Varying Electric Field - Dipoles in the Presence of Viscous Forces.

## Assumptions and Project Goal
The goal of the project is to demonstrate the motion of a dipole in a varying electric field depending on parameters such as the frequency of the electric field and the viscosity coefficient. The user will be able to change these parameters using sliders, allowing them to observe how they affect the motion of the dipole. The primary element of the simulation is the visualization of the dipole’s angle change over time, as well as the animation of its motion in a varying electric field. The simulation will also include a graph showing the relationship between the angle and time, allowing for better observation.

### At what frequency of the field / viscosity will the dipole stop rotating?
The dipole stops rotating when its motion is fully damped by the viscous force. Increasing the frequency of the field or increasing the viscosity makes the resistance (viscous) torque stronger than the torque induced by the electric field, which results in the dipole stopping. In our implementation, for frequencies and viscosities equal to 5, the angle change is smaller than 0.003, meaning the dipole will stop rotating for the human eye.

## Technology
The project is implemented in Python using the following libraries:

- **matplotlib**: for creating graphs and animations
- **scipy**: for solving the motion equation
- **numpy**: for auxiliary calculations

## How to Run the Program
To run the program, you need to set up the Python environment and install the libraries listed above. After launching the program, a window will appear with graphs and an animation. The user can change the frequency and viscosity values using interactive sliders located below the graphs. The simulation will automatically update the graphs and animation, illustrating the effect of the modified parameters on the dipole's motion.

## Observing Results
The first graph will show the change of the dipole's angle over time, and the second graph will display an animation of the dipole's motion in the varying electric field. The user can observe how changes in the parameters affect the dipole's movement and its angle of deflection.


## PL
## Skład zespołu

- Kornelia Błaszczuk 
- Kinga Łukiewicz 

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

