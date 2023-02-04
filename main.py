import random

from deap import base
from deap import creator
from deap import tools

IND_SIZE = 6

creator.create("FitnessMulti", base.Fitness, weights=(1.0, 1.0))
creator.create("Individual", list, fitness=creator.FitnessMulti)

toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, 0, 89)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=IND_SIZE)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

ind1 = toolbox.individual()

print(ind1)
print(ind1.fitness.valid)
