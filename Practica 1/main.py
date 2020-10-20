import requests
import random
import math

num_pop = 500
num_gen = 64
prob_t = 0.05
prob_m = 0.02
cicles = 10
website = "http://memento.evannai.inf.uc3m.es/age/test?c="


#INICIALIZAR POBLACION
population = []
for i in range(num_pop):
    chromosome = ""
    for j in range(num_gen):
        chromosome += str(random.randint(0, 1))
    population.append(chromosome)

for cicle in range(cicles):

    #EVALUAR POBLACION
    population_fitness = []
    for i in range(num_pop):
        population_fitness.append(float(requests.get(website + population[i]).text))
    print("Mejor CH " + str(population_fitness.index(min(population_fitness))) + " con ft: " + str(min(population_fitness)))


    #SELECCIONAR LOS MEJORES
    population_selection = []
    t_size = math.floor(prob_t * num_pop)

    for i in range(num_pop):
        winner = i
        for j in range(t_size):
            if j == 0:
                winner = random.randint(0, num_pop - 1)
            else:
                candidate = random.randint(0, num_pop - 1)
                if population_fitness[candidate] < population_fitness[winner]:
                    winner = candidate
        population_selection.append(population[winner])


    #CRUCE
    population_cross = []

    if num_pop%2 == 1:   #Poblaciones impares
        population_cross.append(population_selection[num_pop - 1])

    for i in range(int(num_pop/2)):
        father = population_selection[i*2]
        mother = population_selection[i*2 + 1]
        son_1 = ""
        son_2 = ""

        for x in range(num_gen):    #Hijo 1
            if random.randint(0, 1) == 0:
                son_1 += father[x]
            else:
                son_1 += mother[x]

        for x in range(num_gen):    #Hijo 2
            if random.randint(0, 1) == 0:
                son_2 += father[x]
            else:
                son_2 += mother[x]

        population_cross.append(son_1)
        population_cross.append(son_2)


    #MUTACION
    population_mutated = []
    for i in range(num_pop):
        chromosome = ""
        for j in range(num_gen):
            if random.random() < prob_m:
                if population_cross[i][j] == '0':
                    chromosome += '1'
                else:
                    chromosome += '0'
            else:
                chromosome += population_cross[i][j]
        population_mutated.append(chromosome)

    population = population_mutated
