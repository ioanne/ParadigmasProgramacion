numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lambda x: x + 2

list(map(lambda x: x + 2, numeros))


def el_cuadrado(x):
    return x**2


numeros = [1, 2, 3, 4, 5, 6]
list(map(el_cuadrado, numeros))


# El map ejecuta una funcion tantas veces como valores en una lista.
# Es decir pasa cada valor por la funcion y va devolviendo los resultados

numeros = [
    el_cuadrado(1),
    el_cuadrado(2),
    el_cuadrado(3),
    el_cuadrado(4),
    el_cuadrado(5),
    el_cuadrado(6),
]
