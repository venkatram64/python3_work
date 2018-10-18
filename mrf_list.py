
import math
import statistics
from functools import reduce
import time

def area(r):
    """Area of circle with radius r """
    return math.pi * (r ** 2)

radii = [2,5,7.1,0.3,10]

#Method 1: Direct method

areas = []

for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

#Method 2: Use 'map' function

a = list(map(area, radii))

print(a)

temps = [("Berlin", 29), ("Cairo", 36), ("Bueno Airs", 19), ("Los Angeles", 26),
         ("Tokyo", 27), ("New York", 28), ("London", 22), ("Delhi",34)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

temp_in_f = list(map(c_to_f, temps))

print(temp_in_f)

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print("avg is " + str(avg))

data_g_a = list(filter(lambda x: x > avg, data))
print("data is more than avg is: " + str(data_g_a))

# Remove missing data

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "",
             "Ecuador", "", "", "Venezueala"]

data = list(filter(None, countries))

print("Removing empty " + str(data))

''' False values are "",0,0.0,0j,[],(),{}, False, None 
 instances which signals they are empty'''

''' Guido van Rossum python creator
Use functools.reduce() if you really need it; however, 99% of the time an 
explicit for loop is more readable.
'''

#Multiply all numbers in a list

data = [2, 3, 5, 7, 11, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
mdata = reduce(multiplier, data)

print("Mulitiplication of data is " + str(mdata))

# by using for loop above one

product = 1

for x in data:
    product = product * x

print("Mulitiplication of data is from for loop " + str(mdata))


"""Return 'True' if n is a prime number, False otherwize """
def is_prime_val(n):
    if n == 1:
        return False # 1 is not prime

    for d in range(2, n):
        if n%d == 0:
            return False
        return True

# Test function

for n in range(1, 21):
    print(n, is_prime_val(n))


# Time function

t0 = time.time()
for n in range(1, 10000000):
    is_prime_val(n)

t1 = time.time()

print("Time required ", t1 - t0)

# other way to finding the prime
# https://www.youtube.com/watch?v=2p3kwF04xcA&index=24&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-
def is_prime_v2(n):
    """Return 'True' if n is a prime number, False otherwize """
    if n == 1:
        return False # 1 is not prime
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
        return True

# Time function

t0 = time.time()

for n in range(1, 10000000):
    is_prime_val(n)

t1 = time.time()

print("Time required ", t1 - t0)

# removing the even

def is_prime_v3(n):
    """Return 'True' if n is a prime number, False otherwize """
    if n == 1:
        return False  # 1 is not prime
    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
        return True


# Time function

t0 = time.time()

for n in range(1, 10000000):
    is_prime_val(n)

t1 = time.time()

print("Time required ", t1 - t0)






