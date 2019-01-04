from random import randint

from population.population import Population
from trees.tools import create_rand_tree


class PopTrees(Population):

    def __init__(self, pop_size, genes, len_genes):
        Population.__init__(self, size=pop_size, genes=genes, len_genes=len_genes)

    def new_individual(self):
        tree_heigth = randint(2, self.len_genes)
        functions, terminals = self.genes
        return create_rand_tree(tree_heigth, functions, terminals)



