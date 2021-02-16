from day_oop.Employee import Employee

class Developer(Employee):
    raise_amount = 1.10 #overring the property

    def __init__(self, first_name, last_name, email, pay, prog_lang):  # constructor
        super().__init__(first_name, last_name, email, pay)
        #Employee.__init__(self, first_name, last_name, email, pay)
        self.prog_lang = prog_lang

    def display(self):
        super().display()
        print(self.prog_lang)


if __name__ == '__main__':
    print(help(Developer))

    dev1 = Developer("Venkatram", "Veerareddy", "venkat.veeraeddy@gmail.com", 40000, "Python")
    dev1.apply_amount()
    dev1.display()



