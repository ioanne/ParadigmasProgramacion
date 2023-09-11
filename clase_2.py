"""
    Crea una clase llamada "Estudiante" con los siguientes atributos: nombre, edad y _promedio.
    Implementa tres métodos: mostrar_informacion() para mostrar los detalles del estudiante,
    actualizar_promedio(nuevo_promedio) para cambiar el promedio del estudiante y
    incrementar_edad() para aumentar en 1 la edad del estudiante cada vez que se llama.
    Además, crea una propiedad llamada promedio para acceder y modificar el promedio de
    manera controlada.
    PEP-8
"""


class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self._promedio = promedio

    def actualizar_promedio(self, promedio):
        """Los getters son métodos."""
        self._promedio = promedio

    @property
    def promedio(self):
        """Los setters son propiedades."""
        return self._promedio

    def mostrar_informacion(self):
        return f"{self.nombre} {self.edad} {self.promedio}"

    def incrementar_edad(self):
        self.edad += 1


estudiante = Estudiante("Juan", 31, 6)
print(estudiante.mostrar_informacion())
print(f"Edad: {estudiante.edad}")
estudiante.incrementar_edad()
print(f"Edad: {estudiante.edad}")
print(estudiante.mostrar_informacion())
estudiante.actualizar_promedio(8)
print(estudiante.promedio)
