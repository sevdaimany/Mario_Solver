import random

CHROMOSOME_LENGTH = 12

class Individual:


    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = 0

    @classmethod 
    def randomMove(cls):
        gene = random.randint(0,2)
        return gene

    @classmethod
    def create_chromosome(cls):
        global CHROMOSOME_LENGTH
        return [cls.randomMove() for _ in range(CHROMOSOME_LENGTH)]
    

    def mutation(self):
        p = random.random()
        if p < 0.2 :
            randIndex = random.randint(0, CHROMOSOME_LENGTH -1) 
            self.chromosome[randIndex] = 0





