import math

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
