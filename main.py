from fitness.bits_fitness import BitFitness
from fitness.nqueens_fit import NQueensFit
from genetic_algorithm import GeneticAlgorithm
from population.pop_nqueens import PopNQueens
from population.population import Population
from reproduction.reproduction import Reproduction
from selection.selection import Selection

from tools import graficar


def main():  # TODO hacer clase/función que reciba los parámetros mutacion_rate, pop_size
    # BITS
    print("BITS")

    len_genes = 5
    genes = [0, 1]
    pop_size = len_genes * 2
    mutation_rate = 0.1
    max_fit = 5  # todos son iguales al individuo original
    ga_bits = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_bits.run(Population, BitFitness, Selection,
                                                                           Reproduction, ref_individual=True)
    graficar(range(len(fitness_max_history)), fitness_max_history, "BITS (max_fit)", "Generaciones", "Max fitness",
             mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_mean_history)), fitness_mean_history, "BITS (mean_fit)", "Generaciones", "Mean fitness",
             mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    print("Generaciones: ", counter)
    print("Tiempo: ", time)

    # STRING
    print("\nSTRING")

    len_genes = 5
    genes = list("qwertyuiopasdfghjklzxcvbnm")
    pop_size = len_genes * 10
    mutation_rate = 0.1
    max_fit = 5  # todos son iguales al individuo original
    ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_string.run(Population, BitFitness, Selection,
                                                                             Reproduction, ref_individual=True)

    graficar(range(len(fitness_max_history)), fitness_max_history, "STRING (max_fit)", "Generaciones", "Max fitness",
             mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_mean_history)), fitness_mean_history, "STRING (mean_fit)", "Generaciones",
             "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    print("Generaciones: ", counter)
    print("Tiempo: ", time)

    # N-Queens
    print("\n--------------------------------------------")
    print("\nN-Queens")

    len_genes = 8
    genes = [i for i in range(len_genes)]

    pop_array = [len_genes * x for x in [2, 5, 10, 20]]
    mutation_array = [0.05, 0.1, 0.3, 0.5]

    time_pop = []
    time_mutation = []
    generations_pop = []
    generations_mutation = []

    for i in range(len(pop_array)):
        pop_size = pop_array[i]
        print("Pop size: ", pop_size)

        mutation_rate = 0.1
        max_fit = 1.0  # minimo numero de errores
        ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
        fitness_max_history, fitness_mean_history, counter, time = ga_string.run(PopNQueens, NQueensFit, Selection,
                                                                                 Reproduction, ref_individual=False)

        graficar(range(len(fitness_max_history)), fitness_max_history, f"N-Queens {len_genes} (max_fit)",
                 "Generaciones", "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
        graficar(range(len(fitness_mean_history)), fitness_mean_history, f"N-Queens {len_genes} (mean_fit)",
                 "Generaciones", "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
        print("Generaciones: ", counter)
        print("Tiempo: ", time)
        print()
        time_pop.append(time)
        generations_pop.append(counter)

    for i in range(len(mutation_array)):
        mutation_rate = mutation_array[i]
        print("mutation_rate: ", mutation_rate)

        pop_size = len_genes * 10
        max_fit = 1.0  # minimo numero de errores
        ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
        fitness_max_history, fitness_mean_history, counter, time = ga_string.run(PopNQueens, NQueensFit, Selection,
                                                                                 Reproduction, ref_individual=False)

        graficar(range(len(fitness_max_history)), fitness_max_history, f"N-Queens {len_genes} (max_fit)",
                 "Generaciones", "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
        graficar(range(len(fitness_mean_history)), fitness_mean_history, f"N-Queens {len_genes} (mean_fit)",
                 "Generaciones", "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
        print("Generaciones: ", counter)
        print("Tiempo: ", time)
        print()
        time_mutation.append(time)
        generations_mutation.append(counter)

    graficar(range(len(time_pop)), time_pop, "Tiempo poblaciones", xlabel="Poblaciones", ylabel="Tiempo", tipo=3,
             ticks=pop_array)
    graficar(range(len(time_mutation)), time_mutation, "Tiempo mutations_rates", xlabel="Mutation rates",
             ylabel="Tiempo", tipo=3, ticks=mutation_array)

    graficar(range(len(generations_pop)), generations_pop, "Generaciones poblaciones", xlabel="Poblaciones",
             ylabel="Generaciones", tipo=3, ticks=pop_array)
    graficar(range(len(generations_mutation)), generations_mutation, "Generaciones mutations_rates",
             xlabel="Mutation rates", ylabel="Generaciones", tipo=3, ticks=mutation_array)


main()
