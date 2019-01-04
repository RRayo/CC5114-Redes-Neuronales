from fitness.trees_fit import TreesFit
from genetic_algorithm import GeneticAlgorithm
from population.pop_trees import PopTrees
from reproduction.reprod_trees import ReprodTrees
from selection.selection import Selection
from tools import graficar, write_trees, write_results


def main():  # TODO hacer clase/función que reciba los parámetros mutacion_rate, pop_size

    n_exp = 10

    # hiperparametros generales
    max_len_genes = 6  # maxima altura de los arboles
    pop_size = 500  # volumen de la poblacion
    mutation_rate = 0.1
    max_generations = 100

    # TREES - Problema Cifras y Letras
    print("TREES - Problema Cifras y Letras")

    funciones = ["+", "-", "*"]
    terminales = [19, 7, 3, 40]

    genes = (funciones, terminales)
    max_fit = 146

    fitness_max_best = []
    fitness_max_worst = []
    fitness_mean_best = []
    fitness_mean_worst = []
    best_trees_global = []
    worst_trees_global = []
    time_global = []
    generations_global = []

    for i in range(n_exp):
        ga_funcion = GeneticAlgorithm(max_len_genes, genes, pop_size, mutation_rate, max_fit)
        results_ga = ga_funcion.run(PopTrees, TreesFit, Selection, ReprodTrees, ref_individual=False,
                                    max_generations=max_generations)
        best_trees, fitness_max_history, fitness_mean_history, generations, time = results_ga

        if not fitness_max_best or len(fitness_max_best) > len(fitness_max_history):
            fitness_max_best = list(fitness_max_history)
            fitness_mean_best = list(fitness_max_history)
            best_trees_global = list(best_trees)

        if not fitness_max_worst or len(fitness_max_worst) < len(fitness_max_history):
            fitness_max_worst = list(fitness_max_history)
            fitness_mean_worst = list(fitness_max_history)
            worst_trees_global = list(best_trees)

        generations_global.append(generations)
        time_global.append(time)
        print(f"\texp {i} listo")

    write_trees(best_trees_global, "BestTreesCyL")
    write_trees(worst_trees_global, "WorstTreesCyL")
    write_results(["Tiempo", "Generaciones"], [time_global, generations_global], "ResultsCyL")

    graficar(range(len(fitness_max_best)), fitness_max_best, "Trees - Cifras y Letras (fitness_max_best)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_max_worst)), fitness_max_worst, "Trees - Cifras y Letras (fitness_max_worst)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)

    graficar(range(len(fitness_mean_best)), fitness_mean_best, "Trees - Cifras y Letras (fitness_mean_best)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_mean_worst)), fitness_mean_worst, "Trees - Cifras y Letras (fitness_mean_worst)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)

    print(f"Tiempo promedio:\t{sum(time_global)/len(time_global)}")
    print(f"Generaciones promedio:\t{sum(generations_global)/len(generations_global)}")
    print()

    # TREES - Problema Funcion
    print("TREES - Problema Funcion")

    funciones = ["+", "-", "*"]
    terminales = ["x"]

    genes = (funciones, terminales)

    funcion = lambda x: x**3 + x ** 2 + 2 * x

    rango_fitness = range(-10, 11)
    fitness_array = []
    for i in rango_fitness:
        d = {"x": i}
        value = funcion(i)
        fitness_array.append((d, value))

    fitness_max_best = []
    fitness_max_worst = []
    fitness_mean_best = []
    fitness_mean_worst = []
    best_trees_global = []
    worst_trees_global = []
    time_global = []
    generations_global = []

    for i in range(n_exp):
        ga_funcion = GeneticAlgorithm(max_len_genes, genes, pop_size, mutation_rate, fitness_array)
        results_ga_fun = ga_funcion.run(PopTrees, TreesFit, Selection, ReprodTrees, ref_individual=False,
                                        max_generations=max_generations)
        best_trees, fitness_max_history, fitness_mean_history, generations, time = results_ga_fun

        if not fitness_max_best or len(fitness_max_best) > len(fitness_max_history):
            fitness_max_best = list(fitness_max_history)
            fitness_mean_best = list(fitness_max_history)
            best_trees_global = list(best_trees)

        if not fitness_max_worst or len(fitness_max_worst) < len(fitness_max_history):
            fitness_max_worst = list(fitness_max_history)
            fitness_mean_worst = list(fitness_max_history)
            worst_trees_global = list(best_trees)

        generations_global.append(generations)
        time_global.append(time)
        print(f"\texp {i} listo")

    write_trees(best_trees_global, "BestTreesFuncion", fitness_array[-1][0])
    write_trees(worst_trees_global, "WorstTreesFuncion", fitness_array[-1][0])
    write_results(["Tiempo", "Generaciones"], [time_global, generations_global], "ResultsFuncion")

    graficar(range(len(fitness_max_best)), fitness_max_best, "Trees - Funcion (fitness_max_best)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_max_worst)), fitness_max_worst, "Trees - Funcion (fitness_max_worst)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)

    graficar(range(len(fitness_mean_best)), fitness_mean_best, "Trees - Funcion (fitness_mean_best)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)
    graficar(range(len(fitness_mean_worst)), fitness_mean_worst, "Trees - Funcion (fitness_mean_worst)\n",
             "Generaciones",
             "Max fitness", mutation_rate=mutation_rate, pop_size=pop_size, tipo=3)

    print(f"Tiempo promedio:\t{sum(time_global)/len(time_global)}")
    print(f"Generaciones promedio:\t{sum(generations_global)/len(generations_global)}")



main()
