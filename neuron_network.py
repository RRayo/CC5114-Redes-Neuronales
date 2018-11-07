# TODO unittest training (?) -> ver si se usa

import numpy as np

from neuron import Neuron
from neuron_layer import NewronLayer


class NewronNetwork:

    def __init__(self, layers):
        self.layers = layers
        self.outputs = []

    def feed(self, inputs):
        for layer in self.layers:
            layer.feed(inputs)
            inputs = layer.outputs
        self.outputs = inputs
        return inputs

    def train(self, inputs, desired_outputs, learning_rate=0.1):
        self.feed(inputs)
        self.back_propagate_error(desired_outputs)
        self.update_weights(inputs, learning_rate)

    def back_propagate_error(self, desired_outputs):
        last = True
        for i in range(len(self.layers) - 1, -1, -1):

            if last:
                self.layers[i].back_propagation_last_layer(desired_outputs)
                last = False
            else:
                self.layers[i].back_propagation_inner_layer(self.layers[i + 1])

    def update_weights(self, inputs, learning_rate=0.1):
        for layer in self.layers:
            layer.update_weights(inputs, learning_rate)
            inputs = layer.outputs


def layer_const(shape, fun):
    """
    Crea un arreglo de layers de neuronas a partir de un shape.
    :param shape: tupla o lista de la forma: (inputs, num_neuronas_layer_1, layer_2, ...).

    :return: arreglo con layers de neuronas.
    """
    layers = []
    aux = -1  # numero de pesos para el layer actual
    for val in shape:
        if aux == -1:
            aux = val
            continue

        neurons = []
        # cuantas neuronas hay en este layer
        for i in range(val):
            bias = np.random.uniform(-2, 2)
            weights = np.random.uniform(-2, 2, aux)
            neurons.append(Neuron(weights, bias, fun))

        layers.append(NewronLayer(neurons))

        aux = val
    return layers
