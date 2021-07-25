import random
from random import seed
from random import *
from individual import Individual


def cruzamentoParte2(pai,mae,newPopulation):
    part1 = randint(1,10)
    individuo1 = Individual(pai.chromosomes[:part1] + mae.chromosomes[part1:])
    individuo2 = Individual(mae.chromosomes[:part1] + pai.chromosomes[part1:])
    newPopulation.append(individuo1)
    newPopulation.append(individuo2)

def cruzamentoParte1(populacao,newPopulation):
    for i in range(len(populacao)-1):
        for j in range(len(populacao)-1):
            porcentagem = randint(0,100)
            if  porcentagem >= 0 and i != j:
                pai = populacao[i]
                mae = populacao[j]
                cruzamentoParte2(pai,mae,newPopulation)

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

    if score == 11 and left_margin_missionaries != 0 and left_margin_canibals != 0:
        score = -11
    print("SCORE " + str(score))
    population[i].score = score

def init_population(population):
  for i in range(2):
    individual = Individual()
    population.append(individual)
    #print(individual)

def main():
    population = []
    newPopulation=[]

    init_population(population)
    for ind in population:
        print(ind)
    score(population)
    cruzamentoParte1(population,newPopulation)
    print(newPopulation)

if __name__ == '__main__':
    main()