from random import *

import numpy as np


def randBinList(n, opciones):
    """
    Arreglo con n bits al azar
    :param n: número de bits en el arreglo
    :param opciones: arreglo con los posibles genes
    :return: Arreglo con bits
    """
    return np.array([opciones[randrange(len(opciones))] for _ in range(1, n + 1)])


def fitBits(desired, real):
    """
    Función de fitness para arreglos de bits
    :param desired: arreglo de bits deseado
    :param real: arreglo de bits por probar
    :return: numero de coincidencias entre los arreglos
    """
    return np.sum(desired == real)


def fitArray(fitFun, desired, real):
    """
    Array con el fitness de toda una población
    :param fitFun: función de fitness
    :param desired: arreglo de bits buscado
    :param real: población con arreglos de bits
    :return: arreglo con fitness de la poblacion
    """
    fit = []
    for i in range(len(desired)):
        fit.append(fitBits(desired[i], real))
    return np.array(fit)


# ordenar poblacion por el fitness del arreglo
def sortPopulation(population, fitness_array):
    population = np.array(population)
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    return population[inds].tolist()


# crear población inicial
def populationBits(size_pop, len_genes, opciones):
    population = []
    for _ in range(1, size_pop + 1):
        population.append(randBinList(len_genes, opciones))
    return np.array(population)


# cruzar 2 padres al azar
def crossover(padre1, padre2):
    r = randint(1, len(padre1) - 1)  # para que tenga al menos algo de cada padre
    cross = padre1[:r]
    cross = np.append(cross, padre2[r:])
    return cross.tolist()


# mutar al azar un individuo
def mutacion(individuo, mutation_rate, opciones):
    for i in range(len(individuo)):
        if random() < mutation_rate:
            individuo[i] = opciones[randrange(len(opciones))]


def main():
    N = 5
    pop_size = 5
    mutation_rate = 0.1
    opciones = [0, 1]

    bits = randBinList(N, opciones)
    print("Original:", bits)

    # inicializar población
    population = populationBits(pop_size, len(bits), opciones)

    print("Población:", len(population))
    for p in population:
        print(p)

    # seleccionar poblacion
    fitness = fitArray(fitBits, population, bits)
    print(fitness)
    population = sortPopulation(population, fitness)  # ordenar por fitness

    while 5 not in fitness:
        population = population[len(population) * 3 // 4:]  # obtener el 25% mejor  # TODO verificar

        # reproduccion
        actual_population = list(population)

        while len(population) < pop_size:
            padre1, padre2 = sample(actual_population, 2)
            hijo = crossover(padre1, padre2)
            mutacion(hijo, mutation_rate, opciones)
            population.append(hijo)  # TODO arreglar inconsistencias de listas y ndarray

        # recalcular fitness
        fitness = fitArray(fitBits, population, bits)
        population = sortPopulation(population, fitness)

    print("Resultado")
    print(population[-1])


# a = [1, 2, 3, 4]
# b = ["a", "b", "c", "d"]
# s = crossover(a, b)
# print(s)
# mutacion(a, 0.1, b)
# print(a)


main()
