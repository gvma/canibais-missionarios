# 3 canibais e 3 missionarios na mesma margem
from random import seed

from individual import Individual

population = []

def get_right_margin_people(people_in_margin):
  return 3 - people_in_margin

def validate(position,  left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config, score):
  if config['people'][position] == 'missionario':
    if left_margin_canibals > left_margin_missionaries - 1:
      score = 0
    elif right_margin_canibals > right_margin_missionaries + 1:
      score = 0
  else:
    if left_margin_canibals - 1 > left_margin_missionaries:
      score = 0
    elif right_margin_canibals + 1 > right_margin_missionaries:
      score = 0
  return score

def init_population():
  for i in range(20):
    individual = Individual()
    population.append(individual)
    print(individual)

def score():
  for i in range(len(population)):
    score = 2
    left_margin_canibals = 3
    left_margin_missionaries = 3
    right_margin_canibals = get_right_margin_people(left_margin_canibals)
    right_margin_missionaries = get_right_margin_people(left_margin_missionaries)
    chromosomes = population[i].chromosomes
    left_margin = True
    for j in range(len(chromosomes)):
      config = chromosomes[i].config
      if validate(0, left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config, score) == 0:
        score = 0
      if config['number_of_people'] == 2:
        if validate(1, left_margin_canibals, left_margin_missionaries, right_margin_canibals, right_margin_missionaries, config, score) == 0:
         score = 0
    print(score)
  return score

init_population()
score()