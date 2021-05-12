import statistics
import csv

# reads csv file
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# To remove headers from CSV
file_data.pop(0)

total_weight = 0
total_entries = len(file_data)
data = []

for person_data in file_data:
    total_weight += float(person_data[2])
    data.append(float(person_data[2]))

data.sort()

print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
