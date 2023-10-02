from categoria import Categoria
from producto import Producto


class ProductoCarniceria(Producto):
    categoria = Categoria("Carnicería")

    def __init__(self, nombre, precio, descripcion, cantidad_inicial, fecha_caducidad):
        super().__init__(nombre, precio, descripcion, cantidad_inicial)
        self.fecha_caducidad = fecha_caducidad

    def obtener_fecha_caducidad(self):
        return f"Caduca el {self.fecha_caducidad}"


class ProductoBazar(Producto):
    categoria = Categoria("Bazar")

    def __init__(self, nombre, precio, descripcion, cantidad_inicial, dimensiones):
        super().__init__(nombre, precio, descripcion, cantidad_inicial)
        self.dimensiones = dimensiones

    def obtener_dimensiones(self):
        return f"Dimensiones: {self.dimensiones}"


class ProductoLimpieza(Producto):
    categoria = Categoria("Limpieza")

    def __init__(self, nombre, precio, descripcion, cantidad_inicial, aroma):
        super().__init__(nombre, precio, descripcion, cantidad_inicial)
        self.aroma = aroma

    def obtener_aroma(self):
        return f"Aroma: {self.aroma}"
