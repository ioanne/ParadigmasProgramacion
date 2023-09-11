tupla = (1, 2, 3, 4)

# Desempaquetando la tupla
n1, n2, n3, n4 = tupla

print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")


def suma(a, b):
    return a, b, a + b


valor1, valor2, suma_valores = suma(2, 5)

print(valor1)
print(valor2)
print(suma_valores)


valor1, valor2, valor3 = 1, 3, 6
