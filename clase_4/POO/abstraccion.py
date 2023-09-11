import abc


class AnimalAbstracto(abc.ABC):
    @abc.abstractmethod
    def hacer_ruido(self):
        pass

    # @abc.abstractclassmethod
    # @classmethod
    # def metodo_de_clase(cls):
    #     pass

    # @abc.abstractproperty
    # @property
    # def propiedad(self):
    #     pass

    # @abc.abstractstaticmethod
    # @staticmethod
    # def metodo_estatico():
    #     pass

    def caminar(self):
        pass


class Animal(AnimalAbstracto):
    """Clase incompleta, no se implementa hacer_ruido."""

    def caminar(self):
        return "caminando"


class Gato(Animal):
    def hacer_ruido(self):
        return "Miau!"


class Perro(Animal):
    def hacer_ruido(self):
        return "Guau!"


# gato = Gato()
# print(gato.hacer_ruido())
# perro = Perro()
# print(perro.hacer_ruido())

mascotas = [Gato(), Perro(), Gato(), Gato(), Perro()]


for mascota in mascotas:
    print(mascota.hacer_ruido())
