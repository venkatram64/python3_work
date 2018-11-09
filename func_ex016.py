import math

def volume(r):
    """Returns the volume for given radius 'r' """
    v = (4.0/3.0) * math.pi * r**3
    return v


v1 = volume(6)

print("Volume of sphere is " + str(v1))


def height_in_cm(feet=0, inches=0):
    """Converts a length from feet and inches to cm """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print("feet to cm " + str(height_in_cm(5, 6)))