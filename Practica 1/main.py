import requests
import random

num_pop = 10
num_gen = 64
population = []
website = "http://memento.evannai.inf.uc3m.es/age/test?c="

#INICIALIZAR POBLACION
for i in range(num_pop):
    chromosome = ""
    for j in range(num_gen):
        chromosome += str(random.randint(0, 1))
    population.append(chromosome)


#EVALUAR POBLACION
best_ch = ""
best_num_ch = -1
best_ft = 999999

for i in range(num_pop):
    r = requests.get(website + population[i])
    if float(r.text) < best_ft:
        best_ft = float(r.text)
        best_ch = population[i]
        best_num_ch = i


print(population)
print("Mejor CH " + str(best_num_ch) + " con ft: " + str(best_ft))
