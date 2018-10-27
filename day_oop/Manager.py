from day_oop.Employee import Employee
from day_oop.Developer import Developer

class Manager(Employee):

    def __init__(self, first_name, last_name, email, pay, employees=None):
        super().__init__(first_name, last_name, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def display(self):
        print("Manager:")
        super().display()
        print("Employees:")
        for emp in self.employees:
            Employee.display(emp)





dev1 = Developer("Venkatram","Veerareddy","venkat.veeraeddy@gmail.com",40000,"Python")

mgr1 = Manager("Srijan","Veerareddy","srijan.veerareddy@gmail.com",50000,[dev1])

mgr1.display()

print(isinstance(mgr1, Employee))

print(issubclass(dev1, Employee))