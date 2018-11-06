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
