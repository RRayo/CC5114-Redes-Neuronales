import numpy


class Perceptron:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feed(self, inputs):
        return 0 if numpy.dot(inputs, self.weights) + self.bias <= 0 else 1


# sum with carry
def p_sum(x1, x2):
    perceptron_nand = Perceptron([-2, -2], 3)
    out_1 = perceptron_nand.feed([x1, x2])
    out_2 = perceptron_nand.feed([x1, out_1])
    out_3 = perceptron_nand.feed([x2, out_1])
    out_carry = perceptron_nand.feed([out_1, out_1])
    out_sum = perceptron_nand.feed([out_2, out_3])
    return out_sum, out_carry
