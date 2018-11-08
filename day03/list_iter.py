
friends = ["Kevin", "Karen", "Jim", "Venkatram","Srijan"]

def iter1():
    for i, val in enumerate(friends):
        print(i, val)


def iter2():
    list = friends.__iter__()
    while True:
        try:
            print(list.__next__())
        except StopIteration:
            break

if __name__ == '__main__':
    iter2()
