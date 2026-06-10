import csv
import statistics
from matplotlib import dates
import matplotlib.pyplot as plt
import pandas as pd

filename = "task/real_data/metric1_run1.pq"


df = pd.read_parquet(filename)
#print(df)
filedata = []
dates = []
for row in df.itertuples():
    filedata.append(row[2])
    dates.append(row[1])
#print(filedata)
#print(dates)


def deviation(factor, memory_usage_data, dates):
    anomalies = []
    factor = float(factor)
    

    
    memory_usage_data = list(map(float, memory_usage_data))

    mean=(statistics.mean(memory_usage_data))

    #print(mean)

    lower_bound = mean-(factor * statistics.pstdev(memory_usage_data))
    upper_bound = mean+(factor * statistics.pstdev(memory_usage_data))

    #print(lower_bound)
    #print(upper_bound)

    for num in range(len(memory_usage_data)):
        if memory_usage_data[num] < lower_bound or memory_usage_data[num] > upper_bound:
            anomalies.append(dates[num])
            anomalies.append(memory_usage_data[num])
    print("Anomalies are ",anomalies)
    return anomalies

def changepointdetection(memory_usage_data, dates):
    changepoints = []
    for i in range(1,len(memory_usage_data)):
        if memory_usage_data[i] > memory_usage_data[i-1]:
            if memory_usage_data[i] - memory_usage_data[i-1] > 10:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i] - memory_usage_data[i-1])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])
                changepoints.append(dates[i])
        elif memory_usage_data[i] < memory_usage_data[i-1]:
            if memory_usage_data[i-1] - memory_usage_data[i] > 10:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i-1] - memory_usage_data[i])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])
                changepoints.append(dates[i])
    return changepoints


def plotdata(data,data1,title):
    plt.title(title)
    plt.xlabel("Date & Time")
    plt.ylabel("Reboot Time")
    plt.plot(data,data1)
    plt.show()

print(deviation(2, filedata, dates))
print(changepointdetection(filedata, dates))
#plotdata(dates , filedata , filename)