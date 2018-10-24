import numpy

from neuron import Neuron


class Perceptron(Neuron):

    def __init__(self, weights, bias):
        Neuron.__init__(self)
        self.weights = weights
        self.bias = bias

    def feed(self, inputs):
        return 0 if numpy.dot(inputs, self.weights) + self.bias <= 0 else 1

    def train(self, desired_output, input, lr=0.1):
        real_output = self.feed(input)
        diff = desired_output - real_output
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (lr * input[i] * diff)
        self.bias = self.bias + (lr * diff)
