# class Auto:
#     def __init__(self, color, rodado, marca):
#         self._color = color
#         self.rodado = rodado
#         self.marca = marca

#     @property
#     def color(self):
#         return self._color

#     def cambiar_color(self, color):
#         self._color = color


"""
Diseño:
    Autos que sean unicamente de color blanco, rojo, azul, negro, gris, gris ocuro
"""


class Auto:
    """Esta sería una manera mas correcta"""

    COLORES_PERMITIDOS = ("blanco", "rojo", "azul", "negro", "gris", "gris oscuro")

    def __init__(self, color, rodado, marca):
        self._color = color if self.validar_color(color) else None
        self.rodado = rodado
        self.marca = marca

    def validar_color(self, color):
        es_valido = False
        if color in self.COLORES_PERMITIDOS:
            es_valido = True
        return es_valido

    def asignar_color(self, color):
        se_asigno = False
        if self.validar_color(color):
            self._color = color
            se_asigno = True
        return se_asigno, self._color

    @property
    def color(self):
        return self._color


auto = Auto(color="blanco", marca="Ford", rodado=30)
print(auto.color)
auto.asignar_color("rojo")
print(auto.color)


se_asigno, color = auto.asignar_color("celeste")

if se_asigno:
    print(f"Se asigno el color {color}")
else:
    print(f"No se asigno el color. Mantiene el mismo color que es: {color}")
