import matplotlib.pyplot as plt
import numpy as np

from perceptron_class import Perceptron


def generar_puntos(N, rango):
    puntos = np.random.uniform(rango[0], rango[1], (N, 2))  # arreglo de [[x,y],[x2,y2], ... ]
    return puntos


