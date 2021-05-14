import random
class Individual():

    def __init__(self, chromosome , length):
        self.chromosome = chromosome
        self.fitness = 0
        self.length = length
        
    def randomMove(self):
        gene = random.randint(0,2)
        return gene

    def create_chromosome(self):
        return [self.randomMove() for _ in range(self.length)]
    

