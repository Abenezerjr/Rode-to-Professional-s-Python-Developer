# import math
#
# h = int(input('Height of wall: '))
# w = int(input('Width of wall: '))
# coverage = 5
#
#
# def paintCalc(height, width, cover):
#     cans = math.ceil((height * width) / 5)
#     print(f"you will need {cans} cans of paint.")
#
#
# paintCalc(height=h, width=w, cover=coverage)

number = int(input("Enter the number you went to check"))


def checkIsPrime(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print('its a prime number!')
    else:
        print('Not prime number!')


checkIsPrime(number)
