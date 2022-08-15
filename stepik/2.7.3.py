# Напишите функцию, для нахождения двойного факториала числа dfactorial(n).
#
# Двойной факториал числа n обозначается n‼ и определяется как произведение всех натуральных чисел в отрезке [1,n],
# имеющих ту же чётность, что и n.
#
# Для чётного n:     n!!=2⋅4⋅6⋅…⋅nn!!=2⋅4⋅6⋅…⋅n
# Для нечётного n: n!!=1⋅3⋅5⋅…⋅nn!!=1⋅3⋅5⋅…⋅n

def dfactorial(n):
    d_factorial = 1
    if n % 2 == 0:
        for i in range(1, (int(n/2)+1)):
            d_factorial = d_factorial*2*i

    else:
        for i in range(0, (int((n-1)/2)+1)):
            d_factorial = d_factorial*(2*i+1)

    return d_factorial
