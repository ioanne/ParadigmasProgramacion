class A:
    def __init__(self, j):
        self.j = j

    def z(self):
        return "ZzZzZ"

    def y(self):
        return "YyYy"


class F:
    def t(self):
        return "hola mundo!"


class B(A, F):
    pass


a = A(j=8)
b = B(j=10)

print(a.j)
print(a.z())
print(a.y())
print(b.j)
print(b.t())
print(b.z())
print(b.y())
