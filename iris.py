from time import time

import matplotlib.pyplot as plt

from activation_functions import *
from tools import *
from sklearn.model_selection import train_test_split

iris_filename = "data/iris-data.txt"

inputs, outputs, min_in, max_in = process_iris_file(iris_filename)

fun = sigmoid
net_shape = (4, 4, 4, 3)
learning_rate = 0.5

network = net_constructor(net_shape, fun)

# TRAINING

X_train, X_test, y_train, y_test = train_test_split(
    inputs, outputs, test_size=0.30, random_state=42)


n = 1000
errors = []

init_time = time()

for i in range(n):
    print(f"Training epoch {i}")
    error_epoch = 0
    for k in range(len(X_train)):
        network.train(X_train[k], y_train[k], learning_rate=learning_rate)
        error_epoch += mean_squared_error(y_train[k], network.outputs)
    errors.append(error_epoch)

end_time = time()
print(f"\nTiempo transcurrido entrenamiento: {end_time - init_time}")


plt.plot(range(n), errors)
plt.title(f"Error de red IRIS, lr={learning_rate}")
plt.xlabel("Epochs")
plt.ylabel("Error")
plt.show()
plt.close()
