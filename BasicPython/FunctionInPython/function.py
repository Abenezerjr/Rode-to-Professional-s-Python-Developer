# function like a machin like you give raw material and it give a product

# in python function define using def with function name and ()
name = input('what is your name: ')


def WhatisYorName():
    """this function does not execute itself to execute it must call"""
    print('my name is chala')
    print(f'my name is {name} ')


# call in function

WhatisYorName()


# function with parameter

def Add(a, b):
    Sum = a + b
    print(Sum)


Add(5, 10)
