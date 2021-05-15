from Individual import Individual

POPULATION_SIZE = 10

def main():
    mylevel = "M_G__M___G"
    generation = 0
    population = []
    solve = False
    initial(POPULATION_SIZE , population , mylevel)
    [print("{} , {}".format(i.chromosome , i.fitness)) for i in population]
    print(len(Individual.level))







def initial(size , population , mylevel):
    Individual.level = mylevel
    Individual.CHROMOSOME_LENGTH = len(mylevel)
    for _ in range(size):
        chromosome = Individual.create_chromosome()
        population.append(Individual(chromosome))




if __name__ == '__main__':
    # target = input()
    main()