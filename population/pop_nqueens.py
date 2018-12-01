from random import randint

from population.population import Population


class PopNQueens(Population):

    def __init__(self, pop_size, genes, len_genes):
        Population.__init__(self, size=pop_size, genes=[], len_genes=len_genes)

    def new_individual(self):
        individual = []
        for i in range(self.len_genes):
            r = randint(0, self.len_genes - 1)
            while r in individual:
                r = randint(0, self.len_genes - 1)
            individual.append(r)
        return individual


# p = PopNQueens(100, 6)
# ind = p.new_individual()
# pop = p.new_population()
#
# print(ind)
# print(pop)
