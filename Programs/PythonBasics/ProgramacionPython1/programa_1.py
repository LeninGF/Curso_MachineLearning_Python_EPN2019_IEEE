"""
Este script hace ........
Autor: LGFE
Fecha: 06/06/06
"""

#%%
import numpy as np
import argparse
from geometria import area_figuras
from geometria import perimetro_figuras

import pandas as pd

#%%

# def hipotenusa(cateto_1, cateto_2):
#     """
#     Esta funcion calcula la hipo de un triag rect
#     :param cateto_1:
#     :param cateto_2:
#     :return:
#     """
#     hip = sqrt(cateto_1**2+cateto_2**2)
#     return hip

def main(radio, lado1, lado2, base, altura):
    area_circulo1 = area_figuras.circulo(radio=radio)
    area_rectangulo1 = area_figuras.rectangulo(lado1=lado1, lado2=lado2)
    per_rectamgulo1 = perimetro_figuras.rectangulo(lado1=lado1, lado2=lado2)
    area_triangulo1 = area_figuras.triangulo(base=base, altura=altura)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--radio',
        '-z',
        type=float,
        default=3.,
        help='Ingrese el radio como un numero flotante'
    )

    parser.add_argument(
        '--lado1',
        '-l1',
        type=float,
        default=3.,
        help='Ingrese el lado rectangulo'
    )

    argumentos = parser.parse_args()

    main(radio=argumentos.radio, lado1=argumentos.lado1, lado2=2, base=2, altura=2)


