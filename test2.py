import pandas as pd 
import numpy as np
from random import uniform
from numpy.random import randint
import random
from random import shuffle 

Solution_sequence1 = [10,20,30,0,0,0]
Solution_sequence2 = [1,0,1,0,1,0]
Cost = [1,2,1,1,3,2]
Tournament_size = 20
#Max_fitness = 10
Chromosome_length = 6



class Individual:
    
        
    def __init__(self):
        
        random.shuffle(Solution_sequence1)
        random.shuffle(Solution_sequence2)
        
        self.gene = [Solution_sequence1,Solution_sequence2]
        
        
    # calculate fitness value by increasing fitness value by calculating cost and applying penalty
    def get_fitness(self):
        fitness = sum(list(np.multiply(np.multiply(self.gene[0],self.gene[1]),Cost))) + self.penalty() 
        return fitness
    
    def penalty(self):
        self.gene = self.gene
        for i in [0,2,4]:
            if self.gene[1][i]+self.gene[1][i+1] != 1 or sum(list(np.multiply(self.gene[0],self.gene[1]))) != 60:
                return 1000
            else:
                return 0
         
    def __repr__(self):
        return ''.join(str(genes)+ " " for genes in np.hstack((["gene[0]"],self.gene[0],["|"],["gene[1]"],self.gene[1])))
        

  
class Population:
    #The class needs population_size as a parameter where as Individual create genes without any parameter
    def __init__(self, population_size):
        self.population_size = population_size
        self.individuals = [Individual() for _ in range(self.population_size)]

       
    #gives fittest individual from list of (population_size) individuals [self.individuals = population]   
    def get_fittest(self):
        
        fittest = self.individuals[0]
        
        for individual in self.individuals[1:]:
            if individual.get_fitness() < fittest.get_fitness():
                fittest = individual
        return fittest
    
    def get_size(self):
        return self.population_size
    
    def get_individual(self,index):
        return self.individuals[index]
    
    def save_individual(self, index, individual):
        self.individuals[index] = individual
        
        
class GeneticAlgorithm:
        
    def __init__(self, population_size=200, crossover_rate = 0.65, mutation_rate = 0.4):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
    def run(self):
        pop = Population(self.population_size)
        fitness_value = []
        
        
        for generation_counter in range(200):
            print('Generation %s - fittest is : %s with fitness value %s' % (generation_counter, pop.get_fittest(), pop.get_fittest().get_fitness()))
            pop = self.evolve_population(pop)
            fitness_value.append(pop.get_fittest().get_fitness())
        print(sorted(fitness_value))
            
       # print("solution found ...") 
        print(pop.get_fittest())
        
    def evolve_population(self, population):
        next_population = Population(self.population_size)
        
        # cross over may preserve the match
        #crossover - all index of next population is undergoing crossover depending on cross over prob.
       
       
        for index in range(next_population.get_size()):
            first = self.random_selection(population) # fittest of 20 random
      #      second = self.random_selection(population) # fittest of 20 random form 100
       #     if first.get_fitness() < second.get_fitness():
            next_population.save_individual(index,first)
       #     else:
      #          next_population.save_individual(index,second) 
     
        # lower mutation prob preserve the sequence higher changes it    
        #mutation - population at all index are undergoing mutation
        for individual in next_population.individuals:
            self.mutate(individual)
            
        return next_population
    """ 
    def crossover(self, individual1, individual2):
        cross_individual = Individual() # single individual genes randomly generated as only one child from 2 parents
        start1 = randint(Chromosome_length)
        end1 = randint(Chromosome_length)
        
        start2 = randint(Chromosome_length)
        end2 = randint(Chromosome_length)
        
        
        if end1 < start1:
            start1 , end1 = end1 , start1
        cross_individual.gene[0] = individual1.gene[0][:start1]+individual2.gene[0][start1:end1]+individual1.gene[0][end1:]
        
        if end2 < start2:
            start2 , end2 = end2 , start2
        cross_individual.gene[1] = individual1.gene[1][:start2]+individual2.gene[1][start2:end2]+individual1.gene[1][end2:]

        return cross_individual
    """      
    
    def mutate(self, individual):
        a = randint(Chromosome_length)
        b = randint(Chromosome_length)
        c = randint(Chromosome_length)
        
        individual.gene[0][a], individual.gene[0][b] = individual.gene[0][b], individual.gene[0][a]
        individual.gene[0][b], individual.gene[0][c] = individual.gene[0][c], individual.gene[0][b]
        
        e = randint(Chromosome_length)
        f = randint(Chromosome_length)
        g = randint(Chromosome_length)
        
        individual.gene[1][e], individual.gene[1][f] = individual.gene[1][f], individual.gene[1][e]
        individual.gene[1][f], individual.gene[1][g] = individual.gene[1][g], individual.gene[1][f]
        
    
    def  random_selection(self, actual_population):
        
        new_population = Population(Tournament_size) # fewer than population e.e. 20 random from 100
        
        for i in range(new_population.get_size()):
            random_index = randint(actual_population.get_size())
            new_population.save_individual(i,actual_population.get_individual(random_index))
            
        return new_population.get_fittest() #gives fittest of 20 random
    
if __name__  == '__main__':
    #print (GeneticAlgorithm(20).evolve_population(Population(15)))
    
    algorithm = GeneticAlgorithm()
    algorithm.run()
