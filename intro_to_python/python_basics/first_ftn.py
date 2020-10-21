'''
print =/= return

print logs to console

return is a value returned from the function invocation
============

Define a function called mod_5_times_6. The function should take a number as an argument, 
perform the modulo by 5 operation, multiply the result by 6, then return the new result.

============
'''
def mod_5_times_6(num):
    return (num % 5) * 6

'''
============

Finish writing the function func, which should take an argument x and return (5x+7)^2.

============
'''
def func(x):
    return ((5 * x) + 7)** 2
    
'''
============

Define a function called lots_of_math with one parameter called x. The function should calculate x2x+3, 
convert that result to an integer, and then return that result mod 7.

============
'''
def lots_of_math(x):
    y = int(x**((2 * x) + 3))
    return y % 7

