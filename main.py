from fitness.bits_fitness import BitFitness
from population.population import Population
from reproduction.reproduction import Reproduction
from selection.selection import Selection



def main(N, mutation_rate):
    N = 5
    pop_size = N*10
    # mutation_rate = 0.1
    mutation_rate = 0.3
    opciones = [0, 1]
    # opciones = "qwertyuiopasdfghjklzxcvbnm"
    # opciones = "bvcasdqwert"

    p = Population(pop_size, opciones, N)
    f = BitFitness()  # TODO generalizar en función superior
    s = Selection()
    r = Reproduction(mutation_rate, opciones, pop_size)

    individuo = p.new_individual()
    # individuo = list("cabra")
    print("Original:", individuo)

    # inicializar población
    population = p.new_population()

    print("Población:", len(population))
    for pop in population:
        print(pop)

    # seleccionar poblacion
    fitness = f.fitness_population(individuo, population)
    print("Fitness:")
    print(fitness)

    while 5 not in fitness:  # TODO generalizar
        # seleccionar
        population = s.best_quartile(population, fitness)

        # reproduccion
        r.reproduce(population)

        # recalcular fitness
        fitness = f.fitness_population(individuo, population)
        print(fitness)

    print("Resultado")
    print(population[fitness.index(5)])


# a = [1, 2, 3, 4]
# b = ["a", "b", "c", "d"]
# s = crossover(a, b)
# print(s)
# mutacion(a, 0.1, b)
# print(a)


main()
