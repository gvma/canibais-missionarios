class Chromosome:

  def __init__(self, config):
    self.config = config

  def __str__(self):
    to_string = 'Number of people: ' + str(self.config['number_of_people']) + ': '
    for i in range(self.config['number_of_people']):
      to_string += str(self.config['people'][i]) + ','
    return to_string + '\n'