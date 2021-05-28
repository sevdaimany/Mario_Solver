import random

# CHROMOSOME_LENGTH = 12

class Individual:

    level = "____"
    CHROMOSOME_LENGTH = 0

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.fittness()
        

    @classmethod 
    def randomMove(cls):
        gene = random.randint(0,2)
        return gene

    @classmethod
    def create_chromosome(cls):  
        return [cls.randomMove() for _ in range(cls.CHROMOSOME_LENGTH)]
    

    def mutation(self , child):
        p = random.random()
        if p  < 0.2:
             randIndex = random.randint(0, self.CHROMOSOME_LENGTH -1) 
             child[randIndex] = 0
    

    # def crossover (self , mate):

    #     # chromosome for offspring
    #     child_chromosome = []
    #     for gp1, gp2 in zip(self.chromosome, mate.chromosome):

    #         # random probability
    #         prob = random.random()

    #         # if prob is less than 0.45, insert gene
    #         # from parent 1
    #         if prob < 0.5:
    #         	child_chromosome.append(gp1)

    #         # if prob is between 0.45 and 0.90, insert
    #         # gene from parent 2
    #         else:
    #         	child_chromosome.append(gp2)

    #         # otherwise insert random gene(mutate),
    #         # for maintaining diversity
            
    #         self.mutation()

    #     # create new Individual(offspring) using
    #     # generated chromosome for offspring

        # return Individual(child_chromosome)

    def crossover(self , mate):
        child_chromosome1 = []
        child_chromosome2 = []
        size1 =(int)((len(self.chromosome) / 2 ) )- 1
        size2 = len(self.chromosome) - size1
        child_chromosome1.extend(self.chromosome[:size1])
        child_chromosome1.extend(mate.chromosome[-1*size2 :])
        self.mutation(child_chromosome1)
#
        child_chromosome2.extend(mate.chromosome[:size1])
        child_chromosome2.extend(self.chromosome[-1*size2 :])
        self.mutation(child_chromosome2)
        return Individual(child_chromosome1) , Individual(child_chromosome2)
        
        





    # def fittness(self):

    #     score = 0
    #     for i in range(self.CHROMOSOME_LENGTH):
    #         current_step = self.level[i]

    #         # for useless jump
    #         if( self.chromosome[i] == 1 ):
    #             if(i == self.CHROMOSOME_LENGTH - 2):
    #                 if(self.level[i + 1] == "_" or self.level[i + 1] == "M"):
    #                     score += -5
    #             elif(i < self.CHROMOSOME_LENGTH - 2):
    #                 if((self.level[i + 1] == "_" and self.level[i + 2] == "_") or (self.level[i + 1] == "M" and self.level[i + 2] == "M")
    #                     or (self.level[i + 1] == "_" and self.level[i + 2] == "M") or (self.level[i + 1] == "M" and self.level[i + 2] == "_")):
    #                     score += -5
            
    #         # restriction for double jump or continuous jumping and slipping continuous
    #         if(self.chromosome[i] == 1 and i != (self.CHROMOSOME_LENGTH - 1) 
    #             and self.chromosome[i + 1] != 0):
    #                 score += -5

    #                 continue


    #         # main part
           
    #         if (current_step == 'G'):

    #             if(self.chromosome[i - 1] == 1 and i == 1):
    #                 score += 10
    #             elif(self.chromosome[i - 2] == 1 and (i != 0 and i != 1)):
    #                 score += 20
    #             elif(self.chromosome[i - 1] == 1 and  (i != 0 and i != 1)):
    #                 score += 10
    #             else:
    #                 score += -99999
    #                 continue
                
    #         elif (current_step == 'L' ):

    #             if( self.chromosome[i - 1] == 2 and i != 0):
    #                 score += 10
    #             else :
    #                 score += -99999
    #                 continue
                
    #         elif (current_step == 'M' and (i == 0 or self.chromosome[i - 1] != 1) ):
    #                 score += 20

            
            

    #     # for jump befor flag
    #     if(self.chromosome[-1] == 1):
    #         score += 10

    #     return score
    

    def fittness(self):
    
        score = 0
        longestPath = 0
        lenPath =0
        for i in range(self.CHROMOSOME_LENGTH):
            current_step = self.level[i]

            # for useless jump
            if( self.chromosome[i] == 1 ):
                if(i == self.CHROMOSOME_LENGTH - 2):
                    if(self.level[i + 1] == "_" or self.level[i + 1] == "M"):
                        score += -1
                elif(i < self.CHROMOSOME_LENGTH - 2):
                    if((self.level[i + 1] == "_" and self.level[i + 2] == "_") or (self.level[i + 1] == "M" and self.level[i + 2] == "M")
                        or (self.level[i + 1] == "_" and self.level[i + 2] == "M") or (self.level[i + 1] == "M" and self.level[i + 2] == "_")):
                        score += -1


            if( self.chromosome[i] == 2 ):
               if i <= self.CHROMOSOME_LENGTH -2 and  self.level[i+1] != 'L' :
                   score += -1
               if i > self.CHROMOSOME_LENGTH -2:
                    score += -1


        
        
            if (current_step == 'G'):
                if (self.chromosome[i-1] != 1 and i >= 1) or (self.chromosome[i-2] != 1 and i >= 2):
                     if lenPath > longestPath :
                        longestPath = lenPath
                     lenPath = 0
                if (self.chromosome[i-2] == 1 and i >=2 ):
                    score +=2


                
            elif (current_step == 'L' ):

                if(self.chromosome[i-1] != 2 and i >=1 ):
                      if lenPath > longestPath :
                        longestPath = lenPath
                      lenPath = 0
                if self.chromosome[i-2] == 1 and i >=2 :
                      if lenPath > longestPath :
                        longestPath = lenPath
                      lenPath = 0
               
                
            elif (current_step == 'M' and (i == 0 or self.chromosome[i - 1] != 1) ):
                    score += 2
            lenPath += 1

            
        if lenPath > longestPath :
            longestPath = lenPath
            lenPath = 0
        
        score += longestPath
                

        # for jump befor flag
        if(self.chromosome[-1] == 1):
            score += 1


        return score


# Individual.level = "____G_ML__G_"
# Individual.CHROMOSOME_LENGTH = len("____G_ML__G_")
# gg = Individual([0,0,0,0,0,0,0,0,0,0,0,0])
# gg2 = Individual([1,1,1,1,1,1,1,1,1,1,1,1])

# print(gg.crossover(gg2))
# print(gg.fitness)