# with open("archivo.txt", "a+") as archivo:
#     archivo.seek(0)
#     a = archivo.readline()
#     print(a)


# Acceder a un archivo
# Solo lectura "r"
# Solo escritura es "w", pero borra el contenido
# Escribir al final sin borrar es "a"
# Escribir y leer es "a+" nos para al final del archivo, por lo que para leer hay que volver al comienzo.
# Leer y escribir es "r+"


with open("archivo.txt", "r+") as archivo:
    archivo.write("1")
    a = archivo.readline()
    print(a)
    archivo.seek(0)
    a = archivo.readline()
    print(a)

# El archivo esta cerrado
try:
    archivo.write("asd")
except ValueError as err:
    print(f"El archivo esta cerrado. {err}")


archivo = open("archivo.txt", "r+")
archivo.write("1")
a = archivo.readline()
print(a)
archivo.seek(0)
a = archivo.readline()
print(a)
archivo.close()
try:
    archivo.write("asd")
except ValueError as err:
    print(f"El archivo esta cerrado. {err}")
