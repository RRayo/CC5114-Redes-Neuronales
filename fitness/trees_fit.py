from fitness.fitness import Fitness
from trees.tools import eval_tree, print_tree


class TreesFit(Fitness):

    def evaluate_fitness(self, individual):

        error = 1

        if type(self.max_fitness) == int:
            tree_value = eval_tree(individual)
            error += abs(tree_value - self.max_fitness)

        elif type(self.max_fitness) == list:
            for terminal_dict, expected_val in self.max_fitness:
                tree_value = eval_tree(individual, dict_terminals=terminal_dict)
                error += abs(tree_value - expected_val)
            if error != 1:
                error /= len(self.max_fitness)
        else:
            raise Exception("Tipo erroneo de max_fitness: " + str(type(self.max_fitness)))

        return 1 / error

    def fitness_population(self, population):
        fit = []
        for i in range(len(population)):
            fit.append(self.evaluate_fitness(population[i]))
        return fit
