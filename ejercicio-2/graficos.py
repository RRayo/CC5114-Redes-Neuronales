import matplotlib.pyplot as plt
import numpy

from perceptron import Perceptron
from tools import generar_puntos


def outputs(percep, inputs, fun):
    real_output = []
    desired_output = []

    for p in inputs:
        real_output.append(percep.feed(p))
        desired_output.append(1 if p[1] > fun(p[0]) else 0)

    return real_output, desired_output


def train(N, input, fun, percep):
    # TODO puede que se esté sobreentrenando
    for i in range(N):
        for x, y in input:
            out = 1 if y > fun(x) else 0
            percep.train(out, [x, y])


def plotear(x, y, outs, fun, N, colors=('r', 'b')):
    color_array = []
    for out in outs:
        if out == 1:
            color_array.append(colors[0])
        else:
            color_array.append(colors[1])

    plt.title("Numero de veces entrenado: " + str(N))
    plt.scatter(x, y, c=color_array)
    plt.plot(x, numpy.array([fun(xi) for xi in x]))
    plt.show()
    plt.close()


def entrenar_multiple(rango, puntos, fun):
    ratio_exitos = []
    for n in rango:
        weights = numpy.random.uniform(-2, 2, 2)
        bias = numpy.random.uniform(-2, 2)
        percep = Perceptron(weights, bias)

        train(n, puntos, fun, percep)
        real_out, desired_out = outputs(percep, random_puntos, funcion)

        total = len(random_puntos)
        aciertos = numpy.sum(numpy.array(real_out) == numpy.array(desired_out))
        ratio_exitos.append(aciertos / total)

        rand_traspose = random_puntos.T

        plotear(rand_traspose[0], rand_traspose[1], real_out, funcion, n)

    plt.plot(rango, ratio_exitos)
    plt.title("Relación de exitos según número de entrenamientos")
    plt.show()
    plt.close()


funcion = lambda x: x
rango = (-10, 10)
random_puntos = generar_puntos(100, rango)

rango_training = range(0, 25, 3)
entrenar_multiple(rango_training, random_puntos, funcion)


