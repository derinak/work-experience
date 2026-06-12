#!/usr/bin/env python3


import csv
import statistics
from matplotlib import dates
import matplotlib.pyplot as plt
import pandas as pd
import math

filename = ""

runs = [
    ("task/real_data/metric1_run1.pq", "2,10,3"),
    ("task/real_data/metric1_run2.pq", "2,2,3"),
    ("task/real_data/metric1_run3_high_variance.pq", "2,2,3"),
    ("task/real_data/metric2_large_run1.pq", "2,5,1"),
    ("task/real_data/metric2_small_run1.pq", "2,5,3"),
    ("task/real_data/metric3_run1.pq", "2,10,3"),
]
#print(value)
#df = pd.read_parquet(filename)
#print(df)
#filedata = []
#dates = []
#for row in df.itertuples():
    #filedata.append(row[2])
    #dates.append(row[1])
#print(filedata)
#print(dates)

def deviation(factor, memory_usage_data, dates, window_size):
    anomalies = []
    factor = float(factor)
    window_size = int(window_size)
    memory_usage_data = list(map(float, memory_usage_data))

    for i in range(len(memory_usage_data)):
        start = max(0, i - window_size)
        end = i + 1
        window = memory_usage_data[start:end]

        median = statistics.median(window)
        stdev = statistics.pstdev(window)

        lower = median - factor * stdev
        upper = median + factor * stdev

        if memory_usage_data[i] < lower or memory_usage_data[i] > upper:
            anomalies.append((dates[i], memory_usage_data[i]))

    return anomalies

def rolling_average(data, window_size):
    rolling_averages = []
    window_size = int(window_size)
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        window = data[start:i + 1]
        average = sum(window) / len(window)
        rolling_averages.append(average)
    print("Rolling Averages:", rolling_averages)
    return rolling_averages

def changepointdetection(data, dates, divergence_threshold, window=30):
    changepoints = []
    changepoint_dates = []
    changepoint_divergence = []
    divergence_threshold = float(divergence_threshold)
    for split_point in range(window, len(data) - window):
        before_group = data[split_point - window : split_point]
        after_group  = data[split_point : split_point + window]

        mean_before = statistics.mean(before_group)
        mean_after = statistics.mean(after_group)

        std_before = statistics.stdev(before_group)
        std_after = statistics.stdev(after_group)

        combined_std = math.sqrt((std_before**2 + std_after**2) / 2)

        if combined_std == 0:
            continue

        divergence = abs(mean_after - mean_before) / combined_std
       
        if divergence > divergence_threshold:
            changepoints.append(split_point)
            changepoint_dates.append(dates[split_point])
            changepoint_divergence.append(divergence)

    print(changepoints)

    filtered = []
    i = 0

    while i < len(changepoints):
        cluster = [i]
        j = i + 1

        while j < len(changepoints) and changepoints[j] - changepoints[i] < 25:
            cluster.append(j)
            j += 1

        best = max(cluster, key=lambda k: changepoint_divergence[k])
        filtered.append(best)

        i = j

    print(filtered)



    # print("Changepoints detected:")
    # for i, date in enumerate(changepoint_dates):
    #     print(f"  Index: {changepoints[i]}, Date: {date}")
    
    return [changepoints[k] for k in filtered]

def plotdata(dates, values, avg_values, title, anomalies, changepoints):
    plt.title(title)
    plt.xlabel("Date & Time")
    plt.ylabel("Reboot Time")

    
    plt.plot(dates, avg_values, marker="*", label="Data")

    
    plt.plot(
        dates,
        values,
        color="blue",
        alpha=0.25,   
        linewidth=2,
        label="Raw Data"
    )

    if anomalies:
        anom_dates = [a[0] for a in anomalies]
        anom_vals = [a[1] for a in anomalies]
        plt.scatter(anom_dates, anom_vals, color="red", s=120, label="Anomalies")


    if changepoints:
        for cp in changepoints:
            plt.axvline(x=dates[cp], color="green", linestyle="--", linewidth=1.25)
            plt.text(dates[cp], max(values), "CP", rotation=90, va="bottom", ha="right")

    plt.legend()
    plt.tight_layout()
    plt.show()



window_size_avrg = 10#input("What window size for the moving average?")

for filename, meta in runs:
    print(filename)
    print(meta)

    factor = input(f"What factor of deviation for Anomalies in {filename}? ")
    window_size = input(f"What window size for Anomalies in {filename}? ")
    threshold = input(f"What threshold for Changepoints in {filename}? ")

    
    df = pd.read_parquet(filename)
    print(df)
    filedata = []
    dates = []
    for row in df.itertuples():
        filedata.append(row[2])
        dates.append(row[1])
    
    plt.figure()

    avg = rolling_average(filedata, window_size_avrg)

    plotdata(dates,filedata,avg,filename,deviation(factor, filedata, dates, window_size),changepointdetection(rolling_average(filedata, window_size_avrg), dates, threshold))#