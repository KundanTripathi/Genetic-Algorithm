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
        self.gene1 = Solution_sequence1
        random.shuffle(Solution_sequence2)
        self.gene2 = Solution_sequence2
        

        
    # calculate fitness value by increasing fitness value by when it matches any digit
    def get_fitness(self):
        fitness = sum(list(np.multiply(np.multiply(self.gene1,self.gene2),Cost))) + self.penalty() 
        return fitness
    
    def penalty(self):
        for i in [0,2,4]:
            if self.gene2[i]+self.gene2[i+1] != 1 or sum(list(np.multiply(self.gene1,self.gene2))) != 60:
                return 1000
            else:
                return 0
         
    def __repr__(self):
        return ''.join(str(genes) for genes in self.gene1), ''.join(str(genes) for genes in self.gene2)


  
class Population:
    #The class needs population_size as a parameter where as Individual create genes without any parameter
    def __init__(self, population_size):
        self.population_size = population_size
        self.individuals = [Individual() for _ in range(population_size)]
    
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
        
    def __init__(self, population_size=100, crossover_rate = 0.65, mutation_rate = 0.1):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        
    def run(self):
        pop = Population(self.population_size)
        
        
        for generation_counter in range(20):
            print('Generation %s - fittest is : %s with fitness value %s' % (generation_counter, pop.get_fittest(), pop.get_fittest().get_fitness()))
            pop = self.evolve_population(pop)
            
       # print("solution found ...") 
        print(pop.get_fittest())
        
    def evolve_population(self, population):
        next_population = Population(self.population_size)
        
        # cross over may preserve the match
        #crossover - all index of next population is undergoing crossover depending on cross over prob.
        for index in range(next_population.get_size()):
            first = self.random_selection(population) # fittest of 20 random
            second = self.random_selection(population) # fittest of 20 random form 100
            next_population.save_individual(index,self.crossover(first,second)) 
        
        # lower mutation prob preserve the sequence higher changes it    
        #mutation - population at all index are undergoing mutation
        for individual in next_population.individuals:
            self.mutate(individual)
            
        return next_population
    
    def crossover(self, individual1, individual2):
        cross_individual = Individual() # single individual genes randomly generated as only one child from 2 parents
        start = randint(Chromosome_length)
        end = randint(Chromosome_length)
        
        if end < start:
            start , end = end , start
            
        cross_individual.gene1 = individual1.gene1[:start]+individual2.gene1[start:end]+individual1.gene1[end:]
        cross_individual.gene2 = individual1.gene2[:start]+individual2.gene2[start:end]+individual1.gene2[end:]

        return cross_individual
        
    def mutate(self, individual):
        a = randint(Chromosome_length)
        b = randint(Chromosome_length)
        c = randint(Chromosome_length)
        
        individual.gene1[a] = individual.gene1[b]
        individual.gene1[b] = individual.gene1[c]
        
        individual.gene2[a] = individual.gene2[b]
        individual.gene2[b] = individual.gene2[c]
        
    
    def  random_selection(self, actual_population):
        
        new_population = Population(Tournament_size) # fewer than population e.e. 20 random from 100
        
        for i in range(new_population.get_size()):
            random_index = randint(actual_population.get_size())
            new_population.save_individual(i,actual_population.get_individual(random_index))
            
        return new_population.get_fittest() #gives fittest of 20 random
    
if __name__  == '__main__':
    print (Individual())
    
    #algorithm = GeneticAlgorithm(50)
    #algorithm.run()
