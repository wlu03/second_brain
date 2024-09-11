import random

# Individuals within each generation
POPULATION_SIZE = 100

# Valid Genes for mutation
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "My name is Wesley"

# Class to represent an individual within a population
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
    @classmethod
    def create_gnome(cls):
        global TARGET
        gnome_len = len(TARGET)
        return [random.choice(GENES) for _ in range(gnome_len)]

    # Perform new offspring generation by mating
    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # Generates a random probability
            prob = random.random()

            # 45% chance from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)
            # 45% chance from parent 2
            elif prob < 0.9:
                child_chromosome.append(gp2)
            # 10% chance of mutation
            else:
                child_chromosome.append(self.mutated_genes())

        # Return the new individual
        return Individual(child_chromosome)

    # Calculate fitness score: how far chromosome is from target
    def calculate_fitness(self):
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt:
                fitness += 1
        return fitness

# Main function
def main():
    global POPULATION_SIZE

    # Current generation
    generation = 1
    found = False
    population = []

    # Generate Initial Population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:
        # Sort population by increasing fitness score
        population = sorted(population, key=lambda x: x.fitness)

        # If the best individual has a fitness of 0, target is reached
        if population[0].fitness == 0:
            found = True
            break

        # Create new generation
        new_generation = []

        # Elitism: carry forward the top 10% to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # Mating pool: mate 90% of the population to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}".format(
            generation,
            "".join(population[0].chromosome),
            population[0].fitness))

        generation += 1

    print("Generation: {}\tString: {}\tFitness: {}".format(
        generation,
        "".join(population[0].chromosome),
        population[0].fitness))

if __name__ == '__main__':
    main()
