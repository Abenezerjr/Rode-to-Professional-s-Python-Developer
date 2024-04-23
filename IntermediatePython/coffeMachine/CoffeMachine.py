MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def isResourceSufficient(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough water {item}")
            return False
    return True


def processCoins():
    print('Please insert coins.')
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def isTransactionSuccessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("'Sorry that's not enough money. Money refunded")
        return False


isOn = True

while isOn:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        isOn = False
    elif choice == 'report':
        print(f"water: {resources['water']} ml ")
        print(f"Milk: {resources['milk']} ml")
        print(f"coffee:{resources['water']} g")
        print(f"money: ${profit} ")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink['ingredients']):
            payment = processCoins()
            isTransactionSuccessful(payment, drink['cost'])
