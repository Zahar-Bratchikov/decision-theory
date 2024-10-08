import math
import numpy as np
import matplotlib.pyplot as plt

# точность 10^-6
tolerance = 10 ** -6
delta = 10 ** -7
a = 0.5
b = 1
iteration = 0


def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)


def derivative_f(x):
    return 2 * x - 2 + 2 * math.sin(x)


def second_derivative_f(x):
    return 2 + 2 * math.cos(x)


x_k = a
x_k_n = x_k - (derivative_f(x_k) / second_derivative_f(x_k))
while ((abs(x_k_n - x_k) < tolerance) and (abs(f(x_k_n) - f(x_k)) < tolerance)):
    x_k = x_k_n
    x_k_n = x_k - (derivative_f(x_k) / second_derivative_f(x_k))
    iteration += 1
print("Минимальный x: " + str(x_k_n))
print("Минимальное значение функции: " + str(f(x_k_n)))
print("Итерации: " + str(iteration))

# Построение графика функции
x_vals = np.linspace(0.5, 1, 400)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(x_min, f(x_min), color="red", label=f"Минимум (x={x_min:.6f}, f(x)={f(x_min):.6f})")
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
