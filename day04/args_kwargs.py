
def my_func(*args):
    for arg in args:
        print(arg)


def my_kwfunc(**kwargs):
    for item in kwargs.items():
        print(item)


#combining above functions, first args and then kwargs parameters
def args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)

    for item in kwargs.items():
        print(item)

if __name__ == '__main__':
    my_func(1, 2, 3, 4)
    print("call list of args")
    l = [15, 21, 36, 54, "venkatram"]
    my_func(*l)
    print("calling kwargs ")
    my_kwfunc(x=123, y=89, name="Venkatram")

    print("calling args and keyward args ")
    args_kwargs(*l, first_name="Venkatram", last_name="Veerareddy")