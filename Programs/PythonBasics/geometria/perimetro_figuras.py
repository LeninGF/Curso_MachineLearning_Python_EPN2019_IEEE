from math import pi, pow, sqrt


def rectangulo(lado1, lado2):
    per = lado1*2+lado2*2
    print('Perimetro de rectangulo de lados {} y {} es {}'.format(lado1, lado2, per))
    return per

def circulo(radio):
    per = 2*pi*radio
    return per

def triangulo(base, altura):
    pass


if __name__ == '__main__':
    print('hola veamos si esto aparece en el programa_1')
    rectangulo(5,5)