from random import *

import numpy as np


def randBinList(n):
    return np.array([randint(0, 1) for _ in range(1, n + 1)])


def fitBits(desired, real):
    return np.sum(desired == real)


def fitArray(fitFun, desired, real):
    fit = []
    for i in range(len(desired)):
        fit.append(fitBits(desired[i], real))
    return np.array(fit)


def sortPopulation(population, fitness_array):
    population = np.array(population)
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    return population[inds].tolist()


def populationBits(size_pop, len_genes):
    population = []
    for _ in range(1, size_pop + 1):
        population.append(randBinList(len_genes))
    return np.array(population)


def crossover(padre1, padre2):
    r = randint(1, len(padre1) - 2)  # para que tenga al menos algo de cada padre
    cross = padre1[:r]
    cross = np.append(cross, padre2[r:])
    return cross


def mutacion(individuo, mutation_rate, opciones):
    for i in range(len(individuo)):
        if random() < mutation_rate:
            individuo[i] = opciones[randrange(len(opciones))]


def main():
    N = 5
    pop_size = 5
    bits = randBinList(N)
    print("Original:", bits)

    # inicializar población
    population = populationBits(pop_size, len(bits))

    print("Población:", len(population))
    for p in population:
        print(p)

    # seleccionar poblacion
    fitness = fitArray(fitBits, population, bits)
    print(fitness)
    population = sortPopulation(population, fitness)  # ordenar por fitness

    while 5 not in fitness:
        print("a")
        population = population[len(population) * 3 // 4:]  # obtener el 25% mejor  # TODO verificar

        # reproduccion
        actual_population = list(population)

        mutation_rate = 0.1
        opciones = [0, 1]

        while len(population) < pop_size:
            padre1, padre2 = sample(actual_population, 2)
            hijo = crossover(padre1, padre2)
            mutacion(hijo, mutation_rate, opciones)
            population.extend(hijo)  # TODO arreglar inconsistencias de listas y ndarray

        # recalcular fitness
        fitness = fitArray(fitBits, population, bits)
        population = sortPopulation(population, fitness)

    print("Resultado")
    print(population[-1])


main()
