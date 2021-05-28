from Individual import Individual
import random
import json
import eel

POPULATION_SIZE = 200
eel.init("frontend")

@eel.expose
def main():
    mylevel = "____G_ML__G_"
    generation = 1
    population = []
    solve = False
    initial(POPULATION_SIZE , population , mylevel)

    population = sorted(population, key = lambda x:x.fitness)
   
    for i in range(20):
        new_generation = [] 

        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[-1*s :])


        s = int((45*POPULATION_SIZE)/100)
        for _ in range(s):
        	parent1 = random.choice(population[-50:])
        	parent2 = random.choice(population[-50:])
        	(child1, child2) = parent1.crossover(parent2)
        	new_generation.append(child1)  
        	new_generation.append(child2)  



        population = new_generation    
        population = sorted(population, key = lambda x:x.fitness)
        [print("{} , {}, {}".format(i.chromosome , i.fitness , generation)) for i in population]
               
        generation += 1
    changed = changeAnswerForMap(population[-1].chromosome)
    return get_json_result({
     "map" : list(mylevel),
      "answer" : changed,
    },
    )








def initial(size , population , mylevel):

    Individual.level = mylevel
    Individual.CHROMOSOME_LENGTH = len(mylevel)

    for _ in range(size):
        chromosome = Individual.create_chromosome()
        population.append(Individual(chromosome))

    
   
def get_json_result(results):
    return json.dumps(results)

def changeAnswerForMap(answer):
    changed = []
    checkContinue = True
    for i in range(len(answer)):
        if(checkContinue):
            if answer[i] == 0 :
                changed.append(0)
            elif answer[i] == 2:
                changed.append(2)
                changed.append(0)
                changed.append(5)
            elif answer[i] == 1:
                if(i == len(answer) -1):
                    changed.append(1)
                    changed.append(0)
                    changed.append(4)
                else:    
                    changed.append(1)
                    changed.append(0)
                    changed.append(0)
                    changed.append(4)
                    checkContinue = False


        else:
            checkContinue = True
    return changed
    


eel.start('index.html' ,size=(500,500))
