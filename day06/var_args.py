def addition_simplified(*args):
    print(sum(args))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)



if __name__ == '__main__':
   # addition_simplified(1,2,3,4,5,6,7)
    what_are_kwargs(1,2,3, name='Venkatram', location='India')