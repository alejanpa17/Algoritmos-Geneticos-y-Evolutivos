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
lambda_ = int(sys.argv[4])#40
num_fam = int(sys.argv[5])#2-5
cicles = int(sys.argv[6])#150

website = "http://163.117.164.219/age/robot4?"
#website = "http://163.117.164.219/age/robot6?"
#website = "http://163.117.164.219/age/robot10?"
#website = "http://163.117.164.219/age/robot10b?"




#INICIALIZAR POBLACION
def initialize_population(num_pop, num_gen):
    population = np.random.uniform(-180,180,[num_pop, num_gen])
    population_variance = np.random.uniform(140,200,[num_pop, num_gen])
    return population.tolist(), population_variance.tolist()


#EVALUAR POBLACION
def evaluate_population(num_pop, num_gen, lambda_, evaluations, website, population, population_fitness):

    evaluated = 0
    if len(population_fitness) > 0:
        evaluated = num_pop - lambda_

    for i in range(evaluated, num_pop):
        evaluate = ""
        value = 0
        for j in range(num_gen):
            evaluate += "c" + str(j + 1) + "=" + str(population[i][j]) + "&"
        try:
            value = abs(float(requests.get(website + evaluate).text))
        except:
            time.sleep(1)
            value = abs(float(requests.get(website + evaluate).text))
        evaluations += 1
        population_fitness.append(value)
    return population_fitness, evaluations


#SELECCION
def tournament_population(num_pop, prob_t, lambda_, num_fam, population, population_variance, population_fitness):
    population_selection = []
    population_selection_var = []

    t_size = math.floor(prob_t * num_pop)

    #TORNEO
    for i in range(lambda_*num_fam):
        winner = random.randint(0, num_pop- 1)
        for j in range(t_size - 1):
            candidate = random.randint(0, num_pop - 1)
            if population_fitness[candidate] < population_fitness[winner]:
                winner = candidate
        population_selection.append(population[winner])
        population_selection_var.append(population_variance[winner])

    return population_selection, population_selection_var


#CRUCE
def cross_population(lambda_, num_gen, num_fam, population_selection, population_selection_var):
    population_cross = []
    population_cross_var = []

    for i in range(lambda_):

        family = []
        family_var = []

        for j in range(num_fam):
            family.append(population_selection[i*num_fam + j])
            family_var.append(population_selection_var[i*num_fam + j])

        family_var = np.rot90(np.array(family_var), k = 3)

        son = np.mean(family, axis=0).tolist()
        son_var = []

        for j in range(num_gen):
            son_var.append(random.choice(family_var[j]))

        population_cross.append(son)
        population_cross_var.append(son_var)

    return population_cross, population_cross_var


#MUTACION
def mutate_population(lambda_, num_gen, population_cross, population_cross_var):
    population_mutated = []
    population_mutated_var = []
    b = 1

    for i in range(lambda_):
        mutated = []
        mutated_var = []
        for j in range(num_gen):
            mutated.append(population_cross[i][j] + np.random.normal(scale = population_cross_var[i][j]))
            tau = b/math.sqrt(2 * math.sqrt(num_gen))
            tau0 = b/math.sqrt(2 * num_gen)
            mutated_var.append(population_cross_var[i][j]*math.exp(np.random.normal(scale = tau0))*math.exp(np.random.normal(scale = tau)))

        population_mutated.append(mutated)
        population_mutated_var.append(mutated_var)

    return population_mutated, population_mutated_var


#UNION DE POBLACIONES
def merge_populations(lambda_, population, population_variance, population_fitness, population_mutated, population_mutated_var):

    for i in range(lambda_):
        index = population_fitness.index(max(population_fitness))
        population.pop(index)
        population_variance.pop(index)
        population_fitness.pop(index)

    return population + population_mutated, population_variance + population_mutated_var



#MAIN
population, population_variance = initialize_population(num_pop, num_gen)
start = time.time()
evaluations = 0
population_fitness = []

for cicle in range(cicles):
    population_fitness, evaluations = evaluate_population(num_pop, num_gen, lambda_, evaluations, website, population, population_fitness)
    print(min(population_fitness))
    if min(population_fitness) == 0:
        break
    population_selection, population_selection_var = tournament_population(num_pop, prob_t, lambda_, num_fam, population, population_variance, population_fitness)
    population_cross, population_cross_var = cross_population(lambda_, num_gen, num_fam, population_selection, population_selection_var)
    population_mutated, population_mutated_var = mutate_population(lambda_, num_gen, population_cross, population_cross_var)
    population, population_variance = merge_populations(lambda_, population, population_variance, population_fitness, population_mutated, population_mutated_var)

print("Tiempo de ejecucion = " + str((time.time() - start)))
print("Numero de evaluaciones = " + str(evaluations))
print("Mejor ft = " + str(min(population_fitness)))
print("Mejor individuo " + str(population[population_fitness.index(min(population_fitness))]))
print("Mejor individuo (varianzas) " + str(population_variance[population_fitness.index(min(population_fitness))]))
