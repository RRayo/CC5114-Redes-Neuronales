# TODO unittest training (?) -> ver si se usa
# TODO clases network, layers
# TODO forwardfeed, backwardfeed, error propagation, weightrecalculation


class NewronLayer:

    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = []

    def feed(self, inputs):
        for n in self.neurons:
            n.feed(inputs)
            self.outputs.append(n.output)

class NewronNetwork:

    def __init__(self, layers):
        self.layers = layers

    def feed(self, inputs):
        for layer in self.layers:
            layer.feed(inputs)
            inputs = layer.outputs
        return inputs