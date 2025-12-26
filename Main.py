import random
import csv
from Individual import Individual
import time
import random
import csv

cross_list = [0.5, 0.7, 0.9]
mutation_list = [0.001, 0.005, 0.01]
pop_list = [50,100,200]

RUNS = 10
max_generation = 1000

# Generate a random 32-bit target
TARGET = ''.join(random.choice('01') for _ in range(32))
print("Randomly generated target:", TARGET)

N = len(TARGET)

SINGLE_POINT_RATE = 0.60

Individual.GENES = "01"
Individual.TARGET = TARGET
Individual.N = N
Individual.ONES = TARGET.count('1')
Individual.ZEROS = TARGET.count('0')
Individual.SINGLE_POINT_RATE = SINGLE_POINT_RATE

def calculate_difference(chromosome, target):
    difference_sum = 0

    for a,b in zip(chromosome , target):
        if a != b:
            difference_sum += 1
    return difference_sum

def run_genetic(POPULATION_SIZE, MUTATION_RATE, CROSS_OVER_RATE, run_id, writer):

    Individual.MUTATION_RATE = MUTATION_RATE
    Individual.CROSS_OVER_RATE = CROSS_OVER_RATE

    population = []
    for i in range(POPULATION_SIZE):
        chromosome = Individual([]).create_chromosome()
        population.append(Individual(chromosome))

    generation_counter = 1
    found = 0
    start_time = time.time()  # start clock

    best = None
    best_str = ""
    avg_fit = 0
    dist = 0

    while generation_counter <= max_generation:

        # we sort here descending based on the fitness , so the first one is the best (since he will have the highest fitness value)
        population.sort(key=lambda x: x.fitness, reverse=True)
        best = population[0]

        best_str = "".join(best.chromosome)
        avg_fit = sum(ind.fitness for ind in population) / len(population)
        dist = calculate_difference(best_str, TARGET)

        if best_str == TARGET:
            found = 1
            end_time = time.time()  # stop the clock immediately
            total_time = end_time - start_time  # calculate duration

            # print results to console
            print(f"[FOUND] pop={POPULATION_SIZE} mut={MUTATION_RATE} cross={CROSS_OVER_RATE} "
                  f"run={run_id} gen={generation_counter} time={total_time:.4f}s")
            break
        else:
            new_generation = []

            # we apply the elitism here (always keep the top 10% fit individuals)
            new_generation.extend(population[: int(POPULATION_SIZE * 0.1)])

            # we will always remove the worst 30% (no offense but they're bad)
            population = population[: int(POPULATION_SIZE * 0.7)]

            # here we make the new generation (based on the selection + we keep applying crossover until the population size is done)
            while len(new_generation) < POPULATION_SIZE:

                # selection of parents
                parent1 = population[0].selection(population)
                parent2 = population[0].selection(population)

                # apply crossover based on probability
                if random.random() < CROSS_OVER_RATE:
                    child1, child2 = parent1.cross_over(parent2.chromosome)
                    new_generation.append(Individual(child1))
                    if len(new_generation) < POPULATION_SIZE:
                        new_generation.append(Individual(child2))
                else:
                    new_generation.append(parent1)
                    if len(new_generation) < POPULATION_SIZE:
                        new_generation.append(parent2)

            # apply mutation for each individual
            for ind in new_generation:
                ind.chromosome = ind.mutation(ind.chromosome)
                ind.fitness = ind.calculate_fitness()

            population = new_generation
            generation_counter += 1

    end_time = time.time()
    total_time = end_time - start_time

    if not found:
        population.sort(key=lambda x: x.fitness, reverse=True)
        best = population[0]
        best_str = "".join(best.chromosome)
        avg_fit = sum(ind.fitness for ind in population) / len(population)
        dist = calculate_difference(best_str, TARGET)

        print(f"[NOT FOUND] pop={POPULATION_SIZE} mut={MUTATION_RATE} cross={CROSS_OVER_RATE} "
              f"run={run_id} bestFitness={best.fitness} dist={dist} best={best_str}")

        generation_counter = max_generation

    writer.writerow([
        POPULATION_SIZE, MUTATION_RATE, CROSS_OVER_RATE,
        run_id, generation_counter, best.fitness, avg_fit,
        best_str, dist, total_time, found
    ])

with open("iterations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "pop_size", "mutation_rate", "crossover_rate",
        "run_id", "generation", "best_fitness", "avg_fitness",
        "best_string", "distance_to_target", "total_time_sec", "found"
    ])

    for POPULATION_SIZE in pop_list:
        for MUTATION_RATE in mutation_list:
            for CROSS_OVER_RATE in cross_list:
                for run_id in range(1, RUNS + 1):
                    run_genetic(POPULATION_SIZE, MUTATION_RATE, CROSS_OVER_RATE, run_id, writer)
