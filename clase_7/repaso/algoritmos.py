# Declaración de variables
# Las variables siempre empiezan con letras o _
nombre = 1

for i in range(0, 5):
    print(i)


lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

# Para recorrer un diccionario y obtener clave y valor se debe acceder desde el metodo items
diccionario = {1: "hola", 2: "chau"}
for k, v in diccionario.items():
    print(f"key: {k} value: {v}")

# Para recorrer un diccionario y obtener su clave se debe acceder desde el metodo keys que devuelve una lista de claves.
diccionario = {1: "hola", 2: "chau"}
for k in diccionario.keys():
    print(k)


# Para recorrer un diccionario y obtener su clave se debe acceder desde el metodo values que devuelve una lista de valores.
diccionario = {1: "hola", 2: "chau"}
for v in diccionario.values():
    print(v)

# Recorrer lista de diccionario
lista_diccionario = [{"1": 1}, {"2": 3}]
for i in lista_diccionario:
    print(i)


# Para recorrer un string
string = "Hola mundo"
for letra in string:
    print(letra)


# Para recorrer una tupla
tupla = (1, 2, 3, 4, 5)
for valor in tupla:
    if valor == 2:
        break
    print(valor)
else:
    print("Esto se ejecuta unicamente si se recorre TODOS los elementos")


tupla = (1, 2, 3, 4, 5)
for valor in tupla:
    if valor == 2:
        continue
    print(valor)
else:
    print("Esto se ejecuta unicamente si se recorre TODOS los elementos")


# El metodo para chequear como evalua es bool
print(bool(10))


if not valor:
    print("Evalua true")


def validar(valor=None):
    """Mostrar el valor cuando NO sea None"""
    if valor != None:
        print("El valor no es None")


def validar2(valor=None):
    """Ojo con esta validacion de None"""
    if valor:
        print("El valor no es None")


def validar3(valor=None):
    if valor == True:
        print("El valor no es None")


def validar_none(valor=None):
    """Mejor validación de None"""
    if valor is not None:
        print("El valor no es None")
