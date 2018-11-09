g = lambda x: 3 * x + 1

output = g(2)

print(output)

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("venkatram", "veerareddy"))

scifi_authors = [
    "Isaac Asimov", "Ray Bradbury", "Robert Heinlien", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wels", "Leigh Brackett"
]

scifi_authors.sort(key=lambda name: name.split(" ")[-1])

print(scifi_authors)

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(4,5,6)


print(f(0))
print(f(1))
print(f(2))

print("****")
print(build_quadratic_function(3, 0, 1)(2)) # 3x^2 + 1 evaluated for x = 2
