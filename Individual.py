import random

CHROMOSOME_LENGTH = 12

class Individual:

    level = "____"

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.fittness()

    @classmethod 
    def randomMove(cls):
        gene = random.randint(0,2)
        return gene

    @classmethod
    def create_chromosome(cls):
        global CHROMOSOME_LENGTH
        CHROMOSOME_LENGTH = len(cls.level)
        return [cls.randomMove() for _ in range(CHROMOSOME_LENGTH)]
    

    def mutation(self):
        p = random.random()
        if p < 0.2 :
            randIndex = random.randint(0, CHROMOSOME_LENGTH -1) 
            self.chromosome[randIndex] = 0
    
    def fittness(self):

        score = 0
        for i in range(CHROMOSOME_LENGTH):
            current_step = self.level[i]


            if (current_step == '_'):
                score += 10
            elif (current_step == 'G'):

                if(i == 0):
                    score += -999
                elif (i == 1):
                    if(self.chromosome[i - 1] == 1):
                        score += 10
                    else:
                        score += -999
                else:
                    if(self.chromosome[i - 2] == 1):
                        score += 20
                    elif(self.chromosome[i - 1] == 1):
                        score += 10
                    else:
                        score += -999
                
            elif (current_step == 'L' ):

                if( self.chromosome[i - 1] == 2):
                    score += 10
                else :
                    score += -999
                
            elif (self.chromosome[i - 1] != 1 and current_step == 'M' ):
                score += 20
            
            


        
        

        if(self.chromosome[-1] == 1):
            score += 10

        return score



