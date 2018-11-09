import os
from time import time

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from activation_functions import *
from tools import *

FOLDER_GRAPHS = os.path.join(os.path.dirname(__file__), "results", "")


def process_iris(iris_filename="data/iris-data.txt", n_experiments=2000, activation_fun=sigmoid, net_shape=(4, 4, 3),
                 learning_rate=0.5, plot=False, title="", random_state=42):
    print("Creando red neuronal")
    print("Parámetros:")
    print(f"activarion function: {activation_fun.__name__}, net_shape={net_shape}, learning_rate={learning_rate}")

    inputs, outputs, min_in, max_in = process_iris_file(iris_filename)
    network = net_constructor(net_shape, activation_fun)

    # TRAINING

    X_train, X_test, y_train, y_test = train_test_split(
        inputs, outputs, test_size=0.30, random_state=random_state)

    errors = []

    init_time = time()

    print(f"Training epochs")
    for i in range(n_experiments):
        error_epoch = 0
        for k in range(len(X_train)):
            network.train(X_train[k], y_train[k], learning_rate=learning_rate)
            error_epoch += mean_squared_error(y_train[k], network.outputs)
        errors.append(error_epoch)

    end_time = time()
    print(f"Tiempo transcurrido entrenamiento: {end_time - init_time}\n\n")

    plt.plot(range(n_experiments), errors)
    plt.title(f"Error de red IRIS, act_fun={activation_fun.__name__} ,lr={learning_rate}, net_shape={net_shape}")
    plt.xlabel("Epochs")
    plt.ylabel("Error")
    if title == "":
        title = activation_fun.__name__ + str(net_shape).replace(", ", "") + str(learning_rate).replace(".",
                                                                                                        "") + ".jpg"
    plt.savefig(FOLDER_GRAPHS + title)
    if plot:
        plt.show()
    plt.close()
