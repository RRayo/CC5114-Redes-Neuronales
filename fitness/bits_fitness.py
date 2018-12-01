import numpy as np

from fitness.fitness import Fitness


class BitFitness(Fitness):

    def evaluate_fitness(self, desired, real):
        return np.sum(np.array(desired) == np.array(real))

