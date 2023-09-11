class Estudiante:
    def __init__(self, nombre, edad, notas=None):
        self._nombre = nombre
        self._edad = edad
        self._notas = notas

    def cargar_nota(self, nota):
        if len(self._notas) <= 3:
            self._notas.append(nota)
            return self._notas

    @property
    def promedio(self):
        notas = 0
        for promedio in self._notas:
            notas += promedio
        return notas / len(self._notas)

    @property
    def sobresaliente(self):
        # If de una linea
        return True if self.promedio >= 8 else False

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}. Edad: {self.edad}. Promedio: {self.promedio}"

    def incrementar_edad(self):
        self.edad += 1
