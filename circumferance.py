def circumference(radius):
    # formula: C = 2 * 3.14 * radius
    pi = 3.14
    return 2 * pi * radius

a = float(input("Enter the radius of the circle: "))
b = circumference(a)

print("The circumference of the circle is:", b)