

employee_file = open("employee.txt", "r")

for employee in employee_file.readlines():
    print(employee)

#print(employee_file.readable())

#print(employee_file.read())

employee_file.close()