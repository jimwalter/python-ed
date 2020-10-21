# Cast 'float' objects to 'int'
print("int(33.3):", int(33.3))
print("type:", type(int(33.3)))

'''
sort of like the FLOOR DIV in that it truncates all decimals of the result

If your intention is to round a decimal number to the nearest whole number, use the round() function.
'''
print("int(6.9999) =", int(6.9999))  # -> 6

print("round(6.9999) =", round(6.9999)) # -> 7

# Not all types can be cast - must be compatible
# These two print statements will throw an error, uncomment them and click 'run' to see what kind of error
# print(float('a'))
# print(int('a'))


# Any 'truthy' object casts to the boolean 'True' simply bc something is there that is not a 'falsey' value
print("bool('a'):", bool('a'))


# Any non-'truthy' object casts to the boolean 'False'
print("bool(''):", bool(''))
print("bool(0):", bool(0))
print("bool(0.0)", bool(0.0))

