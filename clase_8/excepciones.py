# Código sin excepcion
def division_1(a, b):
    resultado = 0
    if b != 0:
        resultado = a / b
    return resultado


print(division_1(0, 5))
print(division_1(5, 0))


def division(dato):
    return dato["a"] / dato["b"]


# print(division(0, 5))
dato = {"a": 5, "c": 9}
try:
    print(division(dato))
except ValueError as error:
    pass
except AttributeError as error:
    pass
except KeyError as error:
    print("La clave no existe")
except ZeroDivisionError as error:
    print("No se puede dividir por 0.")
except Exception as error:
    print("Ocurrio un error desconocido")
else:
    print("Else del try")
finally:
    print("Finalizo la ejecución")
