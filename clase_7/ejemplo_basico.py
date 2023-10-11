import random

# Importante:
import sys

sys.setrecursionlimit(1000)

# contador = 0


# def coincidencia(n=None):
#     global contador
#     contador += 1
#     # Aca se obtiene un valor RANDOM del 0 al 20.
#     valor_random = random.randint(0, 20)
#     if valor_random == n:
#         print(
#             f"Coincidencia en la iteracion: {contador}. Con el valor: {valor_random} y valor anterior: {n}"
#         )
#     else:
#         # Si no hay coincidencia volvemos a llamar hasta encontrar coincidencia.
#         coincidencia(n=valor_random)


# coincidencia()


# Este código es el codigo del ejemplo basico.
# def coincidencia(valor_anterior=None):
#     valor_actual = random.randint(0, 10)

#     if valor_anterior == valor_actual:
#         print(f"Coincidencia: {valor_actual}")
#         return valor_actual
#     else:
#         coincidencia(valor_anterior=valor_actual)


# valor_especial = coincidencia()

# print(f"El valor random especial: {valor_especial}")


"""
Recursividad:
Una funcion que se llama a si misma.
Siempre tiene que ir acompañada de una validación
Por defecto se puede llamar hasta 1.000 veces.
No tenemos que llamar a una funcion recursiva desde esa funcion recursiva.
"""


def restar(n):
    # Condición
    if n <= 0:
        return
    else:
        print(n)
        restar(n - 1)


restar(123)


"""
¿Que nos intera saber de las funciones recursivas?
    1.
    Tiene que ser una función que se llame a si misma.

    2.
    Siempre tiene que haber una condición que nos diga cuando debemos frenar.

    3.
    Retornar el valor que estamos buscando/analizando/calculando

    4.
    Cómo maximo puede hacer 1000 ejecuciones recursivas por defecto.
    Como se cambia este valor?
    import sys
    sys.setrecursionlimit(2000)


Las variables se comportan diferente en las funciones recursivas.

"""
