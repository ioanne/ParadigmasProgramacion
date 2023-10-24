class OneDivisionError(Exception):
    pass


class MyInt(int):
    def __truediv__(self, __value: int) -> float:
        if __value == 1:
            raise OneDivisionError("No se puede dividir por 1.")
        return super().__truediv__(__value)


a = MyInt(10)
b = MyInt(1)


def division(a, b):
    return a / b


division(a, b)
