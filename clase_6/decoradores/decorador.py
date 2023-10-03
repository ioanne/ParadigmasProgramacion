# @algo
# @property
# @classmethod
# @staticmethod


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # Esto es un decorador
    def edad(self):
        pass


# Wrapper = envoltorio


def nombre_funcion(la_funcion_a_decorar):
    def wrapper(*args, **kwargs):
        # Código que se ejecuta antes
        resultado = la_funcion_a_decorar(*args, **kwargs)
        # Código que se ejecuta después
        return resultado

    return wrapper  # se devuelve el wrapper SIN ejecutar


def take_time(func):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()

        # Esta es nuestra función
        resultado = func(*args, **kwargs)

        end = time.time()
        print(f"Tiempo de ejecución: {end - start}")
        return resultado

    return wrapper


@take_time
def foo(uno, dos):
    suma = 0
    for i in range(uno, dos):
        suma = uno + dos
    return suma


print(foo(1, 5000))


def algo(algo2):
    print(algo2(1, 2))


# Decorador con argumentos
def validate(tipo_dato):
    def _validate(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], tipo_dato):
                raise TypeError("El primer argumento debe ser un entero")
            if not isinstance(args[1], tipo_dato):
                raise TypeError("El segundo argumento debe ser un entero")
            resultado = func(*args, **kwargs)
            # Código que se ejecuta después
            return resultado

        return wrapper  # se devuelve el wrapper SIN ejecutar

    return _validate


@validate(int)
def suma(x, y):
    return x + y


class ClaseEjemplo:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        suma = self.suma
        self.suma = self.resta
        self.resta = suma

    def suma(self):
        return self.n1 + self.n2

    def resta(self):
        return self.n1 - self.n2
