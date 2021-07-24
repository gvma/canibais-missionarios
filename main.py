# 3 canibais e 3 missionarios na mesma margem
import random
from random import seed
from random import *
from individual import Individual

population = []
newpopulation = []
score = 0

def selection(populacao,novapopulacao):
    qualquerLista = populacao + novapopulacao
    qualquerLista = sorted(qualquerLista, key=lambda ind: ind.score, reverse=True)
    selected_population = []
    for i in range(50):
        selected_population.append(qualquerLista[i])
    return selected_population

def mutacao(novaPopulacao):
    population_mutation = randint(1,5)

    for i in range(population_mutation):
        ind_index = randint(0,len(novaPopulacao)-1)
        individual = novaPopulacao[ind_index]
        pos_chromosomes = randint(0,10)
        print(individual)
        if individual.chromosomes[pos_chromosomes].config['people'] =="canibal":
            individual.chromosomes[pos_chromosomes].config['people'] = "missionario"
        else:
            individual.chromosomes[pos_chromosomes].config['people'] = "canibal"


def cruzamentoParte2(pai,mae,novaPopulacao):
    part1 = randint(1,10)
    individuo1 = Individual(pai.chromosomes[:part1] + mae.chromosomes[part1:])
    individuo2 = Individual(mae.chromosomes[:part1] + pai.chromosomes[part1:])
    novaPopulacao.append(individuo1)
    novaPopulacao.append(individuo2)

def cruzamentoParte1(populacao,novaPopulacao):
    population_cross_over = randint(10,len(populacao))
    for i in range(population_cross_over):
        x = randint(0,len(populacao)-1)
        y = randint(0,len(populacao)-1)
        while x == y:
            y = randint(0, len(populacao) - 1)
        pai = populacao[x]
        mae = populacao[y]
        cruzamentoParte2(pai,mae,novaPopulacao)
    return novaPopulacao

def get_right_margin_people(position,left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config):
  if config['people'][position] == "missionario":
    left_margin_missionaries += 1
    right_margin_missionaries -= 1
    return left_margin_missionaries, right_margin_missionaries
  elif config['people'][position] == "canibal":
    left_margin_canibals += 1
    right_margin_canibals -= 1
    return left_margin_canibals, right_margin_canibals

def get_left_margin_people(position,left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config):
  if config['people'][position] == "missionario":
    left_margin_missionaries -= 1
    right_margin_missionaries += 1
    return left_margin_missionaries, right_margin_missionaries
  elif config['people'][position] == "canibal":
    left_margin_canibals -= 1
    right_margin_canibals += 1
    return left_margin_canibals, right_margin_canibals

def validate(position,  left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config, score):
  if config['people'][position] == 'missionario':
    if left_margin_canibals > left_margin_missionaries and left_margin_missionaries != 0:
      score -= 1
    elif right_margin_canibals > right_margin_missionaries and right_margin_missionaries != 0:
      score -= 1
  else:
    if left_margin_canibals  > left_margin_missionaries and left_margin_missionaries != 0:
      score -= 1
    elif right_margin_canibals  > right_margin_missionaries and right_margin_missionaries != 0:
      score -= 1
  return score

def init_population():
  for i in range(50):
    individual = Individual()
    population.append(individual)
    print(individual)

def score(population):
  for i in range(len(population)):
    score = 11
    left_margin_canibals = 3
    left_margin_missionaries = 3
    right_margin_canibals = 0
    #print("Right margin " + str(right_margin_canibals))
    right_margin_missionaries = 0
    chromosomes = population[i].chromosomes

    for j in range(len(chromosomes)):
      config = chromosomes[j].config
      print(config)

      if j%2 == 0:
        if config['people'][0] == 'missionario':
          if left_margin_missionaries == 0:
              score -= 1
          else:
              left_margin_missionaries, right_margin_missionaries = get_left_margin_people(0,left_margin_canibals,
                                                                                       left_margin_missionaries,
                                                                                       right_margin_canibals,
                                                                                       right_margin_missionaries,
                                                                                       config)
        if config['people'][0] == 'canibal':
            if left_margin_canibals == 0:
                score -= 1
            else:
                left_margin_canibals, right_margin_canibals = get_left_margin_people(0,left_margin_canibals,
                                                                               left_margin_missionaries,
                                                                               right_margin_canibals,
                                                                               right_margin_missionaries,
                                                                               config)

      if j % 2 != 0:
        if config['people'][0] == 'missionario':
            if right_margin_missionaries == 0:
                score -= 1
            else:
                left_margin_missionaries, right_margin_missionaries = get_right_margin_people(0, left_margin_canibals,
                                                                                       left_margin_missionaries,
                                                                                       right_margin_canibals,
                                                                                       right_margin_missionaries,
                                                                                       config)
        if config['people'][0] == 'canibal':
            if right_margin_canibals == 0:
                score -= 1
            else:
                left_margin_canibals, right_margin_canibals = get_right_margin_people(0, left_margin_canibals,
                                                                               left_margin_missionaries,
                                                                               right_margin_canibals,
                                                                               right_margin_missionaries, config)

      if config['number_of_people'] == 2:
        if j % 2 == 0:
          if config['people'][0] == 'missionario':
              if left_margin_missionaries == 0:
                  score -= 1
              else:
                left_margin_missionaries, right_margin_missionaries = get_left_margin_people(0, left_margin_canibals,
                                                                                         left_margin_missionaries,
                                                                                         right_margin_canibals,
                                                                                         right_margin_missionaries,
                                                                                         config)
          if config['people'][0] == 'canibal':
              if left_margin_canibals == 0:
                  score -= 1
              else:
                left_margin_canibals, right_margin_canibals = get_left_margin_people(0, left_margin_canibals,
                                                                                 left_margin_missionaries,
                                                                                 right_margin_canibals,
                                                                                 right_margin_missionaries,
                                                                                 config)

        if j % 2 != 0:
          if config['people'][0] == 'missionario':
              if right_margin_missionaries != 0:
                  left_margin_missionaries, right_margin_missionaries = get_right_margin_people(0, left_margin_canibals,
                                                                                        left_margin_missionaries,
                                                                                        right_margin_canibals,
                                                                                        right_margin_missionaries,
                                                                                        config)
              else:
                    score -= 1

          if config['people'][0] == 'canibal':
              if right_margin_canibals == 0:
                  score -= 1
              else:
                left_margin_canibals, right_margin_canibals = get_right_margin_people(0, left_margin_canibals,
                                                                                  left_margin_missionaries,
                                                                                  right_margin_canibals,
                                                                                  right_margin_missionaries, config)

        score = validate(1, left_margin_canibals, left_margin_missionaries, right_margin_canibals,
                         right_margin_missionaries, config, score)
      else:
        score = validate(0, left_margin_canibals, left_margin_missionaries, right_margin_canibals,
                         right_margin_missionaries, config, score)
      print("SCORE " + str(score))
    population[i].score = score

init_population()

while True:
    flag = False
    score(population)
    for ind in population:
        if ind.score == 11:
            print(ind)
            flag = True
            break
    if flag:
        break
    newpopulation = cruzamentoParte1(population,[])
    mutacao(newpopulation)
    score(newpopulation)
    population = selection(population,newpopulation)