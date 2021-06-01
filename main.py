from Individual import Individual
import random
import json
import eel
import matplotlib.pyplot as plt
import math

POPULATION_SIZE = 1000
eel.init("frontend")

@eel.expose
def main():


    address = "./levels/level10.txt"
    with open(address) as reader :
        mylevel = reader.read()

    # mylevel = "____G_MLGL_G_"
    generation = 1
    population = []
    avgfit = []
    solve = False
    initial(POPULATION_SIZE , population , mylevel)

    population = sorted(population, key = lambda x:x.fitness)

    check = checkSolution(mylevel)

    avgfit.append(0)
    avg = 0
    for i in population:
        avg += i.fitness
    avg = avg / len(population)
    avgfit.append(avg)

    while avgfit[-1] - avgfit[-2] > 0.00001 or avgfit[-1] < 0 :
        new_generation = [] 

        s = int((4*POPULATION_SIZE)/100)
        new_generation.extend(population[-1*s :])


        s = int((48*POPULATION_SIZE)/100)
        s2 = int((20*POPULATION_SIZE)/100)

        for _ in range(s):
        	parent1 = random.choice(population[-1*s2:])
        	parent2 = random.choice(population[-1*s2:])
        	(child1, child2) = parent1.crossover(parent2)
        	new_generation.append(child1)  
        	new_generation.append(child2)
       


        population = new_generation 

        avg = 0
        for i in population:
            avg += i.fitness
        avg = avg / len(population)
        avgfit.append(avg)


        population = sorted(population, key = lambda x:x.fitness)
        # [print("{} , {}, {}".format(i.chromosome , i.fitness , generation)) for i in population]
               
        generation += 1

    changed = changeAnswerForMap(population[-1].chromosome)
    # for i in avgfit:
    #     print(i , end=" ")

    # chart(range(generation),avgfit[1::])

    return get_json_result({
     "map" : list(mylevel),
      "answer" : changed,
      "hasAnswer" : check
    },
    )

    



def checkSolution(level):
    for i in range(len(level)-1):
        if level[i] == 'G' and level[i+1] == 'L':
            return False
    return True
    






def chart(x , y):
    
    plt.plot(x, y)
    
    plt.xlabel('fittnes')
    
    plt.ylabel('generation')
    
    plt.title('genetic algorithm ')
    
    plt.show()



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



# if __name__ == "__main__":
    # execute only if run as a script
    main()

eel.start('index.html' ,size=(500,500))
