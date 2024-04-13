import os

clear = lambda: os.system('cls')


# isContourne = True


def calculation():
    isContourne = True

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

    for symbol in operations:
        print(symbol)
    operation = input('pick an operation from the above: ')

    num2 = int(input('what is the second number: '))

    calcFunction = operations[operation]
    answer = calcFunction(num1, num2)

    # print(f'{num1} {operation} {num2} = {answer} ')
    while isContourne:
        choose = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation 'q' for quite: ").lower()
        if choose == 'q':
            isContourne = False
        elif choose == 'y':
            operation = input('pick an  operation: ')
            num3 = int(input('enter the next number: '))
            calcFunction = operations[operation]
            result = calcFunction(answer, num3)
            answer = result

        else:
            clear()
            calculation()


calculation()
