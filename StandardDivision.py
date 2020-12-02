import csv 
import math
with open("data.csv",newline='') as f:
    csvReader = csv.reader(f)
    csvData = list(csvReader)

file_data = csvData[0]

sum_of_data = 0

for i in file_data:
    sum_of_data += int(i)


no_of_data = len(file_data)

def Mean():
    mean = sum_of_data/no_of_data
    return mean

squared_list = []

for a in file_data:
    b = int(a)-Mean()
    b = b**2
    squared_list.append(b)

sum_of_square = sum(squared_list)
standard_deviation = math.sqrt(sum_of_square/no_of_data)
print(standard_deviation)
