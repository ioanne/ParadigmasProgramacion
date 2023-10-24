class Vehiculo:
    def __init__(self, color, marca):
        self.color = color  # Atributos
        self.marca = marca  # Atributos
        self.aceleracion = 0
        self.freno_mano = False

    def acelerar(self, intensidad):
        """Metodo de la clase Vehiculo"""
        self.aceleracion = self.aceleracion + intensidad * 5
        return self.aceleracion

    def activar_freno_mano(self):
        self.freno_mano = True


class Auto(Vehiculo):
    def acelerar(self, intensidad):
        """Extendiendo un método"""
        # Agregamos comportamiento
        if not self.freno_mano:
            self.aceleracion = super().acelerar(intensidad)
        else:
            self.aceleracion = 0
        return self.aceleracion


class Camioneta(Vehiculo):
    def acelerar(self, intensidad):
        """Sobreescribiendo el método acelerar."""
        self.aceleracion = self.aceleracion + intensidad * 3
        return self.aceleracion
