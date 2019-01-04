from random import sample, randint, randrange, random

import numpy as np


class Reproduction:

    def __init__(self, mutation_rate, genes, population_size):
        self.mutation_rate = mutation_rate
        self.genes = genes
        self.population_size = population_size

    def reproduce(self, population):
        actual_population = list(population)

        while len(population) < self.population_size:
            padre1, padre2 = sample(actual_population, 2)
            hijo = self.crossover(padre1, padre2)
            self.mutacion(hijo, self.mutation_rate, self.genes)
            population.append(hijo)

    # cruzar 2 padres al azar
    def crossover(self, padre1, padre2):
        r = randint(1, len(padre1) - 1)  # para que tenga al menos algo de cada padre
        cross = padre1[:r]
        cross = np.append(cross, padre2[r:])
        return cross.tolist()

    # mutar al azar un individuo
    def mutacion(self, individuo, mutation_rate, opciones):
        for i in range(len(individuo)):
            if random() < mutation_rate:
                individuo[i] = opciones[randrange(len(opciones))]
