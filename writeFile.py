
employee_file = open("employee.txt", "a")

employee_file.write("Toby - Human Resources")

employee_file.close()

with open("employee.txt", "r") as my_file:
    contents = my_file.readlines()
    for line in contents:
        print(line)


