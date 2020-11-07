import requests
import random
import math
import sys
import time
import numpy as np


#HIPERPARAMETROS
num_pop = int(sys.argv[1])#100
num_gen = int(sys.argv[2])#4 - 10
prob_t = float(sys.argv[3])#0.05
lambda_ = int(sys.argv[4])#10
cicles = int(sys.argv[5])#10

website = "http://163.117.164.219/age/robot4?"


#INICIALIZAR POBLACION
def initialize_population(num_pop, num_gen):
    population = np.random.uniform(-180,180,[num_pop, num_gen])
    population_variance = np.random.uniform(0,180,[num_pop, num_gen])
    return population.tolist(), population_variance.tolist()


#EVALUAR POBLACION
def evaluate_population(num_pop, num_gen, website, population):
    population_fitness = []
    for i in range(num_pop):
        evaluate = ""
        value = 0
        for j in range(num_gen):
            evaluate += "c" + str(j + 1) + "=" + str(population[i][j]) + "&"
        try:
            value = float(requests.get(website + evaluate).text)
        except:
            time.sleep(1)
            value = float(requests.get(website + evaluate).text)
        population_fitness.append(value)
    return population_fitness


#SELECCION
def tournament_population(num_pop, prob_t, lambda_, population, population_variance, population_fitness):
    population_selection = []
    population_selection_var = []

    t_size = math.floor(prob_t * num_pop)

    #TORNEO
    for i in range(lambda_*2):
        winner = i
        for j in range(t_size):
            if j == 0:
                winner = random.randint(0, num_pop- 1)
            else:
                candidate = random.randint(0, num_pop - 1)
                if population_fitness[candidate] < population_fitness[winner]:
                    winner = candidate
        population_selection.append(population[winner])
        population_selection_var.append(population_variance[winner])
    return population_selection, population_selection_var


#CRUCE
def cross_population(lambda_, num_gen, population_selection, population_selection_var):
    population_cross = []
    population_cross_var = []

    for i in range(int(lambda_/2)):

        father = population_selection[i*2]
        father_var = population_selection_var[i*2]

        mother = population_selection[i*2 + 1]
        mother_var = population_selection_var[i*2 + 1]

        son = []
        son_var = []

        for x in range(num_gen):
            son.append((father[x]+mother[x])/2)
            son_var.append(math.sqrt(father_var[x]+mother_var[x]))

        population_cross.append(son)
        population_cross_var.append(son_var)

    return population_cross, population_cross_var


#MUTACION
def mutate_population(lambda_, num_gen, population_cross, population_cross_var):
    population_mutated = []
    population_mutated_var = []

    for i in range(lambda_):
        mutated = []
        mutated_var = []
        for j in range(num_gen):
            mutated.append(population_cross[i][j] + np.random.normal(scale = population_cross_var[i][j]))
            mutated_var.append()

        population_mutated.append(mutated)
        population_mutated_var.append(mutated_var)

    return population_mutated, population_mutated_var




#MAIN
population, population_variance = initialize_population(num_pop, num_gen)
start = time.time()
best_ind = ""
best_fitness = 999999
for cicle in range(cicles):
    population_fitness = evaluate_population(num_pop, num_gen, website, population)
    if min(population_fitness) < best_fitness:
        best_ind = population[0]
        best_fitness = min(population_fitness)
        print(best_fitness)

    population_selection, population_selection_var = tournament_population(num_pop, prob_t, lambda_, population, population_variance, population_fitness)
    population_cross, population_cross_var = cross_population(lambda_, num_gen, population_selection, population_selection_var)
    population_mutated, population_mutated_var = mutate_population(lambda_, num_gen, population_cross, population_cross_var)

print((time.time() - start)/cicles)
print("Mejor ft = " + str(best_fitness))
