# Add
def Add(n1, n2):
    return n1 + n2


# Subtraction
def Subtract(n1, n2):
    return n1 + n2


def Multiply(n1, n2):
    return n1 * n2


def Division(n1, n2):
    return n1 / n2


operations = {
    '+': Add,
    '-': Subtract,
    '*': Multiply,
    '/': Division,
}

num1 = int(input('what is the first number: '))

num2 = int(input('what is the second number: '))

for symbol in operations:
    print(symbol)
operation = input('pick an operation from the above: ')

calcFunction = operations[operation]
answer=calcFunction(num1, num2)

print(f'{num1} {operation} {num2} = {answer} ')