import csv
import statistics
import matplotlib.pyplot as plt
import pandas as pd

#changepoint detector will probabyl start tomorrow so i dont forget anything
def changepointdetection(p_or_m):
    memory_usage_data = []
    dates = []
    
    def choice(p_or_m):
        if p_or_m == "memory":
            return "/home/georgerhodes/Desktop/work-experience/task/data/memory_data.csv"
        elif p_or_m == "performance":
            return "/home/georgerhodes/Desktop/work-experience/task/data/performance_data.csv"
        
    with open(choice(p_or_m),"r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
        print(row[1])
        memory_usage_data.append(row[1])
        print(row[0])
        dates.append(row[0])
    memory_usage_data = list(map(float, memory_usage_data))
    #got all the dates and usage numbers into tables

    #print(memory_usage_data)

    for i in range(1,len(memory_usage_data)):
        if memory_usage_data[i] > memory_usage_data[i-1]:
            if memory_usage_data[i] - memory_usage_data[i-1] > 10:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i] - memory_usage_data[i-1])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])
        elif memory_usage_data[i] < memory_usage_data[i-1]:
            if memory_usage_data[i-1] - memory_usage_data[i] > 10:    
                print("Changepoint at ",dates[i]," with a change of ",memory_usage_data[i-1] - memory_usage_data[i])
                print("new value: ",memory_usage_data[i])
                print("old value: ",memory_usage_data[i-1])