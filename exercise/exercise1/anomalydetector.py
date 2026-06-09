import statistics
import csv

memory_usage_data = []


with open("/home/georgerhodes/Downloads/memory_data.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row[1])
        memory_usage_data.append(row[1])

print(statistics.mean(memory_usage_data))