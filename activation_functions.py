import math

import numpy


def identity(x):
    return x


def binary_step(x):
    if x < 0:
        return 0
    return 1


def sigmoid(x, derivative=False):
    return x * (1 - x) if derivative else 1 / (1 + numpy.exp(-x))


def tanh(x):
    2 / (1 + numpy.exp(-2 * x)) - 1


def relu(x):
    return max(0, x)


def prelu(x, alpha):
    if x < 0:
        return alpha * x
    return x


def elu(x, alpha):
    if x < 0:
        return alpha * (numpy.exp(x) - 1)
    return x


def soft_plus(x):
    return math.log(1 + numpy.exp(x))
