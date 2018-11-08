import unittest

import matplotlib.pyplot as plt

from activation_functions import *
from tools import net_constructor, mean_squared_error


class TestAND(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        inputs = 2
        outputs = 1
        shape = (inputs, outputs)
        self.network = net_constructor(shape, fun)

    def test_training(self):
        n = 2000

        error = []

        inputs = [[1, 1],
                  [1, 0],
                  [0, 1],
                  [0, 0]]
        desired_outputs = [[1],
                           [0],
                           [0],
                           [0]]

        for i in range(n):
            error_epoch = 0
            for k in range(len(inputs)):
                self.network.train(inputs[k], desired_outputs[k], learning_rate=0.5)
                error_epoch += mean_squared_error(desired_outputs[k], self.network.outputs)
            error.append(error_epoch)

        plt.plot(range(n), error)
        plt.title("Error de aprendizaje red AND")
        plt.xlabel("Epoch")
        plt.ylabel("Error")
        # plt.show()
        plt.close()

        epsilon = 0.01

        for i in range(len(inputs)):
            self.network.feed(inputs[i])
            diff = mean_squared_error(self.network.outputs, desired_outputs[i])
            assert diff < epsilon, f"incorrect output for input AND {inputs[i]}, difference: {diff}"


class TestOR(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        inputs = 2
        outputs = 1
        shape = (inputs, outputs)
        self.network = net_constructor(shape, fun)

    def test_training(self):
        n = 2000

        error = []

        inputs = [[1, 1],
                  [1, 0],
                  [0, 1],
                  [0, 0]]
        desired_outputs = [[1],
                           [1],
                           [1],
                           [0]]

        for i in range(n):
            error_epoch = 0
            for k in range(len(inputs)):
                self.network.train(inputs[k], desired_outputs[k], learning_rate=0.5)
                error_epoch += mean_squared_error(desired_outputs[k], self.network.outputs)
            error.append(error_epoch)

        plt.plot(range(n), error)
        plt.title("Error de aprendizaje red OR")
        plt.xlabel("Epoch")
        plt.ylabel("Error")
        # plt.show()
        plt.close()

        epsilon = 0.01

        for i in range(len(inputs)):
            self.network.feed(inputs[i])
            diff = mean_squared_error(self.network.outputs, desired_outputs[i])
            assert diff < epsilon, f"incorrect output for input OR {inputs[i]}, difference: {diff}"


class TestXOR(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        inputs = 2
        inner_layer1 = 2
        outputs = 1
        shape = (inputs, inner_layer1, outputs)
        self.network = net_constructor(shape, fun)

    def test_training(self):
        n = 3000

        error = []

        inputs = [[1, 1],
                  [1, 0.1],
                  [0.1, 1],
                  [0.1, 0.1]]
        desired_outputs = [[0.1],
                           [1],
                           [1],
                           [0.1]]

        for i in range(n):
            error_epoch = 0
            for k in range(len(inputs)):
                self.network.train(inputs[k], desired_outputs[k], learning_rate=0.5)
                error_epoch += mean_squared_error(desired_outputs[k], self.network.outputs)
            error.append(error_epoch)

        plt.plot(range(n), error)
        plt.title("Error de aprendizaje red XOR")
        plt.xlabel("Epoch")
        plt.ylabel("Error")
        plt.show()
        plt.close()

        epsilon = 0.3

        for i in range(len(inputs)):
            self.network.feed(inputs[i])
            diff = mean_squared_error(self.network.outputs, desired_outputs[i])
            print(diff)
            assert diff < epsilon, f"incorrect output for input XOR {inputs[i]}, " \
                                   f"outputs: {self.network.outputs}"
