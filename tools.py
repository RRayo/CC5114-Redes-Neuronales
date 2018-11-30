import numpy as np


# ordenar poblacion por el fitness del arreglo
def sortPopulation(population, fitness_array):
    population = np.array(population)
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    return population[inds].tolist()


