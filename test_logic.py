import unittest

import numpy as np

from activation_functions import *
from neuron import Neuron
from neuron_layer import NeuronLayer
from neuron_network import NeuronNetwork
from tools import net_constructor


# TODO meter OR y XOR
class TestAND(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        inputs = 2
        outputs = 1
        shape = (inputs, outputs)
        self.network = net_constructor(shape, fun)

    def test_training(self):
        # TODO entrenar con todos los inputs
        n = 1000

        inputs = [[1, 1],
                  [1, 0],
                  [0, 1],
                  [0, 0]]
        desired_outputs = [[1],
                           [0],
                           [0],
                           [0]]
        self.network.train(inputs, desired_outputs, learning_rate=0.5)

        w_1 = np.array(self.neuron_1.weights)
        desired_w_1 = np.array([0.40210150899948904, 0.302101508999489])

        b_1 = self.neuron_1.bias
        desired_b_1 = 0.502101508999489

        w_2 = np.array(self.neuron_2.weights)
        desired_w_2 = np.array([0.33026254863991883])

        b_2 = self.neuron_2.bias
        desired_b_2 = 0.43937745312797394

        epsilon = 0.00001
        assert np.abs(w_1 - desired_w_1)[0] < epsilon, "incorrect weight_1 neuron_1"
        assert np.abs(w_1 - desired_w_1)[1] < epsilon, "incorrect weight_2 neuron_1"
        assert np.abs(b_1 - desired_b_1) < epsilon, "incorrect bias neuron_1"

        assert np.abs(w_2 - desired_w_2)[0] < epsilon, "incorrect weight_1 neuron_2"
        assert np.abs(b_2 - desired_b_2) < epsilon, "incorrect bias neuron_2"


class Test2(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        self.neuron_1 = Neuron([0.7, 0.3], 0.5, fun)
        self.neuron_2 = Neuron([0.3, 0.7], 0.4, fun)
        self.neuron_3 = Neuron([0.2, 0.3], 0.3, fun)
        self.neuron_4 = Neuron([0.4, 0.2], 0.6, fun)
        self.layer_1 = NeuronLayer([self.neuron_1, self.neuron_2])
        self.layer_2 = NeuronLayer([self.neuron_3, self.neuron_4])
        self.network = NeuronNetwork([self.layer_1, self.layer_2])

    def test_training(self):
        inputs = [1, 1]
        desired_outputs = [1, 1]

        self.network.train(inputs, desired_outputs, learning_rate=0.5)

        n1_w = np.array(self.neuron_1.weights)
        n2_w = np.array(self.neuron_2.weights)
        n3_w = np.array(self.neuron_3.weights)
        n4_w = np.array(self.neuron_4.weights)

        n1_b = self.neuron_1.bias
        n2_b = self.neuron_2.bias
        n3_b = self.neuron_3.bias
        n4_b = self.neuron_4.bias

        n1_desired_w = np.array([0.7025104485493278, 0.3025104485493278])
        n2_desired_w = np.array([0.30249801135748333, 0.7024980113574834])
        n3_desired_w = np.array([0.22994737881955657, 0.32938362863950127])
        n4_desired_w = np.array([0.41943005652646226, 0.21906429169838573])

        n1_desired_b = 0.5025104485493278
        n2_desired_b = 0.40249801135748337
        n3_desired_b = 0.3366295422515899
        n4_desired_b = 0.6237654881509048

        epsilon = 0.00001

        assert np.abs(n1_w - n1_desired_w)[0] < epsilon, "incorrect weight_1 neuron_1"
        assert np.abs(n1_w - n1_desired_w)[1] < epsilon, "incorrect weight_2 neuron_1"

        assert np.abs(n2_w - n2_desired_w)[0] < epsilon, "incorrect weight_1 neuron_2"
        assert np.abs(n2_w - n2_desired_w)[1] < epsilon, "incorrect weight_2 neuron_2"

        assert np.abs(n3_w - n3_desired_w)[0] < epsilon, "incorrect weight_1 neuron_3"
        assert np.abs(n3_w - n3_desired_w)[1] < epsilon, "incorrect weight_2 neuron_3"

        assert np.abs(n4_w - n4_desired_w)[0] < epsilon, "incorrect weight_1 neuron_4"
        assert np.abs(n4_w - n4_desired_w)[1] < epsilon, "incorrect weight_2 neuron_4"

        assert np.abs(n1_b - n1_desired_b) < epsilon, "incorrect bias neuron_1"
        assert np.abs(n2_b - n2_desired_b) < epsilon, "incorrect bias neuron_2"
        assert np.abs(n3_b - n3_desired_b) < epsilon, "incorrect bias neuron_3"
        assert np.abs(n4_b - n4_desired_b) < epsilon, "incorrect bias neuron_4"
