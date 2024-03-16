import numpy as np
import scipy.integrate as integrate


# визначимо функцію
def f(x):
    return x**3 + x**2


# метод Монте-Карло
def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


if __name__ == "__main__":
    # визначемо межі інтегрування
    a = -1
    b = 1
    y_min = 0
    y_max = 4
    # створимо діапазон значень для х
    x = np.linspace(-1, 1, 100)
    y = f(x)
    # отримаємо значення інтегралу за домогою функції quad
    result, err = integrate.quad(f, a, b)
    # отримаємо значення інтегралу методом Монте-Карло
    mc_result = monte_carlo_integrate(f, a, b, y_min, y_max, 1_000_000)
    # порахуємо різницю між цими двома результатми
    difference = result - mc_result
    print(f"Результат функції quad {result} і її похибка {err}")
    print(f"Результат алгоритму Монте-Карло {mc_result}")
    print(f"Різниця між цими результатами = {difference}")
