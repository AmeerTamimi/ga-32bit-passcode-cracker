# Breaking a 32-bit Binary Passcode using a Genetic Algorithm (GA)

COMP338 – AI Course Project 1 (Fall 2025).  
We generate a random 32-bit passcode, then use a Genetic Algorithm to evolve a population of bitstrings until one matches the target exactly (no brute forcing 2³², we’re not trying to age 900 years).

---

## What this repo does
- Generates a random **32-bit target** (the hidden passcode).
- Runs GA experiments across multiple configs:
  - population sizes: **50, 100, 200**
  - mutation rates: **0.001, 0.005, 0.01**
  - crossover rates: **0.5, 0.7, 0.9**
  - **10 runs** per config, **max 1000 generations**
- Logs `[FOUND]` / `[NOT FOUND]` per run and writes results to **iterations.csv** for plotting + analysis.

---

## Repo structure
- `Main.py` — runs experiments, GA loop, saves `iterations.csv`
- `Individual.py` — `Individual` class + GA operators (fitness, selection, crossover, mutation)
- `Ai-report.pdf` — project writeup + plots + discussion
- `COMP338 - Project 1 - Fall 2025.pdf` — assignment spec 

---

## Quick start
### Requirements
- Python 3.x (no extra libraries needed to run the GA; CSV writing is built-in).

### Run
```bash
python Main.py