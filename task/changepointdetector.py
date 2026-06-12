import csv
import statistics
import matplotlib.pyplot as plt
import pandas as pd

#changepoint detector will probabyl start tomorrow so i dont forget anything
def changepointdetection(p_or_m):
    memory_usage_data = []
    dates = []
    changepoints = []   # store indices of changepoints

    def choice(p_or_m):
        if p_or_m == "memory":
            return "/home/georgerhodes/Desktop/work-experience/task/data/memory_data.csv"
        elif p_or_m == "performance":
            return "/home/georgerhodes/Desktop/work-experience/task/data/performance_data.csv"
        
    # Load CSV
    with open(choice(p_or_m),"r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            memory_usage_data.append(float(row[1]))
            dates.append(row[0])

    # Detect changepoints
    for i in range(1, len(memory_usage_data)):
        diff = memory_usage_data[i] - memory_usage_data[i-1]

        if abs(diff) > 10:
            print(f"Changepoint at {dates[i]} with change {diff}")
            changepoints.append(i)

    # ---- PLOTTING ----
    plt.figure(figsize=(12, 6))
    plt.plot(memory_usage_data, label="Usage", linewidth=2)

    # Add vertical lines for changepoints
    for cp in changepoints:
        plt.axvline(x=cp, color='red', linestyle='--', linewidth=1.5)

    plt.title("Usage Data with Changepoints")
    plt.xlabel("Index (time order)")
    plt.ylabel("Usage Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

choice = input("Enter 'p' for performance or 'm' for memory")

changepointdetection(choice)