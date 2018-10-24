from Employee import Employee

class Developer(Employee):
    raise_amount = 1.10


#print(help(Developer))

dev1 = Developer("Venkatram","Veeraredd","venkat.veeraeddy@gmail.com",40000)
dev1.apply_amount()
dev1.display()



