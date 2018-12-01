import os
import re

import matplotlib.pyplot as plt
import numpy as np

FOLDER_GRAPHS = os.path.join(os.path.dirname(__file__), "results", "")


# ordenar poblacion por el fitness del arreglo
def sortPopulation(population, fitness_array):
    population = np.array(population)
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    return population[inds].tolist()


def graficar(rango, data, problema, xlabel, ylabel, tipo=1, mutation_rate=-1, pop_size=-1, ticks=False, plot=False):
    if tipo == 1:
        plt.plot(rango, data)
    elif tipo == 2:
        plt.scatter(rango, data)
    else:
        plt.bar(rango, data)
        if ticks:
            plt.xticks(rango, ticks)

    if mutation_rate > 0 and pop_size > 0:
        plt.title(f"Problema {problema}, mutation_rate={mutation_rate} ,pop_size={pop_size}")
    else:
        plt.title(f"{problema}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if mutation_rate > 0 and pop_size > 0:
        file_name = problema + str(mutation_rate).replace(".", "") + str(pop_size) + ".jpg"
    else:
        file_name = problema + ".jpg"
    file_name = re.sub("[\s_-]+", "", file_name)
    plt.savefig(FOLDER_GRAPHS + file_name)
    if plot:
        plt.show()
    plt.close()
