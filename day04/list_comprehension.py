def list_comprehension():
    #my_num = [x*x for x in [1, 2, 3, 4, 5, 6]]
    my_num = (x * x for x in [1, 2, 3, 4, 5, 6])   #generator
    return my_num


if __name__ == '__main__':

    for num in list_comprehension():
        print(num)