from bebida import Bebida
from tipo_bebida import TipoBebida


class Vino(Bebida):
    Bebida.tipo_bebida = TipoBebida("Vino")

    def __init__(self, nombre, precio, variedad):
        super().__init__(nombre, precio)
        self.variedad = variedad

    def __str__(self):
        return f"{self.nombre} - {self.variedad}"


class Gaseosa(Bebida):
    Bebida.tipo_bebida = TipoBebida("Gaseosa")

    def __init__(self, nombre, precio, sabor):
        super().__init__(nombre, precio)
        self.sabor = sabor

    def servir_frio(self):
        return f"Sirviendo {self.nombre} bien fría"

    def __str__(self):
        return f"{self.nombre} - {self.sabor}"


class Trago(Bebida):
    Bebida.tipo_bebida = TipoBebida("Trago")

    def __init__(self, nombre, precio, ingredientes: list[Bebida]):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

    def obtener_informacion_ingredientes(self):
        return f"Ingredientes: {', '.join([str(ingrediente) for ingrediente in self.ingredientes])}"

    def servir(self):
        return f"Sirviendo {self.nombre}"

    def agitar(self):
        return f"Agitando {self.nombre}"

    def preparar(self):
        return f"Preparando {self.nombre}"

    def decorar(self):
        return f"Decorando {self.nombre}"

    def mezclar(self):
        return f"Mezclando {self.nombre}"

    def __str__(self):
        return f"{self.nombre} - {self.obtener_informacion_ingredientes()}"
