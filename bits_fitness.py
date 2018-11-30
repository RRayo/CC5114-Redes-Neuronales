import numpy as np

from fitness import Fitness


class BitFitness(Fitness):

    def evaluate_fitness(self, desired, real):
        return np.sum(np.array(desired) == np.array(real))

    def fitness_population(self, desired, population):
        fit = []
        for i in range(len(population)):
            fit.append(self.evaluate_fitness(desired, population[i]))
        return fit