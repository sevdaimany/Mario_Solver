from Individual import Individual
import random

POPULATION_SIZE = 50

def main():
    mylevel = "____G_ML__G_"
    generation = 1
    population = []
    solve = False
    initial(POPULATION_SIZE , population , mylevel)

    population = sorted(population, key = lambda x:x.fitness)

    for i in range(50):

        # sort the population in increasing order of fitness score
        # population = sorted(population, key = lambda x:x.fitness)

        # Otherwise generate new offsprings for new generation
        new_generation = []    

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((50*POPULATION_SIZE)/100)
        new_generation.extend(population[s:])       

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((50*POPULATION_SIZE)/100)
        for _ in range(s):
        	parent1 = random.choice(population[:50])
        	parent2 = random.choice(population[:50])
        	child = parent1.crossover(parent2)
        	new_generation.append(child)  

        population = new_generation    

        population = sorted(population, key = lambda x:x.fitness)

        [print("{} , {}, {}".format(i.chromosome , i.fitness , generation)) for i in population]
               
        generation += 1

    







def initial(size , population , mylevel):

    Individual.level = mylevel
    Individual.CHROMOSOME_LENGTH = len(mylevel)

    for _ in range(size):
        chromosome = Individual.create_chromosome()
        population.append(Individual(chromosome))

    




if __name__ == '__main__':
    # target = input()
    main()