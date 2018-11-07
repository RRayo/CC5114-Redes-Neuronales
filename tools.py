import numpy as np

from neuron import Neuron
from neuron_layer import NeuronLayer
from neuron_network import NeuronNetwork


def net_constructor(shape, fun):
    """
    Crea una red neuronal a partir de un shape.
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
            random_sign = 1 if np.random.rand() < 0.5 else -1
            bias = np.random.uniform(0.5, 2) * random_sign
            weights = np.random.uniform(0.5, 2, aux) * random_sign_array(aux)
            neurons.append(Neuron(weights, bias, fun))

        layers.append(NeuronLayer(neurons))

        aux = val
    return NeuronNetwork(layers)


def random_sign_array(shape):
    array = np.random.rand(shape)
    array[array > 0.5] = 1
    array[array <= 0.5] = -1
    return array


def normalize_data_fun(data_low, data_high, n_low, n_high):
    return lambda x: (x - data_low) * (n_high - n_low) / (data_high - data_low) + n_low


def denormalize_data_fun(data_low, data_high, n_low, n_high):
    return lambda x: ((data_low - data_high) * x - (n_high * data_low) + (data_high * n_low)) / (n_low - n_high)


# f = normalize_data_fun(-10, 10, 0, 1)
# f2 = denormalize_data_fun(-10, 10, 0, 1)
# print(f(5))
# print(f2(0.75))


def mean_absolute_error(expected_out, out):
    expected_out = np.array(expected_out)
    out = np.array(out)
    return np.sum(np.abs(expected_out - out)) / len(expected_out)


def mean_squared_error(expected_out, out):
    expected_out = np.array(expected_out)
    out = np.array(out)
    return np.sum(np.square(expected_out - out)) / len(expected_out)
