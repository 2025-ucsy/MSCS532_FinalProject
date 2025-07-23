# MSCS532_FinalProject

This repository contains the code, scripts, and results for the MSCS-532 Final Project (Part 1):  
**Comparative Empirical Analysis of Array of Structs (AoS) vs Struct of Arrays (SoA) Data Layouts**

## Overview

The project empirically benchmarks two different data organization strategies commonly used in scientific and high-performance computing:  
- **Array of Structs (AoS)**
- **Struct of Arrays (SoA)**

It simulates a simple particle update task and compares the runtime efficiency of both approaches.

## Folder Structure

```text
.
├── benchmarks/        # Output results and plots (e.g., results.csv, runtime_plot.png)
├── src/               # Source code for benchmarks
├── plot_results.py    # Script for plotting the runtime comparison
├── requirements.txt   # Python dependencies
└── .venv/             # Python virtual environment (not required for submission)
```


## Files

- `src/aos_vs_soa.py` — Main script for benchmarking AoS vs SoA
- `plot_results.py` — Reads CSV output and generates a log-log runtime plot
- `requirements.txt` — List of Python packages needed (e.g., numpy, pandas, matplotlib)
- `benchmarks/results.csv` — Collected benchmarking results
- `benchmarks/runtime_plot.png` — Plot comparing AoS and SoA performance

## How to Run

1. **Set up the Python environment:**

   ```sh
   python -m venv .venv
   .venv\Scripts\activate   # (Windows)
   pip install -r requirements.txt

2. **Run the benchmark:**

   ```sh
   python -m src.aos_vs_soa --n 10000 --steps 200

3. **Plot the results:**

   ```sh
   python plot_results.py

The plot will be saved as benchmarks/runtime_plot.png.


## Output

The script produces a CSV of benchmark results and a log-log plot comparing the runtime performance of AoS vs SoA layouts.
