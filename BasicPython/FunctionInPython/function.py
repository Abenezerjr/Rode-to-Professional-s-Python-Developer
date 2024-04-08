# function like a machin like you give raw material and it give a product

# in python function define using def with function name and ()
# name = input('what is your name: ')


# def WhatisYorName():
#     """this function does not execute itself to execute it must call"""
#     print('my name is chala')
#     print(f'my name is {name} ')


# call in function

# WhatisYorName()
#

# function with parameter

# def Add(a, b):
#     Sum = a + b
#     print(Sum)
#
#
# Add(5, 10)


# example 2
def greet(name):
    print(f'hello and find {name}')
    print('this is function')
    print('just wow')


greet('joe')


# Position; Vs KeyWord
# positional argument call a function using position
def greetWith(name, location):
    print(f'Hellow {name}')
    print(f'i come from {location}')


# positional
greetWith('joe', 'london')

# keyWord
greetWith(location='NY', name='don')
