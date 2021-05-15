from Individual import Individual

POPULATION_SIZE = 10

def main():
    generation = 0
    population = []
    solve = False
    initial(POPULATION_SIZE , population)
    [print("{} , {}".format(i.chromosome , i.fitness)) for i in population]
    print(len(Individual.level))







def initial(size , population):
    Individual.level = "M_G__M___G"
    for _ in range(size):
        chromosome = Individual.create_chromosome()
        population.append(Individual(chromosome))




if __name__ == '__main__':
    # target = input()
    main()