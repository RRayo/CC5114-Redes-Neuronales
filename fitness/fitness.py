class Fitness:

    def __init__(self, max_fitness):
        self.max_fitness = max_fitness

    def evaluate_fitness(self, *args):
        raise NotImplementedError("Abstract fitness method")

    def fitness_population(self, *args):
        raise NotImplementedError("Abstract fitness method")