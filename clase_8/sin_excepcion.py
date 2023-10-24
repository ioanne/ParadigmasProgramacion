while True:
    valor = int(input("Ingresar valor: "))
    if valor == 0:
        print("No se puede dividir por 0. Cerrando programa")
        break
    elif valor == 1:
        print("No se puede dividir por 1.")
        continue
    print(100 / valor)
