class Bar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []

    def agregar_bebida(self, bebida):
        self.menu.append(bebida)

    def mostrar_menu(self):
        print(f"Menú de {self.nombre}:")
        for bebida in self.menu:
            print(bebida)

    def realizar_pedido(self, bebida, cantidad):
        return f"Pedido de {cantidad} {bebida.nombre} en {self.nombre}"

    def __str__(self):
        return f"Bar {self.nombre} en {self.direccion} con {self.telefono}"


class SucursalBar(Bar):
    def __init__(self, nombre_sucursal):
        super().__init__(nombre_sucursal)
        self.nombre_sucursal = nombre_sucursal

    def recibir_reserva(self, nombre_cliente, fecha):
        return f"Reserva para {nombre_cliente} en {self.nombre} ({self.nombre_sucursal}) el {fecha}"

    def __str__(self):
        return f"Sucursal {self.nombre}"
