import csv

file = open("google_stock_data.csv", newline='')
reader = csv.reader(file)

header = next(reader)  #The first line is the header
data = [row for row in reader]

print(header)
print(data[0])
