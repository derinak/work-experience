import csv
import statistics
import matplotlib.pyplot as plt
#changepoint detector will probabyl start tomorrow so i dont forget anything

memory_usage_data = []
dates = []
with open("/home/georgerhodes/Desktop/work-experience/task/data/performance_data.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row[1])
        memory_usage_data.append(row[1])
        print(row[0])
        dates.append(row[0])
memory_usage_data = list(map(float, memory_usage_data))
#got all the dates and usage numbers into tables

print(memory_usage_data)

for i in range(1,len(memory_usage_data)):
    for r in range(i+1,len(memory_usage_data)+1):
        mean=statistics.mean(memory_usage_data[i:r])
        print(mean)
        means = []
        means.append(mean)


plt.plot(means)
plt.show()
