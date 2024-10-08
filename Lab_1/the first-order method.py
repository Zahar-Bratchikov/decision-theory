import math
import random

tolerance = 10 ** -6
delta = 10 ** -7
a = 0.5
b = 1.0
L = 10
iteration = 0


def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)


def g(x, x0, L):
    return f(x0) - L * abs(x - x0)


points = []
i = a
while i < b:
    points.append(i)
    i += delta
random_index = random.randint(0, len(points) - 1)

x0 = points[random_index]
p_prev = g(x0, x0, L)

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

