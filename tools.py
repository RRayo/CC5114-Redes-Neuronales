import numpy as np
import matplotlib.pyplot as plt


# ordenar poblacion por el fitness del arreglo
def sortPopulation(population, fitness_array):
    population = np.array(population)
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    return population[inds].tolist()


def graficar(rango, data, problema, xlabel, ylabel, mutation_rate=-1, pop_size=-1, plot=False):
    plt.plot(rango, data)
    plt.title(f"Problema {problema}, mutation_rate={mutation_rate} ,pop_size={pop_size}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    file_name = problema + str(mutation_rate).replace(".", "") + str(pop_size) + ".jpg"
    plt.savefig(FOLDER_GRAPHS + file_name)
    if plot:
        plt.show()
    plt.close()

