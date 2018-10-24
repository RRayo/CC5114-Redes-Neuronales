import matplotlib.pyplot as plt
import numpy as np

from perceptron_class import Perceptron


def generar_puntos(N, funcion, rango):
    puntos = np.random.uniform(rango[0], rango[1], (N, 2))  # arreglo de [[x,y],[x2,y2], ... ]
    deseados = np.array([])
    for i in range(N):
        valor = 0  # abajo
        if funcion(puntos[i][0]) < puntos[i][1]:
            valor = 1  # arriba
            np.append(deseados, valor)
    return puntos, deseados


def separar_puntos(puntos, real_output, funcion):
    p_arriba = []
    p_abajo = []
    for i in range(len(puntos)):
        x, y = puntos[i]
        if real_out[i] == 1:
            p_arriba.append([x, y])
        else:
            p_abajo.append([x, y])
    return np.array(p_abajo), np.array(p_arriba)


def perceptron_output(perceptron, puntos):
    real_output = []
    for p in puntos:
        feed = perceptron.feed(p)
        real_output.append(feed)
    return np.array(real_output)


# MAIN

# perceptron random
random_weights = np.random.uniform(-2, 2, 2)
random_bias = np.random.uniform(-2, 2, 1)[0]
p = Perceptron(random_weights, random_bias)

# funcion
fun = lambda x: x

# dataset
rango = (-10, 10)
n_puntos = 20
puntos, deseados = generar_puntos(n_puntos, fun, rango)

# numero de iteraciones
n = 100

real_out = perceptron_output(p, puntos)
p_abajo, p_arriba = separar_puntos(puntos, real_out, fun)
plt.scatter(p_abajo.T[0], p_abajo.T[1], c='r')
plt.scatter(p_arriba.T[0], p_arriba.T[1], c='b')
plt.plot(range(rango[0], rango[1]), fun(range(rango[0], rango[1])))
# marcar ejes
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
plt.close()
