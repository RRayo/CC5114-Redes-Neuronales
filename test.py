from neuron_network import NeuronNetwork
from tools import *

actication_fun = lambda x: x
shape_network = (4, 3, 2, 2)
layers = net_constructor(shape=shape_network, fun=actication_fun)
net = NeuronNetwork(layers)

inputs = [1, 2, 3, 4]
net.feed(inputs)
print(net.outputs)

desired_outs = [2, 3]
net.train(inputs, desired_outs)
net.feed(inputs)
print(net.outputs)
