import math
import random
import matplotlib.pyplot as plt
import numpy as np

# точность и параметры
tolerance = 10 ** -6
delta = 10 ** -7
a = 0.5
b = 1.0
iteration = 0


def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)


def derivative_f(x):
    return 2 * x - 2 + 2 * math.sin(x)


points_der = []
i = a
while i < b:
    points_der.append(derivative_f(i))
    i += delta
L = max(points_der)


def g(x, x0, L):
    return f(x0) - L * abs(x - x0)


# Генерация случайной точки
points = []
i = a
while i < b:
    points.append(i)
    i += delta

random_index = random.randint(0, len(points) - 1)
x0 = (a + b) / 2 +0.1
p_prev = g(x0, x0, L)

# Поиск минимума
x_new = (a + b) / 2
p_new = g(x_new, x0, L)

while (abs(f(x_new) - p_prev) > tolerance) and (abs(p_new - p_prev) > tolerance):
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    if g(x1, x0, L) >= g(x2, x0, L):
        a = x1
    else:
        b = x2

    x_new = (a + b) / 2
    p_new = g(x_new, x0, L)

    p_prev = p_new
    iteration += 1

x_min = (a + b) / 2

print("Минимальный x: " + str(x_min))
print("Минимальное значение функции : " + str(f(x_min)))
print("Итерации: " + str(iteration))

# Построение графиков
x_vals = np.linspace(0.5, 1, 400)
y_vals_f = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals_f, label="f(x)", color="blue")
plt.scatter(x_min, f(x_min), color="red", label=f"Минимум f(x) (x={x_min:.6f})")

plt.title("Графики функций f(x)")
plt.xlabel("x")
plt.ylabel("Значение функции")
plt.legend()
plt.grid(True)
plt.show()
