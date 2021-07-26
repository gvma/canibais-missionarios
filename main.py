# 3 canibais e 3 missionarios na mesma margem
from chromosome import Chromosome
from random import seed
from random import *
from individual import Individual
from datetime import datetime

population = []
newpopulation = []
score = 0

seed(10)

def selection():
    qualquerLista = population + newpopulation
    qualquerLista = sorted(qualquerLista, key=lambda ind: ind.score, reverse=True)
    selected_population = []
    for i in range(50):
        selected_population.append(qualquerLista[i])
    return selected_population

def mutacao():
    population_mutation = 5
    for i in range(population_mutation):
      if len(newpopulation) != 0:
        ind_index = randint(0,len(newpopulation)-1)
        individual = newpopulation[ind_index]
        pos_chromosomes = 5
        if individual.chromosomes[pos_chromosomes].config['people'][0] =="canibal":
            individual.chromosomes[pos_chromosomes].config['people'][0] = "missionario"
        else:
            individual.chromosomes[pos_chromosomes].config['people'][0] = "canibal"


def cruzamentoParte2(pai,mae):
    part1 = randint(1,10)
    individuo1 = Individual(pai.chromosomes[:part1] + mae.chromosomes[part1:])
    individuo2 = Individual(mae.chromosomes[:part1] + pai.chromosomes[part1:])
    newpopulation.append(individuo1)
    newpopulation.append(individuo2)

def cruzamentoParte1():
    for i in range(len(population)):
        for j in range(len(population)):
            porcentagem = randint(0,100)
            if porcentagem >= 60 and i != j:
                pai = population[i]
                mae = population[j]
                cruzamentoParte2(pai,mae)

def validate(left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, score):
    if left_margin_canibals > left_margin_missionaries and left_margin_missionaries != 0:
        return 2
    elif right_margin_canibals > right_margin_missionaries and right_margin_missionaries != 0:
        return 2
    return score

def init_population():
  for i in range(50):
    individual = Individual()
    population.append(individual)

def score(population):
  for i in range(len(population)):
    score = 3
    left_margin_canibals = 3
    left_margin_missionaries = 3
    right_margin_canibals = 0
    right_margin_missionaries = 0
    chromosomes = population[i].chromosomes
    impossible = False
    for j in range(len(chromosomes)):
      config = chromosomes[j].config
      if impossible or score == 1:
        population[i].score = score
        # print('Configuracao impossivel')
        break
      # print(config)
      if j % 2 == 0:
        if config['people'][0] == 'missionario':
          if left_margin_missionaries == 0:
            score = 1
            impossible = True
          else:
            right_margin_missionaries += 1
            left_margin_missionaries -= 1
        else:
          if left_margin_canibals == 0:
            score = 1
            impossible = True
          else:
            right_margin_canibals += 1
            left_margin_canibals -= 1
        if config['number_of_people'] == 2:
          if config['people'][1] == 'missionario':
            if left_margin_missionaries == 0:
              score = 1
              impossible = True
            else:
              right_margin_missionaries += 1
              left_margin_missionaries -= 1
          else:
            if left_margin_canibals == 0:
              score = 1
              impossible = True
            else:
              right_margin_canibals += 1
              left_margin_canibals -= 1
      else:
        if config['people'][0] == 'missionario':
          if right_margin_missionaries == 0:
            score = 1
            impossible = True
          else:
            right_margin_missionaries -= 1
            left_margin_missionaries += 1
        else:
          if right_margin_canibals == 0:
            score = 1
            impossible = True
          else:
            right_margin_canibals -= 1
            left_margin_canibals += 1
        if config['number_of_people'] == 2:
          if config['people'][1] == 'missionario':
            if right_margin_missionaries == 0:
              score = 1
              impossible = True
            else:
              right_margin_missionaries -= 1
              left_margin_missionaries += 1
          else:
            if right_margin_canibals == 0:
              score = 1
              impossible = True
            else:
              right_margin_canibals -= 1
              left_margin_canibals += 1

      if score != 1:
        score = validate(left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, score)
    population[i].score = score
    if score == 3 and left_margin_canibals != 0 and left_margin_missionaries != 0:
      population[i].score = 1
    # print(config)
    print(left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, score)


init_population()

# chromosomes = []
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('canibal')
# cfg['people'].append('missionario')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 1
# cfg['people'].append('missionario')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('canibal')
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 1
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('missionario')
# cfg['people'].append('missionario')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('canibal')
# cfg['people'].append('missionario')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('missionario')
# cfg['people'].append('missionario')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 1
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 2
# cfg['people'].append('canibal')
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 1
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# cfg = {
#   'people': []
# }
# cfg['number_of_people'] = 1
# cfg['people'].append('canibal')
# cfg['people'].append('canibal')
# chromosomes.append(Chromosome(cfg))
# population.append(Individual(chromosomes))

b = 0
while True:
    flag = False
    score(population)
    for ind in population:
        for ind in population:
            if ind.score == 3:
                print(ind)
                print(ind.score)
                flag = True
                break
    if flag:
        break
    cruzamentoParte1()
    # for ind in newpopulation:
    mutacao()
    score(newpopulation)
    population = selection()
    newpopulation.clear()
    b += 1