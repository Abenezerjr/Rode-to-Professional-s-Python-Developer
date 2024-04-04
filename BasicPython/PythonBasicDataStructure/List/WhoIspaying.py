import random

names = input('Enter the name of the people separated by comma: ').split(",")

istOfName = names
# whoPay = random.choice(istOfName)
whoPay = random.randint(0, len(istOfName)-1)
print(f'{istOfName[whoPay]} is going to pay the meal Today😁 ')
