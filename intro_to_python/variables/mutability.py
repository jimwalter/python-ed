x = 1.5
print(type(x))
print(id(x), x)

x = int(x)
print(id(x), x)

x = 3
y = 3
print(id(x) == id(y))

'''
 int, float, etc., changes when the value associated with that variable changes, 
 it is convenient to think of the variable itself as being destroyed and recreated.
 In this sense, the variable cannot be changed, it must be destroyed in order to 
 represent another value. Thus the scalar types can be described as immutable.
'''

x = 4
y = 2**2
z = int((16.0) ** (0.5))

print(id(x) == id(y), 'same location')
print(id(x) == id(z), 'same location')
