# Declaring multiple vars on the same line

x, y = 1, 2
print(x)
print(y)

# Unpacking

x = (1, 2, 3)

a, b, c = x
print(a, b, c)

# Initialize the same value

w = x = y = z = 0
print(w, x, y, z)

x = a, b, c
print(x)

# Data type methods

name = 'jim'
age = 29

print(type(name))
print(type(age))

# isinstance(arg, datatype)
print(isinstance(name, str))
print(isinstance(age, float))

print(type(age) == int)