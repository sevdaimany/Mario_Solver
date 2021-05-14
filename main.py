from Individual import Individual

def main():
    generation = 0
    population = []
    solve = False
    initial(2 , population)
    [print(i.chromosome) for i in population]






def initial(size , population):
    for _ in range(size):
        chromosome = Individual.create_chromosome()
        population.append(Individual(chromosome))




if __name__ == '__main__':
    main()