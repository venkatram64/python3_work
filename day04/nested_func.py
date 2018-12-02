

def outside():
    my_local_value = "I'm inside function"
    def inside():
        print(my_local_value)
    return inside


if __name__ == '__main__':
    my_func = outside()
    my_func()