# fo_project_24Z

# ENG
## Team Members

- Kornelia Błaszczuk
- Kinga Łukiewicz

## Topic

**Electric Dipoles in a Variable Electric Field – Dipoles in the Presence of Viscous Forces**

## Assumptions and Project Goal

The goal of this project is to illustrate the motion of an electric dipole in a variable electric field, depending on parameters such as the field frequency and viscosity coefficient. The user will be able to adjust these parameters using sliders, allowing them to observe how they affect the dipole's motion.

The core element of the simulation is the visualization of the dipole's angle change over time and an animation of its movement in a variable electric field. The simulation will also include a graph displaying the dependence of the angle on time, enabling better observation.

### At What Frequency and Viscosity Does the Dipole Stop Rotating?

A dipole stops rotating when its motion is fully damped by the viscous force. Increasing the field frequency or the viscosity results in a stronger resistive torque (viscous force) than the torque induced by the electric field, causing the dipole to stop rotating. In our implementation, for a frequency and viscosity of 5, the angle change is less than 0.003, meaning that, to the human eye, the dipole appears to stop rotating.

## Technology

The project is implemented in Python using the following libraries:

- **matplotlib**: for creating plots and animations
- **scipy**: for solving the equations of motion
- **numpy**: for auxiliary calculations

## How to Run the Program

To run the program, set up a Python environment and install the required libraries listed above.
After running the program, a window will appear with plots and an animation. The user can adjust the field frequency and viscosity coefficient using interactive sliders located below the plots. The simulation will automatically update the graphs and animation, illustrating how the changes in parameters affect the dipole's motion.

### Observing the Results

The first plot will show the change in the dipole's angle over time, while the second plot will display an animation of the dipole's movement in the variable electric field.
The user can observe how changes in parameters influence the dipole's motion and its angular displacement.


# PL
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
