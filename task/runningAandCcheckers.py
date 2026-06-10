import csv
import statistics
from matplotlib import dates
import matplotlib.pyplot as plt
import pandas as pd

filename = "task/real_data/metric2_small_run1.pq"


df = pd.read_parquet(filename)
print(df)
filedata = []
dates = []
for row in df.itertuples():
    filedata.append(row[2])
    dates.append(row[1])
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

def changepointdetection(memory_usage_data, dates, threshold):
    changepoints = []
    threshold = int(threshold)
    for i in range(1,len(memory_usage_data)):
        if memory_usage_data[i] > memory_usage_data[i-1]:
            if memory_usage_data[i] - memory_usage_data[i-1] > threshold:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i] - memory_usage_data[i-1])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])
                changepoints.append(dates[i])
        elif memory_usage_data[i] < memory_usage_data[i-1]:
            if memory_usage_data[i-1] - memory_usage_data[i] > threshold:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i-1] - memory_usage_data[i])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])
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

window_size = input("What window size for Anomalies?")

threshold = input("What threshold for Changepoints?")

print(deviation(factor, filedata, dates,window_size))

plotdata(dates , filedata , filename, deviation(factor, filedata, dates, window_size), changepointdetection(filedata, dates, threshold))
