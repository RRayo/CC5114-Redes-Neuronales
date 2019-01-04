from fitness.bits_fitness import BitFitness
from fitness.trees_fit import TreesFit
from genetic_algorithm import GeneticAlgorithm
from population.pop_trees import PopTrees
from population.population import Population
from reproduction.reprod_trees import ReprodTrees
from reproduction.reproduction import Reproduction
from selection.selection import Selection
from tools import graficar


def main():  # TODO hacer clase/función que reciba los parámetros mutacion_rate, pop_size
    # TREES - Problema Cifras y Letras
    print("TREES - Problema Cifras y Letras")

    max_len_genes = 6  # maxima altura de los arboles
    pop_size = 500  # volumen de la poblacion
    mutation_rate = 0.1

    funciones = ["+", "-", "*"]
    terminales = [19, 7, 3, 40]

    genes = (funciones, terminales)
    max_fit = 147

    ga_cifras_letras = GeneticAlgorithm(max_len_genes, genes, pop_size, mutation_rate, max_fit)
    fitness_max_history, fitness_mean_history, counter, time = ga_cifras_letras.run(PopTrees, TreesFit, Selection,
                                                                                    ReprodTrees, ref_individual=False)
    graficar(range(len(fitness_max_history)), fitness_max_history, "Trees - Cifras y Letras (max_fit)\n", "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_mean_history)), fitness_mean_history, "Trees - Cifras y Letras (mean_fit)\n",
             "Generaciones", "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    print("Generaciones: ", counter)
    print("Tiempo: ", time)

    return
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
    #
    # # N-Queens
    # print("\n--------------------------------------------")
    # print("\nN-Queens")
    #
    # len_genes = 8
    # genes = [i for i in range(len_genes)]
    #
    # pop_array = [len_genes * x for x in [2, 5, 10, 20]]
    # mutation_array = [0.05, 0.1, 0.3, 0.5]
    #
    # time_pop_global = []
    # time_mutation_global = []
    # generations_pop_global = []
    # generations_mutation_global = []
    #
    # n_exp = 10
    #
    # for x in range(n_exp):
    #
    #     time_pop = []
    #     time_mutation = []
    #     generations_pop = []
    #     generations_mutation = []
    #
    #     print("Experimento", x)
    #
    #     for i in range(len(pop_array)):
    #         pop_size = pop_array[i]
    #         # print("Pop size: ", pop_size)
    #
    #         mutation_rate = 0.1
    #         max_fit = 1.0  # minimo numero de errores
    #         ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    #         fitness_max_history, fitness_mean_history, counter, time = ga_string.run(PopNQueens, NQueensFit, Selection,
    #                                                                                  Reproduction, ref_individual=False)
    #
    #         # graficar(range(len(fitness_max_history)), fitness_max_history, f"N-Queens {len_genes} (max_fit)",
    #         #          "Generaciones", "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    #         # graficar(range(len(fitness_mean_history)), fitness_mean_history, f"N-Queens {len_genes} (mean_fit)",
    #         #          "Generaciones", "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    #         # print("Generaciones: ", counter)
    #         # print("Tiempo: ", time)
    #         # print()
    #         time_pop.append(time)
    #         generations_pop.append(counter)
    #
    #     for i in range(len(mutation_array)):
    #         mutation_rate = mutation_array[i]
    #         # print("mutation_rate: ", mutation_rate)
    #
    #         pop_size = len_genes * 10
    #         max_fit = 1.0  # minimo numero de errores
    #         ga_string = GeneticAlgorithm(len_genes, genes, pop_size, mutation_rate, max_fit)
    #         fitness_max_history, fitness_mean_history, counter, time = ga_string.run(PopNQueens, NQueensFit, Selection,
    #                                                                                  Reproduction, ref_individual=False)
    #
    #         # graficar(range(len(fitness_max_history)), fitness_max_history, f"N-Queens {len_genes} (max_fit)",
    #         #          "Generaciones", "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    #         # graficar(range(len(fitness_mean_history)), fitness_mean_history, f"N-Queens {len_genes} (mean_fit)",
    #         #          "Generaciones", "Mean fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    #         # print("Generaciones: ", counter)
    #         # print("Tiempo: ", time)
    #         # print()
    #         time_mutation.append(time)
    #         generations_mutation.append(counter)
    #
    #     time_pop_global.append(time_pop)
    #     time_mutation_global.append(time_mutation)
    #     generations_pop_global.append(generations_pop)
    #     generations_mutation_global.append(generations_mutation)
    #
    # time_pop_global = np.sum(np.array(time_pop_global), axis=0)/n_exp
    # time_mutation_global = np.sum(np.array(time_mutation_global), axis=0)/n_exp
    # generations_pop_global = np.sum(np.array(generations_pop_global), axis=0)/n_exp
    # generations_mutation_global = np.sum(np.array(generations_mutation_global), axis=0)/n_exp
    #
    # graficar(range(len(time_pop_global)), time_pop_global, "Tiempo poblaciones", xlabel="Poblaciones", ylabel="Tiempo",
    #          tipo=3,
    #          ticks=pop_array)
    # graficar(range(len(time_mutation_global)), time_mutation_global, "Tiempo mutations_rates", xlabel="Mutation rates",
    #          ylabel="Tiempo", tipo=3, ticks=mutation_array)
    #
    # graficar(range(len(generations_pop_global)), generations_pop_global, "Generaciones poblaciones",
    #          xlabel="Poblaciones",
    #          ylabel="Generaciones", tipo=3, ticks=pop_array)
    # graficar(range(len(generations_mutation_global)), generations_mutation_global, "Generaciones mutations_rates",
    #          xlabel="Mutation rates", ylabel="Generaciones", tipo=3, ticks=mutation_array)


main()
