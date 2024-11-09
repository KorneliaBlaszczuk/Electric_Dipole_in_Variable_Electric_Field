import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.integrate import solve_ivp


# p = q*d - lepiej podawać p na sztywno czy liczyć
def symulacja_dipola_animacja(
    E0=1.0, omega=1.0, gamma=0.1, p=0.1, czas_sym=20
):
    """
    E0 - amplituda pola elektrycznego
    omega - częstotliwośc pola
    gamma - współczynnik lepkości
    p - moment dipolowy
    czas_sym - czas symulacji
    """
    d = 0.1  # Odległość między ładunkami dipola
    I = 1.0  # Moment bezwładności dipola

    def pole_elektryczne(t):
        """
        E(t)
        """
        return E0 * np.cos(omega * t)

    # w obecności sił lepkości
    def rownanie_ruchu(t, y, gamma):
        """
        równanie ruchu dipola z uwzględnieniem sił lepkości
        I - moment bezwładności dipola
        theta - kąt między momentem dipolowym a osią pola elektrycznego
        p - moment dipolowy
        gamma - współczynnik lepkości
        E(t) - zmienne pole elektryczne
        """
        theta, omega_theta = y  # Kąt i prędkość kątowa
        E = pole_elektryczne(t)  # Wartość pola elektrycznego w czasie t
        moment_sily = p * E * np.sin(theta)
        dtheta_dt = omega_theta
        domega_dt = (moment_sily - gamma * omega_theta) / I
        return [dtheta_dt, domega_dt]

    # Warunki początkowe: początkowy kąt i prędkość kątowa
    theta0 = 0.5  # Kąt początkowy (radiany)
    omega_theta0 = 0.0  # Prędkość kątowa początkowa
    y0 = [theta0, omega_theta0]

    # Czas symulacji
    t_start = 0
    t_end = czas_sym
    t_eval = np.linspace(t_start, t_end, 1000)

    # Rozwiązywanie równań ruchu
    def solve_simulation(omega_value, gamma_value):
        """Rozwiązywanie równań ruchu"""

        def pole_elektryczne(t):
            """Aktualizacja funkcji pola elektrycznego przy nowym omega"""
            return E0 * np.cos(omega_value * t)

        # Rozwiązywanie równań ruchu
        sol = solve_ivp(
            rownanie_ruchu,
            [t_start, t_end],
            y0,
            args=(gamma_value,),
            t_eval=t_eval,
            method="RK45",
        )
        return sol

    # Inicjalizowanie zmiennej globalnej theta_values
    global theta_values
    sol = solve_simulation(omega, gamma)
    theta_values = sol.y[0]  # Początkowe obliczenia symulacji

    # Wykres
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    plt.subplots_adjust(left=0.1, bottom=0.25)  # Więcej miejsca na suwak

    # ax[0].plot(sol.t, theta_values, label="Kąt θ (rad)")
    ax[0].set_xlabel("Czas (s)")
    ax[0].set_ylabel("Kąt θ (rad)")
    ax[0].set_title("Zmiana kąta θ w czasie")
    ax[0].legend()
    ax[0].grid()

    # Wykres ruchu dipola
    ax[1].set_xlim(-0.2, 0.2)
    ax[1].set_ylim(-0.2, 0.2)
    ax[1].set_aspect("equal", "box")
    ax[1].set_title("Ruch dipola w polu elektrycznym")

    # Animacja dipola
    (line,) = ax[1].plot(
        [], [], "o-", lw=2, color="blue"
    )  # Linia przedstawiająca dipol
    (positive_charge,) = ax[1].plot([], [], "ro")  # Ładunek dodatni
    (negative_charge,) = ax[1].plot([], [], "bo")  # Ładunek ujemny

    def init():
        line.set_data([], [])
        positive_charge.set_data([], [])
        negative_charge.set_data([], [])
        return line, positive_charge, negative_charge

    # Funkcja do aktualizacji animacji
    def animate(i):
        theta = theta_values[i]
        x1, y1 = d * np.cos(theta) / 2, d * np.sin(theta) / 2
        x2, y2 = -d * np.cos(theta) / 2, -d * np.sin(theta) / 2
        line.set_data([x1, x2], [y1, y2])
        positive_charge.set_data([x1], [y1])
        negative_charge.set_data([x2], [y2])
        return line, positive_charge, negative_charge

    # Dodanie suwaka do zmiany częstotliwości
    ax_slider_om = plt.axes(
        [0.25, 0.15, 0.65, 0.015], facecolor="lightgoldenrodyellow"
    )
    slider_omega = Slider(
        ax_slider_om, "Omega", 0.1, 5.0, valinit=omega, valstep=0.1
    )

    # Dodanie suwaka do zmiany współczynnika lepkości
    ax_slider_ga = plt.axes(
        [0.25, 0.05, 0.65, 0.015], facecolor="lightgoldenrodyellow"
    )
    slider_gamma = Slider(
        ax_slider_ga, "Gamma", 0.1, 5.0, valinit=omega, valstep=0.1
    )

    # Funkcja do aktualizacji symulacji przy zmianie częstotliwości
    def update_simulation(val):
        omega = slider_omega.val  # Aktualna wartość częstotliwości z suwaka
        gamma = slider_gamma.val
        global theta_values
        # Rozwiązanie równań ruchu przy nowym omega i gamma
        sol = solve_simulation(omega, gamma)
        theta_values = sol.y[0]
        ax[0].cla()  # Czyszczenie wykresu zmiany kąta
        ax[0].plot(
            sol.t, theta_values, label="Kąt θ (rad)"
        )  # Aktualizacja wykresu zmiany kąta
        ax[0].set_xlabel("Czas (s)")
        ax[0].set_ylabel("Kąt θ (rad)")
        ax[0].set_title("Zmiana kąta θ w czasie")
        ax[0].grid()

        # Zmiana liczby klatek animacji
        ani.event_source.stop()  # Zatrzymanie starej animacji
        ani.frames = len(theta_values)  # Nowa liczba klatek animacji
        ani.event_source.start()  # Uruchomienie nowej animacji

    ani = FuncAnimation(
        fig,
        animate,
        frames=len(theta_values),
        init_func=init,
        interval=20,
        blit=True,
    )

    # Aktualizacja symulacji po przesunięciu suwaka
    slider_omega.on_changed(update_simulation)
    slider_gamma.on_changed(update_simulation)

    # Początkowe obliczenia symulacji
    update_simulation(None)

    plt.show()


if __name__ == "__main__":
    symulacja_dipola_animacja()
