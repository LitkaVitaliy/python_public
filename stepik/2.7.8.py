# Напишите функцию maxId(L), принимающую на вход список чисел и строк вида:
#
# [1, 2, '42', '3', '4', '5', 6, 13]
# без повторений, и находящую индекс максимального целого числа в списке.

def maxId1(L):
    L = list(map(int, L))
    for i in range(0, len(L)):
        if L[i] == max(L):
            return i


# 2
def maxId2(L):
    L = list(map(int, L))
    return L.index(max(L))
