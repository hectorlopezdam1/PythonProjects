from abc import ABC


class FiguraGeometrica(ABC):
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass


class Triagulo(FiguraGeometrica):
    def calcular_area(lado1, altura):
        area = float(lado1) * float(altura) / 2
        return area
    def calcular_perimetro(lado1, lado2, lado3):
        perimetro = float(lado1) + float(lado2) + float(lado3)
        return perimetro


class Rectangulo(FiguraGeometrica):
    def calcular_area(base, altura):
        area = float(base) * float(altura)
        return area
    def calcular_perimetro(base, altura):
        perimetro = float(base) * 2 + float(altura) * 2
        return perimetro


class Cuadrado(FiguraGeometrica):
    def calcular_area(lado):
        area = float(lado) ** 2
        return area
    def calcular_perimetro(lado):
        perimetro = float(lado) * 4
        return perimetro


class Petagono(FiguraGeometrica):
    def calcular_perimetro(lado):
        perimetro = float(lado) * 5
        return perimetro
    def calcular_area(perimetro, apotema):
        area = float(perimetro) * float(apotema) / 2
        return area












