import random

## Individuals within each generation
POPULATION_SIZE = 100

# Valid Genes for mutation
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
  
TARGET = "My name is Wesley" 

## Class to represent on individual within a population
class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()
        
    # This generates random genes for mutation
    def mutated_genes(self):
        global GENES
        gene = random.choice(GENES)
        return gene
    
    # Create chromosome or string of genes
    def create_gnome(self):
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]
    
    # Perform new offsprings
    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip()
        
