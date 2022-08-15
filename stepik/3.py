# 1. Реализуйте функцию f(x):
# f(x) = 2arctg(x)
# Найдите предел функции (ответ округлите до 3 знака после запятой) при x→+∞
import math
from math import atan
from math import exp


def f(x):
    return 2*atan(x)


lim = f(math.inf)
# print(round(lim, 3))


# 2. Проверьте (для нескольких разных точек), что производная от e^{x} совпадает с исходной функцией, т.е. {(e^{x})}' =
# e^{x}
#
# Для этого реализуйте функцию def_e(x), находящую численное значение производной (с точностью до 3 знака) в точке x.
def def_e(x):
    return exp(x)


x0 = 3
dx = 0.00001
dydx = round((def_e(x0+dx)-def_e(x0))/dx, 3)
# print(dydx)


# 3. Напишите функцию even_indeces(L), которая будет возвращать только элементы с чётными индексами.
# Примечание. Пример вывода дан для L = [1, 1, 2, 3, 5, 8, 13, 21, 34]
def even_indeces(L):
    L2 = []
    for i in range(0, len(L)):
        if i % 2 == 0:
            L2.append(L[i])
    return L2


# Напишите функцию even_elements(l), которая возвращает только чётные элементы списка.
def even_elements(l):
    l2 = []
    for i in range(0, len(l)):
        if int(l[i]) % 2 == 0:
            l2.append(l[i])
    return l2



