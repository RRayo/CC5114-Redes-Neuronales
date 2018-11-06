from neuron_network import NewronNetwork, layer_const

actication_fun = lambda x: x
shape_network = (4, 3, 2, 2)
layers = layer_const(shape=shape_network, fun=actication_fun)
net = NewronNetwork(layers)

inputs = [1, 2, 3, 4]
net.feed(inputs)
print(net.outputs)

desired_outs = [2, 3]
net.train(inputs, desired_outs) # TODO revisar el valor de los delta (no está entrando en la primera layer, probar ejemplo del profe)
net.feed(inputs)
print(net.outputs)
