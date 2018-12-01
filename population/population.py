from random import randrange

import numpy as np


class Population:

    def __init__(self, size, genes, len_genes):
        self.size = size
        self.genes = genes
        self.len_genes = len_genes

    def new_individual(self):
        return [self.genes[randrange(len(self.genes))] for _ in range(1, self.len_genes + 1)]

    def new_population(self):
        population = []
        for _ in range(1, self.size + 1):
            population.append(self.new_individual())
        return population


