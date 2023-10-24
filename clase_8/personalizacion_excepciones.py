class OneDivisionError(Exception):
    pass


def division(a, b):
    if b == 1:
        raise OneDivisionError("No se puede dividir por 1.")
    return a / b


while True:
    valor = int(input("Ingresar valor: "))
    try:
        print(division(100, valor))
    except ZeroDivisionError as error:
        print("No se puede dividir por 0.")
    except OneDivisionError as error:
        print(error)
    else:
        pass
    finally:
        pass
