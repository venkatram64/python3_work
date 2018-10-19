

file = open("google_stock_data.csv")
"""for line in file:
    print(line)
    
    """

lines = [line for line in open("google_stock_data.csv")]

print(lines[0].strip())


csv = lines[0].strip().split(",")

print(csv)