# 3 canibais e 3 missionarios na mesma margem
from random import seed
from random import *
from individual import Individual

population = []
newpopulation = []
score = 0

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
        ind_index = randint(0,len(newpopulation)-1)
        print("IND INDEX " + str(ind_index) + "TAMANHO " + str(ind_index))
        individual = newpopulation[ind_index]
        pos_chromosomes = 5
        #print(individual.chromosomes[pos_chromosomes].config['people'])
        if individual.chromosomes[pos_chromosomes].config['people'][0] =="canibal":
           # print("ENTREI AQUI CANIBAL ~~~~~~~~~~~~~~~~~~~~")
            individual.chromosomes[pos_chromosomes].config['people'][0] = "missionario"
        else:
            individual.chromosomes[pos_chromosomes].config['people'][0] = "canibal"
            #print("ENTREI AQUI MISSIONARIO~~~~~~~~~~~~~~~~~~~~")


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

def validate(left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, score):
    if left_margin_canibals > left_margin_missionaries and left_margin_missionaries != 0:
        score -= 1
    elif right_margin_canibals > right_margin_missionaries and right_margin_missionaries != 0:
        score -= 1
    return score

def init_population():
  for i in range(50):
    individual = Individual()
    population.append(individual)
    #print(individual)

def score(population):
  for i in range(len(population)):
    score = 11
    left_margin_canibals = 3
    left_margin_missionaries = 3
    right_margin_canibals = 0
    right_margin_missionaries = 0
    chromosomes = population[i].chromosomes

    for j in range(len(chromosomes)):
      config = chromosomes[j].config
      #print(config)

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
#===================================== do segundo ====================================================================
      if config['number_of_people'] == 2:
        if j % 2 == 0:
          if config['people'][0] == 'missionario':
              if left_margin_missionaries == 0:
                  score -= 1
              else:
                left_margin_missionaries, right_margin_missionaries = get_left_margin_people(1, left_margin_canibals,
                                                                                         left_margin_missionaries,
                                                                                         right_margin_canibals,
                                                                                         right_margin_missionaries,
                                                                                         config)
          if config['people'][0] == 'canibal':
              if left_margin_canibals == 0:
                  score -= 1
              else:
                left_margin_canibals, right_margin_canibals = get_left_margin_people(1, left_margin_canibals,
                                                                                 left_margin_missionaries,
                                                                                 right_margin_canibals,
                                                                                 right_margin_missionaries,
                                                                                 config)

        if j % 2 != 0:
          if config['people'][0] == 'missionario':
              if right_margin_missionaries != 0:
                  left_margin_missionaries, right_margin_missionaries = get_right_margin_people(1, left_margin_canibals,
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
                left_margin_canibals, right_margin_canibals = get_right_margin_people(1, left_margin_canibals,
                                                                                  left_margin_missionaries,
                                                                                  right_margin_canibals,
                                                                                  right_margin_missionaries, config)

        score = validate(left_margin_canibals, left_margin_missionaries, right_margin_canibals,
                         right_margin_missionaries, score)
      else:
        score = validate(left_margin_canibals, left_margin_missionaries, right_margin_canibals,
                         right_margin_missionaries, score)


    if score == 11 and left_margin_missionaries != 0 and left_margin_canibals != 0:
        print("ENTREI NO -11")
        score = -11
    #print("SCORE " + str(score))
    population[i].score = score

init_population()
b = 0
while True:
    flag = False
    score(population)
    for ind in population:
        #print(ind)
        for ind in population:
            if ind.score == 11:
                print(ind)
                print(ind.score)
                flag = True
                break
    if flag:
        break
    cruzamentoParte1()
    # for ind in newpopulation:
    #     print(ind)
    mutacao()
    score(newpopulation)
    population = selection()
    newpopulation.clear()
    #print("TAMANHO DA POPULACAO" + str(len(population)))
    b += 1