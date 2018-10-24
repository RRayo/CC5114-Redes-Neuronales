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

        # real_out =
        # comparar cuantos se obtuvieron correctamente



        assert self.p_and.feed([0, 0]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([0, 1]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([1, 0]) == 0, "p_and not calculating values correctly"
        assert self.p_and.feed([1, 1]) == 1, "p_and not calculating values correctly"

    def test_training_20(self):
        1