import numpy


class Neuron:

    def __init__(self, weights, bias, fun):
        self.weights = weights
        self.bias = bias
        self.fun = fun
        self.output = 0
        self.delta = 0

    def feed(self, inputs):
        self.output = self.fun(numpy.dot(inputs, self.weights) + self.bias)
        return self.output

    def train(self, desired_output, input, lr=0.1):
        real_output = self.feed(input)
        diff = desired_output - real_output
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (lr * input[i] * diff)
        self.bias = self.bias + (lr * diff)

    def adjust_delta(self, error):
        self.delta = error * transfer_derivate(self.output)

    def update_weights(self, inputs, learning_rate=0.1):
        for i in range(len(inputs)):
            self.weights[i] = self.weights[i] + (learning_rate * self.delta * inputs[i])
        self.bias = self.bias + (learning_rate * self.delta)


def transfer_derivate(output):
    return output * (1.0 - output)
