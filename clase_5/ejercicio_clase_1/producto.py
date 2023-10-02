class Producto:
    categoria = None

    def __init__(self, nombre, precio, descripcion, cantidad_inicial):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad_inicial

    def obtener_descripcion(self):
        return self.descripcion

    def obtener_precio(self):
        return self.precio

    def obtener_categoria(self):
        return self.categoria

    def obtener_disponibilidad(self):
        return f"Unidades: {self.cantidad}."

    def imprimir_informacion(self):
        return f"{self.nombre} - ${self.precio} - {self.categoria}\nDescripción: {self.descripcion} Disponibles: {self.cantidad} unidades"

    def aplicar_descuento(self, descuento):
        self.precio -= descuento

    def aumentar_precio(self, aumento):
        """Aumenta el precio del producto en el porcentaje indicado"""
        self.precio += aumento

    def cambiar_nombre(self, nuevo_nombre):
        """Cambia el nombre del producto"""
        self.nombre = nuevo_nombre

    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def actualizar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    def ajustar_precio(self, porcentaje):
        self.precio *= 1 + porcentaje / 100

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return f"Se han vendido {cantidad} unidades de {self.nombre}."
        else:
            return f"No hay suficiente stock de {self.nombre} para vender {cantidad}."
