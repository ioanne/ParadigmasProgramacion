with open(file="archivo.txt", mode="a+") as file:
    # file.write("Hola mundo!\n")
    file.seek(0)
    print(file.read())
    # Go to end
    file.seek(0, 2)
    file.write("Hola mundo!\n")
