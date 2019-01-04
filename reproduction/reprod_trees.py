from random import sample, randint, randrange, random, choice

import numpy as np

from reproduction.reproduction import Reproduction
from trees.tools import cross_tree, create_rand_tree, print_tree


class ReprodTrees(Reproduction):

    def __init__(self, mutation_rate, genes, population_size):
        Reproduction.__init__(self, mutation_rate=mutation_rate, genes=genes, population_size=population_size)

    # cruzar 2 padres al azar
    def crossover(self, padre1, padre2, prob_cross=0.9):
        if random() < prob_cross:
            min_size = min(len(padre1), len(padre2))
            r = randint(1, min_size - 1)  # para que tenga al menos algo de cada padre
            functions, terminals = self.genes
            cross = cross_tree(padre1, padre2, r, functions, terminals)
            return cross
        else:
            return choice([padre1, padre2])

    # mutar al azar un individuo
    def mutacion(self, individuo, mutation_rate, opciones):
        if random() < mutation_rate:
            functions, terminals = opciones
            rand_tree = create_rand_tree(0, functions, terminals, size=len(individuo))
            self.crossover(individuo, rand_tree, prob_cross=1)
