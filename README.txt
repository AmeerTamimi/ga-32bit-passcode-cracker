# Genetic Algorithm: 32-bit Passcode Guessing (COMP338 Project 1)

This repo implements a **Genetic Algorithm (GA)** that evolves **32-bit binary chromosomes** to exactly match a target **32-bit passcode**.

It also runs **parameter sweeps** (population size / mutation rate / crossover rate) and logs **convergence data** to a CSV file for analysis and visualization (e.g., in Google Colab).

## Features
- 32-bit chromosome representation (`0` / `1`)
- Fitness = number of matching bits with the target (0..32)
- GA loop:
  - Selection
  - Crossover
  - Mutation
  - Elitism (keeps top 10%)
- Parameter sweep runner
- Convergence logging to `convergence.csv`:
  - best fitness
  - average fitness
  - best chromosome string
  - Hamming distance to target
  - found flag

## Output file (CSV)
The program generates `convergence.csv` with columns:
- `pop_size`
- `mutation_rate`
- `crossover_rate`
- `run_id`
- `generation`
- `best_fitness`
- `avg_fitness`
- `best_string`
- `distance_to_target`
- `found`

## How to run
### Run the GA sweeps
```bash
python main.py
This will generate:

convergence.csv

Visualize (Google Colab)
Upload convergence.csv into Colab and use your plotting notebook/script to produce:

convergence curves (fitness/distance vs generation)

success rate per configuration

average generations-to-solution heatmaps

Customize parameters
Edit these in main.py:

RUNS

max_generation

mutation_list

pop_list

cross_list

Authors
Ameer Tamimi

Habeeb Allah