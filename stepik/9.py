print(dir((1, 2, 3)))
print(dir("Uno"))

a = 3
b = 5

print(a.__sub__(b))
print(a.__mul__(b))
print(a.__truediv__(b))
print(a.__eq__(b))
print(a.__pow__(b))
print(a.__floordiv__(b))
print(a.__lt__(b))


class Animal:
    def echo(self, strin):
        print(strin.upper())
        print(strin)
        print(strin.lower())


c = Animal()
c.ae = 5
print(c.ae)
