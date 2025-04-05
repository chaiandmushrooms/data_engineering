def largest_number (x, y, z):
    if x > y and x > z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
z = float(input("Enter your third number: "))

print ("Largest of them all is, drum roll please: {}" .format(largest_number(x, y, z)))

