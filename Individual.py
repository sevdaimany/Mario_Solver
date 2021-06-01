import random

class Individual:

    level = "____"
    CHROMOSOME_LENGTH = 0

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.fittness()
        

    @classmethod 
    def randomMove(cls):
        p = random.random()
        if p < 0.4 :
            return 0
        elif p < 0.7:
            return 2
        return 1
        # gene = random.randint(0,2)
        # return gene

   
    @classmethod
    def create_chromosome(cls):  
        return [cls.randomMove() for _ in range(cls.CHROMOSOME_LENGTH)]
    

    def mutation(self , child):
        p = random.random()
        n = random.randint(0,2)
        if p  < 0.5:
             randIndex = random.randint(0, self.CHROMOSOME_LENGTH -1) 
             child[randIndex] = n
    

    # def mutation(self , child):
    #     p = random.random()
    #     # n = random.randint(0,2)
    #     if p  < 0.5:
    #          randIndex = random.randint(0, self.CHROMOSOME_LENGTH -1) 
    #          child[randIndex] = 0

#     def crossover(self , mate):
#         child_chromosome1 = []
#         child_chromosome2 = []
#         size1 =(int)((len(self.chromosome) / 2 ) )- 1
#         size2 = len(self.chromosome) - size1
#         child_chromosome1.extend(self.chromosome[:size1])
#         child_chromosome1.extend(mate.chromosome[-1*size2 :])
#         self.mutation(child_chromosome1)
# #
#         child_chromosome2.extend(mate.chromosome[:size1])
#         child_chromosome2.extend(self.chromosome[-1*size2 :])
#         self.mutation(child_chromosome2)
#         return Individual(child_chromosome1) , Individual(child_chromosome2)
        

        
   
    def crossover(self , mate):
        child_chromosome1 = []
        child_chromosome2 = []
        size1 =(int)((len(self.chromosome) / 3) )
        size3 = len(self.chromosome) - size1
        child_chromosome1.extend(self.chromosome[:size1])
        child_chromosome1.extend(mate.chromosome[size1:size3])
        child_chromosome1.extend(self.chromosome[-1*size1 :])
        self.mutation(child_chromosome1)
#
        child_chromosome2.extend(mate.chromosome[:size1])
        child_chromosome2.extend(self.chromosome[size1:size3])
        child_chromosome2.extend(mate.chromosome[-1*size1 :])
        self.mutation(child_chromosome2)
        return Individual(child_chromosome1) , Individual(child_chromosome2)
        
     




    def fittness(self):
    
        score = 0
        longestPath = 0
        lenPath =0
        for i in range(self.CHROMOSOME_LENGTH):
            current_step = self.level[i]

            if( self.chromosome[i] == 1 ):
                if(i == self.CHROMOSOME_LENGTH - 2):
                    if(self.level[i + 1] == "_" or self.level[i + 1] == "M"):
                        score += -2
                elif(i < self.CHROMOSOME_LENGTH - 2):
                    if((self.level[i + 1] == "_" and self.level[i + 2] == "_") or (self.level[i + 1] == "M" and self.level[i + 2] == "M")
                        or (self.level[i + 1] == "_" and self.level[i + 2] == "M") or (self.level[i + 1] == "M" and self.level[i + 2] == "_")):
                        score += -2


            if( self.chromosome[i] == 2 ):
               if i <= self.CHROMOSOME_LENGTH -2 and  self.level[i+1] != 'L' :
                   score += -2
               if i > self.CHROMOSOME_LENGTH -2:
                    score += -2


        
        
            if (current_step == 'G'):
                if (self.chromosome[i-1] != 1 and i >= 1) or (self.chromosome[i-2] != 1 and i >= 2):
                     if lenPath > longestPath :
                        longestPath = lenPath
                     score -= 2
                     lenPath = 0
                if (self.chromosome[i-2] == 1 and i >=2 ):
                    score +=2


                
            elif (current_step == 'L' ):

                if(self.chromosome[i-1] != 2 and i >=1 ):
                      if lenPath > longestPath :
                        longestPath = lenPath
                      score -= 2
                      lenPath = 0
                if self.chromosome[i-2] == 1 and i >=2 :
                      if lenPath > longestPath :
                        longestPath = lenPath
                      lenPath = 0
                      score -= 2

               
                
            elif (current_step == 'M' and (i == 0 or self.chromosome[i - 1] != 1) ):
                    score += 2
            lenPath += 1

            
        if lenPath > longestPath :
            longestPath = lenPath
            lenPath = 0
        
        score += longestPath
                

        if(self.chromosome[-1] == 1):
            score += 3


        return score




# Individual.level = "____G_ML__G"
# Individual.CHROMOSOME_LENGTH = len("____G_ML__G")
# gg = Individual([1,2,3,4,5,6,7,8,9,10,11])
# gg2 = Individual([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11])

# (one , two ) = gg.crossover(gg2)
# print(one)
# print(two)
# # print(gg.fitness) 