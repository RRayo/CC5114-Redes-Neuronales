from neuron import Neuron
from neuron_layer import NeuronLayer


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

        layers.append(NeuronLayer(neurons))

        aux = val
    return layers
