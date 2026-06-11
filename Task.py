#!/usr/bin/env python3
import statistics
import math
import pandas as pd
import matplotlib.pyplot as plt

def detect_anomalies(data, window_size=40, n_sigma=2):
    anomaly = []
    for i in range(window_size, len(data)): # For each point after window_size:
        window = data[i - window_size : i] # 1. Get recent window of data
        if data[i] > statistics.mean(window) + (n_sigma * statistics.stdev(window)): # 2. Calculate mean and std_dev # 3. Set threshold = mean + (n_sigma * std_dev)
            anomaly.append(i) # 4. If current value > threshold, mark as anomaly
            print(anomaly)
    return anomaly


def detect_changepoints(data, min_size=10):
    divergence = {}
    for c in range(min_size, len(data) - min_size): # For each possible split point:
        before, after = data[:c], data[c:] # 1. Split data into before/after groups
        difference = abs(statistics.mean(before) - statistics.mean(after)) # 2. Calculate mean and std_dev for each group
        average = math.sqrt((statistics.stdev(before) ** 2 + statistics.stdev(after) ** 2) / 2)
        divergence[c] = difference
    if not divergence:
        return []
    largest_shifts = sorted(divergence.keys(), key=lambda x: divergence[x], reverse=True) # 4. Keep split with maximum divergence
    final_cps = []
    for cp in largest_shifts: # 5. Filter nearby changepoints
        if all(abs(cp - existing) >= min_size for existing in final_cps):
            final_cps.append(cp)
    print(final_cps)
    return sorted(final_cps)


def check_router(parquet_path):
    df = pd.read_parquet(parquet_path)
    value1 = df["total_size"].tolist()
    value2 = list(range(len(value1)))
    anomalies = detect_anomalies(value1)
    clean_data = [value1[i] for i in range(len(value1)) if i not in anomalies]
    changepoints = detect_changepoints(clean_data)
    print(f"Mean: {statistics.mean(value1):.2f} | StdDev : {statistics.stdev(value1):.2f}")
    print(f"Anomalies: {anomalies} | Changepoints: {changepoints}")
    plt.plot(value2, value1, label='Reload time')
    plt.scatter(anomalies, [value1[i] for i in anomalies], color='r', label='Anomalies')
    if changepoints:
        divergence_scores = {}
        for c in changepoints:
            before, after = value1[:c], value1[c:]
            divergence_scores[c] = abs(statistics.mean(before) - statistics.mean(after))
        score_sort = sorted(divergence_scores.keys(), key=lambda x: divergence_scores[x], reverse=True)
        top_cp = []
        for cp in score_sort:
            if all(abs(cp - existing) >= 20 for existing in top_cp):
                top_cp.append(cp)
            if len(top_cp) == 3:
                break
    else:
        top_cp = []
    for i,cp in enumerate(top_cp):
        plt.axvline(cp, color='purple', ls ='--', label='Changepoints' if i == 0 else "")
    plt.title("Memory Usage")
    plt.xlabel("Time sequence")
    plt.ylabel("Memory used")
    plt.legend()
    plt.savefig('3_memory_usage.png')
    
def main():
    check_router('task/real_data/metric3_run1.pq')

main()

