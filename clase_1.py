class Vehiculo:
    # Variable de la clase
    marca = "Ford"

    def __init__(self, color, puertas):
        # Variables de la instancia
        self.color = color
        self.puertas = puertas
        # Variable DENTRO del metodo, solo se puede usar acá.
        hola = "hola"


# Creamos una instancia del vehiculo, instanciando la clase.
auto = Vehiculo("rojo", 5)

print(f"Color: {auto.color}")
print(f"Puertas: {auto.puertas}")
print(f"Marca: {Vehiculo.marca}")

print(type(auto))
