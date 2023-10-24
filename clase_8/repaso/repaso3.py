class Vehiculo:
    caballo_fuerza = 2

    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    @property
    def velocidad(self):
        pass

    def acelerar(self):
        pass

    @classmethod
    def caballo_fuerza(cls):
        return cls._caballo_fuerza

    @staticmethod
    def funcion_basica(a, b):
        pass


def validar(tipos_dato):
    def decorador(func):
        def wrapper(*args, **kwargs):
            resultado = None
            es_correcto = any(
                isinstance(args[0], tipo_dato) for tipo_dato in tipos_dato
            )
            if es_correcto:
                resultado = func(*args, **kwargs)
            else:
                print(f"El tipo de dato no es {tipos_dato}.")
            return resultado

        return wrapper

    return decorador


@validar([int, float])
def suma(valor):
    return 10 + valor


@validar([int, float])
def resta(valor):
    return 10 - valor


@validar([int, float])
def division(valor):
    return 10 / valor


@validar([str])
def suma_caracteres(nombre):
    return "Hola " + nombre


print(suma(10.3))
print(suma(10))
print(suma("asdasdas"))
print(resta(10.3))
print(resta(10))
print(resta("asdas"))
print(division(10.3))
print(division(10))
print(suma_caracteres("Juan!"))
print(suma_caracteres(1))


class Foo:
    def __init__(self):
        self.valor1 = None
        self.valor2 = None

    def sum(self):
        if self.valor1 is not None and self.valor2 is not None:
            return self.valor1 + self.valor2
