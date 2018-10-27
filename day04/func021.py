

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Venkatram", "50")

print("By")


def cube(num):
    return num*num*num


result = cube(5)

print(result)

#if statement

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male or not tall")





