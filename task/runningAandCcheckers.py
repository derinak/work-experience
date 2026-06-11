#!/usr/bin/env python3


import csv
import statistics
from matplotlib import dates
import matplotlib.pyplot as plt
import pandas as pd

filename = ""

value = [
    "metric1_run1.pq",
    "2,10,10",
    "metric1_run2.pq",
    "2,2,15",
    "metric1_run3_high_variance.pq",
    "2,10,10",
    "metric2_large_run1.pq",
    "2,10,10",
    "metric2_small_run1.pq",
    "2,10,10",
    "metric3_run1.pq",
    "2,10,10"
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

def changepointdetection(data, dates, threshold):
    changepoints = []
    changepoint_dates = []
    threshold = int(threshold)
    for split_point in range(threshold, len(data)- threshold):
        before_group = data[0:split_point]
        after_group = data[split_point:]

        mean_before = statistics.mean(before_group)
        mean_after = statistics.mean(after_group)
        std_before = statistics.stdev(before_group)
        std_after = statistics.stdev(after_group)
        
        combined_std = statistics.sqrt((std_before**2 + std_after**2) / 2)

        if combined_std == 0:
            continue


        divergence = abs(mean_after - mean_before) / combined_std
        if divergence > 2.0:
            changepoints.append(split_point)
            changepoint_dates.append(dates[split_point])

    print("Changepoints detected:")
    for i, date in enumerate(changepoint_dates):
        print(f"  Index: {changepoints[i]}, Date: {date}")
    
    return changepoints

def plotdata(dates, values, title, anomalies, changepoints):
    plt.title(title)
    plt.xlabel("Date & Time")
    plt.ylabel("Reboot Time")

    # Main line
    plt.plot(dates, values, marker="*", label="Data")

    # Plot anomalies
    if anomalies:
        anom_dates = [a[0] for a in anomalies]
        anom_vals = [a[1] for a in anomalies]
        plt.scatter(anom_dates, anom_vals, color="red", s=120, label="Anomalies")

    # Plot changepoints
    if changepoints:
        for cp in changepoints:
            plt.axvline(x=dates[cp], color="green", linestyle="--", linewidth=1.25)
            plt.text(dates[cp], max(values), "CP", rotation=90, va="bottom", ha="right")

    plt.legend()
    plt.tight_layout()
    plt.show()


window_size_avrg = 10#input("What window size for the moving average?")

for x in range(1,6):
    rows=2
    # if x==1:
    #     filename="task/real_data/metric1_breakdown_run1.pq"
    #     rows = 3
    # elif x==2:
    #     filename="task/real_data/metric1_breakdown_run2.pq"
    #     rows = 3
    # elif x==3:
    #     filename="task/real_data/metric1_breakdown_run3_high_variance.pq"
    #     rows = 3 
    if x==1:
        filename="task/real_data/metric1_run1.pq"
        print(value[x-1])
        print(value[x])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    elif x==2:
        filename="task/real_data/metric1_run2.pq"
        print(value[x])
        print(value[x+1])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    elif x==3:
        filename="task/real_data/metric1_run3_high_variance.pq"
        print(value[x+1])
        print(value[x+2])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    # elif x==7:
    #     filename="task/real_data/metric2_large_breakdown_run1.pq"
    #     rows= 3
    elif x==4:
        filename="task/real_data/metric2_large_run1.pq"
        print(value[x+2])
        print(value[x+3])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    # elif x==9:
    #     filename="task/real_data/metric2_small_breakdown_run1.pq"
    #     rows = 3
    elif x==5:
        filename="task/real_data/metric2_small_run1.pq"
        print(value[x+3])
        print(value[x+4])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    elif x==6:
        filename="task/real_data/metric3_run1.pq"
        print(value[x+4])
        print(value[x+5])
        factor = input("What factor of deviation for Anomalies in " + filename + "?")
        window_size = input("What window size for Anomalies in " + filename + "?")
        threshold = input("What threshold for Changepoints in " + filename + "?")
    
    df = pd.read_parquet(filename)
    print(df)
    filedata = []
    dates = []
    for row in df.itertuples():
        filedata.append(row[rows])
        dates.append(row[1])
    
    plt.figure()
    plotdata(dates, filedata, filename, deviation(factor, filedata, dates, window_size), changepointdetection(filedata, dates, threshold))#could have rolling avg instead of filedata for the changepoint detection function