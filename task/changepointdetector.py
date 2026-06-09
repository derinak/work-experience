import csv
#changepoint detector will probabyl start tomorrow so i dont forget anything

memory_usage_data = []
dates = []
with open("/home/georgerhodes/Desktop/work-experience/task/data/memory_data.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row[1])
        memory_usage_data.append(row[1])
        print(row[0])
        dates.append(row[0])
memory_usage_data = list(map(float, memory_usage_data))
#got all the dates and usage numbers into tables