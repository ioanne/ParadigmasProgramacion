class Menu:
    def __init__(self):
        self.menu = []

    def agregar_bebida(self, bebida):
        self.menu.append(bebida)

    def mostrar_menu(self):
        for bebida in self.menu:
            print(bebida)

    def buscar_bebida(self, nombre):
        for bebida in self.menu:
            if bebida.nombre == nombre:
                return bebida

    def __str__(self):
        return f"Menú del Bar {self.nombre} menu: {self.menu}"
