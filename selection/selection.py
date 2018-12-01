from tools import sortPopulation


class Selection:

    def best_quartile(self, population, fitness):
        sorted_pop = sortPopulation(population, fitness)
        return sorted_pop[len(sorted_pop) * 3 // 4:]
