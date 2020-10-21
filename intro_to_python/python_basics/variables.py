x = "some string"
print(type(x))  # -> str

'''
    x is assigned to some... thing using the assingment operator, =

'''

# Simple variable assignment
x = 7
# Now you can refer to the integer value '7' using the name 'x'
print(x)


# Assign the result of an expression to a variable
y = 521 / 74 + 7**(1/8)
print(y)


# Reference other variables in an assignment
z = (x + y) / 100
print(z)

# INCREMENTATION
'''
 An incrementation operator is any basic operator combined with the assignment operator =,
 like *= or +=, which denotes multiplicative and additive incrementation, respectively.
 '''

# Assign the name 'z' to the integer value '10'
z = 10

# Increment 'z' by '1'
z += 1 # Equivalent to 'z = z + 1'
print(z)


# Assign the name 'a' to the integer value '3'
a = 3

# Multiply 'a' by 3, and assign the result to 'a'
a *= 3 # Equivalent to 'a = a * 3'
print(a)


# Incrementation works for other operators, too
b = 21
b /= 3 # Equivalent to 'b = b / 3'

# But remember that division results in a 'float'
print(type(b))

# VARS ARE REFERENCES

'''
Variables only reference values, they are not the values themselves.
When variables are changed by an incrementation operator, for example,
the location in memory to where that variable points also changes.
The following example demonstrates this behavior, using the built-in
id() function to show a value associated with the memory location of an object:
'''
n = 27
print(n)
print("ID: ", id(n))

n += 1
print(n)
print("ID: ", id(n))

n /= 7
print(n)
print("ID: ", id(n))

n **= 2
print(n)
print("ID: ", id(n))

'''
Notice how the id of the variable n is not maintained when the value of n is modified. 
This implies that n itself is not changing, but is instead being pointed at a different value in memory. 
This touches on a concept called mutability, and is explored in greater detail in the next unit.
'''