import statistics
import csv

def deviation():
    memory_usage_data = []
    anomalies = []
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


deviation()