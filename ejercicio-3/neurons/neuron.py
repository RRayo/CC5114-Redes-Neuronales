import abc


class Neuron(abc.ABC):

    @abc.abstractmethod
    def __init__(self, weights, bias):
        pass

    @abc.abstractmethod
    def feed(self, inputs):
        pass

    @abc.abstractmethod
    def train(self, desired_output, input, lr=0.1):
        pass
