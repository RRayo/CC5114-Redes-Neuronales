class NewronLayer:

    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = []

    def feed(self, inputs):
        self.outputs = []
        for n in self.neurons:
            n.feed(inputs)
            self.outputs.append(n.output)

    def update_weights(self, inputs, learning_rate=0.1):
        for n in self.neurons:
            n.update_weights(inputs, learning_rate)
            
    def back_propagation_last_layer(self, desired_outputs):
        for i in range(len(self.neurons)):
            error = desired_outputs[i] - self.neurons[i].output
            self.neurons[i].adjust_delta(error)

    def back_propagation_inner_layer(self, next_layer):
        for i in range(len(self.neurons)):
            error = 0
            for neuron in next_layer.neurons:
                error += neuron.weights[i] * neuron.delta
            self.neurons[i].adjust_delta(error)
