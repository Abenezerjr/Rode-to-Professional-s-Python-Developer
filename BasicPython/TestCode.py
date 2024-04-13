# addName = True
# listOfName=[]
# while addName:
#     name = input('writ the name of the group:').split(',')
#     listOfName.append(name)
#     add = input("you when to add a name to countion 'Yes' to exit 'No").lower()
#     if add == 'yes':
#         name = input('writ the name of the group:')
#         listOfName.append(addName)
#
#     else:
#         addName = False
# print(f"list of student name: {listOfName}")
#
# auction_continue = True
# auction = {}
#
# while auction_continue:
#     name = input('Enter the name: ')
#     bid = int(input('Enter the bid price: $'))
#     auction[name] = bid  # Add the new user and bid to the auction dictionary
#     print(auction)
#
#     another = input("Is there any other user? Say 'Yes' to continue or 'No' to quit: ").lower()
#     if another == 'yes':
#         auction_continue = True
#     else:
#         auction_continue=False
#         for i in auction:
#             print(auction[i])
#
# print("Final auction dictionary:")
# print(auction)

# monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(monthDays)
# print(monthDays[1])
# monthDays[1]=29
# print(monthDays)

def add(a1, a2):
    return a1 + a2


def sub(a1, a2):
    return a1 + a2


def mult(a1, a2):
    return a1 + a2


def div(a1, a2):
    return a1 / a2


operation = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

num1 = int(input('enter the number: '))
num2 = int(input('enter the secode number: '))

for i in operation:
    print(i)
symbol = input('enter the symbol from the above: ')

function = operation[symbol]
result = function(num1, num2)

print(f'{num1} {symbol} {num2} = {result}')
