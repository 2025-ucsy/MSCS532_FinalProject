"""
AoS vs SoA benchmark prototype • MSCS-532 Final Project (Part 1)
Run:    python -m src.aos_vs_soa --n 100000 --steps 200
"""

import argparse, time, os
import numpy as np
import pandas as pd

def aos_update(particles, dt):
    for p in particles:
        p["x"] += p["vx"] * dt
        p["y"] += p["vy"] * dt
        p["z"] += p["vz"] * dt

def soa_update(arrays, dt):
    arrays["x"] += arrays["vx"] * dt
    arrays["y"] += arrays["vy"] * dt
    arrays["z"] += arrays["vz"] * dt

def benchmark(n, steps, dt=0.01):
    # AoS: list-of-dicts
    aos = [{"x":0., "y":0., "z":0., "vx":1., "vy":1., "vz":1.} for _ in range(n)]
    t0 = time.perf_counter()
    for _ in range(steps):
        aos_update(aos, dt)
    aos_t = time.perf_counter() - t0

    # SoA: numpy arrays
    soa = {k: np.zeros(n, dtype=np.float64) for k in ("x","y","z","vx","vy","vz")}
    soa["vx"].fill(1.); soa["vy"].fill(1.); soa["vz"].fill(1.)
    t0 = time.perf_counter()
    for _ in range(steps):
        soa_update(soa, dt)
    soa_t = time.perf_counter() - t0

    return {"n": n, "steps": steps, "aos_s": aos_t, "soa_s": soa_t, "speedup": aos_t/soa_t}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10000, help="Number of particles")
    parser.add_argument("--steps", type=int, default=200, help="Number of update steps")
    parser.add_argument("--output", type=str, default="benchmarks/results.csv", help="CSV file for results")
    args = parser.parse_args()

    # Multiple sizes for scaling (you can adjust as needed)
    ns = [args.n] if args.n else [1000, 10000, 50000, 100000, 200000]
    results = []
    for n in ns:
        r = benchmark(n, args.steps)
        print(f"n={r['n']}, steps={r['steps']}: "
              f"AoS {r['aos_s']:.3f}s | SoA {r['soa_s']:.3f}s -> x{r['speedup']:.1f}")
        results.append(r)
    df = pd.DataFrame(results)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"Saved results to {args.output}")
