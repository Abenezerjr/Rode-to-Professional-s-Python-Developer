# if if is the statement that decided something in code
# example one
# age = 14
# if age >= 18:
#     print('you can go what ever you went')
# print("with your family Please!")  # the output
#
# # if else
#
# num_age = 17
#
# if age <= 18:
#     print(f"you age is {age}  you can't buy any alcove")
# else:
#     print("you can buy what ever you went")
#
# # example 2 Odd or even
# num = int(input("Enter the number "))
#
# if num % 2 == 0:
#     print(f"the number is {num} is even")
# else:
#     print(f"the number is {num} is odd")

# example Rollercoaster

height = int(input('Enter your height in cm?: '))

if height > 120:
    print("You can ride")
    age = int(input('what is your age? '))
    if 12 < age < 18:
        pay = 7
        print(f'you only pay {pay}$')
        photos = input("do you want capture some moments 📷? ")
        if photos == 'yes':
            print('you will charge 3$')
            print(f'the total bill of {pay + 3}$')
        else:
            print(f'the total bill of {pay}$')

    elif age < 12:
        pay = 5
        print(f'you only pay {pay}$')
        photos = input("do you want capture some moments 📷? ")
        if photos == 'yes':
            print('you will charge 3$')
            print(f'the total bill of {pay + 3}$')
        else:
            print(f'the total bill of {pay}$')
    else:
        pay = 12
        print(f'you only pay {pay}$')
        photos = input("do you want capture some moments 📷? ")
        if photos == 'yes':
            print('you will charge 3$')
            print(f'the total bill of {pay + 3}$')
        else:
            print(f'the total bill of {pay}$')
else:
    print("sorry you can't ride😒")
