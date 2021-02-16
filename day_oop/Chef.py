
#https://stackoverflow.com/questions/48845989/understanding-class-type-main-classname

#https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3

class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes salad ")

    def make_special_dish(self):
        print("The chef makes bbq ribs")

    # magic or DUNDER methods
    def __repr__(self):
        return "Chef" #Chef('{}')".format(self)

    # magic or DUNDER methods  , comment and test and un comment
    def __str__(self):
        return "'{}'".format(Chef)


if __name__ == '__main__':
    chef = Chef()
    print(repr(chef))
    print(str(chef))

    print(chef) # by default str will be called

    print(1 + 2)
    print(int.__add__(1,2)) #dunder methods
    print(str.__add__('a', 'b'))  # dunder methods

