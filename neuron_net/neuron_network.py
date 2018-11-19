class NeuronNetwork:

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
