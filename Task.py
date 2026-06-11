#!/usr/bin/env python3
import statistics
import math
import pandas as pd
import matplotlib.pyplot as plt

def detect_anomalies(data, window_size=20, n_sigma=3.5):
    anomaly = []
    for i in range(window_size, len(data)):
        window = data[i - window_size : i]
        median = statistics.median(window)
        mad = statistics.median([abs(x - median) for x in window]) or 1.0
        if data[i] > median + (n_sigma * 1.4826 * mad):
            anomaly.append(i)
            print(anomaly)
    return anomaly


def detect_changepoints(data, min_size=10):
    divergence = {}
    for c in range(min_size, len(data) - min_size): 
        before, after = data[:c], data[c:] 
        difference = abs(statistics.mean(before) - statistics.mean(after)) 
        try:
            std_b = statistics.stdev(before)
        except statistics.StatisticsError:
            std_b = 0.0
        try:
            std_a = statistics.stdev(after)
        except statistics.StatisticsError:
            std_a = 0.0
        average = math.sqrt((std_b**2 + std_a**2) / 2) or 1.0
        divergence[c] = difference / average
    if not divergence:
        return []
    largest_shifts = sorted(divergence.keys(), key=lambda x: divergence[x], reverse=True) 
    final_cps = []
    for cp in largest_shifts: 
        if all(abs(cp - existing) >= min_size for existing in final_cps):
            final_cps.append(cp)
    print(final_cps)
    return sorted(final_cps)


def check_router(parquet_path):
    df = pd.read_parquet(parquet_path)
    value1 = df["total_seconds"].tolist()
    value2 = list(range(len(value1)))
    anomalies = detect_anomalies(value1)
    clean_data = list(value1)
    for idx in anomalies:
        clean_data[idx] = statistics.median(value1[max(0, idx-10):min(len(value1), idx+10)])
    changepoints = detect_changepoints(clean_data)
    print(f"Mean: {statistics.mean(value1):.2f} | StdDev : {statistics.stdev(value1):.2f}")
    print(f"Anomalies: {anomalies} | Changepoints: {changepoints}")
    plt.plot(value2, value1, label='Reload time')
    plt.scatter(anomalies, [value1[i] for i in anomalies], color='r', label='Anomalies')
    if changepoints:
        div_scores = {c: abs(statistics.mean(value1[:c]) - statistics.mean(value1[c:])) for c in changepoints}
        score_sort = sorted(div_scores.keys(), key=lambda x: div_scores[x], reverse=True)
        top_cp = []
        for cp in score_sort:
            if all(abs(cp - e) > 40 for e in top_cp): top_cp.append(cp)
            if len(top_cp) == 2: break
    else:
        top_cp = []
    for i,cp in enumerate(top_cp):
        plt.axvline(cp, color='purple', ls ='--', label='Changepoints' if i == 0 else "")
    plt.title("Reload time")
    plt.xlabel("Time sequence")
    plt.ylabel("Duration")
    plt.legend()
    plt.savefig('1_reload_time_1.png')
    
def main():
    check_router('task/real_data/metric1_run1.pq')

main()
