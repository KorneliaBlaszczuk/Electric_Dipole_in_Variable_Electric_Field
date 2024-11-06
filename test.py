import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp


def symulacja_dipola_animacja(E0=1.0, omega=1.0, gamma=0.1, p=0.1, czas_sim=20):
    d = 0.1  # Odległość między ładunkami dipola
    I = 1.0  # Moment bezwładności dipola

    def pole_elektryczne(t):
        return E0 * np.cos(omega * t)

    # w obecności sił lepkości
    def rownanie_ruchu(t, y):
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
    t_end = czas_sim
    t_eval = np.linspace(t_start, t_end, 1000)

    # Rozwiązywanie równań ruchu
    sol = solve_ivp(rownanie_ruchu, [t_start, t_end], y0, t_eval=t_eval, method="RK45")
    theta_values = sol.y[0]  # Kąt θ w funkcji czasu

    # Wykres
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].plot(sol.t, theta_values, label="Kąt θ (rad)")
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


    ani = FuncAnimation(
        fig, animate, frames=len(theta_values), init_func=init, interval=20, blit=True
    )

    plt.show()


if __name__ == '__main__':
    symulacja_dipola_animacja()
