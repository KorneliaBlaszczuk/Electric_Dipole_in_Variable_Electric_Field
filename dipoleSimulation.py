import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp


class DipoleSimulation:
    def __init__(self, E0=1.0, omega=1.0, gamma=0.1, p=0.1, sim_time=20):
        """
        Inicjalizacja parametrów symulacji dipola.
        
        :param E0: Amplituda pola elektrycznego, maksymalna wartość, 
            jaką może osiągnąć pole elektryczne w danym czasie 
            (jednostka: V/m, czyli wolt na metr).
        :param omega: Częstotliwość pola (jednostka: rad/s, 
            czyli radian na sekundę)
        :param gamma: Współczynnik lepkości (jednostka: kg·m²/s, 
            odpowiadająca tłumieniu ruchu obrotowego).
        :param p: Moment dipolowy, wyrażony wzorem p=q*d 
            (jednostka: C·m, czyli kulomb razy metr).
        :param czas_sym: Czas symulacji (jednostka: s, czyli sekunda).
        """
        self.E0 = E0
        self.omega = omega
        self.gamma = gamma
        self.p = p
        self.sim_time = sim_time

        # Inne stałe parametry
        self.d = 0.1  # Odległość między ładunkami dipola (jednostka: m, czyli metr)
        self.I = 1.0  # Moment bezwładności dipola (jednostka: kg·m²)

        self.theta_values = None  # Przechowuje wartości kąta theta z symulacji
        self.y0 = [0.5, 0.0]  # Kąt początkowy (rad) i początkowa prędkość kątowa (rad/s)

        # Przygotowanie rysunku i suwaków
        self.fig, self.ax = plt.subplots(1, 2, figsize=(12, 6))
        self.setup_plot()
        self.create_sliders()

    def electric_field(self, t):
        """
        Oblicza wartość pola elektrycznego w chwili t.

        :param t: Czas (jednostka: s, czyli sekunda).
        """
        return self.E0 * np.cos(self.omega * t)
    
    def equation_of_motion(self, t, y):
        """
        Równanie ruchu dipola z uwzględnieniem sił lepkości.

        :param t:  Czas (jednostka: s, czyli sekunda).
        :param y: Tablica kąta (rad) i prędkości kątowej (rad/s).
        """
        theta, omega_theta = y  # Kąt i prędkość kątowa
        E = self.electric_field(t)  # Wartość pola elektrycznego w czasie t
        torque = self.p * E * np.sin(theta)  # Moment siły
        dtheta_dt = omega_theta
        domega_dt = (torque - self.gamma * omega_theta) / self.I
        return [dtheta_dt, domega_dt]
    
    def solve_simulation(self):
        """
        Rozwiązywanie równań ruchu dla obecnych wartości omega i gamma.
        """
        t_eval = np.linspace(0, self.sim_time, 1000)
        solution = solve_ivp(
            self.equation_of_motion,
            [0, self.sim_time],
            self.y0,
            t_eval=t_eval,
            method="RK45"
        )
        self.theta_values = solution.y[0]
        return solution
    

    def setup_plot(self):
        """
        Ustawienie wykresów i inicjalizacja animacji.
        """
        plt.subplots_adjust(left=0.1, bottom=0.25)  # Dodanie miejsca na suwaki

        # Wykres kąta theta w czasie
        self.ax[0].set_xlabel("Czas (s)")
        self.ax[0].set_ylabel("Kąt θ (rad)")
        self.ax[0].set_title("Zmiana kąta θ w czasie")
        self.ax[0].legend()
        self.ax[0].grid()

        # Animacja ruchu dipola
        self.ax[1].set_xlim(-0.2, 0.2)
        self.ax[1].set_ylim(-0.2, 0.2)
        self.ax[1].set_aspect("equal", "box")
        self.ax[1].set_title("Animacja ruchu dipola w polu elektrycznym")

        # Elementy animacji dipola
        self.line, = self.ax[1].plot([], [], "o-", lw=2, color="black") 
        self.positive_charge, = self.ax[1].plot([], [], "ro")  # Ładunek dodatni
        self.negative_charge, = self.ax[1].plot([], [], "bo")  # Ładunek ujemny

        self.animation = FuncAnimation(
            self.fig,
            self.animate,
            frames=1000,
            init_func=self.init_animation,
            interval=20,
            blit=True,
        )

    def init_animation(self):
        """
        Inicjalizacja animacji.
        """
        self.line.set_data([], [])
        self.positive_charge.set_data([], [])
        self.negative_charge.set_data([], [])
        return self.line, self.positive_charge, self.negative_charge

    def animate(self, i):
        """
        Aktualizacja animacji dla klatki i.
        """
        theta = self.theta_values[i]
        x1, y1 = self.d * np.cos(theta) / 2, self.d * np.sin(theta) / 2
        x2, y2 = -self.d * np.cos(theta) / 2, -self.d * np.sin(theta) / 2
        self.line.set_data([x1, x2], [y1, y2])
        self.positive_charge.set_data([x1], [y1])
        self.negative_charge.set_data([x2], [y2])
        return self.line, self.positive_charge, self.negative_charge

    def create_sliders(self):
        """
        Tworzy suwaki do dynamicznej zmiany omega i gamma.
        """
        # Suwak do zmiany częstotliwości omega
        ax_slider_om = plt.axes([0.25, 0.15, 0.65, 0.015], facecolor="lightgoldenrodyellow")
        self.slider_omega = Slider(ax_slider_om, "Częstotliwość pola", 0.1, 5.0, valinit=self.omega, valstep=0.1)

        # Suwak do zmiany współczynnika lepkości gamma
        ax_slider_ga = plt.axes([0.25, 0.05, 0.65, 0.015], facecolor="lightgoldenrodyellow")
        self.slider_gamma = Slider(ax_slider_ga, "Współczynnik lepkości", 0.1, 5.0, valinit=self.gamma, valstep=0.1)

        # Powiązanie suwaków z funkcją aktualizacji
        self.slider_omega.on_changed(self.update_simulation)
        self.slider_gamma.on_changed(self.update_simulation)

    def update_simulation(self, val):
        """
        Aktualizuje symulację przy zmianie wartości omega lub gamma.

         :param val: Nowa wartość ustawiona na suwaku (częstotliwość 
            omega lub współczynnik lepkości gamma).
        """
        self.omega = self.slider_omega.val
        self.gamma = self.slider_gamma.val
        sol = self.solve_simulation()
        self.theta_values = sol.y[0]

        # Aktualizacja wykresu zmiany kąta theta
        self.ax[0].cla()
        self.ax[0].plot(sol.t, self.theta_values, label="Kąt θ (rad)")
        self.ax[0].set_xlabel("Czas (s)")
        self.ax[0].set_ylabel("Kąt θ (rad)")
        self.ax[0].set_title("Zmiana kąta θ w czasie")
        self.ax[0].grid()

        # Zmiana liczby klatek animacji
        self.animation.event_source.stop()
        self.animation.frames = len(self.theta_values)
        self.animation.event_source.start()

    def run(self):
        """
        Uruchamia symulację.
        """
        self.solve_simulation()
        self.update_simulation(None)
        plt.show()


if __name__ == "__main__":
    symulacja = DipoleSimulation()
    symulacja.run()