import math
import random

# Параметры
tolerance = 10 ** -6
delta = 10 ** -7
a = 0.5  # Начало интервала
b = 1.0  # Конец интервала
L = 10  # Константа Липшица (ее можно подбирать для задачи)
iteration = 0


# Функция f(x), которую минимизируем
def f(x):
    return x ** 2 - 2 * x - 2 * math.cos(x)


# Функция g(x, x0)
def g(x, x0, L):
    return f(x0) - L * abs(x - x0)

points = []
i = a
while i < b:
    points.append(i)
    i += delta
random_index = random.randint(0, len(points)-1)


# Метод ломанных
x0 = points[random_index]  # Выбираем произвольную точку x0
p_prev = g(x0, x0, L)  # Начальная аппроксимация

# Инициализируем x_new и p_new до входа в цикл
x_new = (a + b) / 2
p_new = g(x_new, x0, L)

while (abs(f(x_new) - p_prev) > tolerance) and (abs(p_new - p_prev) > tolerance):
    x1 = (a + b - delta) / 2
    x2 = (a + b + delta) / 2

    # Определение следующей точки
    if g(x1, x0, L) >= g(x2, x0, L):
        a = x1
    else:
        b = x2

    # Новая точка и аппроксимация
    x_new = (a + b) / 2
    p_new = g(x_new, x0, L)

    # Обновляем значение аппроксимации для следующей итерации
    p_prev = p_new
    iteration += 1

# Определяем найденный минимум
x_min = (a + b) / 2

# Вывод результатов
print("Минимальный x: " + str(x_min))
print("Минимальное значение функции : " + str(f(x_min)))
print("Итерации: " + str(iteration))
