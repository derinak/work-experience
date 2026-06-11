#!/usr/bin/env python3


import csv
import statistics
from matplotlib import dates
import matplotlib.pyplot as plt
import pandas as pd

filename = ""

value = {
    "metric_runs": "metric1_run1.pq",
    "values": [2,10,10]
}
print(value)
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
        # Determine window boundaries
        start = max(0, i - window_size)
        end = i + 1

        window = memory_usage_data[start:end]

        median = statistics.median(window)
        stdev = statistics.pstdev(window)

        lower_bound = median - factor * stdev
        upper_bound = median + factor * stdev

        if memory_usage_data[i] < lower_bound or memory_usage_data[i] > upper_bound:
            anomalies.append(dates[i])
            anomalies.append(memory_usage_data[i])
    print("Anomalies:", anomalies)
    return anomalies

def anomaly_indices(anomalies, dates):
    idx = []
    for i in range(0, len(anomalies), 2):
        date = anomalies[i]
        idx.append(dates.index(date))
    return set(idx)

def changepointdetection(memory_usage_data, dates, threshold, ignore_idx=None):
    changepoints = []
    threshold = int(threshold)

    if ignore_idx is None:
        ignore_idx = set()

    for i in range(1, len(memory_usage_data)):
        if i in ignore_idx or (i - 1) in ignore_idx:
            continue  # skip anomaly points entirely

        diff = memory_usage_data[i] - memory_usage_data[i - 1]

        if abs(diff) > threshold:
            print("Changepoint at", dates[i], "change:", abs(diff))
            changepoints.append(dates[i])

    return changepoints

def plotdata(data,data1,title, anom, changepoints):
    plt.title(title)
    plt.xlabel("Date & Time")
    plt.ylabel("Reboot Time")
    plt.plot(data,data1, marker ="*")
    anom_times = anom[0::2]   
    anom_values = anom[1::2]
    plt.scatter(anom_times, anom_values, color="red", s=120, label="Highlighted")
    if changepoints is not None:
        for cp in changepoints[1::2]:
            plt.axvline(x=cp, color="green", linestyle="--", linewidth=1.25)
            plt.text(cp, max(data1), "CP", rotation=90, va="bottom", ha="right")
    plt.show()

factor = input("What factor of deviation for Anomalies?")
def plotdata(data,data1,title, anom, changepoints):
    plt.title(title)
    plt.xlabel("Date & Time")
    plt.ylabel("Reboot Time")
    plt.plot(data,data1, marker ="*")
    anom_times = anom[0::2]   
    anom_values = anom[1::2]
    plt.scatter(anom_times, anom_values, color="red", s=120, label="Highlighted")
    if changepoints is not None:
        for cp in changepoints[1::2]:
            plt.axvline(x=cp, color="green", linestyle="--", linewidth=1.25)
            plt.text(cp, max(data1), "CP", rotation=90, va="bottom", ha="right")
    plt.show()
window_size = input("What window size for Anomalies?")

threshold = input("What threshold for Changepoints?")

for x in range(4,11):
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
    if x==4:
        filename="task/real_data/metric1_run1.pq"
    elif x==5:
        filename="task/real_data/metric1_run2.pq"
    elif x==6:
        filename="task/real_data/metric1_run3_high_variance.pq"
    # elif x==7:
    #     filename="task/real_data/metric2_large_breakdown_run1.pq"
    #     rows= 3
    elif x==7:
        filename="task/real_data/metric2_large_run1.pq"
    # elif x==9:
    #     filename="task/real_data/metric2_small_breakdown_run1.pq"
    #     rows = 3
    elif x==8:
        filename="task/real_data/metric2_small_run1.pq"
    elif x==9:
        filename="task/real_data/metric3_run1.pq"
    
    df = pd.read_parquet(filename)
    print(df)
    filedata = []
    dates = []
    for row in df.itertuples():
        filedata.append(row[rows])
        dates.append(row[1])
    
    
    
    anom = deviation(factor, filedata, dates, window_size)
    ignore_idx = anomaly_indices(anom, dates)

    cp = changepointdetection(filedata, dates, threshold, ignore_idx)

    plt.figure()
    plotdata(dates, filedata, filename, anom, cp)