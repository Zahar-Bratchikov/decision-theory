import math
import matplotlib.pyplot as plt
import numpy as np

# точность 10^-6
tolerance = 10 ** -6
delta = 10 ** -7
a = 0.5
b = 1
iteration = 0


def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)


while (abs(b - a)) >= tolerance:
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2
    if (f(x1) >= f(x2)):
        a = x1
    else:
        b = x2
    iteration += 1
x_min = (a + b) / 2
print("Минимальный x: " + str(x_min))
print("Минимальное значение функции : " + str(f(x_min)))
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
