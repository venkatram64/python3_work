import datetime

class Employee:

    raise_amount = 1.04    # class variable
    no_of_employees = 0

    def __init__(self, first_name, last_name, email, pay):    # constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay
        Employee.no_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def display(self):
        print(self.fullname())
        print('{} {}'.format(self.email, str(self.pay)))

    def apply_amount(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):     #alternative constructor or class method
        first, last, email, pay = emp_str.split('-')
        return cls(first, last, email, float(pay))

    @staticmethod
    def is_workday(day):  #static method
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True



emp1 = Employee("Venkatram", "veerareddy", "venkat.veerareddy@gmail.com",50000)

emp2 = Employee("Srijan", "veerareddy", "srijan.veerareddy@gmail.com",500000)

emp1.apply_amount()

emp1.display()

print(emp1.__dict__)

""" dictionary, see there is no raise_amount, so it is a class variable not a 
 instance variable
 {'first_name': 'Venkatram', 'last_name': 'veerareddy', 'email': 'venkat.veerareddy@gmail.com', 'pay': 52000}
"""

Employee.set_raise_amount(1.2)
emp2.apply_amount()
emp2.display()

emp3 = Employee.from_string("Winnie-Veerareddy-Winnie.Veerareddy@gmail.com-60000")
emp3.display()

my_date = datetime.date(2018, 10, 24)

print("Is today working day? " + str(Employee.is_workday(my_date)))



