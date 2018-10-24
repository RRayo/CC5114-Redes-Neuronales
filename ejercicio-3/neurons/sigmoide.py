import numpy

from neuron import Neuron


class Sigmoide(Neuron):

    def __init__(self, weights, bias):
        Neuron.__init__(self)
        self.weights = weights
        self.bias = bias

    def feed(self, inputs):
        return sigmoid(numpy.dot(inputs, self.weights) + self.bias)

    def train(self, desired_output, input, lr=0.1):
        real_output = self.feed(input)
        diff = desired_output - real_output
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (lr * input[i] * diff)
        self.bias = self.bias + (lr * diff)


def sigmoid(x, derivative=False):
    return x * (1 - x) if derivative else 1 / (1 + numpy.exp(-x))
