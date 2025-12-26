# -------- Individual.py --------
import random


class Individual:
    # Number of individuals in each generation
    POPULATION_SIZE = 0
    # Valid genes
    GENES = "01"
    # Target string to be generated
    TARGET = ""

    ONES = 0
    ZEROS = 0
    N = 0
    MUTATION_RATE = 0
    CROSS_OVER_RATE = 0
    SINGLE_POINT_RATE = 0

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    def random_gene(self):
        gene = random.choice(self.GENES)
        return gene

    def mutation(self, chromosome):
        for i in range(self.N):
            r = random.random()
            if r < self.MUTATION_RATE:
                chromosome[i] = self.random_gene()

        return chromosome

    def create_chromosome(self):
        chromosome = []
        for i in range(self.N):
            chromosome.append(self.random_gene())
        return chromosome

    def cross_over(self, parent2):
        parent1 = self.chromosome

        single_r = random.random()
        if single_r < self.SINGLE_POINT_RATE:

            # We'll be making a single point cross over (the middle)
            # so ch1 will be having the first part of pa2 and second part of pa1, and ch2 the opposite  way
            mid = self.N // 2
            child1 = parent2[:mid]
            child2 = parent1[:mid]

            # here ch1 will have the second part from pa1, and ch2 from pa2
            child1 += parent1[mid:]
            child2 += parent2[mid:]

        else:
            # Here we will make a 2-point cross over
            # so ch1 will be having the first part of pa1, second from pa2 , third from p1 , and ch2 the opposite way
            slice = self.N // 3
            child1 = parent1[:slice] + parent1[2*slice:]
            child2 = parent1[slice:slice*2]

            child1 += parent2[slice:slice*2]
            child2 += parent2[:slice] + parent2[2*slice:]

        return (child1, child2)

    def calculate_fitness(self):
        chromosome = self.chromosome
        fitness_value = 0
        for char, gene in zip(self.TARGET, chromosome):
            if char == gene:
                fitness_value += 1

        fitness_value += 32
        fitness_value -= abs(self.ONES - chromosome.count('1'))
        fitness_value -= abs(self.ZEROS - chromosome.count('0'))

        return fitness_value

    def selection(self, population):
        total_fitness = 0

        for individual in population:
            total_fitness += individual.fitness

        if total_fitness == 0:  # All individuals are basically trash (no offense tho)
            return population[0]
        r = random.random()
        total_sofar = 0
        for individual in population:
            individual_fitness = (individual.fitness / total_fitness)
            total_sofar += individual_fitness
            if total_sofar >= r:
                return individual

        return population[0]  # some edge case (theoritaclly impossible) ... i mean i guess but wallah no way
