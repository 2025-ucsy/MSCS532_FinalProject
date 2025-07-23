"""
Reads benchmarks/results.csv and saves benchmarks/runtime_plot.png
(log-log AoS vs SoA runtime curves).
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the results CSV file
csv = os.path.join("benchmarks", "results.csv")
df = pd.read_csv(csv)

# Create the plot (log-log scale)
plt.figure()
plt.loglog(df["n"], df["aos_s"], marker="o", label="AoS (Array of Structs)")
plt.loglog(df["n"], df["soa_s"], marker="o", label="SoA (Struct of Arrays)")
plt.xlabel("Particles (log scale)")
plt.ylabel("Runtime (seconds, log scale)")
plt.title("AoS vs SoA Runtime Performance")
plt.legend()
out = os.path.join("benchmarks", "runtime_plot.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Saved → {out}")
