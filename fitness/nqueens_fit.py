import numpy as np

from fitness import Fitness


class NQueensFit(Fitness):

    def evaluate_fitness(self, individual):
        error = 1
        _, counts_elements = np.unique(individual, return_counts=True)
        for c in counts_elements:
            error += c - 1  # no contar primera aparicion
        for i in range(len(individual)-1):
            for j in range(i+1, len(individual)):
                if abs(individual[i] - individual[j]) == abs(i - j):
                    error += 1
        return 1 / error

    def fitness_population(self, population):
        fit = []
        for i in range(len(population)):
            fit.append(self.evaluate_fitness(population[i]))
        return fit


from pop_nqueens import PopNQueens

p = PopNQueens(4, 4)
ind = p.new_individual()
print(ind)

f = NQueensFit()
fit = f.evaluate_fitness(ind)
print(fit)
fit = f.evaluate_fitness([1,2,3,1])
print(fit)