'''
Indentation
At its core, a Python script is simply a sequence of instructions to be executed in order. Instructions can be comprised of single, independent statements like print("Hello, world!"), or they can be more complex, made up of groups of statements, or blocks:

def divisible_by_3_or_7(n):
    if n % 7 == n % 3 == 0:
        print("the number is divisible by both 3 and 7!")
    elif n % 3 == 0:
        print("the number is divisible by 3!")
    elif n % 7 == 0:
        print("the number is divisible by 7!")
    else:
        print("the number is not divisible by either 3 or 7!")
Notice how all of the code below the function's definition is indented? This is how Python recognizes what statements go together. Other languages use symbols to denote code blocks, like Java, which uses curly braces and does not require grouped statements to be indented. Python, by contrast, requires indentation in order to distinguish grouped statements.

If grouped statements aren't properly indented at the same level, your code won't run!
'''