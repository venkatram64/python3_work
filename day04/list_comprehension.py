def list_comprehension():
    #my_num = [x*x for x in [1, 2, 3, 4, 5, 6]]
    my_num = (x * x for x in [1, 2, 3, 4, 5, 6])   #generator
    return my_num


def list_comprehension2():
    my_list = [n for n in range(21)]
    print(my_list)

    my_list = [n for n in range(21) if n%2 == 0]
    print(my_list)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list = filter(lambda n: n%2 == 0, nums)
    print(my_list)

    my_list = []
    for letter in 'abcd':
        for num in range(4):
            my_list.append((letter, num))
    print(my_list)

    #above one will be replaced in following way
    my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
    print(my_list)

    names = ['Bruce', 'Clark', 'Peter', 'Logan', "Wade"]
    heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

    my_dict = {}
    for name, hero in zip(names, heros):
        my_dict[name] = hero

    print(my_dict)

    #Dictionary Comprehension
    my_dict = {name: hero for name, hero in zip(names, heros)}
    print(my_dict)

    #Set comprehension
    nums = [1,1,2,1,3,4,3,5,5,6,7,8,7,8,9,9]
    my_set = set()
    for n in nums:
        my_set.add(n)
    print(my_set)

    my_set = {n for n in nums}
    print(my_set)

    #Generator comprehension
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_gen = (n*n for n in nums)
    for i in my_gen:
        print(i)



if __name__ == '__main__':
    for num in list_comprehension():
        print(num)

    list_comprehension2()
