import numpy


class Perceptron:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feed(self, inputs):
        return 0 if numpy.dot(inputs, self.weights) + self.bias <= 0 else 1

    def train(self, desired_output, real_output, input, lr=0.1):
        diff = desired_output - real_output
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (lr * input[i] * diff)
        self.bias = self.bias + (lr * diff)


