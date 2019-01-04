import os
import re

import matplotlib.pyplot as plt
import numpy as np

from trees.tools import print_tree, eval_tree

FOLDER_GRAPHS = os.path.join(os.path.dirname(__file__), "results", "")


# ordenar poblacion por el fitness del arreglo
def sortPopulation(population, fitness_array):
    fitness_array = np.array(fitness_array)
    inds = fitness_array.argsort()
    sorted_pop = []
    for i in inds:
        sorted_pop.append(population[i])
    return sorted_pop


def graficar(rango, data, problema, xlabel, ylabel, tipo=1, mutation_rate=-1, pop_size=-1, ticks=False, save=True,
             plot=False):
    if tipo == 1:
        plt.plot(rango, data)
    elif tipo == 2:
        plt.scatter(rango, data)
    else:
        plt.bar(rango, data)
        if ticks:
            plt.xticks(rango, ticks)

    if mutation_rate > 0 and pop_size > 0:
        plt.title(f"Problema {problema}, mutation_rate={mutation_rate} ,pop_size={pop_size}")
    else:
        plt.title(f"{problema}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if mutation_rate > 0 and pop_size > 0:
        file_name = problema + str(mutation_rate).replace(".", "") + str(pop_size) + ".jpg"
    else:
        file_name = problema + ".jpg"
    file_name = re.sub("[\s_-]+", "", file_name)
    if save:
        plt.savefig(FOLDER_GRAPHS + file_name)
    if plot:
        plt.show()
    plt.close()


def write_trees(trees, title, dict_terminales={}):
    with open(FOLDER_GRAPHS + str(title) + ".txt", "w", encoding="utf-8") as file:
        for i in range(len(trees)):
            file.write(f"Gen:\t{(i + 1)}\n\n")
            valor = eval_tree(trees[i], dict_terminales)
            if dict_terminales:
                for k in dict_terminales.keys():
                    file.write(f"\tVariable:\t{k}\n")
                    file.write(f"\tValor:\t{dict_terminales[k]}\n")
                file.write(f"\tResultado:\t{valor}\n")
            else:
                file.write(f"\tResultado:\t{valor}\n")
            file.write(print_tree(trees[i], print_flag=False))
            file.write("\n\n\n")


def write_results(results_names, data, title):
    with open(FOLDER_GRAPHS + str(title) + ".txt", "w", encoding="utf-8") as file:
        for i in range(len(results_names)):
            file.write(results_names[i])
            file.write(" por experimento:\n")
            file.write(str(data[i]))
            file.write(f"\n\tPromedio:\t{(sum(data[i])/len(data[i]))}\n")
            file.write("\n\n")
