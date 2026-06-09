import statistics
import csv

def deviation(deviate_amount):
    memory_usage_data = []


    with open("/home/georgerhodes/Downloads/memory_data.csv","r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row[1])
            memory_usage_data.append(row[1])

    memory_usage_data = list(map(float, memory_usage_data))

    #breakpoint()

    mean=(statistics.mean(memory_usage_data))

    print(mean)

    lower_bound = mean-(deviate_amount * statistics.pstdev(memory_usage_data))

    upper_bound = mean+(deviate_amount * statistics.pstdev(memory_usage_data))

    print(lower_bound)
    print(upper_bound)
amount = input("enter the factor of deviation")
deviation(amount)