
class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + "@gmail.com"

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete Name!')
        self.first = None
        self.last = None


if __name__ == '__main__':
    p = Person("Venkatram", "Veerareddy")
    p.first = "Srijan"
    p.fullName = "Venkatram Veerareddy"
    print(p.first)
    print(p.last)
    print(p.email)
    #print(p.fullName())
    print(p.fullName)
    del p.fullName