from random import randint
from copy import copy
from chromosome import Chromosome

persons = ['canibal', 'missionario']

class Individual:

  def __init__(self):
    self.score = 0
    self.chromosomes = []
    for i in range(11):
      #   # sorteando para ver quantas pessoas vao passar de uma margem para outra
      config = {
        'people': []
      }
      config['number_of_people'] = randint(1, 2)
      config['people'].append(persons[randint(0, 1)])
      if config['number_of_people'] == 2:
        config['people'].append(persons[randint(0, 1)])
      chromosome = Chromosome(config)
      self.chromosomes.append(chromosome)

  def __str__(self) :
    chromosomes = ''
    for i in range(len(self.chromosomes)):
      chromosomes += str(self.chromosomes[i])
    return chromosomes