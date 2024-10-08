import math

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
