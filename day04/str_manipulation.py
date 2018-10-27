
my_str = "Venkatram reddy"

str_part = my_str[2:14:2]

print(str_part)

print(my_str[::-1])  #reversing string  start:stop:step

#Immutability

name = "Sam"

#name[0] = 'P'

#print(name)

last_letters = name[1:]  #String slicing

new_name = 'P' + last_letters

print(new_name)

print('The {} {} {}'.format('fox', 'brown', 'quick'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777

print("The result was {r}".format(r=result))

# Float formatting follows {value:width:precision

print("The result was {r:10.3f}".format(r=result))

name = "Venkatram"

#f-String

print(f'Hello, his name is {name}')

#lists

my_list = ['one', 'two', 'three']

print(my_list[1:])  #list slicing

another_list = ['four','five']

n_list = my_list + another_list  # list concatination

print(n_list)

n_list.append('six')

print(n_list)




