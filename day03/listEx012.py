

friends = ["Kevin", "Karen", "Jim", "Venkatram","Srijan"]

friends.sort()

print(friends)

friends2 = friends.copy()

lucky_numbers = [42, 8, 15, 23, 4]

lucky_numbers.sort()

print(lucky_numbers)


print(friends)

print(friends[0])

#accessing from back

print(friends[-1])


print(friends[0:3])

print(friends[1:])

#list functions

friends.extend(lucky_numbers)

print(friends)

friends.append("Vasu")

print(friends)

friends.insert(1, "Ram")
print(friends)

friends.remove("Jim")

print(friends)

friends.pop()

print(friends)

print(friends.index("Srijan"))







