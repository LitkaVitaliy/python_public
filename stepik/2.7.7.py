# Напишите 2 функции:
#
# для нахождения факториала числа factorial(n)
# для нахождения суперфакториала числа
# Используйте функцию факториала для вычисления суперфакториала, чтобы сократить объём кода.

def factorial(n):
    if n == 0:
        return 1

    for i in range(1, n):
        n = n*i
    return n


def sf(n, k=1):
    for i in range(1, n+1):
        k = k*factorial(i)
    return k
