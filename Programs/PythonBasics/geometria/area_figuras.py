"""
Esta es la libreria de areas de figuras geométricas
autor
fecha
observaciones:
version:
"""
from math import pi, pow


def circulo(radio):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = pi*pow(radio,2)
    print('El área del círculo de radio {:.3f} es {:.3f}'.format(radio, area))
    return area


def rectangulo(lado1, lado2):
    area = lado1*lado2
    print('El área del rectángulo de lados {:.3f}, {:.3f} es {:.3f}'.format(lado1, lado2, area))
    return area


def triangulo(base, altura):
    area = base*altura/2
    print('El área del triángulo de lados {:.3f}, {:.3f} es {:.3f}'.format(base, altura, area))
    return area

if __name__ == '__main__':
    circulo(radio=3.0)
    triangulo(base=1.2, altura=2.2)
    rectangulo(lado1=2.222, lado2=2.333)

