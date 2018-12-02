

def add_one(my_func):
    def inside_func():
        return my_func() + 1
    return inside_func

@add_one
def add():
    return 9

"""
Decorators add a little something extra to something else
Decorators add something and an existing functions.
"""

if __name__ == '__main__':
    print(add())