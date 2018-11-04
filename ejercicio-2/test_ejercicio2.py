import unittest

import numpy

from perceptron import Perceptron
from tools import generar_puntos


class TestTraining(unittest.TestCase):

    def setUp(self):
        self.funcion = lambda x: x
        rango = (-10, 10)
        self.random_puntos = generar_puntos(100, rango)
        weights = numpy.random.uniform(-2, 2, 2)
        bias = numpy.random.uniform(-2, 2)
        self.perceptron = Perceptron(weights, bias)
        up_down_fun = lambda x, y, fun: 1 if y > fun(x) else 0
        # self.desired_out = numpy.vectorize(up_down_fun)(self.random_puntos, )

    def test_noTraining(self):
        # numero de veces entrenado
        N = 0
        # comparar cuantos se obtuvieron correctamente

        real_out = numpy.array([])
        desired_out = numpy.array([])

        for p in self.random_puntos:
            real_out.append(self.perceptron.feed(p))
            desired_out.append(1 if p[1] > self.funcion(p[0]) else 0)

        total = len(self.random_puntos)
        aciertos = numpy.sum(real_out == desired_out)

        assert aciertos < total * 0.5, "aciertos son mayores al 50% del total"

    def test_training_20(self):
        # numero de veces entrenado
        N = 20
        for i in range(N):
            for x, y in self.random_puntos:
                desired_out = 1 if y > self.funcion(x) else 0
                self.perceptron.train(desired_out, [x, y])

        # comparar cuantos se obtuvieron correctamente

        real_out = []
        desired_out = []

        for p in self.random_puntos:
            real_out.append(self.perceptron.feed(p))
            desired_out.append(1 if p[1] > self.funcion(p[0]) else 0)

        total = len(self.random_puntos)
        aciertos = numpy.sum(real_out == desired_out)

        assert aciertos > total * 0.6, "aciertos son menores al 60% del total"