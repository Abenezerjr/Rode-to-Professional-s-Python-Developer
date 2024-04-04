print('Welcome to Small python Pizza deliveries!')
size = input('what size pizaa do you went?S,M or L : ').upper()
addPepperoni = input('Do You want Pepperoni?Y or N : ').upper()
extraCheese = input('Do You want extraCheese? Y or N : ').upper()

smallPizza = 15
mediumPizza = 20
largePizza = 25
pepperoniForSmallPizza = 2
pepperoniForMLPizza = 3
extraCheeseForPizza = 1
if size == 'S':
    if addPepperoni == 'Y':
        if extraCheese == 'Y':
            print(f'your final bill {smallPizza + pepperoniForSmallPizza + extraCheeseForPizza}')
        else:

            print(f'your final bill {smallPizza + pepperoniForSmallPizza}')
    else:
        if extraCheese == 'Y':
            print(f'your final bill {smallPizza + extraCheeseForPizza}')
        else:
            print(f'your final bill {smallPizza}')

elif size == 'M':
    if addPepperoni == 'Y':
        if extraCheese == 'Y':
            print(f'your final bill {mediumPizza + pepperoniForMLPizza + extraCheeseForPizza}')
        else:
            print(f'your final bill {mediumPizza + pepperoniForMLPizza}')
    else:
        if extraCheese == 'Y':
            print(f'your final bill {mediumPizza + extraCheeseForPizza}')
        else:
            print(f'your final bill {mediumPizza}')
elif size == 'L':
    if addPepperoni == 'Y':
        if extraCheese == 'Y':
            print(f'your final bill {largePizza + pepperoniForMLPizza + extraCheeseForPizza}')
        else:
            print(f'your final bill {largePizza + pepperoniForMLPizza}')
    else:
        if extraCheese == 'Y':
            print(f'your final bill {largePizza + extraCheeseForPizza}')
        else:
            print(f'your final bill {mediumPizza}')
