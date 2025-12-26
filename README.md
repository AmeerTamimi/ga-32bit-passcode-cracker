# Breaking a 32-bit Binary Passcode using a Genetic Algorithm (GA)

COMP338 – AI Course Project 1 (Fall 2025).  
We generate a random 32-bit passcode, then use a Genetic Algorithm to evolve a population of bitstrings until one matches the target exactly (no brute forcing 2³², we’re not trying to age 900 years). :contentReference[oaicite:0]{index=0}

---

## What this repo does
- Generates a random **32-bit target** (the hidden passcode). :contentReference[oaicite:1]{index=1}  
- Runs GA experiments across multiple configs:
  - population sizes: **50, 100, 200**
  - mutation rates: **0.001, 0.005, 0.01**
  - crossover rates: **0.5, 0.7, 0.9**
  - **10 runs** per config, **max 1000 generations** :contentReference[oaicite:2]{index=2}
- Logs `[FOUND]` / `[NOT FOUND]` per run and writes results to **iterations.csv** for plotting + analysis. :contentReference[oaicite:3]{index=3}

---

## Repo structure
- `Main.py` — runs experiments, GA loop, saves `iterations.csv` :contentReference[oaicite:4]{index=4}  
- `Individual.py` — `Individual` class + GA operators (fitness, selection, crossover, mutation) :contentReference[oaicite:5]{index=5}  
- `Ai-report.pdf` — project writeup + plots + discussion :contentReference[oaicite:6]{index=6}  
- `COMP338 - Project 1 - Fall 2025.pdf` — assignment spec :contentReference[oaicite:7]{index=7}  

---

## Quick start
### Requirements
- Python 3.x (no extra libraries needed to run the GA; CSV writing is built-in). :contentReference[oaicite:8]{index=8}

### Run
```bash
python Main.py