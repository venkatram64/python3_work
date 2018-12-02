

def add_one(my_func):
    def inside_func():
        return my_func() + 1
    return inside_func


def add():
    return 9



if __name__ == '__main__':
    new_f = add_one(add)
    print(new_f())