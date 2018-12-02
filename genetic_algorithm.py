from time import time

import numpy as np


class GeneticAlgorithm:

    def __init__(self, len_genes, genes, population_size, mutation_rate, max_fitness):
        self.len_genes = len_genes
        self.genes = genes
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_fitness = max_fitness

    def run(self, population_class, fitness_class, selection_class, reproduction_class, ref_individual=False):
        init_time = time()
        fitness_max_history = []
        fitness_mean_history = []

        p = population_class(self.population_size, self.genes, self.len_genes)
        f = fitness_class(self.max_fitness)
        s = selection_class()
        r = reproduction_class(self.mutation_rate, self.genes, self.population_size)

        individual = None
        if ref_individual:
            individual = p.new_individual()

        population = p.new_population()

        if ref_individual:
            fitness = f.fitness_population(individual, population)
        else:
            fitness = f.fitness_population(population)

        fitness_max_history.append(np.max(fitness))
        fitness_mean_history.append(np.mean(fitness))

        counter = 1
        while f.max_fitness not in fitness and counter < 200:
            population = s.best_quartile(population, fitness)
            r.reproduce(population)
            if ref_individual:
                fitness = f.fitness_population(individual, population)
            else:
                fitness = f.fitness_population(population)

            counter += 1

            fitness_max_history.append(np.max(fitness))
            fitness_mean_history.append(np.mean(fitness))

        return fitness_max_history, fitness_mean_history, counter, time() - init_time
