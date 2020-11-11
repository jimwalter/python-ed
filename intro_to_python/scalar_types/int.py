num_folders = 0

# you see one folder
num_folders += 1

# you see another folder
num_folders += 1

# you see two folders in the corner of the box
num_folders += 2

print(f'There are {num_folders} manilla folders')


# Converting an input to an INT
def mult_x_and_y():
    # get some input from a user
    x = input('Input a value for x: ')

    print(f'{x} is of type {type(x)}')


    # convert that value to an int using int()
    print('\nconverting x')

    x = int(x)
    print(f'{x} is now of type {type(x)}')

    # take in a second value and multiply the two
    y = input('\nInput a value for y: ')
    y = int(y)
    print(f'{x} * {y} = {x*y}')

mult_x_and_y()


# rounding floats using int()
'''
Another use case for the int() function is to round numbers up or down. This approach will
not work for rounding floats based on whether the first decimal place is .5, but it will
put floats into integer form based on the problem you are trying to address. For example, 
here is a function that returns the "middle" letter of a word. Since a letter position is necessary,
an int must be used. It is not possible to get the 3.5th letter of a word, so this function
will round down to the prior position. Don't worry if you don't totally understand what is
happening here, at this point. Just notice that a float is cast to an int in order to be
able to get the letter from some position in a word.
'''
def get_middle_letter(some_word):
    # first get the length
    length_of_word = len(some_word)
    print('length of word', length_of_word)
    print('rounded length', int(length_of_word / 2))

    return some_word[int(length_of_word / 2)]

print(get_middle_letter('coldseptemberrain'))

# int() type casts to int
# indexing requires use of int data type

'''
CHALLENGE:
Write a function called divide_by_7. This function will take a number as an argument(or parameter).
It will divide the number by 7, and return the result of that operation cast as an int.
'''

def divide_by_7(some_num):
    return int(some_num / 7)
