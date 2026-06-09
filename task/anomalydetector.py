import statistics
import csv

def deviation(p_or_m):
    memory_usage_data = []
    anomalies = []
    dates = []

    def choice(p_or_m):
        if p_or_m == "memory":
            return "/home/georgerhodes/Desktop/work-experience/task/data/memory_data.csv"
        elif p_or_m == "performance":
            return "/home/georgerhodes/Desktop/work-experience/task/data/performance_data.csv"
        
    #choice between performance table and memory table
    #performance memory data output is kind of mess up as there is such a large range hence the requirement of changepoint detection, after that is made should allow the specification of windows of the data

    with open(choice(p_or_m),"r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row[1])
            memory_usage_data.append(row[1])
            print(row[0])
            dates.append(row[0])
    memory_usage_data = list(map(float, memory_usage_data))

    #breakpoint()

    mean=(statistics.mean(memory_usage_data))

    print(mean)

    lower_bound = mean-(2 * statistics.pstdev(memory_usage_data))
#function parameter kept flahing error as it was an int not float or smth so i got rid of it until the thing fully works then i can make QOL features like that
    upper_bound = mean+(2 * statistics.pstdev(memory_usage_data))

    print(lower_bound)
    print(upper_bound)

    for num in range(len(memory_usage_data)):
        if memory_usage_data[num] < lower_bound or memory_usage_data[num] > upper_bound:
            anomalies.append(dates[num])
            anomalies.append(memory_usage_data[num])
    print("Anomalies are ",anomalies)

choice = input("Would you like 'memory' data or 'performance' data, type the exact words")
deviation(choice)