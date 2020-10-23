x = 2
# global vars is bad practice, these are called outside effects
def add_n(n):
    global x # telling the add_n function to look for `x` in the global scope
    x += n
    return x


print(x, 'x b4')
print(add_n(2), "print")
print(x, 'x')

location = 'Spain'

def find_location(location):
    location = 'France'
    return location

print(find_location(location), location)

'''
When add_2 gets called by its parent add_2_then_times_3, it tries to execute the instruction x + 2. 
Since add_2 doesn't have its own x to use, it asks its parent for x. Then add_2_then_times_3 looks for an x. 
If no local x is found, add_2_then_times_3 asks its parent for an x to use, and so on. 
All add_2 cares about is being able to use an x. It isn't paying attention to where x comes from, 
only that it has an x to use.
'''