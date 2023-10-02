"""Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir
atributos como nombre y edad. Las subclases deben heredar y definir
métodos y atributos relacionados con el comportamiento y
características de cada tipo de animal."""


class Animal:
    def comer(self):
        return "comiendo"

    def dormir(self):
        return "durmiendo"


class Perro(Animal):
    pass


class Gato(Animal):
    pass


class Dogo(Perro):
    def modo_guardian(self):
        return "cuidado que te como"


perro = Perro()
print(perro.comer())


"""
1. Dedican 5 minutos a pensar y debatir una idea.
2. Dedican 5 minutos a escribir el enunciado de lo que van a hacer, lo bajan a tierra.
3. En 5 minutos pensar en la solución, no en el código.
4. En 20 minutos, escriben todas las clases que van a utilizar con pass y hacen la herencia, composición etc.
5. En 10 minutos, escriben todos los metodos sin implementar. (pass)


Las clases tienen una única responsabilidad, es decir, no deben mezclar peras con manzanas.

Métodos obligatorios de implementacion
Métodos con implemetacion vacia (pass) --> No se implementa nada, pero se debe implementar en las clases hijas

Pensar un algoritmo en POO para practicar el diseño de clases.

Deben crear muchas clases para repretentar el problema que quieren resolver

La idea es que la lógica quede bien separada en distintas capas

Adicional, pueden implementar la composición de clases

No hay que heredar por heredar. La herencia no es lo único en la vida.

"""


class AlgoDePepe:
    pass


class Pepe:
    algo_de_pepe = AlgoDePepe()
