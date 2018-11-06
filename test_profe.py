import unittest

import numpy as np

from activation_functions import sigmoid
from neuron import Neuron
from neuron_layer import NewronLayer
from neuron_network import NewronNetwork


class TestXOR(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        fun = sigmoid
        self.neuron_1 = Neuron([0.4, 0.3], 0.5, fun)
        self.neuron_2 = Neuron([0.3], 0.4, fun)
        self.layer_1 = NewronLayer([self.neuron_1])
        self.layer_2 = NewronLayer([self.neuron_2])
        self.network = NewronNetwork([self.layer_1, self.layer_2])

    def test_training(self):
        inputs = [1, 1]
        desired_outputs = [1]
        self.network.train(inputs, desired_outputs)

        print(self.neuron_1.weights)
        print(self.neuron_1.bias)
        print(self.neuron_2.weights)
        print(self.neuron_2.bias)

        w_1 = np.array(self.neuron_1.weights)
        desired_w_1 = np.array([0.40210150899948904, 0.302101508999489])

        b_1 = self.neuron_1.bias
        desired_b_1 = 0.502101508999489

        w_2 = np.array(self.neuron_2.weights)
        desired_w_2 = np.array([0.33026254863991883])

        b_2 = self.neuron_2.bias
        desired_b_2 = 0.43937745312797394

        epsilon = 0.001

        assert np.abs(w_1 - desired_w_1)[0] < epsilon, "incorrect weight_1 neuron_1"
        assert np.abs(w_1 - desired_w_1)[2] < epsilon, "incorrect weight_2 neuron_1"
        assert np.abs(b_1 - desired_b_1), "incorrect bias neuron_1"

        assert np.sum(np.abs(w_2 - desired_w_2)) / 2 < epsilon, "incorrect weights neuron_2"
        assert np.abs(b_2 - desired_b_2), "incorrect bias neuron_2"
