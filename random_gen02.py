# Generate random numbers from interval [3, 7)

import random

def my_random():
    #Random, scale, shift, return
    return 4*random.random() + 3

for i in range(10):
    print(my_random())

#second way

print("**********Second Way ************")
for i in range(10):
    print(random.uniform(3, 7))

#Rand int

print("**********Rand int ************")

for i in range(20):
    print(random.randint(1, 6))

print("**********Rand choice ************")

outcomes = ["rock", "paper", "scissors"]

for i in range(20):
    print(random.choice(outcomes))



