# TODO unittest training (?) -> ver si se usa
# TODO clases network, layers
# TODO forwardfeed, backwardfeed, error propagation, weightrecalculation

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

    def train(self, inputs, desired_outputs):
        self.feed(inputs)
        self.back_propagate_error(desired_outputs)
        self.update_weights(inputs)

    def back_propagate_error(self, desired_outputs):
        last = True
        for i in range(len(self.layers) - 1, -1, -1):

            if last:
                # por cada neurona del layer se calcula el error y actualiza su delta
                for k in range(len(self.layers[i].neurons)):  # TODO refactor (meter en layers y en neurona)
                    error = desired_outputs[k] - self.layers[i].neurons[k].output
                    self.layers[i].neurons[k].adjust_delta(error)
                last = False
            else:
                # if i == 0:
                #     break

                # por cada neurona del layer se calcula el error y actualiza su delta
                for k in range(len(self.layers[i].neurons)):  # TODO refactor (meter en layers y en neurona)
                    error = 0
                    for neuron in self.layers[i + 1].neurons:
                        error += neuron.weights[k] * neuron.delta
                    self.layers[i].neurons[k].adjust_delta(error)

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
