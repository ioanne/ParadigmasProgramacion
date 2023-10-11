# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


def fibonacci(n):
    """Usar esta funcion desde dentro de la funcion tantas veces sea necesario."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 10):
    print(fibonacci(i))


def factorial(n):
    if n == 0:  # Validaciones, para cuando TERMINA la recursividad
        return 1
    else:
        return n * factorial(n - 1)


resultado = factorial(3)
print(resultado)
