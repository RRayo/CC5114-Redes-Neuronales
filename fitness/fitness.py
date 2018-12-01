class Fitness:

    def evaluate_fitness(self, *args):
        raise NotImplementedError("Abstract fitness method")

    def fitness_population(self, *args):
        raise NotImplementedError("Abstract fitness method")