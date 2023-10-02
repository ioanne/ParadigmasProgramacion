"""Abstracción
1.1. FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo
y Triangulo y que contenga métodos y atributos relacionados con el
cálculo del área y perímetro de una figura geométrica. Definan los
métodos y atributos necesarios para calcular el área y el perímetro de
cada tipo de figura utilizando los conceptos de abstracción."""

from abc import ABC, abstractmethod


# Manera 1
class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


# Manera 2 con abc
class FiguraGeometricaAbstracta(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(FiguraGeometricaAbstracta):
    def calcular_area(self):
        return 10

    def calcular_perimetro(self):
        return 12


class Rectangulo(FiguraGeometrica):
    pass


circulo = Circulo()
rectangulo = Rectangulo()


# Clase abstracta  --> No tiene implementación
# Clase intermedia donde implementamos todo lo que tienen en común las clases hijas --> Solo lo comun
# ------ Aca se hace la magia ------
# Clase a utilizar
# Clase secundaria con pequeñas modificaciones


"""
IP  190.16.18.200
TCP -- IP // TCP/IP 190.16.18.200:1 a 190.16.18.200:65534
HTTP -- TCP/IP 80
HTTPS -- HTTP 447
GenericView -- HTTPS
TemplateView -- GenericView
Marketplace -- TemplateView

MarketplaceSeller -- Marketplace

"""
