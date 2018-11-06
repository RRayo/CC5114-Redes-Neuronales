import numpy


def sigmoid(x, derivative=False):
    return x * (1 - x) if derivative else 1 / (1 + numpy.exp(-x))


def perceptron(x):
    if x <= 0:
        return 0
    return 1
